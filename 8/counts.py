import time
from page_info import url_list

while True:
    print(url_list.find().count())
    time.sleep(5)