text = "Hello, World!"
text2 = "apple,banana,cherry"

fruits = ["apple", "banana", "cherry"]


# count : 문자열 내 특정 문자 몇 개 있는지 찾기
count = text.count("l")
print(count) # 3

# find : 특정 문자열이 처음 나오는 위치 찾기
# 없을 경우 -1 return
position = text.find("World")
print(position) # 7

# index : 특정 문자열이 처음 나오는 위치(인덱스값) 찾기
# 없을 경우 ValueError
try:
    position2 = text.index("World")
    print(position2) # 7
except ValueError:
    print("문자열이 없습니다.")

# join : 특정 문자열을 기준으로 다른 문자열 합쳐줌
joined_fruits = ', '.join(fruits)
print(joined_fruits) # "apple, banana, cherry"

# upper : 문자열 내 소문자를 대문자로 변경
# lower : 대문자를 소문자로 변경
uppercase_text = text.upper()
lowercase_text = text.lower()
print(uppercase_text, lowercase_text) # HELLO, WORLD! hello, world!

# replace : 특정 문자열을 다른 문자열로 변경
replaced_text = text.replace("World", "Python")
print(replaced_text) # Hello, Python!

# split : 특정 문자를 기준으로 나누는 메소드
# 결과는 리스트 형태
fruits2 = text2.split(',')
print(fruits2) # ['apple', 'banana', 'cherry']

# len : 리스트 길이 반환
print(len(fruits)) # 3

# del : 특정 요소 삭제
del fruits[2] # [a] > a는 인덱스 번호
print(fruits) # ['apple', 'banana']

# append : 리스트 맨 뒤에 새로운 요소 추가
fruits.append('tomato')
print(fruits) # ['apple', 'banana', 'tomato']

# sort : 오름차순으로 정렬
# str 값은 영문 순서
fruits.sort()
print(fruits) # ['apple', 'banana', 'tomato']

# reverse : 리스트 요소의 순서를 뒤집기
fruits.reverse()
print(fruits) # ['tomato', 'banana', 'apple']

# index : 특정 요소의 인덱스 반환
print(fruits.index('banana')) # 1

# insert : 특정 위치(인덱스번호)에 요소를 삽입
fruits.insert(0, 'mango')
print(fruits) # ['mango', 'tomato', 'banana', 'apple']

# remove : 특정 요소를 삭제
fruits.remove('mango')
print(fruits) # ['tomato', 'banana', 'apple']

# pop : 리스트에서 마지막 요소(같은 요소가 있을때)를 빼낸 뒤, 그 요소를 삭제
fruits.pop(1)
print(fruits) # ['tomato', 'apple']

# count : 특정 요소의 개수를 셈
print(fruits.count('tomato')) # 1

# extend : 리스트 확장하여 새로운 요소 추가
# += 로도 가능 / fruits += [1, 2, 3]
fruits.extend([1, 2, 3])
print(fruits) # ['tomato', 'apple', 1, 2, 3]

# --------------------------------------------------
# 딕셔너리
empty_dict = {}
my_dict = {'apple': 1, 'banana':2, 'orange':3}
person = {'name':'John', 'age':30, 'gender':'male'}
print(my_dict) # {'apple': 1, 'banana': 2, 'orange': 3}

# 딕셔너리 쌍 추가
my_dict['grape'] = 4
print(my_dict) # {'apple': 1, 'banana': 2, 'orange': 3, 'grape': 4}

# 특정요소 삭제
del my_dict['apple']
print(my_dict) # {'banana': 2, 'orange': 3, 'grape': 4}

# 특정 key에 해당하는 value 얻기
# key가 없다면 KeyError
print(my_dict['banana']) # 2

# key를 리스트화
key_list = list(my_dict.keys())
print(key_list) # ['banana', 'orange', 'grape']

# value를 리스트화
value_list = list(my_dict.values())
print(value_list) # [2, 3, 4]

# items : 튜플 형태로 변환
items = my_dict.items()
print(items) # dict_items([('banana', 2), ('orange', 3), ('grape', 4)])

# clear : 모든 딕셔너리 요소 삭제
my_dict.clear()
print(my_dict) # {}

# get : 키에 대응하는 값을 반환
# key가 없는 경우 None 반환
name = person.get('name')
email = person.get('email')
print(name, email) # John None
email2 = person.get('email', 'unknown') # 기본값 설정 방법
print(email2) # unknown

# in : 해당 키가 딕셔너리 안에 있는지 확인
print('name' in person) # True
print('email' in person) # False
