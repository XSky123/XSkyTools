#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
----------------------------------------
    Filename   : Log.py
    Description: Deal with logging and debugging.
    Author     : XSky123
    Created at : 2017/10/23 20:59
----------------------------------------
"""
import logging
# Main logging model settings
# Perhaps ugly,
# but it is quite flexible.
# (also easy to code XD)
logging.basicConfig(format='[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
_logger = logging.getLogger(__name__)

class Logger:
    def __init__(self):
        self._logger = logging.getLogger(__name__)

    def set_debug_mode(self):
        self._logger.setLevel(logging.DEBUG)
        self._logger.debug("Logger now set to debug mode.")

    def set_info_mode(self):
        self._logger.setLevel(logging.INFO)
        self._logger.debug("Logger now set to info mode.")

    def set_default_mode(self):
        self._logger.setLevel(logging.WARNING)
        self._logger.debug("Logger now set to default mode.")

    def debug(self, content):
        self._logger.debug(content)

    def info(self, content):
        self._logger.info(content)

    def warning(self, content):
        self._logger.warning(content)

    def error(self, content):
        self._logger.error(content)


def set_debug_mode():
    _logger.setLevel(logging.DEBUG)
    _logger.debug("Logger now set to debug mode.")


def set_info_mode():
    _logger.setLevel(logging.INFO)
    _logger.debug("Logger now set to info mode.")


def set_default_mode():
    _logger.setLevel(logging.WARNING)
    _logger.debug("Logger now set to default mode.")


def debug(content):
    _logger.debug(content)


def info(content):
    _logger.info(content)


def warning(content):
    _logger.warning(content)


def error(content):
    _logger.error(content)


def main():
    log = Logger()
    log.set_debug_mode()
    log.info("This is an info.")
    log.warning("Warn!!")

if __name__ == '__main__':
    main()
