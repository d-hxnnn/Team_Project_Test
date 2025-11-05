#word_list 불러오기
import random

def load_words():
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    return words

word_list = load_words()

#answer = 랜덤 추출된 정답, secret = 글자 수만큼 '_' 출력
player_heart = 6
answer = random.choice(word_list).lower()
secret = ["_ "] * len(answer)
print("선택된 단어는 %d글자입니다." %len(answer))
print(" ".join(secret))


#글자 존재하면 secret[t번째]를 guess로 치환, join 함수로 문자열로 출력하여 _ _ _ n _로 출력
while (player_heart > 0):
    guess = input("철자를 추측해주세요").lower()
    t = answer.find(guess)
    if t == -1:
        print("Wrong!")
        player_heart -= 1
        print("남은 목숨은 %d개 입니다" %player_heart)
    elif t>=0:
        secret[t] = guess 
        print(" ".join(secret))

