# wt901.py

import struct
from bleak import BleakClient



class WT901BLE:

    NOTIFY_UUID = "0000ffe4-0000-1000-8000-00805f9a34fb"

    def __init__(self, address):

        self.address = address

        self.client = None
        self.gui = None
        
        #Origin
        self.roll_offset = 0.0
        self.pitch_offset = 0.0
        self.yaw_offset = 0.0

        self.roll_abs = 0.0
        self.pitch_abs = 0.0
        self.yaw_abs = 0.0

        self.streaming = True

        # Acceleration [g]
        
        self.ax = 0.0
        self.ay = 0.0
        self.az = 0.0

        
        # Angular velocity [deg/s]
        
        self.gx = 0.0
        self.gy = 0.0
        self.gz = 0.0

        
        # Orientation [deg]
        
        self.roll = 0.0
        self.pitch = 0.0
        self.yaw = 0.0

    async def connect(self):

        self.client = BleakClient(self.address)

        await self.client.connect()

        print(f"Connected to {self.address}")

    async def disconnect(self):

        if self.client is not None:
            await self.client.disconnect()

    def parse_packet(self, data):

        
        # Expected format:
        # 55 61
        # ax ay az
        # gx gy gz
        # roll pitch yaw
        

        if len(data) != 20:
            return

        if data[0] != 0x55:
            return

        if data[1] != 0x61:
            return

        (
            ax_raw,
            ay_raw,
            az_raw,
            gx_raw,
            gy_raw,
            gz_raw,
            roll_raw,
            pitch_raw,
            yaw_raw
        ) = struct.unpack("<9h", data[2:20])

        
        # Acceleration
        # Datasheet: raw/32768*16g
        

        self.ax = ax_raw / 32768.0 * 16.0
        self.ay = ay_raw / 32768.0 * 16.0
        self.az = az_raw / 32768.0 * 16.0

        
        # Angular velocity
        # Datasheet: raw/32768*2000 deg/s
        

        self.gx = gx_raw / 32768.0 * 2000.0
        self.gy = gy_raw / 32768.0 * 2000.0
        self.gz = gz_raw / 32768.0 * 2000.0

        
        # Absolute angles from sensor
        

        self.roll_abs = roll_raw / 32768.0 * 180.0
        self.pitch_abs = pitch_raw / 32768.0 * 180.0
        self.yaw_abs = yaw_raw / 32768.0 * 180.0

        
        # Relative angles (after zeroing)
        

        self.roll = self.roll_abs - self.roll_offset
        self.pitch = self.pitch_abs - self.pitch_offset
        self.yaw = self.yaw_abs - self.yaw_offset
        
    def notification_handler(self, sender, data):

        if not self.streaming:
            return

        self.parse_packet(data)

        if self.gui is not None:

            self.gui.update_values(
                self.ax,
                self.ay,
                self.az,
                self.gx,
                self.gy,
                self.gz,
                self.roll,
                self.pitch,
                self.yaw
            )

        self.print_state()

    def print_state(self):

        print(
            f"ACC[g] "
            f"({self.ax:6.2f}, "
            f"{self.ay:6.2f}, "
            f"{self.az:6.2f}) | "

            f"GYRO[deg/s] "
            f"({self.gx:7.1f}, "
            f"{self.gy:7.1f}, "
            f"{self.gz:7.1f}) | "

            f"RPY[deg] "
            f"({self.roll:7.2f}, "
            f"{self.pitch:7.2f}, "
            f"{self.yaw:7.2f})"
        )


    async def start_stream(self):

        await self.client.start_notify(
            self.NOTIFY_UUID,
            self.notification_handler
        )
    def set_gui(self, gui):

        self.gui = gui

    def zero_orientation(self):

        self.roll_offset = self.roll_abs
        self.pitch_offset = self.pitch_abs
        self.yaw_offset = self.yaw_abs

    def get_display_angles(self):

        return (
            self.roll - self.roll_offset,
            self.pitch - self.pitch_offset,
            self.yaw - self.yaw_offset
        )
    def reset_orientation(self):

        self.roll_offset = 0.0
        self.pitch_offset = 0.0
        self.yaw_offset = 0.0

        print("Orientation reset")


    def pause_stream(self):

        self.streaming = False

        print("Stream paused")


    def resume_stream(self):

        self.streaming = True

        print("Stream resumed")