import serial
import struct
from . import Globals

state = True

class SensorDataData:
    def __init__(self):
        self.SensorData = "No data yet"

GetData = SensorDataData()
_global_serial = None

def _wifibot_official_crc16(Tableau, Taille_max):
    """
    完全复刻 Wifibot 官方自带的 Crc16 算法源码
    跳过 Tableau[0], 严格从 Tableau[1] 开始计算
    """
    Crc = 0xFFFF
    Polynome = 0xA001
    Parity = 0
    
    for CptOctet in range(0, Taille_max):
        Crc ^= (Tableau[1 + CptOctet])
        for CptBit in range(0, 8):
            Parity = Crc
            Crc >>= 1
            if (Parity % 2 == True):
                Crc ^= Polynome
                
    return Crc

class SocketClient:
    def __init__(self):
        self.ser = None

    def connect(self, host, port):
        global _global_serial
        try:
            self.ser = serial.Serial(
                port=Globals.SERIAL_PORT,
                baudrate=Globals.BAUDRATE,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=0.250
            )
            if self.ser.is_open:
                _global_serial = self.ser
                return True
            return False
        except Exception as e:
            print(f"[Serial Error] Cannot open port {Globals.SERIAL_PORT}: {e}")
            return False

    def run_server(self):
        global state
        while state:
            try:
                if self.ser and self.ser.is_open:
                    if self.ser.in_waiting > 0:
                        data = self.ser.read(self.ser.in_waiting)
                        if data:
                            GetData.SensorData = str(list(data))
            except Exception:
                state = False
                break

def SendToDSPIC(LeftSpeed, RightSpeed, SpeedFlag):
    global _global_serial
    if _global_serial is None or not _global_serial.is_open:
        return
    try:
        sbuffer = []
        sbuffer.append(255)
        sbuffer.append(7)
        
        # 左轮速度拆分 LSB 和 MSB (小端)
        sbuffer.append(int(LeftSpeed) & 0xff)
        sbuffer.append((int(LeftSpeed) >> 8) & 0xff)
        
        # 右轮速度拆分 LSB 和 MSB (小端)
        sbuffer.append(int(RightSpeed) & 0xff)
        sbuffer.append((int(RightSpeed) >> 8) & 0xff)
        
        # SpeedFlag 必须加 1
        sbuffer.append((int(SpeedFlag) + 1) & 0xff)
        
        # ⚠️ 关键点：官方参考代码中传入的大小是 6 (对应计算前 7 个字节中的后 6 个)
        crcsend = _wifibot_official_crc16(sbuffer, 6)
        
        # 拼接 CRC 的 LSB 和 MSB
        sbuffer.append(crcsend & 0xff)
        sbuffer.append((crcsend >> 8) & 0xff)
        
        # 发送二进制数据流
        data = bytearray(sbuffer)
        _global_serial.write(data)
        _global_serial.flush()
    except Exception as e:
        print(f"[Serial Error] Failed to send wifibot protocol packets: {e}")
