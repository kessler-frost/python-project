# format class 1 : class name(params)
# format class 2 : class name
# format func origin : def name(params)
# format func called : name(params)


import re


def get_methods(filename):

    class_names, function_names, method_tree, check = [], [], [], 0

    for code in open(filename, encoding="utf-8").read().split("\n"):

        cn = re.findall(r"\s*class\s+(\w+)|\s*class\s+(\w+)\(.*\)", code)
        fn = re.findall(r"\s*def\s+(\w+)\(.*\):", code)
        cs = re.findall(r"\s*class\s+\w+\(.*\)|\s*class\s+\w+", code)
        fs = re.findall(r"\s*def\s+\w+\(.*\)", code)
        fc = re.findall(r"(\w*)\(", code)

        if len(cn) != 0:
            check = 1
            class_names.append(cn[0])
            method_tree.append(cs[0])
        if len(fn) != 0:
            check = 1
            function_names.append(fn[0])
            method_tree.append(fs[0])
            indentation = re.match(r"(\s*).*", fs[0]).groups()[0] + "\t"
        if check == 0 and len(fc) != 0 and fc[0] != '':
            for func in fc:
                method_tree.append(indentation + "calls function " + str(func))
        check = 0

    return method_tree, class_names, function_names
