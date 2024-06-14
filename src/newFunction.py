import argparse
import sys
import serial
import ps2000b
import platform


class NewPower:
    _instance = None

    def __new__(cls, com: int, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(NewPower, cls).__new__(cls)
            cls._instance.initialize(com)
        return cls._instance

    def initialize(self, com: int):
        self.com = com
        com_connect = "COM{}".format(self.com) if platform.system() == "Windows" else "/dev/ttyACM0"
        print("连接到设备 %s..." % com_connect)
        try:
            self.device = ps2000b.PS2000B(com_connect)
            print("连接状态: %s" % self.device.is_open())
            print("设备信息: %s" % self.device.get_device_information())
        except Exception:
            print('没找到端口')

            # 其余方法保持不变...

    def open_power(self):  # 打开控制
        self.device.enable_remote_control()
        self.device.enable_output()

    def close_power(self):
        self.device.disable_output()

    def control_power(self, voltage, current):
        self.device.voltage = voltage
        self.device.current = current

    def get_voltage(self):
        return self.device.get_voltage()

    def get_current(self):
        return self.device.get_current()


# ...

if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    # 添加命令行参数...
    parse.add_argument("--com", type=int, help="com")
    parse.add_argument("--a", type=float, help="current")
    parse.add_argument("--v", type=float, help="voltage")
    parse.add_argument("--open", action="store_true")
    parse.add_argument("--close", action="store_true")
    parse.add_argument("--gc", action="store_true")
    parse.add_argument("--gv", action="store_true")
    parse.add_argument("--pc", action="store_true")
    args = parse.parse_args()

    # 使用指定的COM端口（或默认端口）创建或获取NewPower实例
    # p = NewPower(args.com if hasattr(args, 'com') else 0)

    import serial.tools.list_ports

    ports = []
    name = []
    for port in serial.tools.list_ports.comports():
        ports.append(port.device)
        name.append(port.description)
    print(ports)
    print(name)

    # 根据命令行参数执行相应的操作...
    # ...
