# 3数之和

target = 183
list_b = [2, 3, 7, 12, 61, 71, 89, 91, 111]
list_a = []


def function():
    for i in list_b:
        target_two = target - i
        list_b.remove(i)
        list_aim = []
        for j in list_b:
            if target_two - j not in list_aim:
                list_aim.append(j)
            else:
                print(i, j, target_two - j)
                return
        list_b.append(i)

function()