import random
hands = ["グー", "チョキ", "パー"]
com_answer = random.randint(1, 3)
print("COM = " + hands[com_answer - 1])
