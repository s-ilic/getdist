#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import print_function
import sys
import logging
import my_getdist

try:
    import argparse
except ImportError:
    print('use "module load" to load python 2.7+ or 3.6+, or see docs/readme_python.html for how to install')
    sys.exit()

try:
    from my_getdist.gui.mainwindow import MainWindow, QApplication
except ImportError:
    print("Could not find my_getdist.gui.mainwindow: configure your PYTHONPATH as described in the readme!")
    raise

parser = argparse.ArgumentParser(description='GetDist GUI')
parser.add_argument('-v', '--verbose', help='verbose', action="store_true")
parser.add_argument('--ini', help='Path to .ini file', default=None)
parser.add_argument('-V', '--version', action='version', version='%(prog)s ' + my_getdist.__version__)
args = parser.parse_args()

# Configure the logging
level = logging.INFO
if args.verbose:
    level = logging.DEBUG
FORMAT = '%(asctime).19s [%(levelname)s]\t[%(filename)s:%(lineno)d]\t\t%(message)s'
logging.basicConfig(level=level, format=FORMAT)

# GUI application
app = QApplication(sys.argv)
mainWin = MainWindow(app, ini=args.ini)
mainWin.show()
mainWin.raise_()
sys.exit(app.exec_())
