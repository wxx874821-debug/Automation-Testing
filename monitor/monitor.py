import requests
import time

urls = [
    "https://www.jd.com", 
    "https://www.taobao.com"
]

results = []

for url in urls:
    start_time = time.time()
    try:
        response = requests.get(url, timeout=5)  # 超时 5 秒
        duration = time.time() - start_time
        status = response.status_code
    except Exception as e:
        duration = None
        status = f"Error: {e}"
    
    results.append({
        "url": url,
        "status": status,
        "response_time": duration
    })

print(results)

import pandas as pd

df = pd.DataFrame(results)
df.to_excel("monitor_results.xlsx", index=False)
print("Results saved to monitor_results.xlsx")

import time

while True:
    results= []
    for url in urls:
        start_time = time.time()
        try:
            response = requests.get(url, timeout=5)  # 超时 5 秒
            duration = time.time() - start_time
            status = response.status_code
        except Exception as e:
            duration = None
            status = f"Error: {e}"
        
        results.append({
            "url": url,
            "status": status,
            "response_time": duration
        })

    df = pd.DataFrame(results)
    df.to_excel("monitor_results.xlsx", index=False)
    print("finish")

    time.sleep(3600)