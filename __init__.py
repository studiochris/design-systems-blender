bl_info = {
    "name": "Design Systems for Blender",
    "description": "Imports design tokens from JSON or .blend files to use in your Scene.",
    "author": "@studiochris",
    "version": (0, 0, 1),
    "blender": (2, 93, 0),
    "location": "Shader Editor > Tools > Design System",
    "warning": "Experimental: First try at writing a Blender Addon or Python",
    "support": "COMMUNITY",
    "category": "Interface",
}

import bpy

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       IntVectorProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Menu,
                       Operator,
                       PropertyGroup,
                       )


    
                       
class DesignSystemSettings(PropertyGroup):
    
    name: StringProperty(
        name = "Current Design System",
        description = "Name of the current design system",
        default = "Nautilus",
        )
    
    version: IntVectorProperty(
        name = "Design System Version",
        description = "Version of the current design system using symantic versioning.\n"
                      "In JSON, this property should be a string of 3 integers joined by a dot (1.2.3)",
        default = (0, 0, 0),
        )
        
    is_loaded: BoolProperty(
        name = "Is a design system loaded?",
        description = "Is a design system loaded?",
        default = False,
    )

dsn_namespace = "design_system_nodes."


class DesignSystemExists(bpy.types.Operator):
    bl_idname = dsn_namespace + "exists"
    bl_label = "Design system exists?"
    bl_description = "Checks for the primary Design System material that holds custom node groups belonging to the Design System addon"
    bl_options = {"REGISTER"}

    exists: bpy.props.BoolProperty()

    def execute(self, context):
        self.report({'INFO'}, str(self.exists))
        return {'FINISHED'}

    def invoke(self, context, event):
        materials = bpy.data.materials
        self.exists = "Design System" in materials
        return self.execute(materials)


    
        
class NODE_EDITOR_PT_DesignSystemPanel(bpy.types.Panel):
    
    bl_label = "Design System"
    bl_idname = "NODE_EDITOR_PT_DesignSystemPanel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Design System"
    bl_options = {'HEADER_LAYOUT_EXPAND'}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        design_system = scene.design_system
        
        formatted_design_system_version = str(design_system.version[0]) + "." + str(design_system.version[1]) + "." + str(design_system.version[2])

        layout.label(text=design_system.name + " " + formatted_design_system_version)

        layout.operator('design_system.op_open_documentation', icon='HELP', text = design_system.name + " Online Docs")

            
class DESIGNSYSTEM_OP_new_design_system(bpy.types.Operator):
    
    bl_idname = "design_system.op_new"
    bl_label = "New Design System"
    bl_description = "Create a new design system"
    
    @classmethod
    def get_context(cls, context):
        return context;
        
    def execute(self, context):
        props = self.properties
        scene = context.scene
        
        self.report({'INFO'}, "New design system started")
        
        return {'FINISHED'}

class DESIGNSYSTEM_OP_load_design_system(bpy.types.Operator):
    
    bl_idname = "design_system.op_load"
    bl_label = "Import Design System"
    bl_description = "Import an existing design system from a JSON file"
    
    @classmethod
    def get_context(cls, context):
        return context;
        
    def execute(self, context):
        props = self.properties
        scene = context.scene
        
        self.report({'INFO'}, "Design System loaded.")
        
        return {'FINISHED'}


class DESIGNSYSTEM_OP_append_design_system(bpy.types.Operator):
    
    bl_idname = "design_system.op_append_reference"
    bl_label = "Append Reference"
    bl_description = "Append a reference to a design system in another .blend file"
    
    @classmethod
    def get_context(cls, context):
        return context;
        
    def execute(self, context):
        props = self.properties
        scene = context.scene
        
        self.report({'INFO'}, "Design System loaded.")
        
        return {'FINISHED'}

class DESIGNSYSTEM_OP_resync_design_system(bpy.types.Operator):
    
    bl_idname = "design_system.op_resync_design_system"
    bl_label = "Resync Design System"
    bl_description = "Reload and update the design system from the original source"
    
    @classmethod
    def get_context(cls, context):
        return context;
        
    def execute(self, context):
        props = self.properties
        scene = context.scene
        
        self.report({'INFO'}, "Design System synced.")
        
        return {'FINISHED'}
          
            
class NODE_EDITOR_PT_DesignSystemPanel_ThemesPanel(bpy.types.Panel):
    
    bl_label = "Themes"
    bl_idname = "NODE_EDITOR_PT_DesignSystemPanel_ThemesPanel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Design System"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        design_system = scene.design_system


class NODE_EDITOR_PT_DesignSystemTokensPanel(bpy.types.Panel):
    
    bl_label = "Tokens"
    bl_idname = "NODE_EDITOR_PT_DesignSystemTokensPanel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Design System"
    bl_options = {'HEADER_LAYOUT_EXPAND'}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        design_system = scene.design_system

class NODE_EDITOR_PT_DesignSystemTokensPanel_ColorsPanel(bpy.types.Panel):
    
    bl_label = "Colors"
    bl_idname = "NODE_EDITOR_PT_DesignSystemTokensPanel_ColorsPanel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_parent_id = 'NODE_EDITOR_PT_DesignSystemTokensPanel'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        design_system = scene.design_system
        
        row = layout.row();
        row.label(text="Crimson", icon_value=bpy.data.materials["zDS_CrimsonThumbnail"].preview.icon_id)
        
        row = layout.row();
        row.label(text="Orange")
        
        row = layout.row();
        row.label(text="Yellow")
        
        
