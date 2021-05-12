def solution(record):
    user_name = dict()
    chat = []
    chat_uid = []
    for info in record:
        _info = info.split(" ")

        if _info[0] in ["Enter", "Leave"]:
            chat.append(_info[0])
            chat_uid.append(_info[1])
            # 새로운 user or 새로운 name으로 재 접속
            if _info[0] == "Enter":
                user_name[_info[1]] = _info[2]
        # change mode
        else:
            user_name[_info[1]] = _info[2]

    answer = []
    for i in range(len(chat)):
        if chat[i] == "Enter":
            answer.append(user_name[chat_uid[i]] + "님이 들어왔습니다.")
        elif chat[i] == "Leave":
            answer.append(user_name[chat_uid[i]] + "님이 나갔습니다.")

    return answer


# test
print(
    solution(
        [
            "Enter uid1234 Muzi",
            "Enter uid4567 Prodo",
            "Leave uid1234",
            "Enter uid1234 Prodo",
            "Change uid4567 Ryan",
        ]
    )
)
# result
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]