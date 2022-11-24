import csv
import sys
import time
import pandas as pd


mylist = {}
dragon_loot = []


def import_inventory(mylist):
    with open('my_file.csv') as mylist:
        reader = csv.DictReader(mylist)
        mylist = reader
            
        
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


def removeFromInventory(inventory,addedItems):
    for v in addedItems:
        if v in inventory.keys():
            inventory[v]-=1
        else:
            inventory[v]=1


addToInventory(mylist,dragon_loot)
import_inventory(mylist)    
displayInventory(mylist)

def addItem(whatToAdd):
    try:
        mylist[whatToAdd] += 1
    except KeyError:
        mylist[whatToAdd] = 1
    addToInventory(mylist,dragon_loot)

    f.write(str(mylist))

    displayInventory(mylist)

def removeItem(whatToRemove):
    try:
        mylist[whatToRemove] -= 1
    except KeyError:
        pass

    f.write(str(mylist))


    displayInventory(mylist)

def changeQuantity(whatToChange, quantity):
    try:
        mylist[whatToChange] += int(quantity)
    except KeyError:
        mylist[whatToChange] = int(quantity)

    f.write(str(mylist))

    displayInventory(mylist)


def overwriteQuantity(whatToChange, quantity):
    mylist[whatToChange] = int(quantity)

    f.write(str(mylist))

    displayInventory(mylist)


def delItem(whatToChange):

    del mylist[whatToChange]

    f.write(str(mylist))


    displayInventory(mylist)







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
            
        elif task == 0:
            f.close()
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

Input[1/2/3/4/5]: """

f = open('inventory_elements.csv', 'w')
        
if __name__ == "__main__":
    user_input()
    
f.close()






