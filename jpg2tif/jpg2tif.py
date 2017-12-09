#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import arcpy,envipy
envipy.Initialize(arcpy) 
from arcpy import env
env.workspace="D:/data/www/ocr/img"
rasters = arcpy.ListRasters("*", "JPG")
for raster in rasters:
    inraster = raster
    outraster= "D:/data/www/ocr/img/tif/"+raster.strip(".jpg")+".tif"
    arcpy.ConvertRaster_envi(inraster, outraster, "TIFF",  "")
print("All have done")