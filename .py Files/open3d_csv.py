# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 00:19:53 2022

@author: Alvis
"""

import numpy as np
import open3d  as o3d  

pcd = o3d.io.read_point_cloud("image3.ply")
print(pcd)
print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd])

#np.savetxt("image3.csv", np.asarray(pcd.points), delimiter =",")




