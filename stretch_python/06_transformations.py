import rclpy, tf2_ros
from rclpy.node import Node
import hello_helpers.hello_misc as hm

class FrameListener(Node):
    def __init__(self):
        super().__init__('stretch_tf_listener')
        self.from_frame_rel = 'base_link'
        self.to_frame_rel = 'link_gripper_fingertip_left'
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)
        self.timer = self.create_timer(0.5, self.on_timer)

    def on_timer(self):
        try:
            # Lookup transform from target to source
            t = self.tf_buffer.lookup_transform(self.to_frame_rel, self.from_frame_rel, rclpy.time.Time())
            print('XYZ:', t.transform.translation)
            print('Quaternion:', t.transform.rotation)
        except tf2_ros.LookupException as e:
            self.get_logger().info(f'Transform not ready: {e}')

# rclpy.init()
node = hm.HelloNode.quick_create('transformations')
fl = FrameListener()
node.move_to_pose({'joint_arm': 0.5}, blocking=False)
rclpy.spin(fl)
