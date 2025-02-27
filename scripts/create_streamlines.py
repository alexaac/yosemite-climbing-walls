# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# create_streamlines.py
# Created on: 2020-01-19 18:49:39.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: create_streamlines <StreamLines> <yose_valley_tiles_rst05> 
# Description: 
# Creates a hydrographic network from a DEM based on a minimum area threshold
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
StreamLines = arcpy.GetParameterAsText(0)

yose_valley_tiles_rst05 = arcpy.GetParameterAsText(1)

# Local variables:
Fill_sample_rst1_tif = ""
Extent = "262530.4112 4175140.0246 284913.2599 4184347.6064"
Cell_Size = "MAXOF"
Output_drop_raster = ""
Output_flow_direction_raster = ""
Output_accumulation_raster = ""
Cells_SQL_Expression = "VALUE < 100"
HydroNetwork = ""
StreamLinks = ""

# Set Geoprocessing environments
arcpy.env.scratchWorkspace = "C:\\GIS\\scratch.gdb"
arcpy.env.workspace = "C:\\GIS\\scratch.gdb"

# Process: Fill
arcpy.gp.Fill_sa(yose_valley_tiles_rst05, Fill_sample_rst1_tif, "")

# Process: Flow Direction
tempEnvironment0 = arcpy.env.extent
arcpy.env.extent = Extent
tempEnvironment1 = arcpy.env.cellSize
arcpy.env.cellSize = Cell Size
arcpy.gp.FlowDirection_sa(Fill_sample_rst1_tif, Output_flow_direction_raster, "NORMAL", Output_drop_raster, "D8")
arcpy.env.extent = tempEnvironment0
arcpy.env.cellSize = tempEnvironment1

# Process: Flow Accumulation
arcpy.gp.FlowAccumulation_sa(Output_flow_direction_raster, Output_accumulation_raster, "", "FLOAT", "D8")

# Process: Set Null
arcpy.gp.SetNull_sa(Output_accumulation_raster, Output_accumulation_raster, HydroNetwork, Cells_SQL_Expression)

# Process: Stream Link
arcpy.gp.StreamLink_sa(HydroNetwork, Output_flow_direction_raster, StreamLinks)

# Process: Stream to Feature
arcpy.gp.StreamToFeature_sa(StreamLinks, Output_flow_direction_raster, StreamLines, "NO_SIMPLIFY")

