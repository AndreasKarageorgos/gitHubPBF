from time import sleep
from os import walk,path,system

def logo():
    print("""
++--------------------------------------------------++
++--------------------------------------------------++
||  ____ _ _   _   _       _     ____  ____  _____  ||
|| / ___(_) |_| | | |_   _| |__ |  _ \| __ )|  ___| ||
||| |  _| | __| |_| | | | | '_ \| |_) |  _ \| |_    ||
||| |_| | | |_|  _  | |_| | |_) |  __/| |_) |  _|   ||
|| \____|_|\__|_| |_|\__,_|_.__/|_|   |____/|_|     ||
||                                                  ||
++--------------------------------------------------++
++--------------------------------------------------++\n\n\n""")

def validPath():
    return path.exists(".git")


def fileSize(file_path):

    file_bytes = path.getsize(file_path)
    file_mb = file_bytes / (1024 * 1024)

    return file_mb

def main():
    logo()
    sleep(0.5)

    commit_message = "GitHubPBF "
    mymessage = "\nThis script may take some time to complete. Feel free to grab a coffee or take a walk while you wait. :)"
    file_counter = 0
    pushed_files = 0
    large_files = 0

    if(not validPath()):
        print("Please add the script in the path that the .git folder is stored")
        return 0

    branch = input("Before this script starts. Did you create a new branch ?? [yes/no]: ") or "no"
    while(branch.lower() != "yes" and branch.lower() != "no"):
        branch = input("Before this script starts. Did you create a new branch ?? [yes/no]: ") or "no"

    if(branch.lower() == "no"):
        print("Create a new branch and re-run the script.")
        return 0

    path_delimiter = path.sep
    folder = input("input the folder that you want to push on GitHub: ") or ""

    while(folder == ""):
        folder = input("Input the folder that you want to push on GitHub: ") or ""

    save_to = input("path to store the folder: ") or ""
    while(save_to == ""):
        save_to = input("path to store the folder: ") or ""


    commit_message = commit_message + input("Enter the commit message: ") or ""

    
    for root,_,files in walk(folder):
        createdir = True
        for f in files:
            if(createdir):
                system(f"mkdir -p {save_to}{path_delimiter}{root}")
                createdir = False
            if(fileSize(f"{root}{path_delimiter}{f}")>=300):
                large_files +=1
            file_counter += 1 

    if(large_files>0):
        print(f"The script detected {large_files} files that exceed the file size limit of GitHub.")
        print("To push these files, you need to install 'Git Large File Storage'. https://git-lfs.com/ \nIf you do not install it, the script will fail.")
        answer = input("Have you installed 'Git Large File Storage' ? [yes/no]").lower() or "no"
        while(answer!="no" and answer!="yes"):
            answer = input("Have you installed 'Git Large File Storage' ? [yes/no]").lower() or "no"
        
        if(answer=="no"):
            print("Install it and then re-run the script.")
            return 0
        else:
            system("git lfs install 1> /dev/null 2> /dev/null")

    for m in mymessage:
        print(m, end="", flush=True)
        sleep(0.05)
    sleep(2)
    print()

    for root,_,files in walk(folder):
        for f in files:
            print(f"File pushed {pushed_files}/{file_counter}")
            f1_path = f"{root}{path_delimiter}{f} {save_to}{path_delimiter}{root}"
            f2_path = f"{save_to}{path_delimiter}{folder}{path_delimiter}*"
            
            system(f"cp {f1_path} 1> /dev/null 2> /dev/null")

            if(fileSize(f"{root}{path_delimiter}{f}")>100):
                system(f"git lfs track \"*{f}\" 1> /dev/null 2> /dev/null")
                system("git add .gitattributes 1> /dev/null 2> /dev/null")
                print(f"Transferring a {fileSize(f'{root}{path_delimiter}{f}')}MB file. Your patience is appreciated")


            system(f"git add {f2_path} 1> /dev/null 2> /dev/null")
            system(f"git commit -s -m \"{commit_message}\" 1> /dev/null 2> /dev/null")
            system("git push origin HEAD 1> /dev/null 2> /dev/null")
            pushed_files += 1


    print(f"File pushed {pushed_files}/{file_counter}")
    return 0


if __name__ == "__main__":
    main()