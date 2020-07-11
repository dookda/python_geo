import arcpy
from arcpy import env
from arcpy.sa import *

## 1 set workspace ##
# env.workspace = r"C:\labarcpy"
# lyr = "cm_rain_32647.shp"

## 2 list field ##
# ListFields (dataset, {wild_card}, {field_type})
# fields = arcpy.ListFields(lyr)

# for field in fields:
# print("{0} is a type of {1} with a length of {2}"
#       .format(field.name, field.type, field.length))
# if field.type == "Double" and field.name != "GRD_LEVEL":
#     print(field.name)

# 3 interpolation
# Idw (in_point_features, z_field, {cell_size}, {power}, {search_radius}, {in_barrier_polyline_features})

# outIDW = Idw(lyr, field.name, 2000, 2)
# outIDW.save("idw_"+field.name)
