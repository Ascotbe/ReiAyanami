#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# project address:https://github.com/Ascotbe/ReiAyanami
import socket
import threading
import argparse
import re
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t','--Target',type=str,help="Target IP, support two modes of 192.168.1.1 or 192.168.1.1/24")
parser.add_argument('-n','--ThreadsNumber',type=int,help="The number of threads to open, the default is 10")
parser.add_argument('-o','--OutputFile',type=str,help="The name of the output file, output to port.txt by default")
parser.add_argument('-p','--PortListInformation',type=str,help="The input port format is 22,445,3389")
parser.add_argument('-P','--PortRangeInformation',type=str,help="The input port format is 1-65535")
parser.add_argument('-r','--ReadFile',type=str,help="Get IP scan from file")
class ThreadPool:  # 线程池，适用于单个插件
    def __init__(self):
        self.ThreaList = []  # 存放线程列表
        self.text = 0  # 统计线程数

    def Append(self, plugin,**kwargs):
        self.text += 1
        self.ThreaList.append(threading.Thread(target=plugin,kwargs=kwargs))

    def Start(self,ThreadNumber):
        print("\033[32m[ + ] "+str(len(self.ThreaList))+"pieces of content have been generated and are being executed in multiple threads\033[0m")
        for t in self.ThreaList:  # 开启列表中的多线程
            t.start()
            while True:
                # 判断正在运行的线程数量,如果小于5则退出while循环,
                # 进入for循环启动新的进程.否则就一直在while循环进入死循环
                if (len(threading.enumerate()) < ThreadNumber):
                    break
        for p in self.ThreaList:
            p.join()



def PortTest(**kwargs):
    ip=str(kwargs.get("ip"))#ip一定要强制转换为str类型，IPy这个包传入的值虽然输出是正常IP，但是类型是class的，socket不支持
    port=int(kwargs.get("port"))

    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.connect((ip, port))
        sk.settimeout(2)
        sk.close()
        print('\033[33m[ + ] Server %s port %d OK!\033[0m' % (ip, port))
        OpenPorts.append(ip+ ":" + str(port) + "\n")#传入列表中

    except Exception as e:
        #print(e)
        print('\033[31m[ ! ] Server %s port %d is not connected!\033[0m' % (str(ip), port))

def Main():
    Pool = ThreadPool()
    for Ip in IpLists:
        for Port in PortLists:
            Pool.Append(PortTest,ip=Ip,port=Port)

    Pool.Start(ThreadsNumber)  # 启动线程池
def PortHandling(PortInformation,PortType):#进行正则匹配处理
    try:
        Pattern = re.compile(r'\d*')  # 查找数字
        RegularResult = Pattern.findall(PortInformation)
        if PortType==1:#处理为范围类型数据
            ExtractContent=[]#剔除空字节内容和超过最大端口数据
            for i in RegularResult:
                if i != "" and int(i) <= 65535:
                    ExtractContent.append(i)
            PortStart=int(ExtractContent[0])#起始端口
            PortEnd=int(ExtractContent[1])#起始端口
            if PortEnd<PortStart:#如果用户输入错误为大的在前面小的在后面的话
                tmp=PortEnd
                PortEnd=PortStart
                PortStart=tmp
            for Port in range(PortStart,PortEnd+1):
                PortLists.append(Port)
        if PortType==2:#处理为字典类型数据
            for Port in RegularResult:
                if Port!=""and int(Port)<=65535:
                    PortLists.append(Port)
    except Exception as e:
        print("\033[31m[ ! ] Please enter the correct port content!\033[0m")

