import imp
import os
import json
import bpy

from .ui import file_browser
from . import utilities
from bpy.types import Operator
from bpy.utils import register_class, unregister_class


class ImportUProjectFile(Operator, file_browser.UProjectFileImportHelper):
    bl_idname = "b2u.import_uproject"
    bl_label = "Import UProject File"

    def execute(self, context):
        if not utilities.isvalid_uprojectfile(self.filepath):
            return {'CANCELLED'}

        uproject_root_path = os.path.dirname(self.filepath)
        uproject_name = utilities.get_uproject_name(self.filepath)

        if uproject_name == '':
            return {'CANCELLED'}

        scene_properties = context.scene.b2u

        setattr(scene_properties, 'unreal_project_name', uproject_name)
        setattr(scene_properties, 'unreal_project_root_path', uproject_root_path)

        self.report({'INFO'}, "success import unreal project: " +
                    uproject_name + ", root path in: " + uproject_root_path)

        context.area.tag_redraw()

        return {'FINISHED'}


class ExportFbxAsset(Operator):
    bl_idname = "b2u.export_fbx_asset"
    bl_label = "Export Asset"

    def execute(self, context):

        scene_properties = context.scene.b2u
        object_properties = context.object.b2u
        export_path = os.path.join(scene_properties.unreal_project_root_path, 'Content', utilities.get_unreal_target_path(
            object_properties.target_path), context.object.name + '.fbx')

        print(export_path)
        bpy.ops.export_scene.fbx(filepath=export_path, use_selection=True)

        return {'FINISHED'}


operator_classes = [
    ImportUProjectFile,
    ExportFbxAsset
]


def register():
    for operator_class in operator_classes:
        register_class(operator_class)


def unregister():
    for operator_class in operator_classes:
        unregister_class(operator_class)
