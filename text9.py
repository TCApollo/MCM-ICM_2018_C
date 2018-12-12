import requests
import xlsxwriter
import json
import time
time_start=time.time()
#outputs表
book = xlsxwriter.Workbook('btc_data_18下半年_output_5000.xlsx')# 创建一个excel对象
sheet = book.add_worksheet('block_123456') # 添加一个sheet页
title = ["区块高度","区块哈希值","区块生成时间","费用","交易哈希值","交易地址序号","收入地址","收入金额"]
for col in range(len(title)):  # 存入第一行标题
        sheet.write(0, col, title[col])
#input表
book1 = xlsxwriter.Workbook('btc_data_18下半年_inputs_5000.xlsx')# 创建一个excel对象
sheet1 = book1.add_worksheet('block_123456') # 添加一个sheet页
title = ["区块高度","区块哈希值","区块生成时间","费用","交易哈希值","交易地址序号","支出地址","支出金额"]
for col in range(len(title)):  # 存入第一行标题
        sheet1.write(0, col, title[col])
# for i in 1000
# #执行API调用并存储响应
# url='https://chain.api.btc.com/v3/block/123456/tx'
# #获得响应对象
# r=requests.get(url)
# #获得状态码
# print("status code:",r.status_code)
# #将API响应存储在一个变量中，这个API返回JSON格式的信息，使用方法json把这些信息转换为一个python字典
# response_dict=r.json()






i = 0
i9=0
blockID=123456
for i0 in range(1):
    blockID=blockID+1
    # 执行API调用并存储响应
    strurl="https://chain.api.btc.com/v3/block/"+str(blockID)+"/tx"
    url = strurl
    time.sleep(0.75)


    # 获得响应对象
    r=requests.get(url,timeout = 50000)


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
            sheet.write(i, 0, str(response_dict['data']['list'][j1]['block_height']))
            sheet.write(i, 1, str(response_dict['data']['list'][j1]['block_hash']))
            sheet.write(i, 2, str(response_dict['data']['list'][j1]['block_time']))
            sheet.write(i, 3, str(response_dict['data']['list'][j1]['fee']))
            sheet.write(i, 4, str(response_dict['data']['list'][j1]['hash']))
            sheet.write(i, 5, str(j2))
            sheet.write(i, 6, str(response_dict['data']['list'][j1]['outputs'][j2]['addresses']))
            sheet.write(i, 7, str(response_dict['data']['list'][j1]['outputs'][j2]['value']))
            # print("j1:", j1)
            # print("j2:", j2)
            # print(response_dict['data']['list'][j1]['outputs'][j2]['addresses'])
        j2=-1
        for i2 in response_dict['data']['list'][j1]['inputs']:  # 寻找交易内收款地址序号
            j2 = j2 + 1  # 地址序号
            i9 = i9 + 1
            sheet1.write(i9, 0, str(response_dict['data']['list'][j1]['block_height']))
            sheet1.write(i9, 1, str(response_dict['data']['list'][j1]['block_hash']))
            sheet1.write(i9, 2, str(response_dict['data']['list'][j1]['block_time']))
            sheet1.write(i9, 3, str(response_dict['data']['list'][j1]['fee']))
            sheet1.write(i9, 4, str(response_dict['data']['list'][j1]['hash']))
            sheet1.write(i9, 5, str(j2))
            sheet1.write(i9, 6, str(response_dict['data']['list'][j1]['inputs'][j2]['prev_addresses']))
            sheet1.write(i9, 7, str(response_dict['data']['list'][j1]['inputs'][j2]['prev_value']))
            # print("j1:", j1)
            # print("j2:", j2)
            # print(response_dict['data']['list'][j1]['outputs'][j2]['addresses'])

    response_dict.clear()
    del r
    print("已下载第"+str(blockID)+"号区块")
book.close()
book1.close()
print("成功保存")
time_end=time.time()
print('下载共花费(s)：',time_end-time_start)
#1000个块共有10万条记录，一个xlsx文件可装100万条记录
#4000个块共用5148秒
#1000个块有13.5兆








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
