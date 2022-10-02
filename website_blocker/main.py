from calendar import month
import time
from datetime import datetime as dt

#  C:\Windows\System32\drivers\etc

hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]


final_list = [redirect + " " + i for i in website_list]

while True:
    # check if time between a range , from 8:00 until 19:00
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 19):
        print("working hours")
        with open(hosts_temp, "r+") as file:
            content = file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    # 127.0.0.1       localhost
                    file.write(redirect + " "+website + "\n")
    else:
        print("Fun hours")

    time.sleep(5)  # it will stop the code for 5 sec
