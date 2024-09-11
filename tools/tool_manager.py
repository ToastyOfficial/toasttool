# coding=utf-8
# Version 1.0.0
# Made By @iitztoasty

import os
import sys
from time import sleep

from core import FingerOfGod
from core import FingerOfGodCollection


class UpdateTool(FingerOfGod):
    TITLE = "Update Tool or System"
    DESCRIPTION = "Update Tool or System"

    def __init__(self):
        super(UpdateTool, self).__init__([
            ("Update System", self.update_sys),
            ("Update Toast Tool", self.update_ht)
        ], installable = False, runnable = False)

    def update_sys(self):
        os.system("sudo apt update && sudo apt full-upgrade -y")
        os.system(
            "sudo apt-get install tor openssl curl && sudo apt-get update tor openssl curl")
        os.system("sudo apt-get install python3-pip")

    def update_ht(self):
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/toasttool/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/toasttool/;"
                  "mkdir toasttool;"
                  "cd toasttool;"
                  "git clone https://github.com/ToastyOfficial/toasttool.git;"
                  "cd toasttool;"
                  "sudo chmod +x install.sh;"
                  "./install.sh")


class UninstallTool(FingerOfGod):
    TITLE = "Uninstall ToastTool"
    DESCRIPTION = "Uninstall ToastTool"

    def __init__(self):
        super(UninstallTool, self).__init__([
            ('Uninstall', self.uninstall)
        ], installable = False, runnable = False)

    def uninstall(self):
        print("toasttool started to uninstall..\n")
        sleep(1)
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/toasttool/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/toasttool/;")
        print("\ntoasttool Successfully Uninstalled... Goodbye.")
        sys.exit()


class ToolManager(FingerOfGodCollection):
    TITLE = "Update or Uninstall | Toasttool"
    TOOLS = [
        UpdateTool(),
        UninstallTool()
    ]
