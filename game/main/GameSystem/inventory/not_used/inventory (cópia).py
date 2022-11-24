import sys
import time
import pandas as pd
import os


class UseInventory():
    def __init__(self):
        #global self.mylist, self.inventory_path
        self.mylist = {}
        self.inventory_path = 'inventory.txt'
        self.dragon_loot = []

        if not os.path.exists(self.inventory_path):
            open('inventory.txt', 'w')
            self.mylist = {}

        self.import_inventory()    
        self.displayInventory(self.mylist)

        self.f = open('inventory.txt', 'w')

        
    def import_inventory(self):
        with open('inventory.txt', 'r') as reader:
            contents = reader.read()
            print(contents)

            reader.close()



    def save_to_inventory(self):
        with open('inventory.txt', 'w') as f:
            self.f.write(str(self.mylist))


    def displayInventory(self, inventory):
        print('    ','Inventory:')
        print(' ''Count', ' ', 'Item Name' )
        print('- - - - - - - - - - -')
        item_total=0
        for k,v in self.mylist.items():
            print(' ',str(v)+'      '+k)
            item_total=sum(self.mylist.values())
        print('- - - - - - - - - - -')
        print('Total number of items: '+ str(item_total))

    def addToInventory(self, inventory,addedItems):
        for v in addedItems:
            if v in inventory.keys():
                inventory[v]+=1
            else:
                inventory[v]=1

        self.save_to_inventory()


    def removeFromInventory(self, inventory,addedItems):
        for v in addedItems:
            if v in inventory.keys():
                inventory[v]-=1
            else:
                inventory[v]=1

        save_to_inventory()



    def addItem(self, whatToAdd):
        try:
            self.mylist[whatToAdd] += 1
        except KeyError:
            self.mylist[whatToAdd] = 1
        self.addToInventory(self.mylist,self.dragon_loot)

        self.f.write(str(self.mylist))

        self.displayInventory(self.mylist)

        self.save_to_inventory()

    def removeItem(self, whatToRemove):
        try:
            self.mylist[whatToRemove] -= 1
        except KeyError:
            pass

        self.f.write(str(self.mylist))


        self.displayInventory(self.mylist)

        self.save_to_inventory()

    def changeQuantity(self, whatToChange, quantity):
        try:
            self.mylist[whatToChange] += int(quantity)
        except KeyError:
            self.mylist[whatToChange] = int(quantity)

        self.f.write(str(self.mylist))

        self.displayInventory(self.mylist)

        self.save_to_inventory()

    def overwriteQuantity(self, whatToChange, quantity):
        self.mylist[whatToChange] = int(quantity)

        self.f.write(str(self.mylist))

        self.displayInventory(self.mylist)

        self.save_to_inventory()

    def delItem(self, whatToChange):

        del self.mylist[whatToChange]

        self.f.write(str(self.mylist))


        self.displayInventory(self.mylist)



        self.save_to_inventory()




def user_input():
    Inventory=UseInventory()
    while 1:
        task = int(input(text))
        if task == 1:
            whatToChange = input("Item Name: ")
            Inventory.delItem(whatToChange)
            
        elif task == 2:
            whatToRemove = str(input("Item To Remove: "))
            Inventory.removeItem(whatToRemove)
            
        elif task == 3:
            whatToAdd = str(input("Item To Add: "))
            Inventory.addItem(whatToAdd)
            
        elif task == 4:
            whatToChange = input("Item Name: ")
            quantity = int(input("Quantity: "))
            Inventory.changeQuantity(whatToChange, quantity)
            
        elif task == 5:
            whatToChange = input("Item Name: ")
            quantity = input("Item Value: ")
            Inventory.overwriteQuantity(whatToChange, quantity)
            
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

        
if __name__ == "__main__":
    user_input()
    
f.close()






