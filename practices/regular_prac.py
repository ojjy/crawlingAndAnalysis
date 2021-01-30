import re
p = re.compile('[a-z]+')
m = p.match('python')
m2 = p.match(' 3 python') # 하나라도 일치하지 않으면 None
print(m)
print(m2)
print("매치된 문자열: ", m.group()) # 매치된 문자열
print("매치된 문자열 시작점: ", m.start())
print("매치된 문자열 끝점: ", m.end())
print("매치된 문자열 (시작점, 끝점) 튜: ", m.span())

m = p.search('python')
m2 = p.search('3 python') #search는 전체 문자열객체가 일치하지 않아도 일치하는 부분 return
print(m)
print(m2)


m = p.findall('life is toooo long') # 일치하는 것을 찾아서 list로 return
print(m)
m2 = p.finditer('life is toooo long') # 이터레이터 오브젝트 생성
print(m2)

for item in m2:
    print(item) # match 객체 생성되고 일치 여부 확

# 컴파일 옵션
# 1. DOTALL, S
# . 닷은 줄바꿈을 제외함 모든 문자와 매치
p = re.compile('a.b')
m = p.match('a\nb') # 줄바꿈이므로 매치되지 않음
print(m)

p = re.compile('a.b', re.DOTALL) #DOTALL옵션은 줄바꿈도 매치 되도록 하는 옵션 약어 S를 써도 됨
m2 = p.match("a\nb") # DOTALL 옵션이 있으므로 \n가 있어도 매치
print(m2)

# 2. IGNORECASE, I 대소문자 상관없이 일치하면 매치
p = re.compile('[a-z]+')
m3_1 = p.match('python')
print(m3_1)
m3_2 = p.match("Python")
print(m3_2)
m3_3 = p.match('PYTHON')
print(m3_3)

p = re.compile('[a-z]+', re.IGNORECASE)
m3_1 = p.match('python')
print(m3_1)
m3_2 = p.match("Python")
print(m3_2)
m3_3 = p.match('PYTHON')
print(m3_3)

# 3. Multiline 옵션
p = re.compile("^python\s\w+") #^는 맨처음 \s 공백 \w 알파벳, 숫자, _중 한문자가 + 여러번 반
data = """python one :: let us practice how to make python programs.
 And let us be talented python programmer.
python two :: We can do everything.
"""

print(p.findall(data))

p = re.compile("^python\s\w+", re.M) #^는 맨처음 \s 공백 \w 알파벳, 숫자, _중 한문자가 + 여러번 반
# 멀티라인 옵션은 여러줄이 있어도 매치되는 것 찾는다.
data = """python one :: let us practice how to make python programs.
 And let us be talented python programmer.
python two :: We can do everything.
"""
print(p.findall(data))


# 4. Verbose 정규식을 장황하게 길게 써도 설명을 달수 있게 끊기 가능



# 백슬레시 \s는 공백을 의미 \section의 경우 백슬래시를 쓰고 싶으면 \\ 백슬래시
# 그러나 파이썬에서 \\는 \로 치환되므로 실제로 \\\\네번을 써야 백슬래시 두개 의미
# 너무 길므로 raw string 의미하는 r'\\'쓰면 \\ 두번의미

