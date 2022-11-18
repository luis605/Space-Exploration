import csv
import sys
import time
import pandas as pd
import os

dragon_loot = []

inventory_path = 'export.csv'

def readCSV():
    global mylist
    mylist = []
    
    with open(inventory_path) as f:
        reader = csv.reader(f)
        mylist = dict(reader)

    mylist.pop("item_name")
    keys_ls = [key for key, val in mylist.items()]

    for count, i in enumerate(keys_ls):
        if i.isnumeric():
            b = int(i)

            keys_ls[count] = b
            print(keys_ls)

    mylist = keys_ls
    mylist = list(mylist)

##    for count, value in enumerate(mylist.keys()):
##        print(mylist[str(value).key])
        

    print("csv to list:",mylist)

    return mylist

if os.path.exists(inventory_path) and os.path.getsize(inventory_path) > 0:
    readCSV()
else:
    mylist = {}

def writeCSV(amount, item):
    amount = str(amount)
    item = str(item)
    with open(inventory_path, 'w') as csvfile:
        fieldnames = ['item_name', 'item_amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'item_name': item, 'item_amount': amount})

def changeCSV(valueToReplace, amount, item):

    for line in open(inventory_path, inplace=True):
        # do what you need to do and then just print:
        print (line.replace(str(1)), str(2))

##    
##    with open(rinventory_path, 'w') as file:
##
##        file.write(data)
##      
##    print("Text changed")



    
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
##import_inventory(mylist)    
displayInventory(mylist)

def addItem(whatToAdd):
    try:
        mylist[whatToAdd] += 1
    except KeyError:
        mylist[whatToAdd] = 1

    mylist[whatToAdd] = (mylist[whatToAdd])
        
    addToInventory(mylist,dragon_loot)

    writeCSV(whatToAdd, mylist[whatToAdd])#f.write(str(mylist))

    displayInventory(mylist)


def removeItem(whatToRemove):
    mylist[whatToRemove] -= 1


    writeCSV(whatToRemove, mylist[whatToRemove])#f.write(str(mylist))


    displayInventory(mylist)

def changeQuantity(whatToChange, quantity):
    try:
        mylist[whatToChange] += int(quantity)
    except KeyError:
        mylist[whatToChange] = int(quantity)

    value_to_replace = mylist[whatToChange]

    mylist[whatToChange] = int(quantity)

    changeCSV(value_to_replace, quantity, whatToChange)

    displayInventory(mylist)


def overwriteQuantity(whatToChange, quantity):
    mylist[whatToChange] = int(quantity)

    f.write(str(mylist))

    displayInventory(mylist)


def delItem(whatToChange):

    del mylist[whatToChange]


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
            csvfile.close()
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

        
if __name__ == "__main__":
    user_input()
    
f.close()






