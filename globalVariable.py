x = "prodip Sarkar" # This is global variable

def myfunc():
    print(f"My name is {x}")

myfunc()

def myName():

    x = "Prodip Sarkarj" # This is local variable
    print(f"My name is {x}")
    
    

myName()

def globFunc():
    global x # global variable
    # x = "Prodip Sarkarj"
    print(f"My name is {x}")

globFunc()

