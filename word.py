import docx

def getTextWord(wordFileName):
    doc = docx.Document(wordFileName) #doc변수에 wordFileName 로드
    fullText = [] #텍스트 변수 추가
    for para in doc.paragraphs:
        fullText.append(para.text) #텍스트 변수에 위에 로드 된 데이터 추가
    return '\n'.join(fullText) #추가된 데이터를 가진 텍스트 변수를 반환