import uiautomator2 as u2
import time
import cloudscraper
from config import BEARER_TOKEN, ACCOUNT_ID
from detect_abds import auto_connect
from golike_api import report_error
from color import RED, RESET, GREEN, YELLOW

d = auto_connect()


def get_latest_tiktok_job():
    url = f"https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={ACCOUNT_ID}&data=null"
    headers = {"Authorization": f"{BEARER_TOKEN}"}
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url, headers=headers)
    response.encoding = "utf-8"
    print(f"{GREEN}{response}{RESET}")

    if response.status_code != 200:
        print(f"{RED}[-] Lỗi khi lấy danh sách job: {response.status_code}{RESET}")
        return None

    try:
        json_data = response.json()
    except Exception as e:
        print(f"[-] Không thể đọc JSON: {e}")
        return None

    if not json_data.get("success") or not json_data.get("data"):
        print("[-] Không có job mới")
        return None

    job_data = json_data["data"]
    print(f"[+] Job ID: {job_data['id']}")
    print(f"[+] Link TikTok: {job_data['link']}")
    time.sleep(3)
    return job_data


def open_tiktok(url, job_data):
    if "video" in url:
        print("[!] URL chứa video, bỏ qua job này...")
        report_error(job_data)
        return False  # báo cho main biết là bỏ qua

    d.shell(f'am start -a android.intent.action.VIEW -d "{url}"')
    time.sleep(5)
    return True


def click_follow():
    if d(text="Follow").wait(timeout=10000):
        d(text="Follow").click()
        time.sleep(2)
        if d(textContains="This account can’t be followed").exists:
            print("[-] Tài khoản bị banned, job fail")
            return False
        print("[+] Đã follow kênh TikTok")
        for i in range(6):
            print(".", end="", flush=True)
            time.sleep(1)
        print(" ✅")
        return True
    else:
        print("[-] Không tìm thấy nút Follow")
        return False
