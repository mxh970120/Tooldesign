'''
Author: mxh970120
Date: 2020.12.22
'''


import numpy as np
import open3d
import json
from collections import OrderedDict


def CaculateAreaVolume(filename, voxel_size):
    # 点云
    pcd = open3d.io.read_point_cloud(filename)

    # 三角网络（从点云转化）
    # 必须要有法向量的数据！
    # https://stackoverflow.com/questions/56965268/how-do-i-convert-a-3d-point-cloud-ply-into-a-mesh-with-faces-and-vertices
    distances = pcd.compute_nearest_neighbor_distance()
    avg_dist = np.mean(distances)
    radius = 1.5 * avg_dist
    r = open3d.utility.DoubleVector([radius, radius * 2])

    mesh = open3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pcd, r)
    meshArea = mesh.get_surface_area()
    # volume = mesh.get_volume()  # under the condition that it is watertight and orientable.
    # 如果不满足条件，需要用体素化近似这个体积
    voxelMesh = open3d.geometry.VoxelGrid.create_from_triangle_mesh(mesh, voxel_size)
    voxelNum = int(str(voxelMesh).split(" ")[2])
    voxelVolume = voxelNum*voxel_size**3

    return meshArea, voxelVolume

if __name__ == '__main__':
    cloudPoint = dict()
    filename = list()
    filename.append("filename1")
    # filename.append('filename2')
    voxel_size = 1
    for file in filename:
        area, volume = CaculateAreaVolume(file, voxel_size)
        cloudPoint[file] = {"area": area, "volume": volume}
    # print(cloudPoint["filename1"]["area"])

    # 转化成JSON并输出
    # c = json.dumps(cloudPoint, sort_keys=False, indent=4, separators=(', ', ': '))
    # f2 = open('CloudpointAreaVolume.json', 'w')
    # f2.write(c)
    # f2.close()
