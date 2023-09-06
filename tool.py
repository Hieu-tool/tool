from time import strftime
import os
import sys
import requests
from time import sleep
from datetime import datetime, timedelta
import requests
import os
try:
  from faker import Faker
  import requests
  from colorama import Fore, Style
  import re
  import pystyle
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system('pip install requests && pip install bs4 && pip install pystyle')
  print('__Vui Lòng Chạy Lại Tool__')
# màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
tim = '\033[1;39m'
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
os.system("cls" if os.name == "nt" else "clear")

# đánh dấu bản quyền
ndp_tool = "\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"

ip = requests.get("https://api.ipgeolocation.io/getip").json()
def banner():
    banner = f"""


\033[1;34m ╭╮╱╭┳━━┳━━━┳╮╱╭╮╱╭━━━━┳━━━┳━━━┳╮
\033[1;37m ┃┃╱┃┣┫┣┫╭━━┫┃╱┃┃╱┃╭╮╭╮┃╭━╮┃╭━╮┃┃
\033[1;34m ┃╰━╯┃┃┃┃╰━━┫┃╱┃┃╱╰╯┃┃╰┫┃╱┃┃┃╱┃┃┃
\033[1;37m ┃╭━╮┃┃┃┃╭━━┫┃╱┃┣━━╮┃┃╱┃┃╱┃┃┃╱┃┃┃╱╭╮
\033[1;34m ┃┃╱┃┣┫┣┫╰━━┫╰━╯┣━━╯┃┃╱┃╰━╯┃╰━╯┃╰━╯┃
\033[1;37m ╰╯╱╰┻━━┻━━━┻━━━╯╱╱╱╰╯╱╰━━━┻━━━┻━━━╯
\033[1;34m 𝐀𝐃𝐌𝐈𝐍_𝐇𝐈𝐄𝐔_𝐓𝐎𝐎𝐋
\033[1;31m────────────────────────────────────────────────────────────
\033[1;31m────────────────────────────────────────────────────────────
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[1;39m┌────────────────────────💚 HIẾU TOOL💚────────────────────────┐
\033[1;32m║   \033[1;39mPYTHON VERSION\033[1;32m     :  4.1                                  \033[1;32m║
\033[1;32m║   \033[1;39mZALO               :  84939271874                          \033[1;32m║
\033[1;32m║   \033[1;39mGROP_zalo          :  https://zalo.me/g/wfakde942          \033[1;32m║
\033[1;32m║   \033[1;39mYOUTUBER           :  HIẾU TOOL                            \033[1;32m║
\033[1;32m║   \033[1;39mYOTUBE_LINK        :  https://www.youtube.com/@hieutool248 \033[1;32m║
\033[1;39m└──────────────────────────────────────────────────────────────┘
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[1;31m────────────────────────────────────────────────────────────
"""

    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.00125)
banner()


