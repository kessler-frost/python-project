import sys
if sys.version_info[0] < 3:
    print("Must use Python 3. Exiting...")
    exit()

import argparse as ag
import subprocess as sp

ps = ag.ArgumentParser(description="Python Script to provide Method Source Tree and different modules in order to help the developer.")

ps.add_argument('-A','--all', help='Select all files',action='store_true', required=False)

ps.add_argument('files_list', metavar='f', nargs='*', help='File to operate the script on.')

args = vars(ps.parse_args())

if args['all'] is True:
    print("Using all the python files in current directory...")
    files = sp.getoutput('ls -a *.py').strip().split('\n')
else:
    files = args['files_list']
    if len(files) < 1:
        print("Provide at least one file.")
        exit()

def python_version_check():
    import subprocess as sp

    print("Python interpreter version currently being used is :- ")
    print(sp.getoutput('python -V'))


def get_libs(filename_list):
    # format 1 : import library1, library2
    # format 2 : from library import class
    # format 3 : from library.class import function
    # format 4 : import library as library

    #import sys
    import re

    #filename = sys.argv[1]

    aspn = input("Do you wish to detect or install libraries for all files or seperately or none at all? a/s/n ")

    if aspn == 'a':

        list_of_libs_lists = []
        for filename in filename_list:
            libraries = []

            for code in open(filename).read().split("\n"):

                try:
                    format_1 = [library.strip() for library in re.match(r"^import\s+(.*)", code).groups()]
                    libraries += format_1
                except AttributeError:
                    pass
                try:
                    format_2 = [library.strip() for library in re.match(r"^from\s+(\w+)\s+import\s+.*", code).groups()]
                    libraries += format_2
                except AttributeError:
                    pass
                try:
                    format_3 = [library.strip() for library in re.match(r"^from\s+(\w+)\.\w+\s+import\s+.*", code).groups()]
                    libraries += format_3
                except AttributeError:
                    pass
                try:
                    format_4 = [library.strip() for library in re.match(r"^import\s+(\w+)\s+as\s+\w+", code).groups()]
                    libraries += format_4
                except AttributeError:
                    pass

                libs = []

                for element in libraries:
                    for token in element.split(","):
                            libs.append(token.strip())

                try:
                    libs.remove("*")
                except ValueError:
                    pass

            print("Libraries used in " + filename + " :")

            for lib in list(set(libs)):
                print(lib)

            list_of_libs_lists.append(list(set(libs)))

        return list_of_libs_lists

    elif aspn == 's':
        list_of_libs_lists = []
        for filename in filename_list:
            yn = input("Get libraries for file " + filename + " ? y/n ")
            if yn == 'y':

                libraries = []

                for code in open(filename).read().split("\n"):

                    try:
                        format_1 = [library.strip() for library in re.match(r"^import\s+(.*)", code).groups()]
                        libraries += format_1
                    except AttributeError:
                        pass
                    try:
                        format_2 = [library.strip() for library in re.match(r"^from\s+(\w+)\s+import\s+.*", code).groups()]
                        libraries += format_2
                    except AttributeError:
                        pass
                    try:
                        format_3 = [library.strip() for library in re.match(r"^from\s+(\w+)\.\w+\s+import\s+.*", code).groups()]
                        libraries += format_3
                    except AttributeError:
                        pass
                    try:
                        format_4 = [library.strip() for library in re.match(r"^import\s+(\w+)\s+as\s+\w+", code).groups()]
                        libraries += format_4
                    except AttributeError:
                        pass

                    libs = []

                    for element in libraries:
                        for token in element.split(","):
                                libs.append(token.strip())

                    try:
                        libs.remove("*")
                    except ValueError:
                        pass

                print("Libraries used in " + filename + " :")

                for lib in list(set(libs)):
                    print(lib)

                list_of_libs_lists.append(list(set(libs)))

            else:
                pass

        return list_of_libs_lists

    else:
        pass


def install_pip():
    import subprocess as sp
    import urllib.request

    print("Checking if pip is installed...")
    ex, s = sp.getstatusoutput('pip -V')

    if ex == 0:
        print('Pip is already installed.')
        return 0
    else:
        urllib.request.urlretrieve("https://bootstrap.pypa.io/get-pip.py", "get-pip.py")
        ex, s = sp.getstatusoutput('python get-pip.py; pip -V')
        if ex == 0:
            print('Pip has been installed successfully.')
            sp.getstatusoutput('rm get-pip.py')
            return 0
        else:
            print('The following error occurred while installing pip.')
            print(s)
            return -1


