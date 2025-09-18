import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time, math

class Diamond(Node):
    def __init__(self):
        super().__init__('diamond_node')
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        time.sleep(2)
        self.draw_diamond()

    def move(self, speed, duration=1.0):
        msg = Twist()
        msg.linear.x = speed
        self.pub.publish(msg)
        time.sleep(duration)
        self.stop()

    def rotate(self,speed,angledegrees):
        msg = Twist()
        msg.angular.z = speed
        angle_rad = math.radians(angledegrees)
        duration = angle_rad/speed
        start = time.time()
        while time.time()-start < duration:
            self.pub.publish(msg)
            time.sleep(.1)
        self.stop()

    def stop(self):
        self.pub.publish(Twist())
        time.sleep(1)

    def draw_diamond(self):
        # Diamond = two pairs of 60° and 120° turns
        for _ in range(2):
            self.rotate(1.0,60.0)
            self.move(2.0)
            self.rotate(1.0,120.0)      # 60 degrees
            self.move(2.0)

def main(args=None):
    rclpy.init(args=args)
    Diamond()
    rclpy.shutdown()

if __name__ == '__main__':
    main()