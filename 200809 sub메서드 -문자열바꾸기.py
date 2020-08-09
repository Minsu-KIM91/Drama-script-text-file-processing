# re.sub(찾을 패턴, 대체할 문자, 찾을 문자열)
import re
sentence = 'I love a lovely dog, really. I am not telling a lie. What a pretty dog! I love this dog.'
re.sub(r'dog', 'cat', sentence)

# 불필요한 공백 줄이기
words = 'I am home now. \n\n\nI am with my cat.\n\n'
re.sub(r'\n','',words)
# print(words)

# ly로 끝나는 단어 추출하기.
sentence = 'I love a lovely dog, really. I am not telling a lie, What a pretty dog! I love this dog.'
re.findall(r'\w+ly', sentence)

