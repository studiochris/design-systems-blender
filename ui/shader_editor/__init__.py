import bpy

from ...constants import *

classes = []

class DesignSystemColorPanel(bpy.types.Panel):
  bl_name = f"{DSPL}ColorPanel"
  bl_label = "Colors"
  bl_idname = "NODE_EDITOR_PT_DesignSystemTokensPanel_ColorsPanel"
  bl_space_type = 'NODE_EDITOR'
  bl_region_type = 'UI'
  bl_parent_id = 'NODE_EDITOR_PT_DesignSystemTokensPanel'

  def register(self, context):
    print(f"Hello")

  def unregister(self, context):
    print(f"Goodbye") 

classes += [DesignSystemColorPanel]