from bs4 import BeautifulSoup

html_doc = open('C:/Users/kwonohsem/Downloads/cookbook_c-2/sample-html.html', 'r').read() #html_doc 변수로 sample-html.html을 읽기전용으로 저장하기
soup = BeautifulSoup(html_doc, 'html.parser') #soup 변수에 BeutifulSoup 객체 생성 뒤에 인수 html.parser을 사용하면 soup객체에 로드되고 파싱돼 사용할 준비가 됨.

print('\n\nHTML이 제거된 전체 텍스트 :')
print(soup.get_text())

print('<title>태그에 액세스 :', end = ' ')
print(soup.title)