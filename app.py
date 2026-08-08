import json

from flask import Flask, render_template, request

from api.search_job import searchjob
from tools.readPDF import readPDF
from api.jianlifenxi import jlfx
from api.mianshitisc import mstsc
from api.mianshijieguofx import msjgfx

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("AIInterviewer.html")

@app.route('/search_job', methods=['GET'])
def search_job():
    return render_template("search_job.html")

@app.route('/sea_job', methods=['POST'])
def sea_job():
    jobName = request.form.get('jobName')
    salaryMin = request.form.get('salaryMin')
    workExperience =request.form.get('workExperience')
    city = request.form.get('city')
    companyName = request.form.get('companyName')
    education = request.form.get('education')
    joblist = searchjob(jobName,city,companyName,education,salaryMin,workExperience)
    return render_template("job_list.html",jobLsts=joblist)

@app.route('/ResumeAnalysis', methods=['GET'])
def ResumeAnalysis():
    return render_template("ResumeAnalysis.html")

@app.route('/AnalysisResult', methods=['POST'])
def AnalysisResult():
    jobName = request.form.get('jobName')
    file = request.files['file']
    file_content = file.read()
    text = readPDF(file_content)
    fxjg = jlfx(text,jobName)
    return render_template("results.html", results=fxjg)

@app.route('/AIInterviewer', methods=['GET'])
def AIInterviewer():
    return render_template("AIInterviewer.html")

@app.route('/InterviewQuestion', methods=['POST'])
def InterviewQuestion():
    jobName = request.form.get('jobName')
    workExperience = request.form.get('workExperience')
    file = request.files['file']
    file_content = file.read()
    text = readPDF(file_content)
    questions = mstsc(text,jobName,workExperience)
    return render_template("Interview_question.html",question=questions)

@app.route('/InterviewResults',methods=['POST'])
def InterviewResults():
    data1 = request.form
    data2 = data1.get('data')
    if not data2:
        return "提交数据为空！",400
    try:
        data = json.loads(data2)
    except json.JSONDecodeError:
        return "前端数据解析错误",400

    jobName = data['jjobName']
    data.pop('jjobName')

    # 把面试题+回答字典拼接成文本
    content_list = []
    for q, a in data.items():
        content_list.append(f"面试题：{q}\n候选人回答：{a}")
    full_text = "\n=====\n".join(content_list)

    try:
        jg = msjgfx(full_text, jobName)
        print("AI返回结果：", jg)
    except Exception as e:
        print("AI调用异常：",e)
        jg = {"综合评估结果": 0, "评语": "AI分析出错"}

    score = jg['综合评估结果']
    return render_template("InterviewResults.html",jg=jg,score=score,jobName=jobName)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=5000)