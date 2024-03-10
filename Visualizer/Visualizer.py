import copy
import open3d as o3d
import numpy as np
from typing import Iterable, Tuple


class Visualizer:
    # TODO create this class
    def __init__(self, data):
        self.data = data

    def visualize(self):
        # Visualize the data
        pass


def visualize_point_clouds(
    clouds_points: Iterable[np.ndarray],
    colors_rgb: Iterable[Tuple[float, float, float]],
) -> None:
    """
    TODO: Generate docstring with copilot
    """

    clouds = []
    for color_rgb, cloud_points in zip(colors_rgb, clouds_points):
        cloud = o3d.geometry.PointCloud()
        cloud.points = o3d.utility.Vector3dVector(cloud_points)
        cloud.paint_uniform_color(color=color_rgb)
        clouds.append(cloud)

    o3d.visualization.draw_geometries(clouds)


def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([0.0, 0.0, 1.0])
    target_temp.paint_uniform_color([1.0, 0.0, 0.0])

    source_temp.transform(transformation)

    o3d.visualization.draw_geometries([source_temp, target_temp])