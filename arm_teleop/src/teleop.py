# # #!/usr/bin/env python3

# # import rospy
# # from sensor_msgs.msg import JointState
# # from std_msgs.msg import Header
# # import sys, select, termios, tty

# # # Define the keys and their corresponding joint indices
# # joint_names = ['joint_0', 'joint_1', 'joint_2', 'joint_3', 'joint_4']
# # key_mapping = {
# #     'a': 0, 'z': 0,  # Increase/decrease joint1
# #     's': 1, 'x': 1,  # Increase/decrease joint2
# #     'd': 2, 'c': 2,  # Increase/decrease joint3
# #     'f': 3, 'v': 3,  # Increase/decrease joint4
# #     'g': 4, 'b': 4,  # Increase/decrease joint5
# # }

# # # Initial joint angles
# # joint_angles = [0.0] * len(joint_names)
# # joint_step = 0.1  # Step size for changing joint angles

# # def get_key():
# #     tty.setraw(sys.stdin.fileno())
# #     select.select([sys.stdin], [], [], 0)
# #     key = sys.stdin.read(1)
# #     termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
# #     return key

# # def main():
# #     global joint_angles
# #     rospy.init_node('teleop_arm')
# #     pub = rospy.Publisher('/robot_arm_controller/command', JointState, queue_size=10)
# #     rate = rospy.Rate(10)  # 10 Hz

# #     while not rospy.is_shutdown():
# #         key = get_key()

# #         if key in key_mapping:
# #             joint_index = key_mapping[key]
# #             if key in 'asdfgh':  # Increase joint angle
# #                 joint_angles[joint_index] += joint_step
# #             elif key in 'zxcvbn':  # Decrease joint angle
# #                 joint_angles[joint_index] -= joint_step

# #             # Clamp the angles within a range if needed
# #             joint_angles[joint_index] = max(-3.14, min(3.14, joint_angles[joint_index]))

# #         elif key == '\x03':  # Ctrl+C
# #             break

# #         # Publish the joint states
# #         joint_state = JointState()
# #         joint_state.header = Header()
# #         joint_state.header.stamp = rospy.Time.now()
# #         joint_state.name = joint_names
# #         joint_state.position = joint_angles

# #         pub.publish(joint_state)
# #         rate.sleep()

# # if __name__ == '__main__':
# #     settings = termios.tcgetattr(sys.stdin)
# #     try:
# #         main()
# #     except rospy.ROSInterruptException:
# #         pass
# #     finally:
# #         termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)


# #!/usr/bin/env python3

# import rospy
# from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
# import sys, select, termios, tty

# # Define the keys and their corresponding joint indices
# joint_names = ['joint_0', 'joint_1', 'joint_2', 'joint_3', 'joint_4']
# key_mapping = {
#     'a': 0, 'z': 0,  # Increase/decrease joint1
#     's': 1, 'x': 1,  # Increase/decrease joint2
#     'd': 2, 'c': 2,  # Increase/decrease joint3
#     'f': 3, 'v': 3,  # Increase/decrease joint4
#     'g': 4, 'b': 4,  # Increase/decrease joint5
# }

# # Initial joint angles
# joint_angles = [0.0] * len(joint_names)
# joint_step = 0.1  # Step size for changing joint angles

# def get_key():
#     tty.setraw(sys.stdin.fileno())
#     select.select([sys.stdin], [], [], 0)
#     key = sys.stdin.read(1)
#     termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
#     return key

# def main():
#     global joint_angles
#     rospy.init_node('teleop_arm')
#     pub = rospy.Publisher('/robot_arm_controller/command', JointTrajectory, queue_size=10)
#     rate = rospy.Rate(10)  # 10 Hz

#     rospy.loginfo("Teleoperation node started. Use keys to control the arm.")

#     while not rospy.is_shutdown():
#         key = get_key()

#         if key in key_mapping:
#             joint_index = key_mapping[key]
#             if key in 'asdfgh':  # Increase joint angle
#                 joint_angles[joint_index] += joint_step
#             elif key in 'zxcvbn':  # Decrease joint angle
#                 joint_angles[joint_index] -= joint_step

#             # Clamp the angles within a range if needed
#             joint_angles[joint_index] = max(-3.14, min(3.14, joint_angles[joint_index]))

#         elif key == '\x03':  # Ctrl+C
#             break

#         # Create the JointTrajectory message
#         trajectory_msg = JointTrajectory()
#         trajectory_msg.joint_names = joint_names
        
#         # Create a single point in the trajectory
#         point = JointTrajectoryPoint()
#         point.positions = joint_angles
#         point.time_from_start = rospy.Duration(0.1)  # Small duration to indicate immediate movement
        
#         trajectory_msg.points = [point]

#         # Publish the trajectory message
#         pub.publish(trajectory_msg)
#         rate.sleep()

# if __name__ == '__main__':
#     settings = termios.tcgetattr(sys.stdin)
#     try:
#         main()
#     except rospy.ROSInterruptException:
#         pass
#     finally:
#         termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

#!/usr/bin/env python3

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import sys, select, termios, tty

# Define the keys and their corresponding joint indices
joint_names = ['joint_0', 'joint_1', 'joint_2', 'joint_3', 'joint_4']
key_mapping = {
    'a': 0, 'z': 0,  # Increase/decrease joint1
    's': 1, 'x': 1,  # Increase/decrease joint2
    'd': 2, 'c': 2,  # Increase/decrease joint3
    'f': 3, 'v': 3,  # Increase/decrease joint4
    'g': 4, 'b': 4,  # Increase/decrease joint5
}

# Initial joint angles
joint_angles = [0.0] * len(joint_names)
joint_step = 0.1  # Step size for changing joint angles

def get_key():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def main():
    global joint_angles
    rospy.init_node('teleop_arm')
    pub = rospy.Publisher('/robot_arm_controller/command', JointTrajectory, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    rospy.loginfo("Teleoperation node started. Use keys to control the arm.")

    while not rospy.is_shutdown():
        key = get_key()
        command_executed = False

        if key in key_mapping:
            joint_index = key_mapping[key]
            if key in 'asdfgh':  # Increase joint angle
                joint_angles[joint_index] += joint_step
            elif key in 'zxcvbn':  # Decrease joint angle
                joint_angles[joint_index] -= joint_step

            # Clamp the angles within a range if needed
            joint_angles[joint_index] = max(-3.14, min(3.14, joint_angles[joint_index]))

            command_executed = True
            rospy.loginfo(f"Key '{key}' pressed. Adjusting joint {joint_index} to {joint_angles[joint_index]} radians.")

        elif key == '\x03':  # Ctrl+C
            rospy.loginfo("Shutting down teleoperation node.")
            break

        # Create the JointTrajectory message
        trajectory_msg = JointTrajectory()
        trajectory_msg.joint_names = joint_names
        
        # Create a single point in the trajectory
        point = JointTrajectoryPoint()
        point.positions = joint_angles
        point.time_from_start = rospy.Duration(0.1)  # Small duration to indicate immediate movement
        
        trajectory_msg.points = [point]

        # Publish the trajectory message
        pub.publish(trajectory_msg)
        
        if command_executed:
            rospy.loginfo(f"Published joint angles: {joint_angles}")

        rate.sleep()

if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    try:
        main()
    except rospy.ROSInterruptException:
        pass
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)