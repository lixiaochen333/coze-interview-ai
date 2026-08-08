import PyPDF2
from io import BytesIO

def readPDF(file_content):
    #将字节流包装成对象
    pdf_file = BytesIO(file_content)
    #创建PDF阅读器对象
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in pdf_reader.pages:
        #读取当前页的内容
        text += page.extract_text()
    print(text)
    return text

if __name__ == '__main__':
    readPDF(open(r'D:\李小晨+后端实习生.pdf','rb').read())