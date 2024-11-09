# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/1/13 16:59
import rospy #导入ROS的python库
from geometry_msgs.msg import Twist # 导入Twist消息类型用于发布速度命令的标准ROS消息类型
import sys, select, termios, tty

msg = """
Control Your Robot!
---------------------------
Moving around:
   w: forward
   a: turn left
   s: backward
   d: turn right

CTRL-C to quit
"""
#将w,a,s,d进行映射
moveBindings = {
    'w':(1,0),#前进
    'a':(0,1),#左转
    's':(-1,0),#后退/刹车
    'd':(0,-1),#右转
    ' ':(0,0)
    }

def getKey():#获取键盘输入
    tty.setraw(sys.stdin.fileno())#设置终端输入模式
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)#使用select检测键盘输入
    if rlist:
        key = sys.stdin.read(1)#如果有键盘输入则读取一个字符
    else:
        key = ''#若没有则返回空
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)#重新恢复终端输入
    return key

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)#获取终端的当前设置
    rospy.init_node('teleop_twist_keyboard')#初始化一个ROS节点
    pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)#创建一个Publisher用于订阅者接受数据
    #设置初始速度
    speed = 1#初始前进速度
    turn = 1.5#初始转向速度
    x = 0#初始线速度
    th = 0#初始角速度
    try:
        print (msg)
        while(1):#寻获获取输入，直到CTRL-C退出
            key = getKey()#获取输入值
            if key in moveBindings.keys():#若值在字典中
                x = moveBindings[key][0]#若前进则只有线速度，没有角速度（其他同理）
                th = moveBindings[key][1]
            else:#没有则保持原始默认值
                x = 0
                th = 0
                if (key == '\x03'):#若输入为CTRL-C则退出
                    break
            twist = Twist()#创建一个Twist类型的消息
            twist.linear.x = x*speed; twist.linear.y = 0; twist.linear.z = 0#设置线速度
            twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = th*turn#设置角速度
            pub.publish(twist)
    except:#如果出新问题则返回error
        print("error")
    finally:#无论任何情况都执行
        twist = Twist()
        twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
        twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
        pub.publish(twist)

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)#最后恢复终端设置
