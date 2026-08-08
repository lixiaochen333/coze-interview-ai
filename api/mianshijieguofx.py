import requests
import json


def msjgfx(question, jobName):
    # 个人访问令牌
    token = ""
    # 工作流id
    workflow_id = "7670219418198130722"
    # 应用id
    app_id = "7660323979546673206"

    # 开始节点输入的值
    payload = {
        "question": question,
        "jobName": jobName
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
    response = requests.post("https://api.coze.cn/v1/workflow/run", headers=headers, json=body,timeout=60)

    # 老师原版解析逻辑，两层loads
    resp_all = json.loads(response.text)
    data = resp_all['data']
    inner = json.loads(data)
    output_str = inner['output']
    print("====Coze原始output_str====")
    print(repr(output_str))
    # 判空保护
    if not output_str or output_str.strip() == "":
        raise Exception("Coze返回output为空，请检查输出节点配置")

    # 解析中文字段JSON
    try:
        output_dict = json.loads(output_str)
    except json.JSONDecodeError as e:
        print("JSON解析失败，原始字符串：", repr(output_str))
        raise e

    return output_dict


# 本地测试入口
if __name__ == '__main__':
    test_ques = """面试题：请讲一下你做过的接口测试项目，介绍测试流程，遇到过什么bug如何解决？
候选人回答：
我之前做过用户登录模块接口测试，首先阅读接口文档，使用Postman设计测试用例，覆盖正常登录、密码错误、账号不存在、入参为空边
"""
    res = msjgfx(test_ques, "软件测试工程师")
    print("=====最终评估结果====")
    print(res)