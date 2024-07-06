import re


def solve(path):
    count = 0
    file = open(path)
    for i in file.readlines():
        if not re.match('^#.*$', i.strip()) and i != '\n' and not re.match('^\s*#.*$', i.strip()):
            count += 1

    return count


input_value = input('please enter your relative address of python file >>>')
print(solve(input_value))
