import cloudscraper
from config import BEARER_TOKEN, ACCOUNT_ID

def send_error():
    url = "https://gateway.golike.net/api/report/send"
    headers = {"Authorization": f"{BEARER_TOKEN}", "Content-Type": "application/json"}
    data = {"description":"Tôi không muốn làm Job này","fb_id":(ACCOUNT_ID)}

    scraper = cloudscraper.create_scraper()
    response = scraper.post(url, headers=headers, json=data)
    response.encoding = "utf-8"

    try:
        result = response.json()
        if result.get("success"):
            print(f"[+] Send reason error thành công: {result.get('message')}, status: {result.get('status')}")
        else:
            print(f"[-] Báo lỗi thất bại: {result}")
    except Exception as e:
        print(f"[-] Lỗi khi đọc JSON từ API: {e}")

def report_error(job_data):
    send_error()
    url = "https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs"
    headers = {"Authorization": f"{BEARER_TOKEN}", "Content-Type": "application/json"}
    data = {
        "ads_id": job_data["id"],
        "account_id": job_data.get("lock", {}).get("account_id", ACCOUNT_ID),
        "object_id": job_data["object_id"]
    }

    scraper = cloudscraper.create_scraper()
    response = scraper.post(url, headers=headers, json=data)
    response.encoding = "utf-8"

    try:
        result = response.json()
        if result.get("success"):
            print(f"[+] Báo lỗi/skip job thành công: {result.get('message')}")
        else:
            print(f"[-] Báo lỗi thất bại: {result}")
    except Exception as e:
        print(f"[-] Lỗi khi đọc JSON từ API: {e}")

def complete_job(job_data):
    url = "https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs"
    headers = {"Authorization": f"{BEARER_TOKEN}", "Content-Type": "application/json"}
    account_id = job_data.get("lock", {}).get("account_id", ACCOUNT_ID)
    data = {"ads_id": job_data["id"], "account_id": account_id}

    scraper = cloudscraper.create_scraper(
    )
    response = scraper.post(url, headers=headers, json=data)
    response.encoding = "utf-8"

    try:
        result = response.json()
        if response.status_code == 200 and result.get("success"):
            print("[+] Job đã hoàn thành trên GoLike")
            return True
        else:
            print(f"[-] Lỗi khi hoàn tất job: {result.get('message', result)}")
            return False
    except Exception as e:
        print(f"[-] Lỗi khi đọc JSON từ API hoàn tất: {e}")
        return False
