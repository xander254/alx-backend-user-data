#!/usr/bin/env python3
import logging
import re
from typing import List
"""
A module that returns the log message obfuscated
"""


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    a func that returns the log message obfuscated
    """
    pattern = r'(' + '|'.join(fields) + r')=.*?(?=' + re.escape(
            separator) + r')'
    return re.sub(pattern, r'\1=' + redaction, message)
