from colorama import Fore, Style, Back
import requests
import json
from os import system as cmd
from platform import platform

banner = f"{Fore.CYAN + Style.BRIGHT}"
with open("banner.txt",'r') as f:
    banner += f.read()
banner += Style.RESET_ALL

def send_sms(number:str, message:str, api_key:str = "textbelt"):
    data = {
        "phone":number,
        "message":message,
        "key":api_key
    }
    response = requests.post("https://textbelt.com/text",data=data)
    
    response_json = json.loads(response.text)
    if bool(response_json["success"]):
        print(f"{Fore.GREEN + Style.BRIGHT}Message sent! {response_json['quotaRemaining']} texts remaining.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED + Style.BRIGHT}Failed to send! {response_json['error']}{Style.RESET_ALL}")


def clear():
    if "Windows" in platform():
        cmd("cls")
    else:
        cmd("clear")

def main():
    while 1:
        clear()
        print(banner)
        print(Fore.YELLOW + "    1. Send SMS")
        print("    2. Help")
        print("    3. I'm done" + Style.RESET_ALL)

        sel = input("Take action: ")
        
        try:
            sel = int(sel)
            if sel == 1:
                number = input("SMS destination: ")
                message = input("SMS body: ")
                api_key = input("textbelt api key? (Leave blank if none): ").strip()

                if api_key == "":
                    api_key = "textbelt"

                if len(message) > 160:
                    print(Fore.RED + Style.BRIGHT + "WARNING! Message length exceeds 160 characters and will not fit into one SMS!" + Style.RESET_ALL)
                
                send_sms(number, message, api_key)
            elif sel == 3:
                print("Goodbye!")
                break
        except Exception as e:
            if type(sel) != int or sel > 3 or sel < 1:
                print("Invalid selection!")
            else:
                print("Unknown error!")
                print(e)
        input("PRESS ENTER")

if __name__ == "__main__":
    main()