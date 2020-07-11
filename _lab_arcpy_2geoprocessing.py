import arcpy
from arcpy import env

## 1 set workspace ##
env.workspace = r"C:\labarcpy"
env.overwriteOutput = True

## 2 buffer ##
# rainsta = r"C:\labarcpy\cm_rain_32647.shp"

# Buffer_analysis (in_features, out_feature_class, buffer_distance_or_field, {line_side}, {line_end_type}, {dissolve_option}, {dissolve_field}, {method})
# staBuff = "stabuffer.shp"
# arcpy.Buffer_analysis("cm_rain_32647.shp", staBuff,
#                       "500 Meters", "FULL", "ROUND", "NONE")

## 3 clip ##
# Clip_analysis (in_features, clip_features, out_feature_class, {cluster_tolerance})
# luClip = "landuseclip.shp"
# arcpy.Clip_analysis("cm_soil_32647.shp", staBuff, luClip)

# print("job success")
