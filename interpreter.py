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

                if commands[idx + 1] == "set" and commands[idx + 3] == "to":
                    if commands[idx + 4].isdigit():
                        val = int(commands[idx + 4])
                        variables[varName] = val
                    else:
                        raise ValueError("Wrong Type Assignment")
                else:
                    raise ValueError(f"Unknown variable operator: {commands[idx + 1]}, {commands[idx + 3]}")

            case "Float":
                idx = commands.index("Float")
                varName = commands[idx + 2]

                if commands[idx + 1] == "set" and commands[idx + 3] == "to":
                    try:
                        val = float(commands[idx + 4])
                    except ValueError:
                        raise ValueError("Wrong Assignment Type")
                    variables[varName] = val
                else:
                    raise ValueError(f"Unknown variable operator: {commands[idx + 1]}, {commands[idx + 3]}")

            case "String":
                idx = commands.index("String")
                varName = commands[idx + 2]

                if (commands[idx + 1] == "set" and commands[idx + 3] == "to"):
                    val = commands[idx + 4]
                    variables[varName] = val
                else:
                    raise ValueError(f"Unknown variable operator: {commands[idx + 1]}, {commands[idx + 3]}")

            case "Boolean":
                idx = commands.index("Boolean")
                varName = commands[idx + 2]

                if commands[idx + 1] == "set" and commands[idx + 3] == "to":
                    if commands[idx + 4] in ["True", "False"]:
                        val = commands[idx + 4] == "True"
                        variables[varName] = val
                    else:
                        raise ValueError("Wrong Type Assignment")
                else:
                    raise ValueError(f"Unknown variable operator: {commands[idx + 1]}, {commands[idx + 3]}")

            case "Input":
                pass

            case ">>":
                pass

            case "if":
                pass

            case "Import":
                pass

    commands = shlex.split(input())