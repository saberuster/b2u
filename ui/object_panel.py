from bpy.types import Panel
from ..constants import ToolInfo
from bpy.utils import register_class, unregister_class


class B2UObjectPanel(Panel):
    """Creates a Panel in the object context of the properties editor"""
    bl_label = "Blender To Unreal"
    bl_idname = f"{ToolInfo.NAME.upper()}_PT_object_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        object_properties = context.object.b2u
        layout = self.layout
        layout.prop(object_properties, 'target_path')
        layout.operator('b2u.export_fbx_asset', icon='EXPORT')


def register():
    register_class(B2UObjectPanel)


def unregister():
    unregister_class(B2UObjectPanel)
