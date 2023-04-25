phone_book = {"John":"123-4567", "Jane":"234-5678" , "Max":"345-6789"}

def search ():
    name = yield
    while True:
        if name in phone_book:
            phone_number = phone_book[name]
        else : 
            phone_number = "찾을 수 없음"
        name = yield phone_number
        
# 코루틴 객체 생성
search_coroutine = search()
next(search_coroutine)

# 검색 예시
result = search_coroutine.send("John")
print(result) # 123-4567
 
result = search_coroutine.send("Jane")
print(result) # 234-5678

result = search_coroutine.send("Sarah")
print(result) # 찾을 수 없음