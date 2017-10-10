# format class 1 : class name(params)
# format class 2 : class name
# format func origin : def name(params)
# format func called 1 : name(params)
# format func called 2 : name(name(params))


import re
from nltk.tokenize import word_tokenize

def preprocess(code):
    return re.sub(r"\".*\"", code, "")


def get_parenthesis_lis(code):
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


def get_methods(filename):

    class_names, function_names, method_tree, check = [], [], [], 0
    indentation = ""

    for code in open(filename, encoding="utf-8").read().split("\n"):

        code = preprocess(code)

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
                parenthesis = get_parenthesis_lis(code)
                indented_functions = indent_functions(fc, parenthesis, indentation)
                for function in indented_functions:
                    method_tree.append(function)
            check = 0

    return method_tree, class_names, function_names
