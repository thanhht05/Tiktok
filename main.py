import time
from tiktok_job import get_latest_tiktok_job, open_tiktok, click_follow
from golike_api import complete_job, report_error

def main():
    n = int(input("Nhập số lần muốn chạy: "))
    price=0
    time_success=0
    for i in range(1, n + 1):
        print(f"\n=== Lần {i}/{n} ===")
        job_data = get_latest_tiktok_job()
        if not job_data:
            print("[-] Không có job để thực hiện, chờ 5 giây...")
            time.sleep(5)
            continue

        # Mở TikTok, nếu trả về False thì bỏ qua sang job mới
        if not open_tiktok(job_data["link"], job_data):
            continue

        success = click_follow()

        if success:
            if complete_job(job_data):
                time_success+=1
                price+=job_data["price_after_cost"]
                print("[+] Hoàn tất job thành công!")
                print(f"[+] Total price: {price}")
                print(f"[+] Số lần thành công: {time_success}/{n}")
            else:
                print("[!] complete_job thất bại, gửi report...")
                report_error(job_data)
        else:
            print("[!] Job bị lỗi!")
            report_error(job_data)

        print(f"[+] Hoàn tất lần {i}")
        print("[*] Đợi 10 giây trước khi job tiếp theo...", end="", flush=True)
        for j in range(10):
            print(".", end="", flush=True)
            time.sleep(1)
        print(" ✅")

if __name__ == "__main__":
    main()
