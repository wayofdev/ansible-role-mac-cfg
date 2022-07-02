<br>

<div align="center">
<img width="456" src="https://raw.githubusercontent.com/wayofdev/ansible-role-tpl/master/assets/logo.gh-light-mode-only.png#gh-light-mode-only">
<img width="456" src="https://raw.githubusercontent.com/wayofdev/ansible-role-tpl/master/assets/logo.gh-dark-mode-only.png#gh-dark-mode-only">
</div>

<br>

<br>

<div align="center">
<a href="https://actions-badge.atrox.dev/wayofdev/ansible-role-mac-cfg/goto"><img alt="Build Status" src="https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fwayofdev%2Fansible-role-mac-cfg%2Fbadge&style=flat-square"/></a>
<a href="https://galaxy.ansible.com/wayofdev/maccfg"><img alt="Ansible Role" src="https://img.shields.io/ansible/role/59609?style=flat-square"/></a>
<a href="https://github.com/wayofdev/ansible-role-mac-cfg/tags"><img src="https://img.shields.io/github/v/tag/wayofdev/ansible-role-mac-cfg?sort=semver&style=flat-square" alt="Latest Version"></a>
<a href="https://galaxy.ansible.com/wayofdev/maccfg"><img alt="Ansible Quality Score" src="https://img.shields.io/ansible/quality/59609?style=flat-square"/></a>
<a href="https://galaxy.ansible.com/wayofdev/maccfg"><img alt="Ansible Role" src="https://img.shields.io/ansible/role/d/59609?style=flat-square"/></a>
<a href="LICENSE"><img src="https://img.shields.io/github/license/wayofdev/ansible-role-mac-cfg.svg?style=flat-square&color=blue" alt="Software License"/></a>
<a href="#"><img alt="Commits since latest release" src="https://img.shields.io/github/commits-since/wayofdev/ansible-role-mac-cfg/latest?style=flat-square"></a>
</div>

<br>

# Ansible Role: macOS config Automation

