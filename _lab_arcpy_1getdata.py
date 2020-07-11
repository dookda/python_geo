import arcpy
from arcpy import env

## 1 set workspace ##
env.workspace = r"C:\labarcpy"

## 2 List data ##
# featureClasses = arcpy.ListFeatureClasses()

# for f in featureClasses:
# print(f)

## 3 check data type ##
# lyr = arcpy.Describe(f)
# print(f, lyr.shapeType)

## 4 if statement ##
# if lyr.shapeType == "Point":
#     print(f)
