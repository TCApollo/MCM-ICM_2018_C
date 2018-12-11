import requests
import xlwt
import json
import time


book = xlwt.Workbook()# 创建一个excel对象
sheet = book.add_sheet('block_123456',cell_overwrite_ok=True) # 添加一个sheet页
title = ["区块高度","区块哈希值","区块生成时间","费用","交易哈希值","交易地址序号","收入地址","收入金额"]
for col in range(len(title)):  # 存入第一行标题
        sheet.write(0, col, title[col])


# for i in 1000
# #执行API调用并存储响应
# url='https://chain.api.btc.com/v3/block/123456/tx'
# #获得响应对象
# r=requests.get(url)
# #获得状态码
# print("status code:",r.status_code)
# #将API响应存储在一个变量中，这个API返回JSON格式的信息，使用方法json把这些信息转换为一个python字典
# response_dict=r.json()

createVar = locals()




i = 0
blockID=550000
for i0 in range(100):
    blockID=blockID+1
    # 执行API调用并存储响应
    strurl="https://chain.api.btc.com/v3/block/"+str(blockID)+"/tx"
    url = strurl
    time.sleep(0.5)

    print(url)
    # 获得响应对象
    r=requests.get(url)


    # 获得状态码

    # 将API响应存储在一个变量中，这个API返回JSON格式的信息，使用方法json把这些信息转换为一个python字典

    response_dict = json.loads(r.text)

    j1 = -1
    for i1 in response_dict['data']['list']:  # 进入交易
        j1 = j1 + 1  # 交易编号
        j2 = -1
        for i2 in response_dict['data']['list'][j1]['outputs']:  # 寻找交易内收款地址序号
            j2 = j2 + 1  # 地址序号
            i = i + 1
            sheet.write(i, 0, response_dict['data']['list'][j1]['block_height'])
            sheet.write(i, 1, response_dict['data']['list'][j1]['block_hash'])
            sheet.write(i, 2, response_dict['data']['list'][j1]['block_time'])
            sheet.write(i, 3, response_dict['data']['list'][j1]['fee'])
            sheet.write(i, 4, response_dict['data']['list'][j1]['hash'])
            sheet.write(i, 5, j2)
            sheet.write(i, 6, response_dict['data']['list'][j1]['outputs'][j2]['addresses'])
            sheet.write(i, 7, response_dict['data']['list'][j1]['outputs'][j2]['value'])
            # print("j1:", j1)
            # print("j2:", j2)
            # print(response_dict['data']['list'][j1]['outputs'][j2]['addresses'])

    response_dict.clear()
    del r
    print("已下载的区块号"+blockID)
book.save('btc_data1101.xls')











# i=0
# j1=-1
# for i1 in response_dict['data']['list']:#进入交易
#     j1=j1+1#交易编号
#     j2 = -1
#     for i2 in response_dict['data']['list'][j1]['outputs']:#寻找交易内收款地址序号
#         j2=j2+1#地址序号
#         i=i+1
#         sheet.write(i,0,response_dict['data']['list'][j1]['block_height'])
#         sheet.write(i,1, response_dict['data']['list'][j1]['block_hash'])
#         sheet.write(i,2,response_dict['data']['list'][j1]['block_time'])
#         sheet.write(i, 3, response_dict['data']['list'][j1]['fee'])
#         sheet.write(i, 4, response_dict['data']['list'][j1]['hash'])
#         sheet.write(i, 5, j2)
#         sheet.write(i, 6, response_dict['data']['list'][j1]['outputs'][j2]['addresses'])
#         sheet.write(i, 7, response_dict['data']['list'][j1]['outputs'][j2]['value'])
#         print("j1:",j1)
#         print("j2:",j2)
#         print(response_dict['data']['list'][j1]['outputs'][j2]['addresses'])
#
# book.save('123456.xls')
# for key in response_dict['data']['list'][2]['outputs']:
#     print(key)



# j1=-1
# BlockHash[]=[]


# i=1
# j2=-1
# j1=-1
# for i1 in response_dict['data']['list']:#进入交易
#     j1=j1+1#交易编号
#     for i2 in response_dict['data']['list'][j1]['outputs']:#寻找交易内收款地址序号
#         j2=j2+1#地址序号
#         for i3 in response_dict['data']['list'][j1]['outputs'][j2]:#进入收款地址
#             print(i3)