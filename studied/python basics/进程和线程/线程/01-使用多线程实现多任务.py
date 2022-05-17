'''
1.导入线程模块
2.创建线程对象
3.启动线程并执行任务
'''

import time
from threading import Thread
def sing():
    for i in range(3):
        print("唱歌...")
        time.sleep(1)


def dance():
    for i in range(3):
        print("跳舞...")
        time.sleep(1)


if __name__=='__main__':
    sing_thread=Thread(target=sing)
    song_thread=Thread(target=dance)
    sing_thread.start()
    song_thread.start()
    # sing()
    # dance()