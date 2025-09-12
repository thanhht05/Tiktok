import json
from curl_cffi import requests
import uiautomator2 as u2


BEARER_TOKEN = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9nYXRld2F5LmdvbGlrZS5uZXRcL2FwaVwvbG9naW4iLCJpYXQiOjE3NTQ5NjUxMjQsImV4cCI6MTc4NjUwMTEyNCwibmJmIjoxNzU0OTY1MTI0LCJqdGkiOiJ3Zk5OeDdLaTVxRUN6NU95Iiwic3ViIjozMDYyNjg3LCJwcnYiOiJiOTEyNzk5NzhmMTFhYTdiYzU2NzA0ODdmZmYwMWUyMjgyNTNmZTQ4In0.FNuP18El0S8YrZf3hag74fzVxswGMd1Xv7wMPy60q38"


def get_account_id():
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": BEARER_TOKEN,
        "content-type": "application/json;charset=utf-8",
        "origin": "https://app.golike.net",
        "priority": "u=1, i",
        "sec-ch-ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "t": "VFZSak1VNVVZM2ROVkdjd1RrRTlQUT09",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
    }

    response = requests.get(
        "https://gateway.golike.net/api/tiktok-account",
        headers=headers,
        impersonate="safari_ios",
    )
    data = json.loads(response.text)
    listAcc = data.get("data", [])
    rs = []
    for item in listAcc:
        rs.append({item["id"], item["nickname"]})

    return rs


l = get_account_id()
print("Dánh sách account")
for item in l:
    print(item)

ACCOUNT_ID = input("Nhập account muốn làm: ")