Role is used to automate use of macOS [defaults](https://support.apple.com/en-gb/guide/terminal/apda49a1bb2-577e-4721-8f25-ffc0836f6997/mac) command to configure system settings. Also, additionally, there is available [duti](https://github.com/moretension/duti) tool, which assigns applications to default document types. And all that in automated way!

Example mods that come enabled by default:

* Finder - Disable the warning before emptying the Trash
* Finder - Show bottom path bar by default
* Finder - Disable the warning when changing a file extension
* Text - Do not disable smart quotes, but set them as simple one's, instead of smart
* and many more...

These defaults are used by wayofdev members, but you may override them by defining your own playbook with your config.

If you **like/use** this role, please consider **starring** it. Thanks!

<br>

## 🗂 Table of contents

* [Requirements](#-requirements)
* [Role Variables](#-role-variables)
  * [Applications](#-applications)
  * [Dock](#-dock)
  * [Finder](#-finder)
  * [Input](#-input)
  * [Language & Region](#-language--region)
  * [Network](#-network)
  * [Power](#-power)
  * [Safari](#-safari)
  * [Screensaver](#-screensaver)
  * [Screenshots](#-screenshots)
  * [Security](#-security)
  * [UI](#-ui)
* [Example Playbook](#-example-playbook)
* [Development](#-development)
* [Testing](#-testing)
  * [on localhost](#-on-localhost)
  * [over SSH](#-over-ssh)
* [Dependencies](#-dependencies)
* [Compatibility](#-compatibility)
* [License](#-license)
* [Author Information](#-author-information)
* [Credits and Resources](#-credits-and-resources)
* [Contributors](#-contributors)

<br>

## 📑 Requirements

  - **Homebrew**: Requires `homebrew` already installed (you can use `wayofdev.homebrew` to install it on your macOS).
  - Up-to-date version of ansible. During maintenance/development, we stick to ansible versions and will use new features if they are available (and update `meta/main.yml` for the minimum version).
- Compatible OS. See [compatibility](#-compatibility) table.
- Role has dependencies on third-party roles on different operating systems. See `requirements.yml` and [dependencies](#-dependencies) section.

<br>

## 🔧 Role Variables

Section shows all possible variants of adding, moving, replacing and removing of applications, spacers, folders. Available variables are listed below, along with example values (see `defaults/main.yml`):

<br>

### → Applications

* Activity Monitor

```yaml
# Show the main window when launching app.
maccfg_activity_monitor_show_main_window: true

# Show all processes.
maccfg_activity_monitor_show_category: 0

# Sort Activity Monitor results
maccfg_activity_monitor_sort_by: "CPUUsage"

# Activity Monitor: Sort Direction
# 0 goes for DSC
maccfg_activity_monitor_sort_direction: 0
```

* Mail.app

```yaml
# Copy email addresses as `foo@example.com` instead of `Foo Bar <foo@example.com>` in Mail.app.
maccfg_mail_use_advanced_copy_format: false
```

*  MacOS Photos.app

```yaml
# Prevent Photos from opening automatically when devices are plugged in.
maccfg_photos_disable_hotplug: true
```

* Other applications

```YAML
# Add iOS Simulator to Launchpad.
maccfg_other_create_simulator_symlink: true
```

<br>

### → Dock

```yaml
# Drag a file over an icon in the Dock, hover, and the application will open.
# https://macos-defaults.com/misc/enable-spring-load-actions-on-all-items.html
maccfg_dock_enable_spring_load_everywhere: true

# Don’t show recent applications in Dock
maccfg_dock_show_recents: false
```

* Hot Corners

```yaml
### Hot Corners

# Possible values:
#  0: no-op
#  2: Mission Control
#  3: Show application windows
#  4: Desktop
#  5: Start screen saver
#  6: Disable screen saver
#  7: Dashboard
# 10: Put display to sleep
# 11: Launchpad
# 12: Notification Center

# Bottom right screen corner → Start screen saver
maccfg_dock_bottom_left_corner: 5
maccfg_dock_bottom_left_modifier: 0

# Bottom right screen corner → Launchpad
maccfg_dock_bottom_right_corner: 11
maccfg_dock_bottom_right_modifier: 0
```

* Mission Control

```yaml
# Mission Control - Speed up animations
maccfg_dock_expose_animation_duration: "0.1"
```

<br>

### → Finder

```yaml
# Allow quitting via ⌘ + Q; doing so will also hide desktop icons
maccfg_finder_allow_quitting: true

# What path should new finder windows open
# Computer     : `PfCm`
# Volume       : `PfVo`
# $HOME        : `PfHm`
# Desktop      : `PfDe`
# Documents    : `PfDo`
# Recents      : `PfAF`
# Other…       : `PfLo`
#
# Set Desktop as the default location for new Finder windows by default
maccfg_finder_new_window_target: "PfDe"
maccfg_finder_new_window_target_path: "file://~/Desktop/"

# Set search scope.
# This Mac       : `SCev`
# Current Folder : `SCcf`
# Previous Scope : `SCsp`
maccfg_finder_search_scope: "SCcf"

# Set preferred view mode.
# Icon View   : `icnv`
# List View   : `Nlsv`
# Column View : `clmv`
# Cover Flow  : `Flwv`
# Use column view in all Finder windows by default
maccfg_finder_view_mode: "clmv"

# Show path bar in Finder (Example: 751 items ... 351 GB left ...)
maccfg_finder_show_path_bar: true

# Keep folders on top when sorting by name
maccfg_finder_keep_folders_on_top: true

# Disable the warning when changing a file extension
maccfg_finder_disable_extension_change_warning: true

# Show status bar
maccfg_finder_show_status_bar: true

# Show bottom path bar by default
maccfg_finder_show_bottom_path_bar: true

# Avoid creating .DS_Store files on network volumes
maccfg_finder_avoid_dsstore_on_network_volumes: true

# Avoid creating .DS_Store files on USB volumes
maccfg_finder_avoid_dsstore_on_usb_volumes: true

# Disable the warning before emptying the Trash
maccfg_finder_disable_trash_warning: true

# Display full POSIX path as Finder window title
maccfg_finder_show_full_title: true

# Show all filename extensions
maccfg_finder_show_all_file_exts: false

# Expand the following File Info panes: General, Open With, Sharing & Permissions
maccfg_finder_expand_fileinfo_panels: true

# Show icons for external hard drives on Desktop
maccfg_finder_desktop_show_ext_hard_drives: true

# Show icons for hard drives on Desktop
maccfg_finder_desktop_show_hard_drives: false

# Show icons for mounted servers on Desktop
maccfg_finder_desktop_show_mounted_servers: false

# Show icons for removable media on Desktop
maccfg_finder_desktop_show_removable_media: true

# Show the ~/Library folder in finder
maccfg_finder_unhide_library_folder: true

# Show the ~/Users folder in finder
maccfg_finder_unhide_users_folder: true

# Install duti - utility to allow to change default file types.
maccfg_finder_install_duti: true

# Prefer custom editor over default TextEdit for plain text files.
# Works only if flag 'install_duti' is set to true
# Examples
# com.sublimetext.3
# com.sublimetext.4
# com.microsoft.VSCode
maccfg_finder_default_editor: "com.sublimetext.4"
```

<br>

### → Input

```yaml
# Disable natural scroll for mouse and trackpad.
maccfg_input_use_native_macos_scroll: false
```

* Keyboard

```yaml
# For 0 - Use F1, F2, etc. keys as Brightness/Media
# For 1 - Use F1, F2, etc. keys as standard function keys on external keyboards each key.
maccfg_input_keyboard_fn_key_state: 1

# What should happen when pressing Fn key?
# 0 - Do Nothing
# 1 - Change Input Source
# 2 - Show Emoji & Symbols
# 3 - Start Dictation (Press Twice)
maccfg_input_keyboard_fn_usage_type: 2
```

* Text

```yaml
# Disable text auto-correction in native apps.
maccfg_input_text_disable_auto_correction: true

# Disable text autocorrection in web.
maccfg_input_text_disable_web_auto_correction: true

# Do not disable smart quotes, but set them as simple one's, instead of smart.
# Use "" for double quotes and '' for single quotes
maccfg_input_text_use_simple_quotes: true
```

* Mouse

```yaml
# Magic mouse should run in two button mode
maccfg_input_mouse_two_button_mode: true

# Magic mouse - enable double tap gesture for zoom
maccfg_input_mouse_double_tap_gesture: true
```

* Trackpad

```yaml
# Map bottom right corner to right-click for integrated trackpad
maccfg_input_trackpad_bottom_right_click_trackpad: true

# Map bottom right corner to right-click for bluetooth trackpad
maccfg_input_trackpad_bottom_right_click_bt_trackpad: true
```

* Shortcuts

```yaml
# Allow global app shortcuts
maccfg_input_shortcuts_allow: true

# Enable global shortcut – ⌥⌘, brings up System Preferences dialog (opt+cmd+comma)
maccfg_input_shortcuts_opt_cmd_comma: true
```

<br>

### → Language & Region

```yaml
# Set the timezone; see `sudo systemsetup -listtimezones` for other values
maccfg_lang_timezone: "Europe/Riga"

# Set main languages - English US, Latvian - LV, Latvian - RU.
maccfg_lang_languages:
  - en-US
  - lv-LV
  - ru-LV

maccfg_lang_locale: "en_US@currency=EUR"

# Use metric measurement units.
maccfg_lang_metric_units: true

# Set "AppleMeasurementUnits" setting to centimeters.
maccfg_lang_apple_units: Centimeters

# Enables the input menu in the menu bar.
maccfg_lang_inputs_in_status_bar: true

# List of input sources.
maccfg_lang_input_sources:
  # Default input sources.
  - name: "ABC"
    id: 252
  - name: "Latvian"
    id: 30765
  - name: "Russian - Phonetic"
    id: 19457
```

<br>

### → Network

```yaml
# Perform hostname change? On remote machines can cause connection lose.
maccfg_network_change_hostname: true

# This mac-book's hostname
# On macOS, this module uses scutil to set HostName, ComputerName, and LocalHostName
maccfg_network_hostname: "mbpro-{{ remote_regular_user }}"
```

<br>

### → Power

Section controls how mac power will be managed on charger or battery:

```yaml
# Mostly here 'pmset' utility is used. For reference see:
# https://www.dssw.co.uk/reference/pmset.html
#
# To get total regular & safe sleep set following parameters to these values:
# powernap: false
# womp: false
# tcpkeepalive: false
# ttyskeepawake false
#
# Restart automatically if the computer freezes
maccfg_power_restart_on_freeze: true

###
# Settings to apply when device is on A/C charger.
###

# Wake the machine when the laptop lid is opened
maccfg_power_on_charger_lidwake: true

# Prevent idle system sleep when any tty (e.g. remote login session) is ’active’.
maccfg_power_on_charger_ttyskeepawake: true

# https://support.apple.com/en-gb/guide/mac-help/mh40773/mac
#
# Power Nap, available on Mac computers with flash memory, lets some Mac computers stay up to date
# even while they’re sleeping. When your Mac goes to sleep, Power Nap activates periodically to update information.
# The information that’s updated depends on whether your Mac is running on battery power (a Mac notebook computer)
# or plugged into a power adapter (a Mac notebook computer or Mac desktop computer).
# When your Mac is asleep and using battery power, Power Nap:
# * Checks for new messages in Mail
# * Updates events in Calendar
# * Updates other iCloud events
# When your Mac is plugged into a power adapter, Power Nap can also do activities such as
# downloading software updates and performing Time Machine backups.
maccfg_power_on_charger_powernap: true

# Set hibernate mode:
# hibernatemode = 0 (binary 0000) by default on supported desktops. The system will not back memory up to
#   persistent storage. The system must wake from the contents of memory; the system will lose context on
#   power loss. This is, historically, plain old sleep.
#
# hibernatemode = 3 (binary 0011) by default on supported portables. The system will store a copy of mem-ory memory
#   ory to persistent storage (the disk), and will power memory during sleep. The system will wake from
#   memory, unless a power loss forces it to restore from disk image.
#
# hibernatemode = 25 (binary 0001 1001) is only settable via pmset. The system will store a copy of mem-ory memory
#   ory to persistent storage (the disk), and will remove power to memory. The system will restore from
#   disk image. If you want "hibernation" - slower sleeps, slower wakes, and better battery life, you
#   should use this setting.
maccfg_power_on_charger_hibernatemode: 3

# Display sleep timer
maccfg_power_on_charger_displaysleep: 15

# Wake on ethernet magic packet. Same as "Wake for network access" in the Energy Saver preferences.
maccfg_power_on_charger_womp: true

# System sleep timer (value in minutes, or 0 to disable)
maccfg_power_on_charger_sleep: 0

# Wake for network access
maccfg_power_on_charger_tcpkeepalive: true

# Display sleep will use an intermediate half-brightness state between full brightness and fully off
maccfg_power_on_charger_halfdim: true

# Wake the machine when power source (AC/battery) is changed
maccfg_power_on_charger_acwake: false

# https://apple.stackexchange.com/a/342286
# Not used with SSD's
maccfg_power_on_charger_disksleep: 0

###
# Settings to apply when device is using battery.
###
maccfg_power_on_battery_lidwake: true
maccfg_power_on_battery_ttyskeepawake: false
maccfg_power_on_battery_powernap: false
maccfg_power_on_battery_hibernatemode: 3
maccfg_power_on_battery_displaysleep: 15
maccfg_power_on_battery_sleep: 30
maccfg_power_on_battery_tcpkeepalive: false
maccfg_power_on_battery_halfdim: true
maccfg_power_on_battery_acwake: false
maccfg_power_on_battery_disksleep: 0
```

<br>

### → Safari

```yaml
# Safari: Enable Develop menu and the Web Inspector in Safari 14+
maccfg_safari_web_inspector: true

# Safari: Change default homepage
maccfg_safari_homepage: "https://app.daily.dev/"

# Safari: Setup new tab behavior
# 0: Homepage
# 1: Empty Page
# 2: Same Page
# 3: Bookmarks
# 4: Top Sites
maccfg_safari_tab_behaviour: 0

# Safari: Setup new window behavior
# 0: Homepage
# 1: Empty Page
# 2: Same Page
# 3: Bookmarks
# 4: Top Sites
maccfg_safari_window_behaviour: 0
```

<br>

### → Screensaver

```yaml
# Set default system screensaver
# Available:
# "Album Artwork"
# "Arabesque"
# "Drift"
# "FloatingMessage"
# "Flurry"
# "Hello"
# "Monterey"
# "Random"
# "Shell"
# "Word of the Day"
maccfg_screensaver_name: "Flurry"

# Show clock when screensaver is running
maccfg_screensaver_show_clock: true

# Show screen saver after:
# Please choose these values, as OSX use dropdown in UI
#
# 0 - do not use screensaver
# 60 - 1 minute
# 120 - 2 minutes
# 300 - 5 minutes
# 600 - 10 minutes
# 1200 - 20 minutes
# 1800 - 30 minutes
# 3600 - 1 hour
maccfg_screensaver_start_after: 300
```

<br>

### → Screenshots

```yaml
# Save to custom folder instead of Desktop.
maccfg_screenshots_directory: "/Users/{{ remote_regular_user }}/Screenshots"

# Change the default file name prefix.
maccfg_screenshots_use_prefix: "src"
```

<br>

### → Security

```yaml
# Require password when screen awakes.
maccfg_security_require_pass_after_awake: true

# Require password immediately after sleep or screen saver begins
# 0 is for immediate password require
maccfg_security_require_pass_delay: 0

# Turn off Feedback Assistant data auto-gathering.
maccfg_privacy_apple_feedback_assistant: false

# Turn off personalized ads, a little less tracking from apple side...
maccfg_privacy_disable_personalized_ads: true
```

* Firewall

```yaml
# Turn on system firewall.
# Turned off by default.
# If this role is used with dev-env-osx playbook, then lulu firewall is used instead.
# Modes:
# https://discussions.apple.com/thread/3148672
# 0 - disabled
# 1 - enabled in "open" mode
# 2 - enabled in "strict" mode
maccfg_firewall_mode: 0
```

* Updates

```yaml
# Check for software updates once per week
# Default: 7 (in days)
maccfg_updates_delay_days: 7
```

* Firevault

```yaml
# FileVault full-disk encryption with a 256-bit key to help prevent unauthorized access to the information on startup disk.
# Can be risky to enable it on remote machines!
maccfg_firevault_enabled: true
```

<br>

### → UI

```yaml
# Expand save panel by default.
maccfg_ui_expand_save_panel: true

# Expand save panel by default.
maccfg_ui_expand_print_panel: true

# Automatically quit printer app once the print jobs complete.
maccfg_ui_quit_print_job: true

# Reveal IP address, hostname, OS version, etc. when clicking the clock in the login window (only).
maccfg_ui_login_clock_clickable: true

# Show bluetooth in menu bar.
maccfg_ui_menu_bar_bluetooth_icon: true
```

<br>

## 📗 Example Playbook

```yaml
---
- hosts: all

  # is needed when running over SSH
  environment:
    - PATH: "/usr/local/bin:/usr/local/sbin:/opt/homebrew/bin:{{ ansible_env.PATH }}"

  vars:
    maccfg_firevault_enabled: false

  roles:
    - wayofdev.homebrew
    - wayofdev.maccfg
```

<br>

## ⚙️ Development

To install dependencies and start development you can check contents of our `Makefile`

**Install** [poetry](https://github.com/python-poetry/poetry) using [poetry-bin](https://github.com/gi0baro/poetry-bin) and all dev python dependencies:

```bash
$ make install
```

**Install** only python dependencies, assuming that you already have poetry:

```bash
$ make install-deps
```

**Install** all git hooks:

```bash
$ make hooks
```

**Lint** all role files:

```bash
$ make lint
```

<br>

## 🧪 Testing

You can check `Makefile` to get full list of commands for remote and local testing. For local testing you can use these comands to test whole role or separate tasks:

### → on localhost

> :warning: **Notice**: By defaut all tests are running against your local machine!

```bash
# run molecule tests on localhost
$ poetry run molecule test --scenario-name default-macos-on-localhost -- -vvv

# or with make command
$ make m-local

# choose which tags will be included
$ export TASK_TAGS="dock-validate,dock-install"; make m-local
```

<br>

### → over SSH

```bash
# run molecule scenarios against remote machines over SSH
# this will need VM setup and configuration
$ poetry run molecule test --scenario-name default-macos-over-ssh -- -vvv

$ make m-remote

# tags also can be passed
$ export TASK_TAGS="dock-validate,dock-install"
$ make m-remote
```

<br>

## 📦 Dependencies

Installation handled by `Makefile` and requirements are defined in `requirements.yml`

  - [wayofdev.homebrew](https://github.com/wayofdev/ansible-role-homebrew) - soft dependency, required if Homebrew isn't installed yet and only if you need `duti`
  - [ansible.community.general](https://docs.ansible.com/ansible/latest/collections/community/general/index.html)

<br>

## 🧩 Compatibility

This role has been tested on these systems:

| system / container | tag      |
| :----------------- | -------- |
| macos              | monterey |
| macos              | big-sur  |

<br>

## 🤝 License

[![Licence](https://img.shields.io/github/license/wayofdev/ansible-role-dock?style=for-the-badge&color=blue)](./LICENSE)

<br>

## 🙆🏼‍♂️ Author Information

This role was created in **2022** by [lotyp / wayofdev](https://github.com/wayofdev).

<br>

## 🧱 Credits and Resources

**Useful resources:**

* [duti](https://github.com/moretension/duti)

<br>

## 🫡 Contributors

<img align="left" src="https://img.shields.io/github/contributors-anon/wayofdev/ansible-role-dock?style=for-the-badge"/>

<a href="https://github.com/wayofdev/ansible-role-maccfg/graphs/contributors">
  <img src="https://opencollective.com/wod/contributors.svg?width=890&button=false">
</a>

<br>
