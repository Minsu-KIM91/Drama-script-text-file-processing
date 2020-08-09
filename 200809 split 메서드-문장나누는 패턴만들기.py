# re.split(패턴, 문자열)
import re
sentence = 'I love a lovely dog, really. I am not telling a Lie. What a pretty dog! I love this dog'
re.split(r'[.?!]', sentence)


data = 'a:3; b:4; c:5'
for i in re.split(r';', data):
	print(re.split(r':', i))


