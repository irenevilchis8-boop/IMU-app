import tkinter as tk


class IMUGui:

    def __init__(self, imu):

        self.imu = imu
        self.root = tk.Tk()

        self.root.title("WT901BLE Monitor")
        self.root.geometry("400x350")

        self.values = {}

        row = 0

        # ACC
        tk.Label(
            self.root,
            text="ACCELERATION [g]",
            font=("Arial", 12, "bold")
        ).grid(row=row, column=0, sticky="w")

        row += 1

        for name in ["ax", "ay", "az"]:

            tk.Label(
                self.root,
                text=name,
                width=10
            ).grid(row=row, column=0)

            self.values[name] = tk.Label(
                self.root,
                text="0.000",
                width=12
            )

            self.values[name].grid(row=row, column=1)

            row += 1

        # GYRO
        tk.Label(
            self.root,
            text="GYROSCOPE [deg/s]",
            font=("Arial", 12, "bold")
        ).grid(row=row, column=0, sticky="w")

        row += 1

        for name in ["gx", "gy", "gz"]:

            tk.Label(
                self.root,
                text=name,
                width=10
            ).grid(row=row, column=0)

            self.values[name] = tk.Label(
                self.root,
                text="0.000",
                width=12
            )

            self.values[name].grid(row=row, column=1)

            row += 1

        # ORIENTATION
        tk.Label(
            self.root,
            text="ORIENTATION [deg]",
            font=("Arial", 12, "bold")
        ).grid(row=row, column=0, sticky="w")

        row += 1

        for name in ["roll", "pitch", "yaw"]:

            tk.Label(
                self.root,
                text=name,
                width=10
            ).grid(row=row, column=0)

            self.values[name] = tk.Label(
                self.root,
                text="0.000",
                width=12
            )

            self.values[name].grid(row=row, column=1)

            row += 1
        
        # Buttons
        
        button_frame = tk.Frame(self.root)
        button_frame.grid(
            row=row,
            column=0,
            columnspan=2,
            pady=15
        )

        tk.Button(
            button_frame,
            text="Zero",
            width=10,
            command=self.imu.zero_orientation
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Reset",
            width=10,
            command=self.imu.reset_orientation
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Pause",
            width=10,
            command=self.imu.pause_stream
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            button_frame,
            text="Resume",
            width=10,
            command=self.imu.resume_stream
        ).grid(row=0, column=3, padx=5)
        
        tk.Button(
            button_frame,
            text="Exit",
            width=10,
            command=self.root.destroy
        ).grid(row=0, column=4, padx=5)

    def update_values(
        self,
        ax, ay, az,
        gx, gy, gz,
        roll, pitch, yaw
    ):

        self.values["ax"].config(text=f"{ax:.3f}")
        self.values["ay"].config(text=f"{ay:.3f}")
        self.values["az"].config(text=f"{az:.3f}")

        self.values["gx"].config(text=f"{gx:.3f}")
        self.values["gy"].config(text=f"{gy:.3f}")
        self.values["gz"].config(text=f"{gz:.3f}")

        self.values["roll"].config(text=f"{roll:.0f}")
        self.values["pitch"].config(text=f"{pitch:.0f}")
        self.values["yaw"].config(text=f"{yaw:.0f}")

        self.root.update()