class NODE_EDITOR_PT_DesignSystemTokensPanel_GradientsPanel(bpy.types.Panel):
    
    bl_label = "Gradients"
    bl_idname = "NODE_EDITOR_PT_DesignSystemTokensPanel_GradientsPanel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_parent_id = 'NODE_EDITOR_PT_DesignSystemTokensPanel'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        design_system = scene.design_system
        
class NODE_EDITOR_PT_DesignSystemTokensPanel_TexturesPanel(bpy.types.Panel):
    
    bl_label = "Textures"
    bl_idname = "NODE_EDITOR_PT_DesignSystemTokensPanel_TexturesPanel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_parent_id = 'NODE_EDITOR_PT_DesignSystemTokensPanel'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        design_system = scene.design_system
        
class NODE_EDITOR_PT_DesignSystemTokensPanel_SurfacesPanel(bpy.types.Panel):
    
    bl_label = "Surfaces"
    bl_idname = "NODE_EDITOR_PT_DesignSystemTokensPanel_SurfacesPanel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_parent_id = 'NODE_EDITOR_PT_DesignSystemTokensPanel'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        design_system = scene.design_system
        
class NODE_EDITOR_PT_DesignSystemTokensPanel_MaterialsPanel(bpy.types.Panel):
    
    bl_label = "Materials"
    bl_idname = "NODE_EDITOR_PT_DesignSystemTokensPanel_MaterialsPanel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_parent_id = 'NODE_EDITOR_PT_DesignSystemTokensPanel'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        design_system = scene.design_system
        
class NODE_EDITOR_PT_DesignSystemTokensPanel_EnvironmentsPanel(bpy.types.Panel):
    
    bl_label = "Environments"
    bl_idname = "NODE_EDITOR_PT_DesignSystemTokensPanel_EnvironmentsPanel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_parent_id = 'NODE_EDITOR_PT_DesignSystemTokensPanel'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        design_system = scene.design_system
        
        # buttons linking to online documentation   

    
class NODE_EDITOR_PT_DesignSystemDocsPanel(bpy.types.Panel):
    
    bl_label = "Documentation"
    bl_idname = "NODE_EDITOR_PT_DesignSystemDocsPanel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Design System"
    bl_options = {'HEADER_LAYOUT_EXPAND'}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        design_system = scene.design_system
        
        # buttons linking to online documentation

class DESIGNSYSTEM_OP_open_documentation(bpy.types.Operator):
    
    bl_idname = "design_system.op_open_documentation"
    bl_label = "Design System Docs"
    bl_description = "Open design system documentation in your default browser"
    
    @classmethod
    def get_context(cls, context):
        return context;
        
    
    def execute(self, context):
        props = self.properties
        scene = context.scene
        design_system = scene.design_system
        
        self.report({'INFO'}, "Opened " + design_system.name + " Documentation")
        
        return {'FINISHED'}
    
class NODE_EDITOR_PT_DesignSystemMaintenancePanel(bpy.types.Panel):
    
    bl_label = "Maintenance"
    bl_idname = "NODE_EDITOR_PT_DesignSystemMaintenancePanel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Design System"
    bl_parent_id = 'NODE_EDITOR_PT_DesignSystemPanel'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        design_system = scene.design_system

        layout.operator('design_system.op_resync_design_system', text="Check for Updates", icon='FILE_PARENT')
        layout.operator('design_system.op_resync_design_system', icon='FILE_REFRESH')

        layout.separator(factor=1.0)

        row = layout.row()
        row.label(text="Load a design system from...", icon='IMPORT')
        
        row = layout.row()
        row.operator('design_system.op_new', text="New ")
        row.operator('design_system.op_load', text="Import")
        
        row = layout.row()
        row.operator('design_system.op_append_reference', icon="FILE_BACKUP")

        
        
class NODE_EDITOR_PT_DesignSystemAboutPanel(bpy.types.Panel):
    
    bl_label = "About DS Addon"
    bl_idname = "NODE_EDITOR_PT_DesignSystemAboutPanel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Design System"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        design_system = scene.design_system
    
# -----------------------------------------
#  Register & Unregister
# -----------------------------------------

classes = (
    DesignSystemSettings,
    DesignSystemExists,
    DESIGNSYSTEM_OP_new_design_system,
    DESIGNSYSTEM_OP_load_design_system,
    DESIGNSYSTEM_OP_append_design_system,
    DESIGNSYSTEM_OP_resync_design_system,
    DESIGNSYSTEM_OP_open_documentation,
    NODE_EDITOR_PT_DesignSystemPanel,
    NODE_EDITOR_PT_DesignSystemPanel_ThemesPanel,
    NODE_EDITOR_PT_DesignSystemTokensPanel,
    NODE_EDITOR_PT_DesignSystemTokensPanel_ColorsPanel,
    NODE_EDITOR_PT_DesignSystemTokensPanel_GradientsPanel,
    NODE_EDITOR_PT_DesignSystemTokensPanel_TexturesPanel,
    NODE_EDITOR_PT_DesignSystemTokensPanel_SurfacesPanel,
    NODE_EDITOR_PT_DesignSystemTokensPanel_MaterialsPanel,
    NODE_EDITOR_PT_DesignSystemTokensPanel_EnvironmentsPanel,
    NODE_EDITOR_PT_DesignSystemDocsPanel,
    NODE_EDITOR_PT_DesignSystemMaintenancePanel,
    NODE_EDITOR_PT_DesignSystemAboutPanel,
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
        
    bpy.types.Scene.design_system = PointerProperty(type=DesignSystemSettings)
        
def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
        
    del bpy.types.Scene.design_system
        
if __name__ == "__main__":
    register()
    