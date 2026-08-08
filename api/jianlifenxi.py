import requests
import json
from tools.readPDF import readPDF
def jlfx(file,jobName):
    # 个人访问令牌
    token = ''
    # 工作流ID
    workflow_id = '7670160934119702582'
    # 应用ID
    app_id = '7660323979546673206'

    # 开始节点传输的值
    payload = {
        "file": file,
        "jobName": jobName
    }

    # 请求头
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json"
    }

    # 请求体
    body = {
        "workflow_id": workflow_id,
        "app_id": app_id,
        "parameters": payload
    }

    response = requests.post('https://api.coze.cn/v1/workflow/run', headers=headers, json=body)

    data = json.loads(response.text)['data']
    output = json.loads(data)['output']
    print(output)
    return output

if __name__ == '__main__':
    text = readPDF(open(r'D:\李小晨+后端实习生.pdf','rb').read())
    jlfx(text,"后端实习生")