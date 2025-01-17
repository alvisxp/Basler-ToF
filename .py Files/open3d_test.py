# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 00:19:53 2022

@author: Alvis
"""

import numpy as np
import open3d  as o3d  

print("Load a ply point cloud, print it, and render it")
pcd = o3d.io.read_point_cloud("image3.ply")
print(pcd)
print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd])

#print("Downsample the point cloud with a voxel of 0.05")
#downpcd = pcd.voxel_down_sample(voxel_size=0.05)
#o3d.visualization.draw_geometries([downpcd])

#print("Recompute the normal of the downsampled point cloud")
#downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(
#radius=0.1, max_nn=30))
#o3d.visualization.draw_geometries([downpcd])

#downpcd = pcd.voxel_down_sample(voxel_size=0.05)

#np.savetxt("image3_full.csv", np.asarray(pcd.points), delimiter =",")

#print(np.asarray(downpcd.normals)[:10, :])



