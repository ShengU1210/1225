import requests

url = 'https://rate.bot.com.tw/xrt/flcsv/0/day'
rate = requests.get(url)
rate.encoding = 'utf-8'
rt = rate.text
rts = rt.split('\n')

for i in rts:
    try:
        a = i.split(',')
        if len(a) > 12:  # 確保資料行有至少 13 個欄位
            print(a[0] + ': ' + a[12])
    except Exception as e:
        print("解析錯誤:", e)
