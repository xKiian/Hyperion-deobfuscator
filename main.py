from pystyle import *
import zlib, re, os, base64
from time import time, sleep
from getpass import getpass
dark = Col.dark_gray
light =  Colors.StaticMIX((Col.cyan, Col.purple, Col.gray))
acc = Colors.StaticMIX((Col.cyan, Col.purple, Col.blue, Col.gray))
purple = Colors.StaticMIX((Col.purple, Col.blue))
bpurple = Colors.StaticMIX((Col.purple, Col.cyan))

# The print is from billythegoat356 ( credits to him )
def p(text):
    # sleep(0.05)
    return print(stage(text))

def stage(text: str, symbol: str = '...', col1 = light, col2 = None) -> str:
    if col2 is None:
        col2 = light if symbol == '...' else purple
    if symbol == '...' or symbol == '!!!':
        return f"""     {Col.Symbol(symbol, col1, dark)} {col2}{text}{Col.reset}"""
    else:
        return f""" {Col.Symbol(symbol, col1, dark)} {col2}{text}{Col.reset}"""

text = r"""
 ▄  █ ▀▄    ▄ █ ▄▄  ▄███▄   █▄▄▄▄ ▄█ ████▄    ▄       ██▄   ▄███▄   ████▄ ███   ▄████ ▄      ▄▄▄▄▄   ▄█▄    ██     ▄▄▄▄▀ ████▄ █▄▄▄▄ 
█   █   █  █  █   █ █▀   ▀  █  ▄▀ ██ █   █     █      █  █  █▀   ▀  █   █ █  █  █▀   ▀ █    █     ▀▄ █▀ ▀▄  █ █ ▀▀▀ █    █   █ █  ▄▀ 
██▀▀█    ▀█   █▀▀▀  ██▄▄    █▀▀▌  ██ █   █ ██   █     █   █ ██▄▄    █   █ █ ▀ ▄ █▀▀ █   █ ▄  ▀▀▀▀▄   █   ▀  █▄▄█    █    █   █ █▀▀▌  
█   █    █    █     █▄   ▄▀ █  █  ▐█ ▀████ █ █  █     █  █  █▄   ▄▀ ▀████ █  ▄▀ █   █   █  ▀▄▄▄▄▀    █▄  ▄▀ █  █   █     ▀████ █  █  
   █   ▄▀      █    ▀███▀     █    ▐       █  █ █     ███▀  ▀███▀         ███    █  █▄ ▄█            ▀███▀     █  ▀              █   
  ▀             ▀            ▀             █   ██                                 ▀  ▀▀▀                      █                 ▀    
                                                                                                             ▀                      """

System.Size(150, 47)
os.system("cls && title Hyperion Deobfuscator ^| Made by xKian and UnlegitQ")
print("\n\n")
print(Colorate.Diagonal(Colors.DynamicMIX((purple, dark)), Center.XCenter(text)))
print("\n\n")
file = input(stage(f"Drag the file you want to deobfuscate {dark}-> {Col.reset}", "?", col2 = bpurple)).replace('"','').replace("'","")
if file == "": file = "in.py"
now = time()
print("\n")
p(f"reading file")
with open(file) as f:
    script = f.read()
try:
    if not "class" in script:
        p("file is not comouflated")
        com = False
        script = script[script.index("b'"):script.rindex("))")]
    else:
        p("file is comouflated")
        com, ines = True, []
        for l in script.splitlines():
            if r"=b'" in l:
                p(f"  found code part in {acc}"+ l[:90].replace(" ",""))
                a = l[l.find("=b'")+len("=b'"):l.rfind("')")]                                                                                                                                               
                ines.append(a)
        script1 = ""   
        for l in ines:
            script1 += l
        script = f"b'{script1}'"
    script = zlib.decompress(eval(script)).decode()
except Exception as e:
    p(f"error: {Col.red}{e}{Col.reset}")
    sleep(3)
    exit()


p("got encrypted code")

lines0 = script.split("\n")

lines = []
lines.clear()
p("removing empty lines")
for line in lines0:
    if len(re.sub(r"\s", "", line)) > 0:
        lines.append(line)

p("replacing globals")
try:
    os.remove("temp.py")
    os.remove("out.py")
    os.remove("code.py")
    os.remove("vars.py")
    p("removed old files")
except:pass
if com:
    p("removing credits")  
    lines = lines[13:] # first 13 lines are credits 
p("writing second layer to temp.py")
for line in lines:
    with open("temp.py", "a+") as f:
        f.write(line+"\n")

def replace(c,r):
    p(f"replacing {acc}{c[:40]}... {light} with {r[:40]}")
    with open('temp.py', 'r') as file :filedata = file.read()
    filedata = filedata.replace(c, r) # i must read the file over and over again, because it updates everytime i replace something
    with open('temp.py', 'w') as file:file.write(filedata)
def rreplace(c,r):
    p(f"replacing {acc}{c[27:][:20]}... {light} with {r[:40]}")
    with open('out.py', 'r') as file :filedata = file.read()
    filedata = filedata.replace(c, r) # i must read the file over and over again, because it updates everytime i replace something
    with open('out.py', 'w') as file:file.write(filedata)
#x = int(input(stage(f"open temp.py and type the line where the last globals() is (its 15 in 90% of the cases) {dark}-> {Col.reset}", "?", col2 = bpurple)).replace('"','').replace("'",""))
x = 15 # ig its always 15, but not sure
llines = 0
p("replacing globals")
p("replacing vars")
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
p("replacing classes with strings")
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
p("splitting code into 2 seperate files")
p("writing variables to vars.py")
llines = 0
for l in lines:
    llines += 1
    if llines < y and llines > x:
        with open("vars.py", "a+") as f:
            f.write(l+"\n")
    if llines == y: break
llines = 0
p("writing code to code.py")
for l in lines:
    llines += 1
    if llines >= y:
        #print(l)
        with open("code.py", "a+") as f:
            f.write(l+"\n")
        if llines == len(lines): break

p("replacing vars and code")
os.system("start pythonw deobfuscate.py") # its in a seperate file because its the code from unleqitq
p("got clean src")
p("cleaning up")
sleep(1)
lines.clear()
if os.path.exists("out.py"):
    with open("out.py", "r") as f:
        script = f.read().splitlines()
        for line in script:
            lines.append(line)
else: print("error")
p("removing unhexlify stuff")
for l in lines:
    if r"binascii.unhexlify" in l and r".decode('8ftu'[::+-+-(-(+1))])" in l:
        code1 = l[l.index(".unhexlify(b'"):l.rindex(".decode('8ftu'[::+-+-(-(+1))])")]
        ccode = code1[12:]
        p(f"got unhexlify code {ccode[:-1][:30]}...")
        code = eval("__import__('binascii')"+code1+".decode('utf8')")
        rreplace(f"eval(binascii{code1}.decode('8ftu'[::+-+-(-(+1))]))", code)
        
print(stage("your code is in out.py", "!!!", col2 = purple))
now = round(time() - now, 2)
print('\n')
getpass(stage(f"Obfuscation completed succesfully in {light}{now}s{bpurple}.{Col.reset}", "?", col2 = bpurple))