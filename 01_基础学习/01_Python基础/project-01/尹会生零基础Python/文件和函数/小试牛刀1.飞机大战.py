"""
对象：我方飞机、敌机
属性：坐标、生命值
行为：移动、命中
"""
from pynput.keyboard import Key,Listener,KeyCode

background = [
    [0, 0, 0],
    [0, 'x', 0],
    [0, 0, 0]
]

print(background[0])
print(background[1])
print(background[2])

def on_press(key):

    if key == KeyCode.from_char('w'):
        moved = False
        for i in range(0,3):
            for j in range(0,3):
                if  background[i][j] == 'x' and i > 0:
                    background[i][j] = '0'
                    background[i-1][j] = 'x'
                    moved = True
                    break
            if moved:
                break

            # else:
            #     continue
            # break

    elif key == KeyCode.from_char('a'):
        moved = False
        for i in range(0, 3):
            for j in range(0, 3):
                if background[i][j] == 'x' and j > 0:
                    background[i][j] = '0'
                    background[i ][j-1] = 'x'
                    moved = True
                    break
            if moved:
                break
            # else:
            #     continue
            # break

    elif key == KeyCode.from_char('s'):
        moved = False
        for i in range(0, 3):
            for j in range(0, 3):
                if background[i][j] == 'x' and i < 2:
                    background[i][j] = '0'
                    background[i + 1][j] = 'x'
                    moved = True
                    break
            if moved:
                 break
            # else:
            #     continue
            # break


    elif key == KeyCode.from_char('d'):
        moved = False
        for i in range(0, 3):
            for j in range(0, 3):
                if background[i][j] == 'x' and j < 2:
                    background[i][j] = '0'
                    background[i][j + 1] = 'x'
                    moved = True
                    break
            if moved:
                break

            # else:
            #     continue
            # break

    print()
    print(background[0])
    print(background[1])
    print(background[2])

with Listener(on_press=on_press) as listener:
    listener.join()