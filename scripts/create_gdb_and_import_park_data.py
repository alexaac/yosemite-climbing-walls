# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# create_gdb_and_import_park_data.py
# Created on: 2020-01-19 18:55:29.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: create_gdb_and_import_park_data <v_park_gdb_name> <park_data_gdb> <Data_Folder> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
v_park_gdb_name = arcpy.GetParameterAsText(0)
if v_park_gdb_name == '#' or not v_park_gdb_name:
    v_park_gdb_name = "park_data" # provide a default value if unspecified

park_data_gdb = arcpy.GetParameterAsText(1)
if park_data_gdb == '#' or not park_data_gdb:
    park_data_gdb = "C:\\GIS\\park_data.gdb" # provide a default value if unspecified

Data_Folder = arcpy.GetParameterAsText(2)

# Local variables:
Rivers = ""
Springs = ""
Waterbodies = ""
Rock_Fall_Hazard_line_shp = ""
Trails = ""
Wilderness_stock_routes = ""
Winter_trails = ""
Trailheads = ""
YOSE_CADBaseMap_20190905 = ""
Yosemite_Climbing_Areas_shp = ""
YOSE_Parking_20190521 = ""
Yosemite_Roads = ""
yoseglg = ""
park_data_gdb__2_ = park_data_gdb

# Set Geoprocessing environments
arcpy.env.scratchWorkspace = "C:\\GIS\\scratch.gdb"
arcpy.env.workspace = "C:\\GIS\\scratch.gdb"

# Process: Create File GDB
arcpy.CreateFileGDB_management(Data_Folder, v_park_gdb_name, "CURRENT")

# Process: Feature Class to Geodatabase (multiple) 
arcpy.FeatureClassToGeodatabase_conversion("'';'';'';'';'';'';'';'';'';'';'';'';''", park_data_gdb)

