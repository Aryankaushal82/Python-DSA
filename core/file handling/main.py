from pathlib import Path
def readFileAndFolder():
    path = Path('') # jis folder m file hai vhi path aajega
    items = list(path.glob('*')) # * means all files and folders
    for i, item in enumerate(items):
        print(f"{i}: {item}")

def createFile():
    try:
        readFileAndFolder()
        name = input("Enter file name: ")
        p = Path(name)
        if p.exists():
            print("File already exists")
            return
        with open(p,'w') as fs:
            data = input("Enter data to write in file: ")
            fs.write(data)
        print("File created successfully")
    except Exception as e:
        print("Error: ", e)


def updateFile():
    readFileAndFolder()
    name = input("Enter file name to update: ")
    p = Path(name)
    

def readFile():
    try:
        readFileAndFolder()
        name = input("Enter file name to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print("Data in file: ", data)
            print("File read successfully")
        else:
            print("File not found or is not a file")
    except Exception as e:
        print("Error: ", e)



print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")


check = int(input("Enter your choice: "))

if check == 1:
    createFile()
if check == 2:
    readFile()
if check == 3:
    updateFile()
    