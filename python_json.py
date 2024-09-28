import json
import csv

# 假設這是你的 JSON 資料
json_data = '''
[
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Anna", "age": 22, "city": "London"},
    {"name": "Mike", "age": 32, "city": "San Francisco"}
]
'''

# 解析 JSON 資料
data = json.loads(json_data)

# 指定 CSV 檔案名稱
csv_file = 'csv_week3.csv'

# 取得 JSON 資料的欄位名稱
fieldnames = data[0].keys()

# 將 JSON 資料寫入 CSV 檔案
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f"JSON 資料已成功轉換並儲存到 {csv_file}")