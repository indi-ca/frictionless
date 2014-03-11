#!/usr/bin/python

"""Remap

Remaps Python keyboard mapping files between OSX and Windows

Usage:
   remap.py
   remap.py to_osx <osx_file> <win_file>
   remap.py to_windows <osx_file> <win_file>

Options:
    -h --help     Show this screen.
    --version     Show version.

"""

__author__ = "Indika Piyasena"

import os
import sys
import glob
import logging
from docopt import docopt

from map_keyboard import MapKeyboardLayoutFile

logger = logging.getLogger(__name__)


class Remap:
    def __init__(self):
        self.configure_logging()
        self.win_file = 'Win_Pycharm_Frictionless.xml'
        self.osx_file = 'OSX_Pycharm_Frictionless.xml'
        self.keyboard_mapper = MapKeyboardLayoutFile()

    def convert(self):
        arguments = docopt(__doc__, version='Remap 0.1')

        self.win_file = arguments['<win_file>']
        self.osx_file = arguments['<osx_file>']

        logger.info('Using Windows file: {0}'.format(self.win_file))
        logger.info('Using OSX file: {0}'.format(self.osx_file))

        if arguments['to_osx']:
            self.convert_to_osx()

        elif arguments['to_windows']:
            self.convert_to_windows()

        else:
            logger.info('Determining translation path from date modified...')
        return

        self.last_file_updated()
        pass

    def convert_to_windows(self):
        logger.info('Converting OSX -> Windows')
        source_file = self.osx_file
        target_file = self.win_file
        self.keyboard_mapper.convert_to_windows(source_file, target_file)
        os.utime(target_file, (self.atime(source_file), self.mtime(source_file)))

    def convert_to_osx(self):
        logger.info('Converting Windows -> OSX')
        source_file = self.win_file
        target_file = self.osx_file
        self.keyboard_mapper.convert_to_osx(source_file, target_file)
        os.utime(target_file, (self.atime(source_file), self.mtime(source_file)))

    def last_file_updated(self):
        """
        Attempt to figure out which file is the source based on last modified
        time
        """
        query = '*.xml'
        keymap_files = glob.glob(query)

        sorted_files = sorted(keymap_files, key=self.mtime, reverse=1)
        last_modified_file = sorted_files[0]
        second_last_modified_file = sorted_files[1]

        t1 = self.mtime(last_modified_file)
        t2 = self.mtime(second_last_modified_file)

        logger.debug('Last modified time: {0}'.format(t1))
        logger.debug('Second Last modified time: {0}'.format(t2))

        last_modified_time = self.mtime(last_modified_file)
        last_access_time = self.atime(last_modified_file)

        if sys.platform == "win32":
            logger.info('Detected Windows environment')
            # self.regenerate_osx(last_access_time, last_modified_time)
        elif sys.platform == 'darwin':
            logger.info('Detected OSX environment')
            # self.regenerate_windows(last_access_time, last_modified_time)
        else:
            logger.error('Unhandled platform: {0}'.format(sys.platform))
        pass

    @staticmethod
    def configure_logging():
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        pass

    def mtime(self, filename):
        return os.stat(filename).st_mtime

    def atime(self, filename):
        return os.stat(filename).st_atime


if __name__ == "__main__":
    print "Running Remap in stand-alone-mode"
    remap = Remap()
    remap.convert()
