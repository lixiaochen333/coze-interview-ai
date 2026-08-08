import requests
import json

url = "https://api.coze.cn/v1/workflow/run"
headers = {
    "Authorization": "Bearer pat_DpQmgAU9DCe7F8ILoAvfdUXY33EA118kQFKZCGGvlQ3kxnHUbfPc3sSuFHFiZIVr",
    "Content-Type": "application/json"
}

payload = {
    "workflow_id": "7670219418198130722",
    "is_async": False,
    "parameters": {
        "question": "面试官：说一说Python装饰器原理\n候选人：装饰器可以在不修改原函数代码的情况下扩展函数功能，本质是接收函数作为参数，返回新函数，利用闭包实现。",
        "jobName": "后端开发工程师"
    }
}

try:
    resp = requests.post(url, headers=headers, json=payload, timeout=30)
    text = resp.text
    print("原始返回文本：", text)
    res_json = resp.json()
    print("res_json['data'] 值：", res_json["data"])
    print("res_json['data'] 类型：", type(res_json["data"]))

    # 判断data是字符串还是字典
    data = res_json["data"]
    if isinstance(data, str):
        data = json.loads(data)

    output_str = data["output"]
    result = json.loads(output_str)

    print("综合评估结果：", result["综合评估结果"])
    print("评语：", result["评语"])

except requests.exceptions.Timeout:
    print("请求超时")
except Exception as e:
    print("异常：", e)