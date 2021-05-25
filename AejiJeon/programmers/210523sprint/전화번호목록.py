# 해쉬 이용한 풀이
# 시간 복잡도: O(n)

def solution(phone_book):
    answer = True
    phone_dict = {}
    for phone_number in phone_book:
        phone_dict[phone_number] = 1
    for phone_number in phone_book:

        temp = ""
        for number in phone_number:
            temp += number
            # phone_number의 접두사인 temp가 
            # phone_book에 있는 phone_number와 같은 경우

            if temp in phone_dict and temp != phone_number:
                answer = False
    return answer