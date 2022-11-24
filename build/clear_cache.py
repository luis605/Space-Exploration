import os

os.chdir("../")
os.popen('find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf')
