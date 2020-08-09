# 모던 패밀리 대본 텍스트 파일 가공하기.
import os, re, codecs
os.chdir(r'C:\Users\alstn\OneDrive\바탕 화면\python')

f= codecs.open('mf_s1_ep1_pilot.txt', 'r', encoding = 'utf-8')
script101 = f.read()

# print(script101[:100])

# 특정 등장인물의 대사만 모으기.(Claire)
Line = re.findall(r'Claire :.+', script101)
# print(Line[:3])
for item in Line[:3]:
	print(item)

f.close

f= open('Claire.txt', 'w', encoding='utf-8')
Claire=''
for i in Line:
	Claire += i +'\n'
f.write(Claire)
f.close()




