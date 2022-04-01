import bpy
from . import properties, operators, utilities
from .ui import scene_panel, object_panel, file_browser


bl_info = {
    "name": "blender to unreal tools",
    "author": "saberuster",
    "version": (1, 0, 0),
    "blender": (3, 1, 0),
    "description": "some utils for transfer data from blender to unreal engine",
}


modules = [
    utilities,
    properties,
    file_browser,
    operators,
    scene_panel,
]


def register():
    """
    Registers the addon classes when the addon is enabled.
    """
    properties.register()
    operators.register()
    scene_panel.register()
    object_panel.register()


def unregister():
    object_panel.unregister()
    scene_panel.unregister()
    operators.unregister()
    properties.unregister()
