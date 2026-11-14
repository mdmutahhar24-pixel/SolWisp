import shlex
import math


storedVariables = dict()


specialVals = {"Pi": math.pi, "EulersNumber": math.e, "ImaginaryUnit": 1j, "Tau": (2 * math.pi), "PytagoreasConstant": (2 ** 0.5), "TheodorusConstant": (3 ** 0.5), "GoldenRatio": ((1 + math.sqrt(5))/2)}




def valNumReturn(val):
    try:
        return int(val)
    except ValueError:
        pass


    try:
        return float(val)
    except ValueError:
        raise ValueError("Not a number")


def checkVals(val):
    if (storedVariables.get(val) != None):
        return storedVariables.get(val)
    elif (specialVals.get(val) != None):
        return specialVals.get(val)
    else:
        return val


with open("main.sw", "r") as file:
    content = file.read()
    lines = content.splitlines()
    indentPostStatement = 0
    for inputCommands in lines:
        inputCommands = shlex.split(inputCommands)
        for command in inputCommands:
            match command:
                case "Say":
                    val = inputCommands.index("Say")
                    print(checkVals(inputCommands[idx + 1]))
                case "Set":
                    idx = inputCommands.index("Set")
                    varName = inputCommands[idx + 1]
                    if (len(inputCommands) > idx + 3 and inputCommands[idx + 2] == 'to'):
                        if (specialVals.get(inputCommands[idx + 3]) != None):
                            storedVariables[varName] = specialVals.get(inputCommands[idx + 3])
                        else:
                            storedVariables[varName] = inputCommands[idx + 3]
                    else:
                        if (len(inputCommands) > idx + 5 and inputCommands[idx + 2] == 'to'):
                            signs = ['+', "-", "*", "/", "//", "%"]
                            foundOperation = None
                            for i in signs:
                                if (i in inputCommands):
                                    foundOperation = i
                            prevNum = valNumReturn(inputCommands.index(foundOperation - 1))
                            afterNum = valNumReturn(inputCommands.index(foundOperation + 1))
                            if (foundOperation == "+"):
                                storedVariables[varName] = prevNum + afterNum
                            if (foundOperation == '-'):
                                storedVariables[varName] = prevNum - afterNum
                            if (foundOperation == '*'):
                                storedVariables[varName] = prevNum * afterNum
                            if (foundOperation == '/'):
                                storedVariables[varName] = prevNum / afterNum
                            if (foundOperation == '//'):
                                storedVariables[varName] = prevNum // afterNum
                            if (foundOperation == '%'):
                                storedVariables[varName] = prevNum % afterNum
                        storedVariables[varName] = None
                case "Ask":
                    idx = inputCommands.index("Ask")
                    prompt = inputCommands[idx + 1]
                    if (len(inputCommands) > idx + 3 and inputCommands[idx + 2] == "to"):
                        print(prompt)
                        val = input()
                        storedVariables[inputCommands[idx + 3]] = val
                case "Add":
                    idx = inputCommands.index("Add")
                    addedValue = checkVals(inputCommands[idx + 1])
                    if (len(inputCommands) > idx + 3 and inputCommands[idx + 2] == 'to'):
                        varVal = storedVariables.get(inputCommands[idx + 3])
                        if (varVal != None):
                            storedVariables[inputCommands[idx + 3]] = valNumReturn(varVal) + valNumReturn(addedValue)
                        else:
                            raise ValueError("Could not find variable")
                case "Subtract":
                    idx = inputCommands.index("Subtract")
                    addedValue = checkVals(inputCommands[idx + 1])
                    if (len(inputCommands) > idx + 3 and inputCommands[idx + 2] == 'from'):
                        varVal = storedVariables.get(inputCommands[idx + 3])
                        if (varVal != None):
                            storedVariables[inputCommands[idx + 3]] = valNumReturn(varVal) - valNumReturn(addedValue)
                        else:
                            raise ValueError("Could not find variable")
                case "Multiply":
                    idx = inputCommands.index("Multiply")
                    addedValue = checkVals(inputCommands[idx + 1])
                    if (len(inputCommands) > idx + 3 and inputCommands[idx + 2] == 'to'):
                        varVal = storedVariables.get(inputCommands[idx + 3])
                        if (varVal != None):
                            storedVariables[inputCommands[idx + 3]] = valNumReturn(varVal) * valNumReturn(addedValue)
                        else:
                            raise ValueError("Could not find variable")
                case "Divide":
                    idx = inputCommands.index("Divide")
                    addedValue = checkVals(inputCommands[idx + 1])
                    if (len(inputCommands) > idx + 3 and inputCommands[idx + 2] == 'from'):
                        varVal = storedVariables.get(inputCommands[idx + 3])
                        if (varVal != None):
                            storedVariables[inputCommands[idx + 3]] = valNumReturn(varVal) / valNumReturn(addedValue)
                        else:
                            raise ValueError("Could not find variable")
                case "IntegerDivision":
                    idx = inputCommands.index("IntegerDivision")
                    addedValue = checkVals(inputCommands[idx + 1])
                    if (len(inputCommands) > idx + 3 and inputCommands[idx + 2] == 'from'):
                        varVal = storedVariables.get(inputCommands[idx + 3])
                        if (varVal != None):
                            storedVariables[inputCommands[idx + 3]] = int(valNumReturn(varVal) // valNumReturn(addedValue))
                        else:
                            raise ValueError("Could not find variable")
                case "Modulo":
                    idx = inputCommands.index("Modulo")
                    addedValue = checkVals(inputCommands[idx + 1])
                    if (len(inputCommands) > idx + 3 and inputCommands[idx + 2] == 'from'):
                        varVal = storedVariables.get(inputCommands[idx + 3])
                        if (varVal != None):
                            storedVariables[inputCommands[idx + 3]] = valNumReturn(varVal) % valNumReturn(addedValue)
                        else:
                            raise ValueError("Could not find variable")
                case "Exponent":
                    idx = inputCommands.index("Exponent")
                    addedValue = checkVals(inputCommands[idx + 1])
                    if (len(inputCommands) > idx + 3 and inputCommands[idx + 2] == 'to'):
                        varVal = storedVariables.get(inputCommands[idx + 3])
                        if (varVal != None):
                            storedVariables[inputCommands[idx + 3]] = valNumReturn(varVal) ** valNumReturn(addedValue)
                        else:
                            raise ValueError("Could not find variable")
                case "If":
                    idx = inputCommands.index('If')