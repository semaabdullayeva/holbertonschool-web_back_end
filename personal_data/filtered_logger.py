#!/usr/bin/env python3

"""
Regex-ing
"""
import re

def filter_datum(fields, redaction, message, separator):
    """
    The function should use a regex to replace
    occurrences of certain field values.
    """
    pattern = r'(?<=^|{})({})(?={})'.format(separator, '|'.join(fields), separator)
    return re.sub(pattern, redaction, message)
