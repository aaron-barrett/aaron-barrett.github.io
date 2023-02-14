import runpy
import os

path = "html_generators"
dir_list = [ f for f in os.listdir(path) if f.endswith(".py") and "run" not in f]
for f in dir_list:
    print("Running: ", f)
    runpy.run_path(os.path.join( path , f))