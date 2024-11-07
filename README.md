# check_copyright

Espressif repository for the script to check SPDX License Header in the files. 

# Information about optional parameters

| Short parameter name | Full parameter name       | Default value               | Description                                                                                    |
|----------------------|---------------------------|-----------------------------|------------------------------------------------------------------------------------------------|
| -v                   | --verbose                 | false                       | Print additional information for debugging                                                     |
| -r                   | --replace                 | false                       | Tries to add/replace license header                                                            |
| -m                   | --max-lines               | 30                          | How far to check for copyright notice in a file                                                |
| -f                   | --fuzzy-ratio             | 95                          | Minimum %% ratio to be considered as equal to the old header style                             |
| -d                   | --debug                   | false                       | Print debug info                                                                               |
| -du                  | --dont-update-ignore-list | false                       | Don't update ignore list                                                                       |
| -dr                  | --dry-run                 | false                       | Just check license headers without replace                                                     |
| -i                   | --ignore                  | check_copyright_ignore      | Path to the file with list of ignoring files                                                   |
| -l                   | --lines-changed           | 5                           | Minimum number of changed lines that will enforce copyright date update                        |
| -c                   | --config                  | check_copyright_config.yaml | Path to the config file                                                                        |
|                      | filenames                 | Require parameter           | Path to the folder or file to check. If it is a folder, all files will be analyzed recursively |

# How to add check to a new project

## Prepare steps:

If you want to add that script into your project, you should

1. (Optional) Create file [with the list of ignoring files](#configure-ignore-list) (i.e. `ignore_list_copyright`) 
2. Create [config file](#creating-config-file) (i.e `check_copyright_config.yaml`)

## As pre-commit

You can use this script as a [pre-commit](https://pre-commit.com/) hook. You should add pre-commit hook into 
`.pre-commit-config.yaml` with arguments `--replace` and `--config <path to the config>`. 
You can also add external arguments from the table above (i.e --verbose)

Example of the .pre-commit-config.yaml file 
```yaml
- repo: https://github.com/espressif/check-copyright/
  rev: v1.0.0
  hooks:
    - id: check-copyright
      args: ['--config', 'ci/check_copyright_config.yaml', '--ignore', 'ci/ignore_list_copyright']
```

## As CI

For CI you need to use flag --dry-run. Script returns list of files without SPDX header without trying to replace it.

Example of Gitlab CI:
```yaml
check_copyright:
  before_script:
    - pip install git+https://github.com/espressif/check-copyright.git@master
  script:
    - python -m check_copyright --verbose --dry-run --ignore ci/ignore_list_copyright --config ci/check_copyright_config.yaml .
```


# Configure ignore list

To skip license header checks for some files, you can create a file with the list of paths to ignore. You should pass the path to the ignore list as the `--ignore` parameter.
```text
tools/test1/main/test_file.c
tools/test1/tools/pythonTestFile.py
include/new_project/pgenheaders.h
...
```

# Creating config file

You also need to set rules for group of files, which licenses can be used etc:

```yaml
DEFAULT:
  perform_check: yes  # should the check be performed?
  # Sections setting this to 'no' don't need to include any other options as they are ignored
  # When a file is using a section with the option set to 'no', no checks are performed.

  # what licenses (or license expressions) are allowed for files in this section
  # when setting this option in a section, you need to list all the allowed licenses
  allowed_licenses:
    - Apache-2.0
  license_for_new_files: Apache-2.0  # license to be used when inserting a new copyright notice
  new_notice_c: |  # notice for new C, CPP, H, HPP and LD files
    /*
     * SPDX-FileCopyrightText: {years} Vaillant Group International GmbH. All rights reserved.
     * SPDX-License-Identifier: {license}
     */
  new_notice_python: |  # notice for new python files
    # SPDX-FileCopyrightText: {years} Espressif Systems (Shanghai) CO LTD
    # SPDX-License-Identifier: {license}

  # comment lines matching <old_header> section
  # are replaced with this template prefixed with the correct comment notation (# or // or *) and SPDX- notation
  header_copyright: '{years} Vaillant Group International GmbH. All rights reserved.'

  old_header: |  # old copyright header
    //
    // Copyright (c) {years} Vaillant Group International GmbH. All rights reserved.
    //

# You can create your own rules for files or group of files
examples_and_unit_tests:
  include:
   - 'examples/'
   - 'components/**/test/**'
   - 'components/**/test_apps/**'
   - 'tools/test_apps/**'
  allowed_licenses:
  - Apache-2.0
  - Unlicense
  - CC0-1.0
  license_for_new_files: Unlicense OR CC0-1.0

ignore:  # You can also select ignoring files here
  perform_check: no  # Don't check files from that block
  include:
    - components/bt/host/nimble/nimble/
    - components/bt/common/osi/
    - components/bt/porting/ext/
    - components/bt/porting/nimble/
    - components/http_parser/
    - components/wpa_supplicant/src/
    - '!components/wpa_supplicant/esp_supplicant/'
    - components/bt/host/bluedroid/
    - '!components/bt/host/bluedroid/api/'
    - '!components/bt/host/bluedroid/btc/'
    - examples/zigbee/
```
