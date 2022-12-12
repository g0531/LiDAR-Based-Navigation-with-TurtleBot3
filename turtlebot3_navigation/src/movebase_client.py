#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import smach
import smach_ros
import actionlib
import math
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Twist


# def movebase_client():
#     client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
#     client.wait_for_server()

#     goal = MoveBaseGoal()
#     goal.target_pose.header.frame_id = "map"
#     goal.target_pose.header.stamp = rospy.Time.now()
#     point = 5
#     count = 0
#     for i in range(5):
#         if(i == 0):
#             goal.target_pose.pose.position.x = -0.2159
#             goal.target_pose.pose.position.y = 2.6625
#             goal.target_pose.pose.orientation.w = 0.7353
#             client.send_goal(goal)
#             wait = client.wait_for_result()
#             if not wait:
#                 rospy.logerr("Action server not available!")
#                 rospy.signal_shutdown("Action server not available!")
#             else:
#                 rospy.loginfo("Point1 get!")           
#         if(i == 1):
#             goal.target_pose.pose.position.x = -1.0
#             goal.target_pose.pose.position.y = 0.0199
#             goal.target_pose.pose.orientation.w = 0.9124
#             client.send_goal(goal)
#             wait = client.wait_for_result()
#             if not wait:
#                 rospy.logerr("Action server not available!")
#                 rospy.signal_shutdown("Action server not available!")
#             else:
#                 rospy.loginfo("Point2 get!")
#         elif (i == 2):
#             goal.target_pose.pose.position.x = 3.0
#             goal.target_pose.pose.position.y = 0.36
#             goal.target_pose.pose.orientation.w = -1.0
#             client.send_goal(goal)
#             wait = client.wait_for_result()
#             if not wait:
#                 rospy.logerr("Action server not available!")
#                 rospy.signal_shutdown("Action server not available!")
#             else:
#                 rospy.loginfo("Point3 get!")
#         elif (i == 3):
#             goal.target_pose.pose.position.x = 2.85
#             goal.target_pose.pose.position.y = 4.26
#             goal.target_pose.pose.orientation.w = 0.6
#             client.send_goal(goal)
#             wait = client.wait_for_result()
#             if not wait:
#                 rospy.logerr("Action server not available!")
#                 rospy.signal_shutdown("Action server not available!")
#             else:
#                 rospy.loginfo("Point4 get!")
#         elif (i == 4):
#             goal.target_pose.pose.position.x = -0.7778
#             goal.target_pose.pose.position.y = 3.547
#             goal.target_pose.pose.orientation.w = 0.7353
#             client.send_goal(goal)
#             wait = client.wait_for_result()
#             if not wait:
#                 rospy.logerr("Action server not available!")
#                 rospy.signal_shutdown("Action server not available!")
#             else:
#                 rospy.loginfo("Point5 get!")
#     return client.get_result()

def movebase_client():
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    point = 5
    count = 0
    for i in range(1):
        if (i == 0):
            goal.target_pose.pose.position.x = -0.82
            goal.target_pose.pose.position.y = 3.7
            goal.target_pose.pose.orientation.z = -0.707
            goal.target_pose.pose.orientation.w = 0.707
            client.send_goal(goal)
            wait = client.wait_for_result()
            if not wait:
                rospy.logerr("Action server not available!")
                rospy.signal_shutdown("Action server not available!")
            else:
                rospy.loginfo("Point5 get!")
    return client.get_result()




class Foo(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1','outcome2'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('Executing state FOO')
        try:
                result = movebase_client()
                if result:
                    return 'outcome1'
        except rospy.ROSInterruptException:
            return 'outcome2'


class Bar(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome3'])

    def execute(self, userdata):
        rospy.loginfo('Executing state BAR')
        try:
            aruco_sub()
        except rospy.ROSInterruptException:
            pass
            rospy.loginfo('Aruco:wrong!')
        return 'outcome3'


def aruco_sub():
    rospy.Subscriber("/aruco_single/pose", PoseStamped,callback)
    rospy.spin()


        
def callback(data):
    if(data != None):
        x = data.pose.position.x
        y = data.pose.position.y
        z = data.pose.position.z
        distance = math.sqrt(pow(x,2)+pow(y,2))
        rospy.loginfo("distance"+str(distance))
    else:
        distance = 100
    pub = rospy.Publisher('/cmd_vel', Twist,queue_size=10)
    msg = Twist()
    if not rospy.is_shutdown():
        if(distance<0.03):
            msg.linear.x=0
            msg.angular.z=0
            pub.publish(msg)
            rospy.loginfo("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"+str(distance))
        else:
            msg.linear.x=0.1
            msg.angular.z=0
            pub.publish(msg)
            rospy.loginfo("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"+str(distance))

def main():
    rospy.init_node('movebase_client_py')

    # 创建一个状态机
    sm = smach.StateMachine(outcomes=['outcome4'])

    # 打开状态机容器
    with sm:
        # 使用add方法添加状态到状态机容器当中
        smach.StateMachine.add('FOO', Foo(), 
                               transitions={'outcome1':'BAR', 
                                            'outcome2':'FOO'})
        smach.StateMachine.add('BAR', Bar(), 
                               transitions={'outcome3':'outcome4'})
    
    # 创建并启动内部监测服务器
    sis = smach_ros.IntrospectionServer('my_smach_introspection_server', sm, '/SM_ROOT')
    sis.start()
    
    # 开始执行状态机
    outcome = sm.execute()
    
    # 等待退出
    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()





