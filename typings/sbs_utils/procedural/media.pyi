from sbs_utils.mast.maststory import MediaLabel
def _media_schedule (kind, label, ID=0):
    """Sets the folder from which music is streamed; ID is ship, OR client, OR zero for server.
        """
def get_mission_dir_filename (filename):
    ...
def load_json_data (file):
    ...
def media_schedule (kind, name, ID=0):
    """Sets the folder from which music is streamed; ID is ship, OR client, OR zero for server.
    
    
    Args:
        name (_type_): _description_
        ID (_type_): _description_"""
def media_schedule_random (kind, ID=0):
    ...
def music_schedule (name, ID=0):
    ...
def music_schedule_random (ID=0):
    ...
def settings_add_defaults (additions):
    ...
def settings_get_defaults ():
    ...
def skybox_schedule (name, ID=0):
    ...
def skybox_schedule_random (ID=0):
    ...
def sub_task_schedule (label, data=None, var=None):
    """create an new task and start running at the specified label
    
    Args:
        label (str or label): The label to run
        data (duct, optional): Data to initialie task variables. Defaults to None.
        var (str, optional): Set the variable to the task created. Defaults to None.
    
    Returns:
        MastAsyncTask : The MAST task created"""
