def python_version_check():
    import subprocess as sp

    print("Python interpreter version currently being used is :- ")
    print(sp.getoutput('python -V'))