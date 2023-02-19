import os 

if (os.path.basename(os.getcwd()) != "math"):
    while (os.path.basename(os.getcwd()) != "aaron-barrett.github.io"):
        os.chdir("../")
    os.chdir("math")
dir_list = [ f for f in os.listdir("tex") if f.endswith(".tex") and "header" not in f]
for f in dir_list:
    name = os.path.splitext(f)
    os.system("pandoc tex/" + f + " --mathjax -o pandoc_html/" + name[0] + ".html")
    