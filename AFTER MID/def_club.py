'''
name = ['a','b', 'c' , 'd']
for i in range(len(name)):
    print({name[i]})
'''
def qooqqoqo():
    print("cc")
    ans = []  # 設定ans

    while True:  # 迴圈開始

        input_ans = input('input')
        if input_ans == '0':
            break
        else:
            print(input_ans)
            ans.append(input_ans)

    return (ans)  # 結束


print(qooqqoqo())
