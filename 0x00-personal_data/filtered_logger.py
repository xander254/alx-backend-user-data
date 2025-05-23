#!/usr/bin/env python3
import logging
import re
from typing import List
import logging
"""
A module that returns the log message obfuscated
"""


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR
                                  )
        return super().format(record)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    a func that returns the log message obfuscated
    """
    pattern = r'(' + '|'.join(fields) + r')=.*?(?=' + re.escape(
            separator) + r')'
    return re.sub(pattern, r'\1=' + redaction, message)
