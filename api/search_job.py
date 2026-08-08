import requests
import json
def searchjob(jobName,city,companyName,education,salaryMin,workExperience):
    # #个人访问令牌
    # token = ''
    # #工作流ID
    # workflow_id = '7660366179324084258'
    # #应用ID
    # app_id = '7660323979546673206'

    #开始节点传输的值
    payload = {
        "jobName": jobName,
        "city": city,
        "companyName": companyName,
        "education": education,
        "salaryMin": salaryMin,
        "workExperience": workExperience
    }
    #请求头
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json"
    }

    #请求体
    body = {
        "workflow_id": workflow_id,
        "app_id": app_id,
        "parameters": payload
    }

    response = requests.post('https://api.coze.cn/v1/workflow/run', headers=headers, json=body)

    data = json.loads(response.text)['data']
    output = json.loads(data)['output']

    return output

if __name__ == '__main__':
    searchjob("python开发工程师",'','',7,5000,3)