import random

janken_table = ["グー", "チョキ", "パー"]
com_answer = random.randint(0, 2)
print("Com =", janken_table[com_answer])

# グー、チョキ、パーを数字で入力してもらう
your_answer = int( input("0.グー、1.チョキ、2.パーのいずれかを半角数字で入力してください：") )
print("You =", janken_table[your_answer])
