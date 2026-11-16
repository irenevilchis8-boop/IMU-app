# WT901BLE IMU Monitor

Python application for connecting to a WT901BLE-series IMU over Bluetooth Low Energy (BLE), decoding sensor measurements, and displaying them in real time.

## Features

- BLE connection to WT901BLE sensors
- Real-time acceleration monitoring
- Real-time angular velocity monitoring
- Real-time orientation monitoring
- Orientation zeroing (relative pose)
- Stream pause and resume
- Tkinter graphical interface
- Ready for ROS2 integration

---

## Tested Hardware

Tested with:

- WT901BLE68

---

## Protocol

The sensor transmits packets in the following format:

```
55 61
Acceleration X
Acceleration Y
Acceleration Z
Angular Velocity X
Angular Velocity Y
Angular Velocity Z
Roll
Pitch
Yaw
```

Values are transmitted as signed 16-bit integers.

Byte order:

```
Low Byte
High Byte
```

(little endian)

---

## Measurement Conversion

### Acceleration

Raw values are converted to g:

```python
acc = raw / 32768.0 * 16.0
```

Outputs:

```text
ax
ay
az
```

Units:

```text
g
```

---

### Angular Velocity

Raw values are converted to:

```python
gyro = raw / 32768.0 * 2000.0
```

Outputs:

```text
gx
gy
gz
```

Units:

```text
deg/s
```

---

### Orientation

Raw values are converted to:

```python
angle = raw / 32768.0 * 180.0
```

Outputs:

```text
roll
pitch
yaw
```

Units:

```text
degrees
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/imu-monitor.git

cd imu-monitor
```

Create virtual environment:

```bash
python3 -m venv .venv

source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Finding Sensor Address

Open Bluetooth manager:

```bash
bluetoothctl
```

Start scanning:

```bash
scan on
```

Wait until the sensor appears:

```text
WT901BLE68
```

Example:

```text
FF:3F:7B:9C:51:25 WT901BLE68
```

Stop scan:

```bash
scan off
```

Exit:

```bash
exit
```

---

## Configuration

Open:

```python
wt901_read.py
```

Modify:

```python
ADDRESS = "FF:3F:7B:9C:51:25"
```

to the address of your sensor.

---

## Running

Launch the application:

```bash
python3 wt901_read.py
```

---

## GUI Controls

### Zero

Uses the current orientation as the reference frame.

Example:

Before:

```text
Roll  = 15°
Pitch = 5°
Yaw   = 20°
```

Press Zero:

```text
Roll  = 0°
Pitch = 0°
Yaw   = 0°
```

---

### Reset

Returns to the sensor's absolute orientation.

---

### Pause

Stops updating displayed values.

---

### Resume

Resumes data updates.

---

## Project Structure

```text
imu-monitor/
│
├── README.md
├── requirements.txt
├── wt901.py
├── imu_gui.py
├── wt901_read.py
└── .gitignore
```

### wt901.py

BLE communication and packet decoding.

### imu_gui.py

Graphical user interface.

### wt901_read.py

Application entry point.

---

## Future Work

- ROS2 Humble integration
- Quaternion output
- CSV logging
- Calibration wizard
- 3D orientation visualization
- Data recording and playback

---

## License

MIT License