def libs_install(list_of_libs_lists):

    import subprocess as sp
    import pip

    installed_packages_list = [i.key for i in pip.get_installed_distributions()]
    # import sys
    # py_file = sys.argv[1]

    till = [] # to be installed libraries list
    nfp = [] # not found in pip

    for gll in list_of_libs_lists:
        for gl in gll:
            if gl not in installed_packages_list:
                ex, s = sp.getstatusoutput('pip search ' + gl)
                if ex == 0:
                    if gl not in till:
                        till.append(gl)
                else:
                    if gl not in nfp:
                        nfp.append(gl)

    if len(nfp) > 0:

        not_found = 'The following packages were not found in pip :- ' + ' '.join(nfp)
        print(not_found)

    if len(till) > 0:

        all_or_sep_or_none = "Do you wish to install all packages or seperately each package or none at all? a/s/n "
        aspn = input(all_or_sep_or_none)

        if aspn == 'a':
            yn = input("Do you wish to install " + ' '.join(till) + " packages that were found in pip? y/n ")
            if yn == 'y':
                command = 'pip install ' + ' '.join(till)
                print('Running ' + command)
                ex, s = sp.getstatusoutput(command)
                if ex == 0:
                    print("Succesfully installed " + ' '.join(till) + '.')
                else:
                    print("The below error occurred in pip install.")
                    print(s)
            else:
                pass

        elif aspn == 's':
            for lib in till:

                yn = input("Install " + lib + "? y/n ")
                if yn == 'y':
                    command = 'pip install ' + lib
                    print('Running ' + command)
                    ex, s = sp.getstatusoutput(command)
                    if ex == 0:
                        print("Succesfully installed " + lib + '.')
                    else:
                        print("The below error occurred in pip install.")
                        print(s)
                else:
                    pass
        else:
            pass

    else:
        print("All the required packages were already installed.")


def get_methods(filename):
    # format class 1 : class name(params)
    # format class 2 : class name
    # format func origin : def name(params)
    # format func called 1 : name(params)
    # format func called 2 : name(name(params))


    import re
    from nltk.tokenize import word_tokenize


    def get_parenthesis_list(code):
        parenthesis = []
        for element in code:
            if element == "(" or element == ")":
                parenthesis.append(element)

        return parenthesis


    def get_indentation(parenthesis):
        indentation_list = [0]
        current_indentation = 0
        for paran in parenthesis[1:]:
            if paran == ')':
                current_indentation -= 1
            elif paran == '(':
                current_indentation += 1
                indentation_list.append(current_indentation)
        return indentation_list


    def indent_functions(functions, parenthesis, indentation):
        indented_function_calls = []

        def make_indent(value):
            indent = ""
            for x in range(value):
                indent += "\t"
            return indent

        indentation_list = get_indentation(parenthesis)
        for index, func in enumerate(functions):
            indented_function_calls.append(indentation + make_indent(indentation_list[index]) + "calls function " + func)
        return indented_function_calls


    class_names, function_names, method_tree, check = [], [], [], 0
    indentation = ""

    for code in open(filename, encoding="utf-8").read().split("\n"):

        if len(code) != 0 and word_tokenize(code)[0] != "#":
            cn = re.findall(r"\s*class\s+(\w+)|\s*class\s+(\w+)\(.*\)", code)
            fn = re.findall(r"\s*def\s+(\w+)\(.*\):", code)
            cs = re.findall(r"\s*class\s+\w+\(.*\)|\s*class\s+\w+", code)
            fs = re.findall(r"\s*def\s+\w+\(.*\)", code)
            fc = re.findall(r"(\w*)\(", code)
            if len(cn) != 0:
                check = 1
                if type(cn[0]) == tuple:
                    class_names.append(cn[0][0])
                method_tree.append(cs[0])
                indentation = re.match(r"(\s*).*", cs[0]).groups()[0] + "\t"
            if len(fn) != 0:
                check = 1
                function_names.append(fn[0])
                method_tree.append(fs[0])
                indentation = re.match(r"(\s*).*", fs[0]).groups()[0] + "\t"
            if check == 0 and len(fc) != 0 and fc[0] != '':
                parenthesis = get_parenthesis_list(code)
                indented_functions = indent_functions(fc, parenthesis, indentation)
                for function in indented_functions:
                    method_tree.append(function)
            check = 0

    return method_tree, class_names, function_names


def get_method_source(filename_list):

    tree_output_file = "method_source_tree.txt"
    store = open(tree_output_file, "w", encoding="utf-8")
    methods = []
    all_method_trees = []
    
    for filename in filename_list:
        method_tree, name_one, name_two = get_methods(filename)
        all_method_trees.append(method_tree)
        for name in name_one:
            methods.append(name)
        for name in name_two:
            methods.append(name)
    max_width = max(len(method_name) for method_name in methods)
    
    for f in range(len(filename_list)):
        store.write('Method source tree for ' + filename_list[f] + ' is:\n')
        for s in all_method_trees[f]:
            store.write(s + "\n")
            
        store.write("\n\n")
    store.close()
    
    indexing_file = "indexed_files.txt"
    store = open(indexing_file, 'w', encoding="utf-8")    
    store.write("NAME".ljust(max_width + 5) + "TYPE\t\t\t" + "LOCATION" + "\n\n\n")
    for filename in filename_list:
        method_tree, class_names, function_names = get_methods(filename)
        for class_name in class_names:
            store.write(str(class_name).ljust(max_width + 5) + "class\t\t\t" + str(filename) + "\n")
        for function_name in function_names:
            store.write(str(function_name).ljust(max_width + 5) + "function\t\t" + str(filename) + "\n")
        store.write("\n\n")
    store.close()
    return all_method_trees


