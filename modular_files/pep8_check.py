import subprocess as sp

py_file = 'get_libs.py'
def pep8_check():

    print("Running pep8 check... ")
    ex, s = sp.getstatusoutput('pep8 ' + py_file +
                                ' > ' + py_file + '_pep8.txt')

    if ex == 0:
        print("The file given was according to pep8 conventions.")
    else:
        print("Pep8 check complete, the details have been stored in " + py_file + "_pep8.txt.")

if len(sp.getoutput('pip freeze | grep pep8').strip()) > 0:
    pep8_check()

else:
    yn = input("Pep8 is not installed. Do you wish to install pep8 to improve code formatting? y/n ")

    if yn == 'y':
        ex, s = sp.getstatusoutput('pip install pep8')
        if ex == 0:
            print("Pep8 successfully installed.")
            pep8_check()
        else:
            print("The below error occurred while installing pep8: ")
            print(s)
            exit()

    else:
        exit()
