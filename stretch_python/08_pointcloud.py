import rclpy, tf2_ros, tf2_sensor_msgs
import numpy as np
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
import sensor_msgs_py.point_cloud2 as pc2

class PCSubscriber(Node):
    def __init__(self):
        super().__init__('pointcloud_subscriber')
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)
        self.sub = self.create_subscription(PointCloud2, '/camera/depth/color/points', self.callback, 10)

    def callback(self, msg):
        try:
            transform = self.tf_buffer.lookup_transform('base_link', 'camera_color_optical_frame', rclpy.time.Time())
            pc_transformed = tf2_sensor_msgs.do_transform_cloud(msg, transform)
            pc_numpy = pc2.read_points_numpy(pc_transformed, field_names=('x', 'y', 'z'), skip_nans=True)
            print('First 3 points:', pc_numpy[:3])
        except tf2_ros.LookupException as e:
            self.get_logger().info(f'Transform not ready: {e}')

rclpy.init()
node = PCSubscriber()
rclpy.spin(node)
