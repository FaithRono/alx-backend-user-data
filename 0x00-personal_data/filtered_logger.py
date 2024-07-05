#!/usr/bin/env python3
"""
filtered logger
"""

import re


def filter_datum(fields, redaction, message, separator):
    return re.sub(f'({"|".join(fields)})=.*?{separator}', lambda x: x.group(
        0).split('=')[0] + '=' + redaction + separator, message)
