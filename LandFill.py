import sys
reload(sys)
sys.setdefaultencoding("latin-1")

import xlrd, arcpy, string, os, zipfile, fileinput, time
from datetime import date
start_time = time.time()

INPUT_PATH = "input"
OUTPUT_PATH = "output"
if arcpy.Exists(OUTPUT_PATH + "\\LandFill.gdb"):
	os.system("rmdir " + OUTPUT_PATH + "\\LandFill.gdb /s /q")
os.system("del " + OUTPUT_PATH + "\\*LandFill*.*")
arcpy.CreateFileGDB_management(OUTPUT_PATH, "LandFill", "9.3")
arcpy.env.workspace = OUTPUT_PATH + "\\LandFill.gdb"


elapsed_time = time.time() - start_time
print elapsed_time