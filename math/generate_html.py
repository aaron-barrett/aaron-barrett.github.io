import os 

path = "tex"
dir_list = [ f for f in os.listdir(path) if f.endswith(".tex") and "header" not in f]
for f in dir_list:
    name = os.path.splitext(f)
    os.system("pandoc " + path + "/" + f + " --mathjax -o html/" + name[0] + ".html")
    