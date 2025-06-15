import os

print("Welcome to CleanMyDesktop.")

print("This software will now clean your desktop 😁")

print("We will make a list of unwanted items and hide them from your desktop.")

Username = os.getlogin()

# chnage to DE directory
os.chdir(f'C:/Users/{Username}/desktop')

FilesToDelete = []

print(f"Enter the files you want to delete, {Username}.")

while True:
  FileToAppend = input("Enter a file name with extension: ")
  FilesToDelete.append(FileToAppend)
  LastFile = input("Is that the last file? Yes/No")
  LastFile = LastFile.capitalize()
  if LastFile == "Yes":
    print("okay lets clean up!")
    break
  else:
    print("alright!")

for filename in FilesToDelete:
    FilePath = os.path.join(f'C:/Users/{Username}/desktop', filename)
    # Check if the file exists before deleting
    if os.path.isfile(FilePath):
        os.remove(FilePath)
        print(f"Cleaned: {filename}")
    else:
        print(f"File not found: {filename}")
