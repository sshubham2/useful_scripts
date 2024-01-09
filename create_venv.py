'''
    required files -
    1. requirements.txt
    2. create_venv.py
'''

import venv
from pathlib import Path
from subprocess import run

env_path = Path.cwd()/'my-env'
venv.create(env_path, with_pip=True)
req_file = Path.cwd()/'requirements.txt'
req_file.exists()
py_loc = env_path/'Scripts/python'
update_pip = run([py_loc, '-m', 'pip', 'install', '--upgrade', "pip"], cwd=Path.cwd(), capture_output=True, text=True)
result = run([py_loc, '-m', 'pip', 'install', '-r', req_file], cwd=Path.cwd(), capture_output=True, text=True)