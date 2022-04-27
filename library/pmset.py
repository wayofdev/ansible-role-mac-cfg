#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule


def parse_pmset_output(output):
    # Parses `pmset -g custom` into a 2-level dict.
    section_name = ''
    result = {}
    for line in output.split('\n'):
        if line == '' or 'Sleep On Power Button' in line:
            continue
        if line[0] != ' ' and line[-1] == ':':
            section_name = line[:-1]
            result[section_name] = {}
        else:
            k, v = line.split()
            result[section_name][k] = v
    return result


def run_module():
    module_args = dict(
        on_battery=dict(type='dict', required=False, default=dict()),
        on_charger=dict(type='dict', required=False, default=dict()),
    )
    result = dict(changed=False, diff=dict(before='', after=''))
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    _, stdout, _ = module.run_command(["pmset", "-g", "custom"], check_rc=True)

    commands = []
    output = parse_pmset_output(stdout)

    def add_diff(block, param, old_value, new_value):
        result['diff']['before'] += '{block}.{param}={val}\n'.format(
            block=block, param=param, val=old_value)
        result['diff']['after'] += '{block}.{param}={val}\n'.format(
            block=block, param=param, val=new_value)

    blocks = [('on_charger', '-c', output['AC Power']), ]

    if 'Battery Power' in output:
        blocks.append(('on_battery', '-b', output['Battery Power']))

    for block, mode_flag, current_values in blocks:
        # Iterate over user-specified parameters and check if there's anything
        # to change.
        for param, value in module.params[block].items():
            if value is None: continue
            if param not in current_values:
                continue
            orig = current_values[param]
            if isinstance(value, int):
                orig = int(orig)
            if orig != value:
                add_diff(block, param, orig, value)
                commands.append(['pmset', mode_flag, param, value])

    if commands:
        result['changed'] = True
    if module.check_mode:
        module.exit_json(**result)

    for command in commands:
        # Explicitly convert all arguments to strings, so that
        # module.run_command doesn't choke on ints.
        cmd = [str(v) for v in command]
        module.run_command(cmd, check_rc=True)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
