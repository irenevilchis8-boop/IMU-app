import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import Poly3DCollection


class CubeVisualizer:

    def __init__(self):

        self.fig = plt.figure()

        self.ax = self.fig.add_subplot(
            111,
            projection="3d"
        )

        plt.ion()

    def rotation_matrix(
        self,
        roll,
        pitch,
        yaw
    ):

        cr = np.cos(np.radians(roll))
        sr = np.sin(np.radians(roll))

        cp = np.cos(np.radians(pitch))
        sp = np.sin(np.radians(pitch))

        cy = np.cos(np.radians(yaw))
        sy = np.sin(np.radians(yaw))

        Rx = np.array([
            [1, 0, 0],
            [0, cr, -sr],
            [0, sr, cr]
        ])

        Ry = np.array([
            [cp, 0, sp],
            [0, 1, 0],
            [-sp, 0, cp]
        ])

        Rz = np.array([
            [cy, -sy, 0],
            [sy, cy, 0],
            [0, 0, 1]
        ])

        return Rz @ Ry @ Rx

    def update(
        self,
        roll,
        pitch,
        yaw
    ):

        self.ax.clear()

        vertices = np.array([
            [-1, -1, -1],
            [ 1, -1, -1],
            [ 1,  1, -1],
            [-1,  1, -1],
            [-1, -1,  1],
            [ 1, -1,  1],
            [ 1,  1,  1],
            [-1,  1,  1]
        ])

        R = self.rotation_matrix(
            roll,
            pitch,
            yaw
        )

        vertices = vertices @ R.T

        faces = [
            [vertices[j] for j in [0,1,2,3]],
            [vertices[j] for j in [4,5,6,7]],
            [vertices[j] for j in [0,1,5,4]],
            [vertices[j] for j in [2,3,7,6]],
            [vertices[j] for j in [1,2,6,5]],
            [vertices[j] for j in [4,7,3,0]]
        ]

        cube = Poly3DCollection(
            faces,
            alpha=0.4,
            facecolor='cyan',
            edgecolor='black'
        )

        self.ax.add_collection3d(cube)

        self.ax.set_xlim([-2,2])
        self.ax.set_ylim([-2,2])
        self.ax.set_zlim([-2,2])

        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")

        self.ax.set_title(
            f"R={roll:.1f} "
            f"P={pitch:.1f} "
            f"Y={yaw:.1f}"
        )

        plt.draw()
        plt.pause(0.001)
