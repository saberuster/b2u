import os
import configparser


def isvalid_uprojectfile(filepath):
    """
    Checks filepath is a valid .uproject file
    :param str filepath: the file path of the .uproject file
    :return bool: filepath is a valid .uproject or not
    """
    _, ext = os.path.splitext(filepath)
    return ext == '.uproject'


def get_uproject_name(filepath):
    """
    Get uproject name from Config/DefaultGame.ini
    :param str filepath: .uproject file location
    :return str: uproject name
    """
    uproject_root_dir = os.path.dirname(filepath)
    game_ini_config = os.path.join(
        uproject_root_dir, 'Config', 'DefaultGame.ini')
    config = configparser.ConfigParser()
    config.read(game_ini_config)
    return config['/Script/EngineSettings.GeneralProjectSettings']['ProjectName']


def get_unreal_target_path(target_path):
    """
    Remove '/Game' prefix and space if exist
    :param str target_path
    :return str
    """
    return target_path.strip().removeprefix('/Game').removeprefix('/').removesuffix('/')
