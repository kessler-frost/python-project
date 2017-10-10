import subprocess as sp

"""
Below code is to input a file from terminal using '-f' flag.
"""
# import sys
# py_file = sys.argv[1]

rll = ['tensorflow'] # required libraries list
till = [] # to be installed libraries list
nfp = [] # not found in pip

for rl in rll:
    lib = sp.getoutput('pip freeze | grep ' + rl).strip()
    if not len(lib) > 0:
        f_lib = sp.getoutput('pip search ' + rl).strip()
        if len(f_lib) > 0:
            till.append(rl)
        else:
            nfp.append(rl)

if len(nfp) > 0:
    not_found = 'The following packages were not found in pip :- ' + ' '.join(nfp)
    print(not_found)
if len(till) > 0:
    yn = input("Do you wish to install " + ' '.join(till) + " that were found in pip? y/n ")
    if yn == 'y':
        command = 'pip install ' + ' '.join(till)
        print('Running ' + command)
        ex, s = sp.getstatusoutput(command)
        if ex == 0:
            print("Succesfully installed " + ' '.join(till) + '.')
        else:
            print(s)
            print("The above error occurred in pip install.")
            exit()
    else:
        exit()

else:
    print("All the required packages were already installed.")
