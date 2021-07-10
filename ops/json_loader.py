import json
import bpy
from ..constants import *

class JsonLoader(bpy.types.Operator):
  """Tooltip description"""
  bl_idname = f"{DSOP}.load_json"
  bl_label = "My Class Name"
  bl_description = "Description that shows in blender tooltips"
  bl_options = {"REGISTER"}

  def execute(self, context):
    
    return {"FINISHED"}
