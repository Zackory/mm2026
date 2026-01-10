import rclpy, sys
from rclpy.node import Node
from speech_recognition_msgs.msg import SpeechRecognitionCandidates

class SpeechSub(Node):
    def __init__(self):
        super().__init__('speech_sub')
        self.sub = self.create_subscription(SpeechRecognitionCandidates, 'speech_to_text', self.callback, 10)

    def callback(self, msg):
        transcript = ' '.join(map(str, msg.transcript))
        print(transcript)
        # Do something with the text
        sys.exit(0)

rclpy.init()
speech_sub = SpeechSub()
rclpy.spin(speech_sub)
