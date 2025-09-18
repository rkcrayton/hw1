import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class Circle(Node):
    def __init__(self):
        super().__init__('circle_node')
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        time.sleep(2)
        self.draw_circle()

    def draw_circle(self, radius=2.0):
        msg = Twist()
        msg.linear.x = 1.0              # forward speed
        msg.angular.z = 1.0 / radius    # angular speed = v/r

        # Publish enough steps to complete ~360°
        duration = int(2 * 3.14159 * radius / 0.1)  # circumference / step
        for _ in range(duration):
            self.pub.publish(msg)
            time.sleep(0.1)

        # stop at the end
        self.pub.publish(Twist())

def main(args=None):
    rclpy.init(args=args)
    Circle()
    rclpy.shutdown()

if __name__ == '__main__':
    main()