import get_methods as gm


def get_method_source(filename_list, name_source_file):
    store = open(name_source_file, "w", encoding="utf-8")
    methods = []
    for filename in filename_list:
        dummy, name_one, name_two = gm.get_methods(filename)
        for name in name_one:
            methods.append(name)
        for name in name_two:
            methods.append(name)
    max_width = max(len(method_name) for method_name in methods)
    store.write("NAME".ljust(max_width + 5) + "TYPE\t\t\t" + "LOCATION" + "\n\n\n")
    for filename in filename_list:
        method_tree, class_names, function_names = gm.get_methods(filename)
        for class_name in class_names:
            store.write(str(class_name).ljust(max_width + 5) + "class\t\t\t" + str(filename) + "\n")
        for function_name in function_names:
            store.write(str(function_name).ljust(max_width + 5) + "function\t\t" + str(filename) + "\n")
        store.write("\n\n")
    store.close()

# filename_list = ["sample.txt", "other.txt"]
# get_method_source(filename_list, "source_table.txt")
