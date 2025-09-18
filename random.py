import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time,math


class Triangle(Node):
    def __init__(self):
        super().__init__('triangle_node')
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel',10)
        time.sleep(2)
        self.draw_triangle()

    def move(self,duration=2.0):
        msg = Twist()
        msg.linear.x = 1.0
        self.pub.publish(msg)
        time.sleep(duration)

        self.stop()

    def rotate(self,angle,speed=1.0):
        msg = Twist()
        angle_rad = math.radians(angle)
        duration = angle_rad/speed
        msg.angular.z = speed
        start = time.time()
        while time.time()-start <duration:
            self.pub.publish(msg)
            time.sleep(0.1)
        self.stop()


    def stop(self):
        self.pub.publish(Twist())
        time.sleep(1)
    
    def draw_triangle(self,side =3.0):
        for _ in range(3):
            self.move(duration = side)
            self.rotate(120)

def main(args=None):
    rclpy.init(args=args)
    Triangle()
    rclpy.shutdown()

if __name__ == '__main__':
    main()