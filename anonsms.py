import colorama
import requests
import json

def send_sms(number:str, message:str, api_key:str = "textbelt"):
    data = {
        "phone":number,
        "message":message,
        "key":api_key
    }
    response = requests.post("https://textbelt.com/text",data=data)
    
    response_json = json.loads(response.text)
    if bool(response_json["success"]):
        print(f"{colorama.Fore.GREEN + colorama.Style.BRIGHT}Message sent! {response_json['quotaRemaining']} texts remaining.{colorama.Style.RESET_ALL}")
    else:
        print(f"{colorama.Fore.RED + colorama.Style.BRIGHT}Failed to send! {response_json['error']}{colorama.Style.RESET_ALL}")



