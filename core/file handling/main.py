from pathlib import Path
def readFileAndFolder():
    path = Path('') # jis folder m file hai vhi path aajega
    items = list(path.glob('*')) # * means all files and folders
    for i, item in enumerate(items):
        print(f"{i}: {item}")

def createFile():
    readFileAndFolder()
    name = input("Enter file name: ")
    pass


print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")


check = int(input("Enter your choice: "))

if check == 1:
    createFile()
