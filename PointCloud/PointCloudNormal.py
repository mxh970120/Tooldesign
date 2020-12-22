'''
Author: mxh970120
Date: 2020.12.22
'''

import numpy as np
import open3d as o3d

pcd = o3d.io.read_point_cloud("filename")



# 计算法向量
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(
    radius=0.1, max_nn=30))
o3d.visualization.draw_geometries([pcd])

o3d.io.write_point_cloud("filename", pcd)

