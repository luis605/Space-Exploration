'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import os

exec_from_main = "game/data/game.txt"
exec_from_version = "../../data/game.txt"
try:
    file_name = exec_from_main
    file_read = open( file_name, "r" )
except FileNotFoundError as FileNotFound_e:
    file_name = exec_from_version
    file_read = open( file_name, "r" )

  

# asking the user to enter the string to be 
# searched
text = "version: "
  
lines = file_read.readlines()
  
new_list = []
idx = 0
  
for line in lines:
          
 
    if text in line:
        new_list.insert(idx, line)
        idx += 1
  
    file_read.close()
  

if len(new_list)==0:
    #print("\n\"" +text+ "\" is not found in \"" +file_name+ "\"!")
    pass
else:
  

    lineLen = len(new_list)
    #print("\n**** Lines containing \"" +text+ "\" ****\n")
    for i in range(lineLen):
        end=new_list[i]
##    print()

version = ' '.join(new_list)
my_string=str(version)
game_version = my_string.split("version: ",1)[1]
