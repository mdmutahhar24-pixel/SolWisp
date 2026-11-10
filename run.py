import shlex

commands = shlex.split(input())

variables = dict()

while "break" not in commands:
    for command in commands:
        match command:
            case "Say":
                idx = commands.index("Say")
                varCheck = variables.get(commands[idx + 1])
                if (varCheck == None):
                    print(commands[idx + 1])
                else:
                    print(varCheck)

            case "Integer":
                idx = commands.index("Integer")
                varName = commands[idx + 2]

                if commands[idx + 4].isdigit():
                    val = int(commands[idx + 4])
                    variables[varName] = val
                else:
                    raise ValueError("Wrong Type Assignment")

            case "Float":
                idx = commands.index("Float")
                varName = commands[idx + 2]

                try:
                    val = float(commands[idx + 4])
                except ValueError:
                    raise ValueError("Wrong Assignment Type")
                variables[varName] = val

            case "String":
                idx = commands.index("String")
                varName = commands[idx + 2]

                val = commands[idx + 4]
                variables[varName] = val 

            case "Boolean":
                idx = commands.index("Boolean")
                varName = commands[idx + 2]

                if commands[idx + 4] in ["True", "False"]:
                    val = commands[idx + 4] == "True"
                    variables[varName] = val
                else:
                    raise ValueError("Wrong Type Assignment")

    commands = shlex.split(input())