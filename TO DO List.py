#Jaime Lopez and Luis Jacinto 
# 1/11/23 
# To-do List 
def bold_text(text):
    bold_start = '\033[1m'
    bold_end = '\033[0m'
    return bold_start + text + bold_end

def complete (word):
    word=input("what would u like to mark as done")
    bold_text(word.upper())

list=["hellcat", "Bugaati","bentley", "benz", "Genisis", "Amg GT","trackhawk", "M5", "E30", "SS"]
while True: 
    choice = input(print("What would you like to do? \n1. add \n2. view \n3. mark done \n4. remove \n5. exit"))
    if choice == "add":
        list.append(input("what would you like to add"))
    if choice == "view":
        print(list)
    if choice == "done":
        word=input("what would u like to mark as done")
        x=list.index(word)
        list[x]=(word +" x")
        print(list)
    if choice == "remove":
        list.remove(input("What would lou like to remove"))
    if choice == "exit":
        quit()
