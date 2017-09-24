import time
from page_parsing import url_list
# 监控

while True:
    print(url_list.find().count())
    time.sleep(5)
