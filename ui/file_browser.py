import bpy
from bpy_extras.io_utils import ImportHelper


class UProjectFileImportHelper(ImportHelper):
    """
    This class subclasses the import helper to define a custom file browser for importing assets.
    """
    filter_glob: bpy.props.StringProperty(
        default="*.uproject",
        options={"HIDDEN"},
        subtype="FILE_PATH",
    )
