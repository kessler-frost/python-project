import subprocess as sp

all_files = ['test.py']
command = '2to3 -w ' + ' '.join(all_files) # -w flag is used to write the converted text back to source file

ex, s = sp.getstatusoutput(command)
if ex == 0:
    print("Python 2 files have been successfully converted to Python 3.")
    exit()
else:
    print("Some error/warning occurred :")
    print(s)
    exit()
