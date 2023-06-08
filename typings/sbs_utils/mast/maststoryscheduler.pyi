from sbs_utils.mast.maststory import AppendText
from sbs_utils.mast.maststory import AwaitGui
from sbs_utils.mast.maststory import Blank
from sbs_utils.mast.maststory import BuildaConsole
from sbs_utils.mast.maststory import ButtonControl
from sbs_utils.mast.maststory import CheckboxControl
from sbs_utils.mast.maststory import Choose
from sbs_utils.mast.maststory import Clickable
from sbs_utils.mast.maststory import Console
from sbs_utils.mast.maststory import DropdownControl
from sbs_utils.mast.maststory import Face
from sbs_utils.mast.maststory import GuiContent
from sbs_utils.mast.maststory import Hole
from sbs_utils.mast.maststory import ImageControl
from sbs_utils.mast.maststory import MastStory
from sbs_utils.mast.maststory import OnChange
from sbs_utils.mast.maststory import RadioControl
from sbs_utils.mast.maststory import Refresh
from sbs_utils.mast.maststory import Row
from sbs_utils.mast.maststory import Section
from sbs_utils.mast.maststory import Ship
from sbs_utils.mast.maststory import SliderControl
from sbs_utils.mast.maststory import Style
from sbs_utils.mast.maststory import Text
from sbs_utils.mast.maststory import TextInputControl
from sbs_utils.mast.maststory import WidgetList
from sbs_utils.mast.mastsbs import Button
from sbs_utils.gui import Context
from sbs_utils.gui import FakeEvent
from sbs_utils.gui import Gui
from sbs_utils.gui import Page
from sbs_utils.mast.errorpage import ErrorPage
from sbs_utils.mast.parsers import LayoutAreaParser
from sbs_utils.mast.parsers import StyleDefinition
from sbs_utils.mast.mast import Mast
from sbs_utils.mast.mast import Scope
from sbs_utils.mast.mastscheduler import MastAsyncTask
from sbs_utils.mast.mastscheduler import MastRuntimeNode
from sbs_utils.mast.mastscheduler import PollResults
from sbs_utils.mast.mastsbsscheduler import MastSbsScheduler
from sbs_utils.tickdispatcher import TickDispatcher
class AppendTextRuntimeNode(StoryRuntimeNode):
    """class AppendTextRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.AppendText):
        ...
class AwaitGuiRuntimeNode(StoryRuntimeNode):
    """class AwaitGuiRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.AwaitGui):
        ...
    def poll (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.AwaitGui):
        ...
class BlankRuntimeNode(StoryRuntimeNode):
    """class BlankRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.Blank):
        ...
class BuildaConsoleRuntimeNode(MastRuntimeNode):
    """Lower level console building command to allow layout"""
    def enter (self, mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.BuildaConsole):
        ...
class ButtonControlRuntimeNode(StoryRuntimeNode):
    """class ButtonControlRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.ButtonControl):
        ...
    def on_message (self, sim, event):
        ...
    def poll (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.ButtonControl):
        ...
class CheckboxControlRuntimeNode(StoryRuntimeNode):
    """class CheckboxControlRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.CheckboxControl):
        ...
    def on_message (self, ctx, event):
        ...
class ChoiceButtonRuntimeNode(StoryRuntimeNode):
    """class ChoiceButtonRuntimeNode"""
    def __init__ (self, choice, index, tag, node):
        """Initialize self.  See help(type(self)) for accurate signature."""
    def on_message (self, sim, event):
        ...
class ChooseRuntimeNode(StoryRuntimeNode):
    """class ChooseRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.Choose):
        ...
    def expand (self, button: sbs_utils.mast.mastsbs.Button, task: sbs_utils.mast.mastscheduler.MastAsyncTask):
        ...
    def poll (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.Choose):
        ...
class ClickableRuntimeNode(StoryRuntimeNode):
    """class ClickableRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.Clickable):
        ...
    def on_message (self, sim, event):
        ...
    def poll (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.Clickable):
        ...
class ConsoleRuntimeNode(MastRuntimeNode):
    """class ConsoleRuntimeNode"""
    def enter (self, mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.Console):
        ...
class DropdownControlRuntimeNode(StoryRuntimeNode):
    """class DropdownControlRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.DropdownControl):
        ...
    def on_message (self, sim, event):
        ...
    def poll (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.DropdownControl):
        ...
