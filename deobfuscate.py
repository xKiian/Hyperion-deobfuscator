import binascii
import os
# by Unleqitq
def deobf(line: str) -> str:
	name0, val0 = line.split("=")
	index = name0.index("[")
	name = eval(name0[index+1:-1])
	try:
		val = eval(val0)
		if (type(val)==str):
			return name+"='"+val.replace("\\", "\\\\").replace("'", "\\'").replace("\n","\\n")+"'"
		if (type(val)==int or type(val) == float or type(val) == bool):
			return name+"="+str(val)
	except:
		pass
	return name+"="+val0

lines = []
fname = "vars.py"
with open(fname) as file:
	lines = file.read().split("\n")

try:
	os.remove(fname)
except:
	pass

with open(fname, "a") as file:
	for line in lines:
		try:
			file.write(deobf(line)+"\n")
		except:
			file.write(line+"\n")
import os
variables = {}
variableNames = []

with open(fname) as file:
    lines = file.read().split("\n")
    for line in lines:
        try:
            name, val = line.split("=", 1)
            variables[name] = val
            variableNames.append(name)
        except:
            pass

variableNames.sort(key=len, reverse=True)

with open("code.py") as file:
    code = file.read()

for name in variableNames:
    code = code.replace(name, variables[name])

with open("out.py", 'w') as file:
    file.write(code)
