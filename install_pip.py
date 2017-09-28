import platform
import subprocess as sp
import urllib.request

ex, s = sp.getstatusoutput('pip -V')

if ex == 0:
    print('Pip is already installed.')
    exit()
else:
    pip_file = urllib.URLopener()
    pip_file.retrieve("https://bootstrap.pypa.io/get-pip.py", "get-pip.py")
    ex, s = sp.getstatusoutput('python get-pip.py; pip -V')
    if ex == 0:
        print('Pip has been installed successfully.')
        exit()
    else:
        print('The following error occurred while installing pip.')
        print(s)
        exit()
