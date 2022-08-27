# auto_rar
## 功能
使用密码表解压rar文件，如果密码不存在，则允许输入密码存入密码表

## 背景
平时会下载很多工口物，他们往往又改了后缀名又加了密码，操作起来十分麻烦。<br>
于是我萌生了一个想法，为什么不能右键点一下按钮就能实现改后缀+解压一条龙呢？
这个小玩应就这么诞生了。

## 使用方法
因为这玩意是我自己用，所以就不整什么保姆级教程了。<br>
// -w是为了不弹窗，-F是为了打包成一整个exe文件<br>
1、新建一个目录，存放程序和密码表的。<br>
2、在注册表 HKEY_CLASSES_ ROOT / Directory / background / shell 下面，新增一个auto_rar的项。<br>
3、在auto_rar下，新增一个command的项，值为 D:\右键脚本\auto_rar\main.exe %1 目录嘛反正就是自己随便放一个。<br>
4、把第一步的main.exe放到第三步的目录里。<br>
5、创建一个password.txt，也放到这个目录里，修改main.py里的密码文件目录，和你这里配置的一样。<br>
6、检查一下main.py里的winrar地址对不对。<br>
7、pyinstaller -F main.py -w，把生成的main.exe放到第一步的目录里。