print(f"\033[1;37m\033[1;33mip của bạn là: {ip['ip']}  \033[1;37m")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Trao Đổi Sub  \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTool TDS FB FULL JOD\033[1;31m[\033[1;33mlive\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mTool TDS FB VIP\033[1;31m[\033[1;33mlive\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3\033[1;31m] \033[1;32mTool TDS Pro5 {1 page}\033[1;31m[\033[1;33mlive\033[1;31m]")

print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m4\033[1;31m] \033[1;32mTool TDS IG \033[1;31m[\033[1;33mV1\033[1;31m] \033[1;31m[\033[1;33mlive\033[1;31m]")

print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m5\033[1;31m] \033[1;32mTool TDS TikTok & TDS TIKTOK NOW \033[1;31m[\033[1;33mlive\033[1;31m] ")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═══════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Tương Tác Chéo  \033[1;37m║")
print("\033[1;37m╚═══════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m6\033[1;31m] \033[1;32mTool TTC TikTok [chưa fix] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m7\033[1;31m] \033[1;32mTool TTC Pro5 \033[1;31m[\033[1;33mlive\033[1;31m]  ")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Tiện Ích      \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m8\033[1;31m] \033[1;32mTool Đào Mail ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m9\033[1;31m] \033[1;32mTool Tạo Thẻ Thanh Toán ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m10\033[1;31m] \033[1;32mTool Check Valid")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m11\033[1;31m] \033[1;32mTool LOC PROXY \033[1;31m[\033[1;33mlive\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m12\033[1;31m] \033[1;32mtool buff view,tym,.. tiktok\033[1;31m『\033[1;33mNEW\033[1;31m』 ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m13\033[1;31m] \033[1;32mTool Get Cookie Pro5 Facebook\033[1;31m『\033[1;33mNEW\033[1;31m』")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool PROFILE       \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m14\033[1;31m] \033[1;32mTool Reg Page Pro5")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m15\033[1;31m] \033[1;32msharefb")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m16\033[1;31m] \033[1;32mTool Reg Page Pro5 \033[1;31m[\033[1;33mV2\033[1;31m]")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m17\033[1;31m] \033[1;32mTOOL TĂNG SHARE AO BẰNG TOKEN")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m18\033[1;31m] \033[1;32mTool Buff View Story Max Speed Pro5 ")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool SPAM SMS      \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m19\033[1;31m] \033[1;32mtool spam sms\033[1;31m[\033[1;33mV5\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m20\033[1;31m] \033[1;32mTool SPAM SMS \033[1;31m[\033[1;33mV6\033[1;31m] ")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔══════════════╗")
print("\033[1;37m║ \033[1;33mTool Golike  \033[1;37m║")
print("\033[1;37m╚══════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m21\033[1;31m] \033[1;32mTool Golike Tiktok ")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m00\033[1;31m] \033[1;32mThoát Tool")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═══════════╗")
print("\033[1;37m║\033[1;33mhỗ trợ Tool\033[1;37m║")
print("\033[1;37m╚═══════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m101\033[1;31m] \033[1;32mĐể support qua zalo ngay")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m102\033[1;31m] \033[1;32mĐể vào nhóm zalo cập nhật tool")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m103\033[1;31m] \033[1;32mĐể vào kênh yotube")

print("\033[1;31m────────────────────────────────────────────────────────────")

chon = int(input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;37m: \033[1;33m'))
#tool tds
if chon == 1 :
	exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/1.Tool%20TDS%20FB%20FULL%20JOD.py').text) 
elif chon == 2:
	exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/2.Tool%20TDS%20FB%20VIP.py').text)
elif chon == 3 :
	exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/3.Tool%20TDS%20Pro5%20%7B1%20page%7D.py').text) 
elif chon == 4 :
	exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/4.Tool%20TDS%20IG%20%5BV1%5D.py').text) 
elif chon == 5 : 
 exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/5.Tool%20TDS%20TikTok%20%26%20TDS%20TIKTOK%20NOW.py').text) 
 
 
 #tool ttc
elif chon == 6 :
	exec(requests.get('').text)
elif chon == 7 :
	exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/7.Tool%20TTC%20Pro5.py').text)

#tool công cụ 
elif chon == 8 :
 exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/8.Tool%20%C4%90%C3%A0o%20Mail.py').text)
elif chon == 9 :
 exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/9.Tool%20T%E1%BA%A1o%20Th%E1%BA%BB%20Thanh%20To%C3%A1n.py').text)
elif chon == 10 :
	exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/10.Tool%20Check%20Valid.py').text)
elif chon == 11 :
	exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/11.Tool%20LOC%20PROXY.py').text)
elif chon == 12 :
	exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/12.tool%20buff%20view%2Ctym%2C..%20tiktok.py').text)
elif chon == 13 :
	exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/13.Tool%20Get%20Cookie%20Pro5%20Facebook.py').text)
elif chon == 14 :
	exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/14.Tool%20Reg%20Page%20Pro5.py').text)	
elif chon == 15 :
	exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/15.sharefb.py').text)
elif chon == 16 :
	exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/16Tool%20Reg%20Page%20Pro5%20%5BV2%5D.py').text)
elif chon == 17 :
	exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/17.TOOL%20T%C4%82NG%20SHARE%20AO%20B%E1%BA%B0NG%20TOKEN.py').text)
elif chon == 18 :
	exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/18.Tool%20Buff%20View%20Story%20Max%20Speed%20Pro5.py').text)
elif chon == 19 :
	exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/spamv5.py').text)
elif chon == 20 :
	exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/spamv6.py').text)
elif chon == 21 :
	exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/golike.py').text)
elif chon == 22 :
	exec(requests.get('https://run.mocky.io/v3/a9191eff-c08d-413e-add0-134b4d4ec917').text)
elif chon == 00 :
	exec(requests.get('https://raw.githubusercontent.com/Hieu-tool/tools/main/exit.py').text)
elif chon == 101:
	os.system("termux-open-url https://zalo.me/84939271874")
elif chon == 102:
	os.system("termux-open-url https://zalo.me/g/wfakde942")
elif chon == 103:
	os.system("termux-open-url https://www.youtube.com/@hieutool248")
else :
     exit()
