# -*- coding: utf-8 -*-            
# @Author : Jiazimo
# @Time : 2024/1/19 22:31
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
speed_level = 0#初始速度
def callback(data):
    #速度信息
    global speed_level
    twist = Twist()
    # 检测按键输入，改变速度档次
    if data.axes[7] == 1:  # 7上用于加速
        speed_level += 1
    elif data.axes[7] == -1:  # 7下用于减速
        speed_level -= 1
    print('当前速度档位为:'+str(speed_level))
    # 限制速度档次在0-3之间
    speed_level = max(0, min(3, speed_level))
    #设置速度窗口
    twist = Twist()
    twist.linear.x = data.axes[1] * 0.2* speed_level  # 前进和后退
    twist.angular.z = data.axes[2] * 0.5 * speed_level  # 左右转向
    pub.publish(twist)

#主函数
def start():
    global pub
    rospy.init_node('joy_control')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rospy.Subscriber("joy", Joy, callback)
    rospy.spin()

if __name__ == '__main__':
    start()