def Banner():
    end="\033[0m"
    red = "\033[25;31m"
    cyan = "\033[25;36m"

    LinuxHeader='''{}
         ██▀███  ▓█████  ██▓    ▄▄▄     ▓██   ██▓ ▄▄▄       ███▄    █  ▄▄▄       ███▄ ▄███▓ ██▓
        ▓██ ▒ ██▒▓█   ▀ ▓██▒   ▒████▄    ▒██  ██▒▒████▄     ██ ▀█   █ ▒████▄    ▓██▒▀█▀ ██▒▓██▒
        ▓██ ░▄█ ▒▒███   ▒██▒   ▒██  ▀█▄   ▒██ ██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██  ▀█▄  ▓██    ▓██░▒██▒
        ▒██▀▀█▄  ▒▓█  ▄ ░██░   ░██▄▄▄▄██  ░ ▐██▓░░██▄▄▄▄██ ▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██    ▒██ ░██░
        ░██▓ ▒██▒░▒████▒░██░    ▓█   ▓██▒ ░ ██▒▓░ ▓█   ▓██▒▒██░   ▓██░ ▓█   ▓██▒▒██▒   ░██▒░██░
        ░ ▒▓ ░▒▓░░░ ▒░ ░░▓      ▒▒   ▓▒█░  ██▒▒▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░▓
          ░▒ ░ ▒░ ░ ░  ░ ▒ ░     ▒   ▒▒ ░▓██ ░▒░   ▒   ▒▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░░  ░      ░ ▒ ░
          ░░   ░    ░    ▒ ░     ░   ▒   ▒ ▒ ░░    ░   ▒      ░   ░ ░   ░   ▒   ░      ░    ▒ ░
           ░        ░  ░ ░           ░  ░░ ░           ░  ░         ░       ░  ░       ░    ░
                                         ░ ░
                                                               {}     {} by:ascotbe  version:0.1 {}
            '''.format(cyan,end,red,end)
    WindowsHeader=u'''{}
    
                                Welcome ReiAyanami
    
    {}                                        {} by:ascotbe  version:0.1 {}
            '''.format(cyan,end,red,end)
    if sys.platform == "win32" or sys.platform == "cygwin":
        print(WindowsHeader)
    elif sys.platform == "linux" or sys.platform == "darwin":
        print(LinuxHeader)

if __name__ == '__main__':
    args = parser.parse_args()
    IpTarget = args.Target
    ThreadsNumber = args.ThreadsNumber
    OutputFile=args.OutputFile
    PortListInformation=args.PortListInformation#字典类型端口
    PortRangeInformation=args.PortRangeInformation#范围型端口
    ReadFile=args.ReadFile
    Banner()#输出横幅
    IpLists=[]#存放需要扫描的IP
    OpenPorts=[]#存放扫描开放的Ip:Port
    PortLists=[]#需要扫描的端口列表
    PortType=0#端口类型默认为0,1表示范围型端口,2表示字典型端口
    DefaultList=[20,21,22,23,80,161,389,443,873,1025,1099,2222,2601,2604,3312,3311,4440,5900,5901,5902,7002,9000,9200,10000,50000,50060,50030,8080,139,445,3389,13389,7001,1521,3306,1433,5000,5432,27017,6379,11211]#常用端口扫描列表

    if ThreadsNumber==None:#默认线程数
        ThreadsNumber=10
    if OutputFile==None:#默认输出文件
        OutputFile="port.txt"
    #对目标进行处理
    if IpTarget==None and ReadFile==None:
        print("\033[31m[ ! ] Scanning IP information is not entered!\033[0m")
        sys.exit(0)
    elif IpTarget!=None and ReadFile!=None:
        print("\033[31m[ ! ] Only one type of IP method can be entered!\033[0m")
        sys.exit(0)
    elif IpTarget==None and ReadFile!=None:
        with open(ReadFile, 'r') as f:
            for line in f.readlines():
                if line.strip() not in IpLists:#剔除重复IP
                    IpLists.append(line.strip())  # 把末尾的'\n'删掉
            print("\033[32m[ + ] Number of scanned ip:" + str(len(IpLists)) + "\033[0m")  # IP个数有多少
    elif IpTarget!=None and ReadFile==None:
        from IPy import IP#需要导入包，如果是红蓝对抗在不动别人机器的情况下推荐不适用该方式
        ip = IP(IpTarget)  # 后面批量生成C段扫描会用到
        print("\033[32m[ + ] Number of scanned ip:" + str(ip.len()) + "\033[0m")  # IP个数有多少
        for x in ip:
            IpLists.append(x)

    if PortListInformation==None and PortRangeInformation==None:#默认默认扫描端口信息
        PortLists=DefaultList
        print("\033[32m[ + ] Scanning the default port" + str(PortLists) + "\033[0m")
    elif PortListInformation!=None and PortRangeInformation!=None:#都不等于空的情况
        print("\033[31m[ ! ] Only one format port can be entered, please use -h to view the help file!\033[0m")
        sys.exit(0)
    elif PortListInformation == None and PortRangeInformation != None:#输入范围型端口
        PortType=1
        PortHandling(PortRangeInformation, PortType)  # 放入列表中进行处理
        print("\033[32m[ + ] Scanning the default port" + str(PortLists) + "\033[0m")
    elif PortListInformation != None and PortRangeInformation == None:#输入字典型端口
        PortType=2
        PortHandling(PortListInformation,PortType)#放入列表中进行处理
        print("\033[32m[ + ] Scanning the default port" + str(PortLists) + "\033[0m")


    Main()
    with open(OutputFile, 'w+') as f:#想文件中写入端口信息
        for OpenPort in OpenPorts:
            f.write(OpenPort)
