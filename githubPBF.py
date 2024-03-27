from time import sleep
from os import walk,path,system

def logo():
    print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@w          . ~@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@       .      .       p@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@_            .              @@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@.   .       .           .     . *@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@w .           .       .   . .    .  @@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@..  . .@@d        ..         @@       Z@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@        @@@@@@ i@@@@@@@@d.Y@@@@@@       :@@@@@@@@@@@@@@
@@@@@@@@@@@@@@    .    @@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@
@@@@@@@@@@@@@i         @@@@@@@@@@@@@@@@@@@@@@@@~      .  @@@@@@@@@@@@@
@@@@@@@@@@@@@. .      @@@@@@@@@@@@@@@@@@@@@@@@@@o       . @@@@@@@@@@@@
@@@@@@@@@@@@m        @@@@@@@@@@@@@@@@@@@@@@@@@@@@1  .  .  @@@@@@@@@@@@
@@@@@@@@@@@@         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@ .  .  .B@@@@@@@@@@@
@@@@@@@@@@@@         @@@@@@@@@@@@@@@@@@@@@@@@@@@@W.       Z@@@@@@@@@@@
@@@@@@@@@@@@         @@@@@@@@@@@@@@@@@@@@@@@@@@@@t     .  @@@@@@@@@@@@
@@@@@@@@@@@@w         @@@@@@@@@@@@@@@@@@@@@@@@@@@        .@@@@@@@@@@@@
@@@@@@@@@@@@@. ..     {@@@@@@@@@@@@@@@@@@@@@@@@@ .      . @@@@@@@@@@@@
@@@@@@@@@@@@@+      . . @@@@@@@@@@@@@@@@@@@@@@c        . @@@@@@@@@@@@@
@@@@@@@@@@@@@@   . p      . @@@@@@@@@@@@@@c          .. @@@@@@@@@@@@@@
@@@@@@@@@@@@@@@    .)@h       /@@@@@@@@@   .           X@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@      @@   .  @@@@@@@@@@@   .         O@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@p     @@@@@@@@@@@@@@@@@@            @@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@   ..      @@@@@@@@@@@ .  .     @@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@>.      .@@@@@@@@@@@ ..     @@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@(     @@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n\n\n\n\n""")

def fileSize(file_path):

    file_bytes = path.getsize(file_path)
    file_mb = file_bytes / (1024 * 1024)

    return file_mb

def main():
    logo()
    sleep(0.5)

    branch = input("Before this script starts. Did you create a new branch ?? [yes/no]: ") or "no"
    while(branch.lower() != "yes" and branch.lower() != "no"):
        branch = input("Before this script starts. Did you create a new branch ?? [yes/no]: ") or "no"

    if(branch.lower() == "no"):
        return 0

    path_delimiter = path.sep
    folder = input("input the folder that you want to push on GitHub: ") or ""

    while(folder == ""):
        folder = input("Input the folder that you want to push on GitHub: ") or ""

    save_to = input("path to store the folder: ") or ""
    while(save_to == ""):
        save_to = input("path to store the folder: ") or ""


    commit_message = input("commit message: ") or "pbf"


    mymessage = "\nThis script may take some time to complete. Feel free to grab a coffee or take a walk while you wait. :)"
    for m in mymessage:
        print(m, end="", flush=True)
        sleep(0.08)
    sleep(2)
    print()

    system("git lfs install 1> /dev/null 2> /dev/null")

    file_counter = 0
    pushed_files = 0
    for root,_,files in walk(folder):
        for f in files:
            system(f"mkdir -p {save_to}{path_delimiter}{root}")
            file_counter += 1
    

    for root,_,files in walk(folder):
        for f in files:
            print(f"File pushed {pushed_files}/{file_counter}")
            f1_path = f"{root}{path_delimiter}{f} {save_to}{path_delimiter}{root}"
            f2_path = f"{save_to}{path_delimiter}{folder}{path_delimiter}*"
            
            system(f"cp {f1_path} 1> /dev/null 2> /dev/null")

            if(fileSize(f"{root}{path_delimiter}{f}")>100):
                system(f"git lfs track \"*{f}\" 1> /dev/null 2> /dev/null")
                system("git add .gitattributes 1> /dev/null 2> /dev/null")
                print("Large file detected. Please be patient.")


            system(f"git add {f2_path} 1> /dev/null 2> /dev/null")
            system(f"git commit -s -m \"{commit_message}\" 1> /dev/null 2> /dev/null")
            system("git push origin HEAD 1> /dev/null 2> /dev/null")
            pushed_files += 1


    print(f"File pushed {pushed_files}/{file_counter}")
    return 0


if __name__ == "__main__":
    main()