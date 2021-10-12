import tkinter as tk
import client as cli


# 测试多个客户端的性能
def test():
    global pool
    pool = set()

    print('begin creation')
    # 创建一组客户端
    for i in range(100):
        pool.add( cli.Client() )
    print('create 100 client complete!')

def CreateWindow():
    def OnBtnUp(event):
        test()
    app = tk.Tk()
    app['width']  = 400
    app['height'] = 300
    app.bind('<ButtonRelease-1>', OnBtnUp)
    return app

def main():
    app = CreateWindow()
    print('Click on Window to send message ...')
    print('-----------------------------------')
    app.mainloop()
    print('-----------------------------------')
    print('End')

if __name__ == '__main__':
    main()

