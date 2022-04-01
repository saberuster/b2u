from cgitb import text
import bpy
import string
from ..constants import ToolInfo


class B2UScenePanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Blender To Unreal"
    bl_idname = f"{ToolInfo.NAME.upper()}_PT_scene_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        scene_properties = context.scene.b2u

        layout = self.layout
        layout.operator('b2u.import_uproject', icon='IMPORT')

        # project name field
        row = layout.row()
        split = row.split(factor=0.2)
        c = split.column()
        c.label(text='project name:')
        split = split.split()
        c = split.column()
        c.label(text=scene_properties.unreal_project_name)

        # root path field
        row = layout.row()
        split = row.split(factor=0.2)
        c = split.column()
        c.label(text='root path:')
        split = split.split()
        c = split.column()
        c.label(text=scene_properties.unreal_project_root_path)


def register():
    bpy.utils.register_class(B2UScenePanel)


def unregister():
    bpy.utils.unregister_class(B2UScenePanel)
