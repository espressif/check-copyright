# SPDX-FileCopyrightText: 2022 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: Apache-2.0

import setuptools

AUTHOR = 'Espressif Systems'
MAINTAINER = 'Dmitry Bondarenko'
EMAIL = 'dmitry.bondarenko@espressif.com'

NAME = 'check-copyright'
SHORT_DESCRIPTION = 'The script for checking SPDX license header'
LICENSE = 'Apache License 2.0'
URL = 'https://github.com/espressif/check-copyright'
REQUIRES = [
    'comment_parser == 1.2.3',
    'thefuzz == 0.19.0',
    'thefuzz[speedup] == 0.19.0; sys_platform != "win32"',
    # don't depend on python-Levenshtein on Windows, as it requires Microsoft C++ Build Tools to install
    'pyyaml == 5.4.1',
    'pathspec == 0.9.0'
]

setuptools.setup(
    
    name=NAME,
    description=SHORT_DESCRIPTION,
    long_description_content_type='text/markdown',
    license=LICENSE,
    version='1.0.0',
    author=AUTHOR,
    maintainer=MAINTAINER,
    author_email=EMAIL,
    url=URL,
    install_requires=REQUIRES,
    py_modules=['check_copyright'],
    scripts=['check_copyright.py']
)
