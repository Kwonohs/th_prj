namesList = ['유나', '지은', '스튜어트', '케빈']
sentence = '우리 강아지는 소파 위에서 잔다.'

names  = 'j'.join(namesList) #namesList에 str을 하나의 str로 붙여주는 함수
print(type(names), ':', names)
print(names)

wordList = sentence.split(' ') #띄어쓰기로 sentence문장을 분리하기
print((type(wordList)), ':', wordList)

additionExample = '파이썬' + '파이썬' + '파이썬'
multiplicationExample = '파이썬' * 2
print('텍스트 덧셈 :', additionExample)
print('텍스트 곱셈 :', multiplicationExample)