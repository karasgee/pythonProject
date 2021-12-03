Kevin = {'10/15': {'對手:': '灰狼', '上場時間': 32, '得分': 19, '籃板': 7},
         '10/12': {'對手': '76人', '上場時間': 26, '得分': 23, '籃板': 7},
         '10/9': {'對手': '公鹿', '上場時間': 23, '得分': 18, '籃板': 6},
         '10/4': {'對手': '湖人', '上場時間': 0, '得分': 0, '籃板': 0},
         '7/9': {'對手': 'ESP', '上場時間': 30, '得分': 14, '籃板': 2}}

Lebron = {'10/15': {'對手:': '國王', '上場時間': 29, '得分': 30, '籃板': 6},
          '10/12': {'對手': '勇士', '上場時間': 26, '得分': 17, '籃板': 6},
          '10/9': {'對手': '太陽', '上場時間': 0, '得分': 0, '籃板': 0},
          '10/4': {'對手': '勇士', '上場時間': 18, '得分': 9, '籃板': 3},
          '7/9': {'對手': '太陽', '上場時間': 0, '得分': 0, '籃板': 0}}

Markus = {'10/15': {'對手:': '雷霆', '上場時間': 30, '得分': 31, '籃板': 5},
          '10/12': {'對手': '雷霆', '上場時間': 0, '得分': 0, '籃板': 0},
          '10/9': {'對手': '灰狼', '上場時間': 4, '得分': 0, '籃板': 0},
          '10/4': {'對手': '勇士', '上場時間': 16, '得分': 5, '籃板': 0},
          '7/9': {'對手': '快艇', '上場時間': 10, '得分': 3, '籃板': 1}}
x = [1, 2, 3, 4, 5]
num_Kevin = [Kevin[key]['得分'] for key in Kevin]
num_Lebron = [Lebron[key]['得分'] for key in Lebron]
num_Markus = [Markus[key]['得分'] for key in Markus]
plt.xticks(x)
plt.plot(x, num_Kevin, '-*', color='r', label="Kevin")
plt.plot(x, num_Lebron, '--^', color='g', label="Lebron")
plt.plot(x, num_Markus, ':+', color='b', label="Markus")
plt.xlabel("Round", fontsize=16)
plt.ylabel("Score", fontsize=16)
plt.title("Game Result", fontsize=24)
plt.legend(loc='best')

plt.show()

plt.plot(x, num_Markus, ':+', color='b', label="Markus")
plt.show()