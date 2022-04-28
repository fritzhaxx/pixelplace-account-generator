import os
import threading
import httpx
import colorama
import random
import string
import time
import re
import keyboard as keyboard
from capmonster_python import RecaptchaV2Task

# this code isnt very good because it wasnt mean to be released lol thx

def randomString(n):
    return "".join([random.choice(string.ascii_lowercase) for _ in range(n)])

def randomInt(n):
    return "".join([random.choice("0123456789") for _ in range(n)])

def captchaSolver():
    capmonster = RecaptchaV2Task("") # pur ur capmonster key here
    task_id = capmonster.create_task("https://pixelplace.io/7-pixels-world-war", "6LcZpc8UAAAAAHHJCAYkiNoWaVCgafT_Juzbcsnr")
    result = capmonster.join_task_result(task_id)
    print(f"{colorama.Fore.GREEN}[+] Solved a captcha{colorama.Fore.RESET}")
    return result.get("gRecaptchaResponse")

def mainWorker():
    threadId = randomInt(4)
    print(f"{colorama.Fore.BLUE}[+] Started thread-{threadId}")
    email = randomString(8) + "@thunder24mail.com" # replace with ur mail domain
    captchaKey = captchaSolver()
    createAccount(email, captchaKey, threadId)
    captchaKey = captchaSolver()
    verifyAccount(email, captchaKey, threadId)
    print(f"{colorama.Fore.BLUE}[+] Finished thread-{threadId}")

def verifyAccount(email, captchaKey, threadId):
    try:

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": "email.mail.pixelplace.io",
            "Pragma": "no-cache",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }
        emailText = httpx.get(f"http://185.250.251.189:6969/get/?to={email}", headers={"Authorization": ""}).text # replace with your mail api.
        verifyMailLink = re.findall("http[s]?://(?:(?!http[s]?://)[a-zA-Z]|[0-9]|[$\-_@.&+/]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", emailText)[0] # get link from plaintext mail
        r = httpx.get(verifyMailLink, headers=headers, follow_redirects=True, verify=False)
        print(f"{colorama.Fore.YELLOW}[+] Verified email {email} | thread-{threadId} {colorama.Fore.RESET}")
        payload = {
            "email": email,
            "password": "Wishperedlefilsdepute1234", # cool password because this female is retarded (Wishpered)
            "g-recaptcha-response": captchaKey
        }
        headers = {
            "Host": "pixelplace.io",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "U_PREFS": "1",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://pixelplace.io",
            "DNT": "1",
            "Connection": "keep-alive",
            "Referer": "https://pixelplace.io/7-pixels-world-war",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers"
        }
        r = httpx.post("https://pixelplace.io/api/login.php", headers=headers, data=payload, verify=False)
        # get all the sussy cookies
        authId = r.headers.get('set-cookie').split('authId=')[1].split(';')[0]
        authKey = r.headers.get('set-cookie').split('authKey=')[1].split(';')[0]
        authToken = r.headers.get('set-cookie').split('authToken=')[1].split(';')[0]
        headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": f"authId={authId}; authKey={authKey}; authToken={authToken}",
            "origin": "https://pixelplace.io",
            "pragma": "no-cache",
            "referer": "https://pixelplace.io/7-pixels-world-war",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "u_prefs": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }
        username = f"{randomString(8)}"
        payload = {
            "username": username
        }
        r = httpx.post("https://pixelplace.io/api/account-username.php", headers=headers, data=payload, verify=False) # change username cuz u cannot place pixels if u dont do that
        print(f"{colorama.Fore.MAGENTA}[+] Changed username to {username} | thread-{threadId} {colorama.Fore.RESET}")
        headers = {
            "Host": "pixelplace.io",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "U_PREFS": "1",
            "X-Requested-With": "XMLHttpRequest",
            "DNT": "1",
            "Connection": "keep-alive",
            "Referer": "https://pixelplace.io/7-pixels-world-war",
            "Cookie": f"authId={authId}; authKey={authKey}; authToken={authToken}",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Cache-Control": "max-age=0",
            "TE": "trailers"
        }
        # get new authKey and save
        authKey = httpx.get("https://pixelplace.io/api/get-painting.php?id=7&connected=1", headers=headers).json()["user"]["key"]
        with open("tokens.txt", "a+") as f:
            f.write(f"{username}, {authId}, {authToken}, {authKey}\n")
    except Exception as e:
        print(e)


def createAccount(email, captchaKey, threadId):
    try:

        payload = {
            "email": email,
            "password": "Wishperedlefilsdepute1234",
            "confirm": "Wishperedlefilsdepute1234",
            "g-recaptcha-response": captchaKey
        }

        headers = {
            "Host": "pixelplace.io",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "U_PREFS": "1",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://pixelplace.io",
            "DNT": "1",
            "Connection": "keep-alive",
            "Referer": "https://pixelplace.io/7-pixels-world-war",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers"
        }
        r = httpx.post("https://pixelplace.io/api/register.php", headers=headers, data=payload, verify=False)
        print(f"{colorama.Fore.GREEN}[+] Created account {email} | thread-{threadId} {colorama.Fore.RESET}")
        if r.status_code == 200:
            time.sleep(20) # too lazy so i just wait for the mail 20sc
        else:
            print(f"{colorama.Fore.RED}[!] An error occured | thread-{threadId} {colorama.Fore.RESET}")
            exit()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    while True:
        threading.Thread(target=mainWorker).start()
        time.sleep(2) # start thread each 2 sec cuz lazy
        #input()
        #keyboard.read_key()
