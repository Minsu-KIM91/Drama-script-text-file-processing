import os, re, codecs
os.chdir(r'C:\Users\alstn\OneDrive\바탕 화면\python')

f=codecs.open('mf_s1_ep1_pilot.txt', 'r', encoding='utf-8')
script102=f.read()

char=re.compile(r'[A-Z][a-z]+ :')
re.findall(char, script102)
# 여기까지 하고 실행시키면 위와 같은 문자열형태가 중복포함 다 나온다.
# 중복값 제거. set 키워드로 중복된 원소 지우기.
# a=[1,2,2,3,4,5,5,6]
# set(a)

set(re.findall(char, script102))

# 슬라이싱으로 특정위치의 문자 지우기.
claire='Claire :'
claire=re.sub(' :','',claire)
claire
# 위에 두줄 대신에 아래 한줄만 사용해도 됨.
claire[:-2]

# 중복제거한 목록에서 :과 (공백) 지워서 다듬기.
y=set(re.findall(char, script102))
z= list(y)
character=[]
for i in z:
	character += [i[:-2]]
character