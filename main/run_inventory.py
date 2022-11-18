'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''


from game.main.GameSystem import inventory


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

== SPECIAL ==
Get Quantity[6]:

Input[1/2/3/4/5]: """



if __name__ == "__main__":
    user_input()
