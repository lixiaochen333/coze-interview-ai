import requests
import json
from tools.readPDF import readPDF

def mstsc(input,jobName,workExperience):
    # 个人访问令牌
    token = ''
    # 工作流id
    workflow_id = '7670200338574557194'
    # 应用id
    app_id = '7660323979546673206'

    # 开始节点输入的值
    payload = {
        "input": input,
        "jobName": jobName,
        "workExperience": workExperience
    }

    # 请求头
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    # 请求体
    body = {
        "workflow_id": workflow_id,
        "app_id": app_id,
        "parameters": payload
    }

    # 发起请求
    response = requests.post("https://api.coze.cn/v1/workflow/run", headers=headers, json=body)
    # =========新增打印开始=========
    print("=== response.text 接口原始返回 ===")
    print(response.text)
    # =========新增打印结束=========

    resp_json = json.loads(response.text)
    data_str = resp_json['data']  # data_str 是字符串
    data = json.loads(data_str)  # 再解析一次，转成字典

    output_str = data['output']  # 这里就是output_str，Coze返回的json字符串
    # =========新增打印开始=========
    print("\n==== output_str原始内容 repr =====")
    print(repr(output_str))
    # =========新增打印结束=========

    output = json.loads(output_str)

    questions = []
    for i in output:
        que = i.get('question')
        questions.append(que)
    print(questions)
    return questions

if __name__ == '__main__':
    text = readPDF(open(r'D:\李小晨+后端实习生.pdf','rb').read())
    mstsc(text,"python开发工程师","1-3年")