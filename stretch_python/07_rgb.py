import rclpy, cv2
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.sub = self.create_subscription(Image, '/camera/color/image_raw', self.callback, 10)
        self.bridge = CvBridge()

    def callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        # Do something with your image
        cv2.imshow('image', image)
        cv2.waitKey(3)

rclpy.init()
image_sub = ImageSubscriber()
rclpy.spin(image_sub)
