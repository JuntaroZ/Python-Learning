import random
janken_table = ["グー", "チョキ", "パー"]
com_answer = random.randint(0, 2)
print("Com =", janken_table[com_answer])

while True:
    try:
        # グー、チョキ、パーを数字で入力してもらう
        your_answer = int( input("0.グー、1.チョキ、2.パーのいずれか数字を半角で入力してください：") )
        print("You =", janken_table[your_answer])
        break
    except:
        print("半角数字(0,1,2)を入力してください。")
        continue

