# format 1 : import library1, library2
# format 2 : from library import class
# format 3 : from library.class import function
# format 4 : import library as library

import sys
import re

input_file = sys.argv[1]

libraries = []

for code in open(input_file).read().split("\n"):

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

print(list(set(libs)))

