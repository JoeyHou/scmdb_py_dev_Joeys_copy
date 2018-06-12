activate_this = '/var/www/scmdb_py/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/scmdb_py')

from scmdb_py import app as application
application.secret_key = 's3cr3t'