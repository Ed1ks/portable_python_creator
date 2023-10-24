import os
import subprocess
from os.path import exists
from pathlib import Path

# Tutorial: https://codefaq.org/windows/how-to-get-portable-python-3-9-on-windows-10/

PYTHONDIR = 'python3.11.4'
PYTHONPTHNAME = 'python311._pth'
DEPENDENCIES = ['PyQt6', 'pypiwin32', 'pyodbc', 'pydash']

file_exists = exists(f"{PYTHONDIR}/python.exe")

if file_exists:
    # Create required Directories
    Path(f"{PYTHONDIR}/Lib/site-packages").mkdir(parents=True, exist_ok=True)
    print(f"Directory created: {PYTHONDIR}/Lib/site-packages")

    # Edit python311._pth
    with open(f"{PYTHONDIR}/{PYTHONPTHNAME}", "w") as file:
        file.write(
            f"""Lib/site-packages
{PYTHONPTHNAME.replace('._pth', '')}.zip
.

# Uncomment to run site.main() automatically
import site
""")
    print(f"changed file for portable python: {PYTHONDIR}/{PYTHONPTHNAME}")

    # install pip
    os.chdir(PYTHONDIR)

    if not exists(f"get-pip.py"):
        try:
            bash_com = 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
            process = subprocess.Popen(bash_com)
            process.wait()
        except (Exception, ) as e:
            print(e)

    # install dependencies
    if exists(f"get-pip.py"):
        if not os.path.isdir('Lib/site-packages/pip'):
            subprocess.call("get-pip.py", shell=True)

        for dependency in DEPENDENCIES:
            subprocess.call(f"python -m pip install {dependency}", shell=True)
    else:
        print(f"cant find file get-pip.py")
        print(f"please restart...")
else:
    print(f'{PYTHONDIR}/python.exe wurde nicht gefunden')

input("Press Enter to continue...")
exit()
