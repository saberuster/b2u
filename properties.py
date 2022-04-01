from bpy.props import StringProperty, PointerProperty
from bpy.types import PropertyGroup, Scene, Object
from bpy.utils import register_class, unregister_class


class B2UlAddonProperties:
    """
    This class holds the properties for the addon.
    """
    pass


class B2UWindowManagerProperties(PropertyGroup):
    """
    This class holds the properties for a window.
    """
    pass


class B2USceneProperties(PropertyGroup):
    """
    This class holds the properties for a scene.
    """
    unreal_project_root_path: StringProperty()
    unreal_project_name: StringProperty()


class B2UObjectProperties(PropertyGroup):
    """
    This class holds the properties for a object.
    """
    target_path: StringProperty()


def register():
    """
    Registers the property group class and adds it to the window manager context when the
    addon is enabled.
    """
    if not PropertyGroup.bl_rna_get_subclass_py('B2USceneProperties'):
        register_class(B2USceneProperties)
        Scene.b2u = PointerProperty(type=B2USceneProperties)

    if not PropertyGroup.bl_rna_get_subclass_py('B2UObjectProperties'):
        register_class(B2UObjectProperties)
        Object.b2u = PointerProperty(type=B2UObjectProperties)


def unregister():
    """
    Unregisters the property group class and deletes it from the window manager context when the
    addon is disabled.
    """
    scene_property_class = PropertyGroup.bl_rna_get_subclass_py(
        'B2USceneProperties')
    if scene_property_class:
        unregister_class(scene_property_class)

    if hasattr(Scene, 'b2u'):
        del Scene.b2u

    object_property_class = PropertyGroup.bl_rna_get_subclass_py(
        'B2UObjectProperties')
    if object_property_class:
        unregister_class(object_property_class)

    if hasattr(Object, 'b2u'):
        del Object.b2u
