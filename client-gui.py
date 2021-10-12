import tkinter as tk
import client as cli

def CreateWindow():
    def OnBtnUp(event):
        cli.main()
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

