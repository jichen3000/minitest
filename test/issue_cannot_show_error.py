# This is for version 1.7.2.
# The issue is that it cannot show error in the test statement.

import os, sys, inspect

# add parent path aka minitest to sys.path, so I can import the files
# realpath() will make your script run, even if you symlink it :)
current_file_path = os.path.split(inspect.getfile( inspect.currentframe() ))[0]
parent_file_path = os.path.realpath(os.path.abspath(os.path.join(current_file_path, '..')))
if parent_file_path not in sys.path:
    sys.path.insert(0, parent_file_path)

if __name__ == '__main__':
    from minitest import *

    with test("cannot show error"):
        "ok".p()
        "ok".pppp()
        "ok2".p()

        pass