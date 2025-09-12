import subprocess
import uiautomator2 as u2


def auto_connect():
    # Lấy danh sách device từ adb
    result = (
        subprocess.check_output(["adb", "devices"]).decode("utf-8").strip().split("\n")
    )

    # Bỏ dòng đầu "List of devices attached"
    devices = [line.split()[0] for line in result[1:] if "\tdevice" in line]

    if not devices:
        raise RuntimeError("❌ Không tìm thấy thiết bị ADB nào, kiểm tra lại kết nối!")

    # Ưu tiên chọn thiết bị có dạng IP:PORT (ổn định hơn mDNS)
    ip_devices = [d for d in devices if ":" in d]
    if ip_devices:
        serial = ip_devices[0]
    else:
        serial = devices[0]

    print(f"✅ Đang kết nối với thiết bị: {serial}")
    return u2.connect(serial)
