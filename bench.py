#!/usr/bin/env python3
import jinja2
import sys
import os
from shutil import copyfile
try:
    os.mkdir('build')
except:
    pass

num = int(sys.argv[1])
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
make_template = templateEnv.get_template("Makefile")
code_template = templateEnv.get_template("bench.c")

base = os.getcwd() + "/build/"
files = ["test" + str(num)];
for i in range(1, num):
    with open("{}test{}.c".format(base, i), "w") as outfile:
        outfile.write(code_template.render(next_num=str(i+1), base=base))
        files.append("test" + str(i))
with open(base + "Makefile", "w") as makefile:
    makefile.write(make_template.render(files=files))

copyfile("end.c", base + "test" + str(num) + ".c")
