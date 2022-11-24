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

  
def find(word):
    lines = file_read.readlines()
    for line in lines:
      if word in line:
        return line
    file_read.close()



version = find("version: ")

try:
    file_name = exec_from_main
    file_read = open( file_name, "r" )
except FileNotFoundError as FileNotFound_e:
    file_name = exec_from_version
    file_read = open( file_name, "r" )

    
name = find("name: ")

try:
    file_name = exec_from_main
    file_read = open( file_name, "r" )
except FileNotFoundError as FileNotFound_e:
    file_name = exec_from_version
    file_read = open( file_name, "r" )


type_game = find("type: ")

##version = ' '.join(new_list)
version_string=str(version)
game_version = version_string.split("version: ",1)[1]
print(game_version)


name_string=str(name)
game_name = name_string.split("name: ",1)[1]
print(game_name)


type_string=str(type_game)
game_type = type_string.split("type: ",1)[1]
print(game_type)
