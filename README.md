<h1 align="center" >Welcome to ReiAyanami</h1>

 <p align="center">
    <a href="https://github.com/Ascotbe/ReiAyanami"><img alt="Release" src="https://img.shields.io/badge/Ascotbe-ReiAyanami-green"></a>
    <a href="https://github.com/Ascotbe/ReiAyanami"><img alt="Release" src="https://img.shields.io/badge/LICENSE-GPL-ff69b4"></a>
	<a href="https://github.com/Ascotbe/ReiAyanami/stargazers"><img alt="Release" src="https://img.shields.io/github/stars/ascotbe/ReiAyanami.svg"></a>
	<a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Version-0.1-red"></a>
 </p>

### :point_right:关于ReiAyanami

这是一个快速端口发现扫描器，可以帮助红队在内网机器上快速进行扫描，适用场景：

- 没有任何代码环境以及未安装Nmap并且无法出网
- 演习环境禁止安装任何东西
- 只有Python代码环境并且机器不能出网（该环境如果要使用Python版禁止使用-t方式，请使用-r方式



### :loudspeaker:使用说明

| 命令 | 作用                   | 备注                                                         |
| ---- | ---------------------- | ------------------------------------------------------------ |
| -t   | 自动生成方式进行扫描   | 该种方法支持192.168.1.1和192.168.1.1/24这两种输入方式，该方式需要目标机器装有`IPy`这个包，如果目标机器只有Pyhon环境推荐使用 **-r** 来操作 |
| -n   | 线程数                 | 默认10个线程运行                                             |
| -o   | 输出结果到文件         | 默认输出文件为 **port.txt**                                  |
| -p   | 列表形式的端口         | 只要是使用非数字隔开即可，超过65535的端口都会剔除，如果不输出 **-p** 或者 **-P** 会对默认端口进行扫描。eg:22,139,445,3389 |
| -P   | 范围形式的端口         | 只要是使用非数字隔开即可，超过65535的端口都会剔除，如果不输出 **-p** 或者 **-P** 会对默认端口进行扫描。eg:1-65535 |
| -r   | 读取文件中的IP进行扫描 | 在文件中每个IP分一行                                         |



### :gift:自行编译

由于打包的文件过于大，不适合快捷传输，所以需要干净的Python环境，建议使用完全干净的系统和只安装`pyinstaller`、`IPy`这两个包的Python环境

> Windows

建议在Windows XP上进行编译好通用全系统运行，需要使用如下环境

- Python 3.4.4
- pywin32-221版本

编译命令如下，编译好的文件在WindowsXP 32位以上系统运行良好

```
python3 -m pip install pyinstaller==3.2.1
python3 -m pip install IPy==1.0
pyinstaller -F ReiAyanami.py --icon=eva.ico
```

> Linux

Linux编译需要使用32位系统和64位系统进行编译两次

```
python3 -m pip install pyinstaller==3.2.1
python3 -m pip install IPy==1.0
pyinstaller -F ReiAyanami.py
```

### :warning:免责声明

在原有的[协议](https://github.com/Ascotbe/ReiAyanami/blob/master/LICENSE)中追加以下内容：

- 本项目禁止进行未授权商业用途
- 本项目仅面向**合法授权**的企业安全建设行为，在使用本项目进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。
- 如您在使用本项目的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。
- 在使用本项目前，请您**务必审慎阅读、充分理解各条款内容**，限制、免责条款或者其他涉及您重大权益的条款可能会以加粗、加下划线等形式提示您重点注意。 除非您已充分阅读、完全理解并接受本协议所有条款，否则，请您不要使用本项目。您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。
