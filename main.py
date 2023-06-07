from pystyle import *
import zlib
import re
import os
import base64
from time import time, sleep
from getpass import getpass

dark = Col.dark_gray
light = Colors.StaticMIX((Col.cyan, Col.purple, Col.gray))
acc = Colors.StaticMIX((Col.cyan, Col.purple, Col.blue, Col.gray))
purple = Colors.StaticMIX((Col.purple, Col.blue))
bpurple = Colors.StaticMIX((Col.purple, Col.cyan))


def p(text):
    # sleep(0.05)
    return print(stage(text))


def stage(text: str, symbol: str = '...', col1=light, col2=None) -> str:
    if col2 is None:
        col2 = light if symbol == '...' else purple
    if symbol in {'...', '!!!'}:
        return f"""     {Col.Symbol(symbol, col1, dark)} {col2}{text}{Col.reset}"""
    else:
        return f""" {Col.Symbol(symbol, col1, dark)} {col2}{text}{Col.reset}"""


import contextlib
import pathlib

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

file = input(stage(f"Drag the file you want to deobfuscate {dark}-> {Col.reset}", "?", col2=bpurple)).replace('"', '').replace("'", "")
if file == "":
    file = "in.py"

now = time()
print("\n")
p("reading file")
script = pathlib.Path(file).read_text()

try:
    if "class" not in script:
        p("file is not camouflated")
        com = False
        script = script[script.index("b'"):script.rindex("))")]
    else:
        p("file is camouflated")
        com, lines = True, []
        for line in script.splitlines():
            if r"=b'" in line:
                p(f"  found code part in {acc}" + line[:90].replace(" ", ""))
                a = line[line.find("=b'") + len("=b'"):line.rfind("')")]
                lines.append(a)
        script1 = "".join(lines)
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
lines.extend(line for line in lines0 if len(re.sub(r"\s", "", line)) > 0)
p("replacing globals")

with contextlib.suppress(Exception):
    os.remove("temp.py")
    os.remove("out.py")
    os.remove("code.py")
    os.remove("vars.py")
    p("removed old files")

if com:
    p("removing credits")
    lines = lines[13:]  # first 13 lines are credits

p("writing second layer to temp.py")
for line in lines:
    with open("temp.py", "a+") as f:
        f.write(line + "\n")


def replace(c, r):
    p(f"replacing {acc}{c[:40]}... {light} with {r[:40]}")
    with open('temp.py', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace(c, r)
    with open('temp.py', 'w') as file:
        file.write(filedata)


def rreplace(c, r):
    p(f"replacing {acc}{c[27:][:20]}... {light} with {r[:40]}")
    with open('out.py', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace(c, r)
    with open('out.py', 'w') as file:
        file.write(filedata)


x = 15  # assuming it's always 15, but not sure
llines = 0
p("replacing globals")
p("replacing vars")
for line in lines:
    llines += 1
    if ".join" not in line:
        if len(line) < 150:
            var = line.split("=", 1)[1]
            code = line[line.find(")") + len(")"):line.rfind("="[0])]
            try:
                decrypted = eval(code)
            except:
                decrypted = code
            if "vars" in line:
                code = line[line.find(")") + len(")"):line.rfind("="[0])].replace("[", "").replace("]", "").replace("'", "")
                replace(str(code), "vars")
            decrypted = str(decrypted).replace("[", "").replace("]", "").replace("'", "")
            replace(decrypted, str(var))

    if llines == x:
        break

p("decrypted declarations")
with open("temp.py", "r") as f:
    script = f.read().splitlines()
    lines.clear()
    for line in script:
        lines.append(line)

p("replacing classes with strings")
llines = 0
for line in lines:
    llines += 1
    if ".join" not in line:
        if len(line) > 150:
            var = line.split("=", 1)[1]
            code = line[line.find(")") + len(")"):line.rfind("="[0])].replace("[", "").replace("]", "").replace("'", "")
            decrypted = eval(var)
            decrypted = str(decrypted)
            if "built-in" in decrypted:
                decrypted = decrypted.replace("<built-in function ", "").replace(">", "")
            elif "class" in decrypted:
                decrypted = decrypted.replace("<class '", "").replace("'>", "")
            if "unhexlify" in decrypted:
                decrypted = "binascii.unhexlify"
            replace(str(var), decrypted)
            replace(str(code), decrypted)
    if llines == x:
        break

llines = 0
for i in lines:
    llines += 1
    if "from builtins import" in str(i):
        y = llines
        break

p(f"found script start at line {str(y)}")

with open("temp.py", "r") as f:
    script = f.read().splitlines()
    lines.clear()
    for line in script:
        lines.append(line)

p("splitting code into 2 separate files")
p("writing variables to vars.py")
llines = 0
for line in lines:
    llines += 1
    if llines < y and llines > x:
        with open("vars.py", "a+") as f:
            f.write(line + "\n")
    if llines == y:
        break

llines = 0
p("writing code to code.py")
for line in lines:
    llines += 1
    if llines >= y:
        with open("code.py", "a+") as f:
            f.write(line + "\n")
        if llines == len(lines):
            break

p("replacing vars and code")
os.system("start pythonw deobfuscate.py")
p("got clean src")
p("cleaning up")
sleep(1)
lines.clear()
if os.path.exists("out.py"):
    with open("out.py", "r") as f:
        script = f.read().splitlines()
        for line in script:
            lines.append(line)
else:
    print("error")

p("removing unhexlify stuff")
for line in lines:
    if r"binascii.unhexlify" in line and r".decode('8ftu'[::+-+-(-(+1))])" in line:
        code1 = line[line.index(".unhexlify(b'"):line.rindex(".decode('8ftu'[::+-+-(-(+1))])")]
        ccode = code1[12:]
        p(f"got unhexlify code {ccode[:-1][:30]}...")
        code = eval(f"__import__('binascii'){code1}.decode('utf8')")
        rreplace(f"eval(binascii{code1}.decode('8ftu'[::+-+-(-(+1))]))", code)

print(stage("your code is in out.py", "!!!", col2=purple))
now = round(time() - now, 2)
print('\n')
getpass(stage(f"Obfuscation completed successfully in {light}{now}s{bpurple}.{Col.reset}", "?", col2=bpurple))
