from os import chdir, getcwd, listdir, path
from importlib import import_module

chdir(getcwd()+"/happypants/blueprints")
blueprints = [bp for bp in listdir() if path.isdir(bp) and bp != "__pycache__"]
chdir("..")
chdir("..")
liste = listdir("/home/happypants/Documents/PythonProjects/Flask/HP-first-website/happypants/blueprints")
print(blueprints)
bps = []
for bp in blueprints:
    bps.append(import_module("happypants.blueprints."+bp))

