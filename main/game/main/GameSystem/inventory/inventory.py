'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

# Imports
import csv
import sys
import time
import pandas as pd
import os
import json


# Vars Declaration
global mylist, inventory_path
mylist = {}
inventory_path = 'game/data/inventory.txt'
json_path = 'game/data/inventory.json'
dragon_loot = []


# File Handling


def import_inventory():
    with open(json_path) as json_file:
        mylist_1 = json.load(json_file)

        # printing original string 
        mylist_2 = str(mylist_1)
          
        # using json.loads() method
        global mylist
        mylist = json.loads(mylist_2)
        print(mylist, "\n\n\n")
     

def save_to_inventory():
    with open(json_path, 'w') as fp:
        json_object = json.dumps(mylist, indent = 4) 
        json.dump(json_object, fp)



    

# Dictionary Manipulation
def displayInventory(inventory):
    print('    ','Inventory:')
    print(' ''Count', ' ', 'Item Name' )
    print('- - - - - - - - - - -')
    item_total=0
    for k,v in mylist.items():
        print(' ',str(v)+'      '+k)
        item_total=sum(mylist.values())
    print('- - - - - - - - - - -')
    print('Total number of items: '+ str(item_total))



def addToInventory(inventory,addedItems):
    for v in addedItems:
        if v in inventory.keys():
            inventory[v]+=1
        else:
            inventory[v]=1

    save_to_inventory()


def removeFromInventory(inventory,addedItems):
    for v in addedItems:
        if v in inventory.keys():
            inventory[v]-=1
        else:
            inventory[v]=1

    save_to_inventory()







def addItem(whatToAdd):
    try:
        mylist[whatToAdd] += 1
    except KeyError:
        mylist[whatToAdd] = 1
    addToInventory(mylist,dragon_loot)

    displayInventory(mylist)

    save_to_inventory()

def removeItem(whatToRemove):
    try:
        mylist[whatToRemove] -= 1
    except KeyError:
        pass

    displayInventory(mylist)

    save_to_inventory()

def changeQuantity(whatToChange, quantity):
    try:
        mylist[whatToChange] += int(quantity)
    except KeyError:
        mylist[whatToChange] = int(quantity)

    displayInventory(mylist)

    save_to_inventory()


def getQuantity(item):
    print(mylist[item])
    return mylist[item]

def overwriteQuantity(whatToChange, quantity):
    mylist[whatToChange] = int(quantity)

    displayInventory(mylist)

    save_to_inventory()

def delItem(whatToChange):

    del mylist[whatToChange]

    displayInventory(mylist)



    save_to_inventory()



# Inputs Handler
def user_input():
    while 1:
        task = int(input(text))
        if task == 1:
            whatToChange = input("Item Name: ")
            delItem(whatToChange)
            
        elif task == 2:
            whatToRemove = str(input("Item To Remove: "))
            removeItem(whatToRemove)
            
        elif task == 3:
            whatToAdd = str(input("Item To Add: "))
            addItem(whatToAdd)
            
        elif task == 4:
            whatToChange = input("Item Name: ")
            quantity = int(input("Quantity: "))
            changeQuantity(whatToChange, quantity)
            
        elif task == 5:
            whatToChange = input("Item Name: ")
            quantity = input("Item Value: ")
            overwriteQuantity(whatToChange, quantity)

        elif task == 6:
            item = input("Item Name: ")
            getQuantity(item)
            
        elif task == 0:
            break
        else:
            print("Please reenter int value")
            time.sleep(1)




    
text = """

Type: `quit` to exit [value: 0]
--------------------------
Delete from inventory[1]:
Remove from inventory[2]:
Add to inventory[3]:
Change Quantity[4]:
Overwrite Quantity[5]:

== SPECIAL ==
Get Quantity[6]:

Input[1/2/3/4/5]: """
        
if __name__ == "__main__":
    inventory_path = '../../../data/inventory.txt'
    json_path = '../../../data/inventory.json'

    user_input()
    


if not os.path.exists(inventory_path) or os.stat(path_of_file).st_size == 0:
    open(json_path, 'w')
    save_to_inventory()



###
import_inventory()
displayInventory(mylist)
###

