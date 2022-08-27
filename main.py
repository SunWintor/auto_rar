import os
import subprocess
import sys
import tkinter

PWD_FILE = 'D:/右键脚本/auto_rar/password.txt'
DETACHED_PROCESS = 0x00000008


def auto_rar(filename):
    print("fileName:" , filename)
    try:
        with open(PWD_FILE, 'r', encoding='utf-8') as passFile:
            for line in passFile.readlines():
                password = line.strip('\n')
                print("password:" , password)
                flag = rar_once(filename, password)
                if flag:
                    print('pass')
                    return True
    except Exception as e:
        print('error:', e)
        return False


def rar_once(filename, password):
    dir = os.path.dirname(filename)
    print("dir:" , dir)
    # 使用Rar.exe而非WinRAR.exe的原因是，Rar.exe不会弹出命令行
    cmd = r'"C:\Program Files\WinRAR\Rar.exe" X -Y -p%s %s -AD %s ' % (password, filename, dir)
    print("cmd:" , cmd)
    # 这种方式可以禁止命令行弹出
    subprocess.call(cmd, creationflags=DETACHED_PROCESS)
    os.system(cmd)
    if os.system(cmd) == 0:
        print('密码正确!', password)
        return True


def pwd_window():
    win = tkinter.Tk()
    win.title('window')
    win.geometry('300x200')
    ent = tkinter.Entry(win, font=(None, 24))
    btn = tkinter.Button(win, text='输入密码', font=(None, 24), command=lambda: pwd_btn(ent.get()))
    ent.pack()
    btn.pack()
    win.protocol('WM_DELETE_WINDOW', close_window)
    win.mainloop()


def close_window():
        sys.exit()


def pwd_btn(password):
    try:
        rar_once(sys.argv[1], password)
        with open(PWD_FILE, 'a') as pwd:
            pwd.write('\n' + password)
        sys.exit()
    except Exception as e:
        print('error:', e)


if len(sys.argv) != 2:
    print("error")
    sys.exit()

over = auto_rar(sys.argv[1])
print("over:", over)
if not over:
    pwd_window()
