def solution(phone_book):
    for idx1 in range(len(phone_book)):
        phone = phone_book[idx1]
        N = len(phone)
        for idx2 in range(len(phone_book)):
            if idx1 != idx2 and phone == phone_book[idx2][:N]:
                return False
    return True


if __name__ == "__main__":
    INPUT1 = [
        ["119", "97674223", "1195524421"],
        ["123", "456", "789"],
        ["12", "123", "1235", "567", "88"]
    ]
    ANSWER = [
        False,
        True,
        False
    ]

    for index in range(2):
        print(True) if ANSWER[index] == solution(INPUT1[index]) else print(False)