def pep8_verify(filename_list):

    import subprocess as sp

    #py_file = 'filename.py'

    def pep8_check(filename):

        aspn = input("Do you wish to run pep8 test for all the given files or seperately or none at all? a/s/n ")
        if aspn == 'a':
            for filename in filename_list:
                print("Running pep8 check for " + filename + "... ")
                ex, s = sp.getstatusoutput('pep8 ' + filename +
                                            ' > ' + filename + '_pep8.txt')

                if ex == 0:
                    print("The file given was according to pep8 conventions.")
                else:
                    print("Pep8 check complete, the details have been stored in " + filename + "_pep8.txt.")

        elif aspn == 's':
            for filename in filename_list:
                yn = input("Run pep8 test for " + filename + " ? y/n ")
                if yn == 'y':
                    print("Running pep8 check for " + filename + "... ")
                    ex, s = sp.getstatusoutput('pep8 ' + filename +
                                                ' > ' + filename + '_pep8.txt')

                    if ex == 0:
                        print("The file given was according to pep8 conventions.")
                    else:
                        print("Pep8 check complete, the details have been stored in " + filename + "_pep8.txt.")
                else:
                    pass
        else:
            pass


    ex, s = sp.getstatusoutput('pip freeze | grep pep8')

    for filename in filename_list:
        if ex == 0:
            pep8_check(filename)

        else:
            yn = input("Pep8 is not installed. Do you wish to install pep8 to improve code formatting? y/n ")

            if yn == 'y':
                ex, s = sp.getstatusoutput('pip install pep8')
                if ex == 0:
                    print("Pep8 successfully installed.")
                    pep8_check(filename)
                else:
                    print("The below error occurred while installing pep8: ")
                    print(s)
            else:
                pass


def py2to3_conversion(filename_list):
    import subprocess as sp

    #all_files = ['test.py']
    aspn = input("Do you wish to run this module on all files or seperately or none at all? a/s/n ")

    if aspn == 'a':
        command = '2to3 -w ' + ' '.join(filename_list) # -w flag is used to write the converted text back to source file

        ex, s = sp.getstatusoutput(command)
        if ex == 0:
            print("Python 2 files have been successfully converted to Python 3. The source backup has been created with <filename>.bak.")

        else:
            print("Some error/warning occurred :")
            print(s)

    elif aspn == 's':
        for filename in filename_list:
            yn = input("Convert " + filename + " from python 2 to python 3? y/n")
            if yn == 'y':
                command = '2to3 -w ' + filename # -w flag is used to write the converted text back to source file

                ex, s = sp.getstatusoutput(command)
                if ex == 0:
                    print("Python 2 files have been successfully converted to Python 3. The source backup has been created with <filename>.bak.")

                else:
                    print("Some error/warning occurred :")
                    print(s)
            else:
                pass

    else:
        pass

#files = str(sys.argv[1:])

print("Running modules...")

python_version_check()

yn = input("Do you want to run Module - Show imported libraries (mandatory if installation of any package is required)? y/n ")
if yn == 'y':
    list_of_libs_lists = get_libs(files)

    if install_pip() == 0:
        yn = input("Do you want to run Module - Install required libraries? y/n ")
        if yn == 'y':
            libs_install(list_of_libs_lists)
        else:
            pass
    else:
        print("Please install pip manually.")
        pass
else:
    pass

yn = input("Do you want to run Module - Method source tree with class and file names? y/n ")
if yn == 'y':
    all_method_trees = get_method_source(files)
    print("The tree has been written to a file named method_source_tree.txt and the index of all classes and functions to a file named indexed_files.txt in the current directory.")
    
    yn = input("Do you want to see the method trees for all files here as well? y/n ")
    if yn == 'y':
        for f in range(len(files)):
            print("\n")
            print("Method tree for file " + files[f])
            for s in all_method_trees[f]:
                print(s)
                
        print("\n\n")
    else:
        pass
else:
    pass

yn = input("Do you want to run Module - Pep8 format verification? y/n ")
if yn == 'y':
    pep8_verify(files)
else:
    pass

yn = input("Do you want to run Module - Python 2 to Python 3 Conversion? y/n ")
if yn == 'y':
    py2to3_conversion(files)
else:
    pass
    
print("\nThanks for using our script! :)")