#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, Richard Oliver <source@richard-oliver.co.uk>
# (c) 2022, lotyp <lotyp7.woop@gmail.com>

# Known bugs:
# - enabled: True will return a false-success if FileVault is in the
#   process of decrypting the volume.

import subprocess as sp
from ansible.module_utils.basic import AnsibleModule


# for more info about exit codes: man fdesetup
fdesetup_errors = {
    0: "No error, or successful operation.",
    1: "FileVault is Off.",
    2: "FileVault appears to be On but Busy.",
    11: "Authentication error.",
    12: "Parameter error.",
    13: "Unknown command error.",
    14: "Bad command error.",
    15: "Bad input error.",
    16: "Legacy FileVault error.",
    17: "Added users failed error.",
    18: "Unexpected keychain found error.",
    19: "Keychain error. This usually means the FileVaultMaster keychain could not be moved or replaced.",
    20: "Deferred configuration setup missing or error.",
    21: "Enable failed (Keychain) error.",
    22: "Enable failed (CoreStorage) error.",
    23: "Enable failed (DiskManager) error.",
    24: "Already enabled error.",
    25: "Unable to remove user or disable FileVault.",
    26: "Unable to change recovery key.",
    27: "Unable to remove recovery key.",
    28: "FileVault is either off, busy, or the volume is locked.",
    29: "Did not find FileVault information at the specified location.",
    30: "Unable to add user to FileVault because user record could not be found.",
    31: "Unable to enable FileVault due to management settings.",
    32: "FileVault is already active.",
    33: "Command option is unsupported on this file system.",
    34: "An option or parameter is not supported for APFS volumes.",
    35: "An error occurred during FileVault disablement.",
    36: "This computer does not support enabling FileVault.",
    37: "One or more users have a blank password. FileVault cannot be enabled.",
    99: "Internal error."
}


def main():
    active = False

    module = AnsibleModule(
        argument_spec=dict(
            enabled=dict(required=True, type='bool'),
        ),
        supports_check_mode=True
    )

    # Check whether FileVault is enabled
    try:
        sp.check_output(["fdesetup", "isactive"])
        active = True
    except sp.CalledProcessError as e:
        if e.returncode == 1:
            active = False
        else:
            module.fail_json(msg="fdesetup failed: " + fdesetup_errors[e.returncode])

    enabled = module.params.get('enabled')

    if active:
        # FileVault is currently enabled
        if module.check_mode:
            module.exit_json(changed=not enabled)

        if enabled:
            module.exit_json(changed=False);
        else:
            try:
                sp.check_output(["fdesetup", "disable"])
                module.exit_json(changed=True)
            except sp.CalledProcessError as e:
                module.fail_json(msg="fdesetup failed: " + fdesetup_errors[e.returncode])
    else:
        # FileVault is currently disabled
        if module.check_mode:
            module.exit_json(changed=enabled)

        if not enabled:
            module.exit_json(changed=False);
        else:
            try:
                sp.check_output(["fdesetup", "enable", "-defer", "/dev/null", "-showrecoverykey", "-forceatlogin", "0",
                                 "-dontaskatlogout"])
                module.exit_json(changed=True)
            except sp.CalledProcessError as e:
                module.fail_json(msg="fdesetup failed: " + fdesetup_errors[e.returncode])


if __name__ == '__main__':
    main()