class FaceRuntimeNode(StoryRuntimeNode):
    """class FaceRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.Face):
        ...
    def poll (self, mast, task, node: sbs_utils.mast.maststory.Face):
        ...
class GuiContentRuntimeNode(StoryRuntimeNode):
    """class GuiContentRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.GuiContent):
        ...
class HoleRuntimeNode(StoryRuntimeNode):
    """class HoleRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.Hole):
        ...
class ImageControlRuntimeNode(StoryRuntimeNode):
    """class ImageControlRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.ImageControl):
        ...
class OnChangeRuntimeNode(StoryRuntimeNode):
    """class OnChangeRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.ImageControl):
        ...
    def poll (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.OnChange):
        ...
    def test (self):
        ...
class RadioControlRuntimeNode(StoryRuntimeNode):
    """class RadioControlRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.RadioControl):
        ...
    def on_message (self, sim, event):
        ...
class RefreshRuntimeNode(StoryRuntimeNode):
    """class RefreshRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.Refresh):
        ...
class RerouteGuiRuntimeNode(StoryRuntimeNode):
    """class RerouteGuiRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.ImageControl):
        ...
class RowRuntimeNode(StoryRuntimeNode):
    """class RowRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.Row):
        ...
class SectionRuntimeNode(StoryRuntimeNode):
    """class SectionRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.Section):
        ...
class ShipRuntimeNode(StoryRuntimeNode):
    """class ShipRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.Ship):
        ...
class SliderControlRuntimeNode(StoryRuntimeNode):
    """class SliderControlRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.SliderControl):
        ...
    def on_message (self, ctx, event):
        ...
class StoryPage(Page):
    """A interface class for creating GUI pages
    
        """
    def __init__ (self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def activate_console (self, console):
        ...
    def add_console_widget (self, widget):
        ...
    def add_content (self, layout_item, runtime_node):
        ...
    def add_on_change (self, runtime_node):
        ...
    def add_row (self):
        ...
    def add_section (self, clickable_tag=None, clickable=None):
        ...
    def add_tag (self, layout_item, runtime_node):
        ...
    def add_tag_by_value (self, tag, runtime_node):
        ...
    def get_pending_layout (self):
        ...
    def get_pending_row (self):
        ...
    def get_tag (self):
        ...
    def on_event (self, ctx, event):
        """on_event
        
        Called when the option pages page has been interacted with
        
        :param ctx:
        :type ctx: Artemis Cosmos simulation
        :param event: The event data
        :type event: event"""
    def on_message (self, ctx, event):
        """on_message
        
        Called when the option pages page has been interacted with
        
        :param ctx:
        :type ctx: Artemis Cosmos simulation
        :param event: The event data
        :type event: event"""
    def present (self, ctx, event):
        """Present the gui """
    def set_button_layout (self, layout):
        ...
    def set_widget_list (self, console, widgets):
        ...
    def start_story (self, ctx, client_id):
        ...
    def swap_layout (self):
        ...
    def tick_mast (self, ctx, t):
        ...
class StoryRuntimeNode(MastRuntimeNode):
    """class StoryRuntimeNode"""
    def apply_style_def (self, style_def, layout_item, task):
        ...
    def apply_style_name (self, style_name, layout_item, task):
        ...
    def databind (self):
        ...
    def on_message (self, sim, event):
        ...
class StoryScheduler(MastSbsScheduler):
    """class StoryScheduler"""
    def __init__ (self, mast: sbs_utils.mast.mast.Mast, overrides=None):
        """Initialize self.  See help(type(self)) for accurate signature."""
    def on_event (self, ctx, event):
        ...
    def refresh (self, label):
        ...
    def run (self, ctx, client_id, page, label='main', inputs=None):
        ...
    def runtime_error (self, message):
        ...
    def story_tick_tasks (self, ctx, client_id):
        ...
class TextInputControlRuntimeNode(StoryRuntimeNode):
    """class TextInputControlRuntimeNode"""
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.TextInputControl):
        ...
    def on_message (self, sim, event):
        ...
class TextRuntimeNode(StoryRuntimeNode):
    """class TextRuntimeNode"""
    def databind (self):
        ...
    def enter (self, mast: sbs_utils.mast.mast.Mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.Text):
        ...
class WidgetListRuntimeNode(MastRuntimeNode):
    """class WidgetListRuntimeNode"""
    def enter (self, mast, task: sbs_utils.mast.mastscheduler.MastAsyncTask, node: sbs_utils.mast.maststory.WidgetList):
        ...
