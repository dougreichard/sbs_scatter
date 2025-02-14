from ...helpers import FrameContext
from ...futures import Trigger
from ...mast.mast import Scope

class ClickableTrigger(Trigger):
    def __init__(self, task, name):
        self.name = name
        self.task = task
        # Needs to be set by Mast
        # Pure mast this is active Label
        # Python ith should be a callable
        self.label = None 
        # 0 for python the node loc of the on in Mast
        self.loc = 0
        task.main.page.add_on_click(self)

    def click(self, click_tag):
        if self.name is not None:     
            if click_tag != self.name:
                    return False
        self.task.set_value("__CLICKED__", click_tag, Scope.TEMP)
        self.task.push_inline_block(self.label, self.loc)
        self.task.tick_in_context()
        return True

def gui_click(name_or_layout_item=None):
    """Trigger to watch when the specified layout element is clicked

    Args:
        layout_item (layout object): The object to watch

    Returns:
        trigger: A trigger watches something and runs something when the element is clicked
    """    
    task = FrameContext.task
    name = name_or_layout_item
    if name is not None:
        if not isinstance(name_or_layout_item, str):
            name = name_or_layout_item.click_tag
    return ClickableTrigger(task, name)


