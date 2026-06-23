#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String

from . import TCPclient
from . import Globals
import threading

class WifibotControlNode(Node):
    def __init__(self):
        super().__init__('wifibot_control_node')
        
        # 修复这里：改为打印 Globals.SERIAL_PORT，不再调用不存在的 HOST 和 PORT
        self.get_logger().info(f"Connecting to Wifibot via serial port: {Globals.SERIAL_PORT}...")
        self.client_socket = TCPclient.SocketClient()
        # 传入虚拟的参数以适配之前 TCPclient 的 connect 函数定义
        self.connected = self.client_socket.connect(None, None)
        
        if self.connected:
            self.get_logger().info("Successfully connected to Wifibot via Serial!")
            self.tcp_thread = threading.Thread(target=self.run_tcp_server)
            self.tcp_thread.daemon = True
            self.tcp_thread.start()
        else:
            self.get_logger().error("Connection failed! Please check serial connection or port permissions.")
            raise SystemExit

        # 订阅控制话题
        self.subscription = self.create_subscription(
            Twist, 'cmd_vel', self.cmd_vel_callback, 10
        )

        # 发布传感器话题
        self.sensor_pub = self.create_publisher(String, '/wifibot/sensors', 10)
        self.timer = self.create_timer(0.1, self.publish_sensors)

        self.max_speed_val = 240.0 
        self.declare_parameter('max_linear_speed', 1.0)   
        self.declare_parameter('max_angular_speed', 1.0)  

    def run_tcp_server(self):
        try:
            self.client_socket.run_server()
        except Exception as e:
            self.get_logger().error(f"Serial server thread exit: {e}")

    def publish_sensors(self):
        raw_data = TCPclient.GetData.SensorData
        if raw_data and raw_data != "No data yet":
            msg = String()
            msg.data = raw_data
            self.sensor_pub.publish(msg)

    def cmd_vel_callback(self, msg: Twist):
        linear = msg.linear.x
        angular = msg.angular.z

        max_l = self.get_parameter('max_linear_speed').get_parameter_value().double_value
        max_a = self.get_parameter('max_angular_speed').get_parameter_value().double_value

        ratio_linear = max(-1.0, min(1.0, linear / max_l))
        ratio_angular = max(-1.0, min(1.0, angular / max_a))

        left_raw = self.max_speed_val * (ratio_linear - ratio_angular)
        right_raw = self.max_speed_val * (ratio_linear + ratio_angular)

        left_speed = int(max(-self.max_speed_val, min(self.max_speed_val, left_raw)))
        right_speed = int(max(-self.max_speed_val, min(self.max_speed_val, right_raw)))

        if left_speed >= 0 and right_speed >= 0:
            speed_flag = 80  
        elif left_speed >= 0 and right_speed < 0:
            speed_flag = 64  
        elif left_speed < 0 and right_speed >= 0:
            speed_flag = 16  
        else:
            speed_flag = 0   

        TCPclient.SendToDSPIC(abs(left_speed), abs(right_speed), speed_flag)

    def stop_robot(self):
        if self.connected:
            TCPclient.SendToDSPIC(0, 0, 0)
            self.get_logger().info("Wifibot stopped safely.")

def main(args=None):
    rclpy.init(args=args)
    try:
        node = WifibotControlNode()
        rclpy.spin(node)
    except SystemExit:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        if 'node' in locals():
            node.stop_robot()
            node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
