inputName = input("input: ")
print(type(inputName))
outputName = inputName.replace('.', '')
outputName = outputName.replace(' ', '')
outputName = 'P' + outputName

print(outputName)
