import os

folder = input("Enter folder path: ")

if os.path.exists(folder):
    files = os.listdir(folder)

    print("\nFiles in the folder:")

    for file in files:
        path = os.path.join(folder, file)

        if os.path.isfile(path):
            print(file)

    print("\nTotal files:", len(files))

else:
    print("Folder not found!")