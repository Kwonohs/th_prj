from PyPDF2 import PdfReader as reader
#오류가 해결이 안된다..
def getTextPDF(pdfFileName, password = ''):
    pdf_file = open(pdfFileName, 'rb')
    read_pdf = reader(pdf_file)
    if password != '':
        read_pdf.decrypt(password) #password를 넘겨서 암호를 사용해 파일의 암호 해제를 시도하는것
    text = []
    for i in range(0, len(reader.pages(pdf_file))):
        text.append(read_pdf.getPage(i).extractText())
    return '\n'.join(text)