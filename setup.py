# SPDX-FileCopyrightText: 2022 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: Apache-2.0

import io
import os

import setuptools

AUTHOR = 'Dmitry Bondarenko'
MAINTAINER = 'Sergei Silnov'
EMAIL = 'sergei.silnov@espressif.com'

NAME = 'check_copyright'
SHORT_DESCRIPTION = 'The script for checking SPDX license header'
LICENSE = 'Apache License 2.0'
URL = 'https://github.com/espressif/check_copyright'
REQUIRES = [
    'comment_parser == 1.2.3',
    'thefuzz[speedup] == 0.19.0',
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
