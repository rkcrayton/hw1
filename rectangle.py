import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time, math

class Rectangle(Node):
    def __init__(self):
        super().__init__('rectangle_node')
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        time.sleep(2)
        self.draw_rectangle()

    def move(self, speed, duration):
        msg = Twist()
        msg.linear.x = speed
        self.pub.publish(msg)
        time.sleep(duration)
        self.stop()

    def rotate(self,angular_speed=1.57, duration = 2.0):
        msg = Twist()
        msg.angular.z = angular_speed 
        self.pub.publish(msg)
        time.sleep(duration)
        self.stop()

    def stop(self):
        self.pub.publish(Twist())
        time.sleep(1)

    def draw_rectangle(self):
        for _ in range(2):
            self.move(3.0, duration = 3.5)
            self.rotate()  # 90 degrees
            self.move(2.0,duration=3.0)
            self.rotate()

def main(args=None):
    rclpy.init(args=args)
    Rectangle()
    rclpy.shutdown()

if __name__ == '__main__':
    main()