from pystyle import *
import zlib, re, os
dark = Col.dark_gray
light = Col.light_gray
purple = Colors.StaticMIX((Col.purple, Col.blue))
bpurple = Colors.StaticMIX((Col.purple, Col.cyan))

# The print is from billythegoat356 ( credits to him )

def p(text):
    # sleep(0.05)
    return print(stage(text))

def stage(text: str, symbol: str = '.', col1 = light, col2 = None) -> str:
    if col2 is None:
        col2 = light if symbol == '.' else purple
    return f""" {Col.Symbol(symbol, col1, dark)} {col2}{text}{Col.reset}"""



file = input(stage(f"Drag the file you want to deobfuscate {dark}-> {Col.reset}", "?", col2 = bpurple)).replace('"','').replace("'","")
p(f"Reading file")
with open(file) as f:
    script = f.read()
try:
    script = script[script.index("b'"):script.rindex("))")]
    script = zlib.decompress(eval(script)).decode()
except:
    p("The script is camouflated, please wait for the next update or if you have a brain scroll to the right\nand put every b'code' into one big one, \nso your end result will be (b'big code here')) (yes with to closing brackets at the end) and then run the script again.")
    exit()
#print(script)
p("got encrypted code")

lines0 = script.split("\n")

lines = []
lines.clear()
for line in lines0:
    if len(re.sub(r"\s", "", line)) > 0:
        lines.append(line)
name = eval(lines[0].split("=")[0][9:-1])
for i in range(len(lines)):
    lines[i] = re.sub(fr"^{name}(\W)", r"globals\1", re.sub(fr"(\W){name}(\W)", r"\1globals\2", lines[i]))
lines.pop(0)
p("Replacing globals")
try:
    os.remove("temp.py")
    os.remove("out.py")
    os.remove("code.py")
    os.remove("vars.py")
except:pass


for line in lines:

    with open("temp.py", "a+") as f:
        f.write(line+"\n")
def replace(c,r):
    with open('temp.py', 'r') as file :filedata = file.read()
    filedata = filedata.replace(c, r) # i must read the file over and over again, because it updates everytime i replace something
    with open('temp.py', 'w') as file:file.write(filedata)
#x = int(input(stage(f"open temp.py and type the line where the last globals() is (its 15 in 90% of the cases) {dark}-> {Col.reset}", "?", col2 = bpurple)).replace('"','').replace("'",""))
x = 15 # ig its always 15, but not sure
llines = 0
for l in lines:
    llines += 1
    if not ".join" in l:
        if  len(l) < 150:
            var = l.split("=",1)[1]
            code = l[l.find(")")+len(")"):l.rfind("="[0])]
            try:decyrpted = eval(code)
            except:decyrpted = code
            if "vars" in l:
                code = l[l.find(")")+len(")"):l.rfind("="[0])].replace("[" , "").replace("]" , "").replace("'" , "")
                replace(str(code), "vars")
            decyrpted = str(decyrpted).replace("[" , "").replace("]" , "").replace("'" , "")
            replace(str(decyrpted), str(var))

    if llines == x: break
p("decrypted declarations")
with open("temp.py", "r") as f:
    script = f.read().splitlines()
    lines.clear()
    for line in script:
        lines.append(line)
p("reading temp.py")
llines = 0
for l in lines:
    llines += 1
    if not ".join" in l:
        if  len(l) > 150:
            var = l.split("=",1)[1]
            code = l[l.find(")")+len(")"):l.rfind("="[0])].replace("[" , "").replace("]" , "").replace("'" , "") # i could just update the rfind but....
           # print(code)
            #print(var)
            decrypted = eval(var)
            decrypted = str(decrypted)
            if "built-in" in decrypted:decrypted = decrypted.replace("<built-in function " , "").replace(">" , "") #im to lazy to get a better way to do this, it works ig 
            elif "class" in decrypted:decrypted = decrypted.replace("<class '" , "").replace("'>" , "")
            if "unhexlify" in decrypted:decrypted = "binascii.unhexlify" # we dont talk about this
            replace(str(var), str(decrypted))
            replace(str(code), str(decrypted))
    if llines == x: break
llines = 0
for i in lines:
    llines += 1
    if "from builtins import" in str(i):
        y = int(llines)
        break
p("found script start at line " + str(y))
with open("temp.py", "r") as f:
    script = f.read().splitlines()
    lines.clear()
    for line in script:
        lines.append(line)   
p("decrypted the rest")
#y = int(input(stage(f"open temp.py and type the line where the 'from builtins import ...' is {dark}-> {Col.reset}", "?", col2 = bpurple)))

llines = 0
for l in lines:
    llines += 1
    if llines < y and llines > x:
        with open("vars.py", "a+") as f:
            f.write(l+"\n")
    if llines == y: break
llines = 0
for l in lines:
    llines += 1
    if llines >= y:
        #print(l)
        with open("code.py", "a+") as f:
            f.write(l+"\n")
        if llines == len(lines): break


os.system("start pythonw deobfuscate.py") # its in a seperate file because its the code from unleqitq
print(stage("your code is in out.py", "!", col2 = purple))
x = input(stage(f"do you want to remove the temp files? (y/n) {dark}-> {Col.reset}", "?", col2 = bpurple))
if x == "y":
    try:
        os.remove("temp.py")
        os.remove("code.py")
        os.remove("vars.py")
    except:pass