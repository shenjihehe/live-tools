import pymongo

client = pymongo.MongoClient('localhost',27017)# $lt/$lte/$gt/$gte/$ne，依次等价于</<=/>/>=/!=。（l表示less g表示greater e表示equal n表示not  ）
warden = client['warden']
sheet_tab = warden['sheet_tab']

# path = 'G:/practice/python/pycharm/5/walden.txt'
# with open(path,'r') as f:
#     lines = f.readlines()
#     for index,line in enumerate(lines):
#         data = {
#             'index':index,
#             'line':line,
#             'words':len(line.split())
#         }
#         sheet_tab.insert_one(data)
#         print('成功！')


# $lt/$lte/$gt/$gte/$ne，依次等价于</<=/>/>=/!=。（l表示less g表示greater e表示equal n表示not  ）
# for item in sheet_tab.find({'words':{'$lt':5}}):
#     print(item)

for item in sheet_tab.find():
    print(item['line'])