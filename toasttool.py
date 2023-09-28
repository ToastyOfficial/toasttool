#!/usr/bin/env python3
# Version 1.0.0
# Made By @iitztoasty

import os
import sys
import webbrowser
from platform import system
from time import sleep

from core import FingerOfGodCollection
from tools.anonsurf import AnonSurfTools
from tools.tool_manager import ToolManager

logo = """\033[33m
 ______   ______     ______     ______     ______      ______   ______     ______     __       
/\__  _\ /\  __ \   /\  __ \   /\  ___\   /\__  _\    /\__  _\ /\  __ \   /\  __ \   /\ \      
\/_/\ \/ \ \ \/\ \  \ \  __ \  \ \___  \  \/_/\ \/    \/_/\ \/ \ \ \/\ \  \ \ \/\ \  \ \ \____ 
   \ \_\  \ \_____\  \ \_\ \_\  \/\_____\    \ \_\       \ \_\  \ \_____\  \ \_____\  \ \_____\
    \/_/   \/_____/   \/_/\/_/   \/_____/     \/_/        \/_/   \/_____/   \/_____/   \/_____/
                                                                                                                    
                                                                                 
                    \033[34m[✔]          Fuck Your Free World          [✔]
                    \033[34m[✔]            Version 2.2.0               [✔]
		    \033[60m[X]           Save The Children            [X]
                    \033[91m[X]    The End Is Near.. Revelation2:9     [X]
\033[97m """

all_tools = [
    AnonSurfTools(),
    ToolManager()
]


class AllTools(FingerOfGodCollection):
    TITLE = "All tools"
    TOOLS = all_tools

    def show_info(self):
        print(logo + '\033[0m \033[97m')


if __name__ == "__main__":
    try:
        if system() == 'Linux':
            fpath = os.path.expanduser("~/toasttoolpath.txt")
            if not os.path.exists(fpath):
                os.system('clear')
                # run.menu()
                print("""
                        [@] Set Path (All your tools will be installed in that directory)
                        [1] Manual 
                        [2] Default
                """)
                choice = input("Z4nzu =>> ").strip()

                if choice == "1":
                    inpath = input("Enter Path (with Directory Name) >> ").strip()
                    with open(fpath, "w") as f:
                        f.write(inpath)
                    print("Successfully Set Path to: {}".format(inpath))
                elif choice == "2":
                    autopath = "/home/toasttool/"
                    with open(fpath, "w") as f:
                        f.write(autopath)
                    print("Your Default Path Is: {}".format(autopath))
                    sleep(3)
                else:
                    print("Try Again..!!")
                    sys.exit(0)

            with open(fpath) as f:
                archive = f.readline()
                os.makedirs(archive, exist_ok=True)
                os.chdir(archive)
                AllTools().show_options()

        # If not Linux and probably Windows
        elif system() == "Windows":
            print(
                r"\033[91m Please Run This Tool On A Debian System For Best Results\e[00m"
            )
            sleep(2)
            webbrowser.open_new_tab("https://tinyurl.com/win-WSL2")

        else:
            print("Please Check Your System or Open New Issue ...")

    except KeyboardInterrupt:
        print("\nExiting ..!!!")
        sleep(2)
