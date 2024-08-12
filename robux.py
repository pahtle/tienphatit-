import os
import time
import sys

def clear_screen():
    # Xóa màn hình tùy theo hệ điều hành
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')

def print_with_delay(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Xóa màn hình trước khi bắt đầu chương trình
clear_screen()

# Trang trí chào mừng
print("\033[96m" + "*" * 50)
print("\033[92m" + " CHÀO MỪNG BẠN ĐẾN VỚI TOOL HACK ROBUX".center(50))
print("\033[96m" + "*" * 50 + "\033[0m")

# Nhập tên tài khoản Roblox của bạn
username = input("\033[93mNhập tên tài khoản Roblox của bạn: \033[0m")

# Nhập số lần chạy
so_lan_spam = int(input("\033[93mNhập số lần chạy (1 lần= 1000 robux: \033[0m"))

# Xóa màn hình sau khi nhập thông tin
clear_screen()

# Spam câu "Đã hack thành công 1000 roblux" với trang trí
print("\n\033[95m" + "-" * 50)
print_with_delay(f"🌟 Đang hack tài khoản {username} 🌟", 0.1)
print("-" * 50 + "\033[0m")

for _ in range(so_lan_spam):
    print("\033[92m" + "Đã hack thành công 1000 robux".center(50) + "\033[0m")
    time.sleep(0.1)

# Spam vô hạn "không làm đòi có ăn thì ăn 💩" với chữ màu đỏ và trang trí
print("\n\033[91m" + "=" * 50)
print_with_delay("Không làm đòi có ăn thì ăn 💩".center(50), 0.05)
print("=" * 50 + "\033[0m")

try:
    while True:
        print("\033[91m" + "không làm đòi có ăn thì ăn 💩" + "\033[0m")
        time.sleep(0.2)
except KeyboardInterrupt:
    print("\033[94mChương trình đã dừng lại! Chúc bạn một ngày vui vẻ!\033[0m")
