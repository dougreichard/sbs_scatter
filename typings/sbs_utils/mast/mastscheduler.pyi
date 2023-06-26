from sbs_utils.mast.mast import Assign
from sbs_utils.mast.mast import AwaitCondition
from sbs_utils.mast.mast import AwaitFail
from sbs_utils.mast.mast import Behavior
from sbs_utils.mast.mast import Cancel
from sbs_utils.mast.mast import Comment
from sbs_utils.mast.mast import Delay
from sbs_utils.mast.mast import DoCommand
from sbs_utils.mast.mast import End
from sbs_utils.mast.mast import EndAwait
from sbs_utils.mast.mast import Fail
from sbs_utils.mast.mast import IfStatements
from sbs_utils.mast.mast import Import
from sbs_utils.mast.mast import InlineData
from sbs_utils.mast.mast import Input
from sbs_utils.mast.mast import Jump
from sbs_utils.mast.mast import Label
from sbs_utils.mast.mast import Log
from sbs_utils.mast.mast import Logger
from sbs_utils.mast.mast import LoopBreak
from sbs_utils.mast.mast import LoopEnd
from sbs_utils.mast.mast import LoopStart
from sbs_utils.mast.mast import Marker
from sbs_utils.mast.mast import Mast
from sbs_utils.mast.mast import MastCompilerError
from sbs_utils.mast.mast import MastDataObject
from sbs_utils.mast.mast import MastNode
from sbs_utils.mast.mast import MatchStatements
from sbs_utils.mast.mast import Parallel
from sbs_utils.mast.mast import ParseData
from sbs_utils.mast.mast import PyCode
from sbs_utils.mast.mast import ReturnIf
from sbs_utils.mast.mast import Rule
from sbs_utils.mast.mast import Scope
from sbs_utils.mast.mast import Timeout
from sbs_utils.mast.mast import Yield
from sbs_utils.engineobject import EngineObject
from enum import Enum
from enum import IntEnum
from zipfile import ZipFile
def first_newline_index (s):
    ...
def first_non_newline_index (s):
    ...
def first_non_space_index (s):
    ...
def first_non_whitespace_index (s):
    ...
def get_story_id ():
    ...
def get_task_id ():
    ...
def getmembers (object, predicate=None):
    ...
def isfunction (object):
    ...
class AssignRuntimeNode(MastRuntimeNode):
    """class AssignRuntimeNode"""
    def poll (self, mast, task: 'MastAsyncTask', node: 'Assign'):
        ...
class AwaitConditionRuntimeNode(MastRuntimeNode):
    """class AwaitConditionRuntimeNode"""
    def enter (self, mast: 'Mast', task: 'MastAsyncTask', node: 'AwaitCondition'):
        ...
    def poll (self, mast: 'Mast', task: 'MastAsyncTask', node: 'AwaitCondition'):
        ...
class AwaitFailRuntimeNode(MastRuntimeNode):
    """class AwaitFailRuntimeNode"""
    def poll (self, mast, task: 'MastAsyncTask', node: 'AwaitFail'):
        ...
class BehaviorRuntimeNode(MastRuntimeNode):
    """class BehaviorRuntimeNode"""
    def enter (self, mast, task, node: 'Behavior'):
        ...
    def poll (self, mast, task: 'MastAsyncTask', node: 'Behavior'):
        ...
class CancelRuntimeNode(MastRuntimeNode):
    """class CancelRuntimeNode"""
    def poll (self, mast, task: 'MastAsyncTask', node: 'Cancel'):
        ...
class DelayRuntimeNode(MastRuntimeNode):
    """class DelayRuntimeNode"""
    def enter (self, mast, task, node):
        ...
    def poll (self, mast, task, node):
        ...
class DoCommandRuntimeNode(MastRuntimeNode):
    """class DoCommandRuntimeNode"""
    def poll (self, mast, task: 'MastAsyncTask', node: 'DoCommand'):
        ...
class EndAwaitRuntimeNode(MastRuntimeNode):
    """class EndAwaitRuntimeNode"""
class EndRuntimeNode(MastRuntimeNode):
    """class EndRuntimeNode"""
    def poll (self, mast, task, node: 'End'):
        ...
class FailRuntimeNode(MastRuntimeNode):
    """class FailRuntimeNode"""
    def poll (self, mast, task, node: 'Fail'):
        ...
class IfStatementsRuntimeNode(MastRuntimeNode):
    """class IfStatementsRuntimeNode"""
    def first_true (self, task: 'MastAsyncTask', node: 'IfStatements'):
        ...
    def poll (self, mast, task, node: 'IfStatements'):
        ...
class JumpRuntimeNode(MastRuntimeNode):
    """class JumpRuntimeNode"""
    def poll (self, mast: 'Mast', task: 'MastAsyncTask', node: 'Jump'):
        ...
class LogRuntimeNode(MastRuntimeNode):
    """class LogRuntimeNode"""
    def enter (self, mast, task: 'MastAsyncTask', node: 'Log'):
        ...
class LoggerRuntimeNode(MastRuntimeNode):
    """class LoggerRuntimeNode"""
    def enter (self, mast: 'Mast', task: 'MastAsyncTask', node: 'Logger'):
        ...
class LoopBreakRuntimeNode(MastRuntimeNode):
    """class LoopBreakRuntimeNode"""
    def enter (self, mast, task: 'MastAsyncTask', node: 'LoopBreak'):
        ...
    def poll (self, mast, task, node: 'LoopBreak'):
        ...
class LoopEndRuntimeNode(MastRuntimeNode):
    """class LoopEndRuntimeNode"""
    def poll (self, mast, task, node: 'LoopEnd'):
        ...
class LoopStartRuntimeNode(MastRuntimeNode):
    """class LoopStartRuntimeNode"""
    def enter (self, mast, task: 'MastAsyncTask', node: 'LoopStart'):
        ...
    def poll (self, mast, task, node: 'LoopStart'):
        ...
class MastAllTask(object):
    """class MastAllTask"""
    def __init__ (self, main) -> 'None':
        """Initialize self.  See help(type(self)) for accurate signature."""
    def run_event (self, event_name, event):
        ...
    def tick (self) -> 'PollResults':
        ...
class MastAnyTask(object):
    """class MastAnyTask"""
    def __init__ (self, main) -> 'None':
        """Initialize self.  See help(type(self)) for accurate signature."""
    def run_event (self, event_name, event):
        ...
    def tick (self) -> 'PollResults':
        ...
class MastAsyncTask(EngineObject):
    """class MastAsyncTask"""
    def __init__ (self, main: "'MastScheduler'", inputs=None, conditional=None):
        """Initialize self.  See help(type(self)) for accurate signature."""
    def _add (id, obj):
        ...
    def _remove (id):
        ...
    def add_dependency (id, task):
        ...
    def add_event (self, event_name, event):
        ...
    def call_leave (self):
        ...
    def clear ():
        ...
    def do_jump (self, label='main', activate_cmd=0):
        ...
    def do_resume (self, label, activate_cmd, runtime_node):
        ...
    def eval_code (self, code):
        ...
    def exec_code (self, code):
        ...
    def format_string (self, message):
        ...
    def get (id):
        ...
    def get_as (id, as_cls):
        ...
    def get_objects_from_set (the_set):
        ...
    def get_role_object (link_name):
        ...
    def get_role_objects (role):
        ...
    def get_role_set (role):
        ...
    def get_scoped_value (self, key, defa, scope):
        ...
    def get_symbols (self):
        ...
    def get_value (self, key, defa):
        ...
    def get_variable (self, key):
        ...
    def has_inventory_list (collection_name):
        ...
    def has_inventory_set (collection_name):
        ...
    def has_links_list (collection_name):
        ...
    def has_links_set (collection_name):
        ...
    def jump (self, label='main', activate_cmd=0):
        ...
    def next (self):
        ...
    def pop_label (self, inc_loc=True, true_pop=False):
        ...
    def push_inline_block (self, label, activate_cmd=0, data=None):
        ...
    def push_label (self, label, activate_cmd=0, data=None):
        ...
    def resolve_id (other: 'EngineObject | CloseData | int'):
        ...
    def resolve_py_object (other: 'EngineObject | CloseData | int'):
        ...
    def run_event (self, event_name, event):
        ...
    def runtime_error (self, s):
        ...
    def set_value (self, key, value, scope):
        ...
    def set_value_keep_scope (self, key, value):
        ...
    def start_task (self, label='main', inputs=None, task_name=None) -> 'MastAsyncTask':
        ...
    def stop_for_dependency (id):
        ...
    def tick (self):
        ...
class MastFallbackTask(object):
    """class MastFallbackTask"""
    def __init__ (self, main, labels, conditional) -> 'None':
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def active_label (self):
        ...
    def rewind (self):
        ...
    def run_event (self, event_name, event):
        ...
    def tick (self) -> 'PollResults':
        ...
class MastRuntimeError(object):
    """class MastRuntimeError"""
    def __init__ (self, message, line_no):
        """Initialize self.  See help(type(self)) for accurate signature."""
class MastRuntimeNode(object):
    """class MastRuntimeNode"""
    def enter (self, mast, scheduler, node):
        ...
    def leave (self, mast, scheduler, node):
        ...
    def poll (self, mast, scheduler, node):
        ...
class MastScheduler(object):
    """class MastScheduler"""
    def __init__ (self, mast: 'Mast', overrides=None):
        """Initialize self.  See help(type(self)) for accurate signature."""
    def _start_task (self, label='main', inputs=None, task_name=None) -> 'MastAsyncTask':
        ...
    def cancel_task (self, name):
        ...
    def get_seconds (self, clock):
        """Gets time for a given clock default is just system """
    def get_value (self, key, defa=None):
        ...
    def get_variable (self, key):
        ...
    def is_running (self):
        ...
    def on_start_task (self, t):
        ...
    def runtime_error (self, message):
        ...
    def start_all_task (self, labels='main', inputs=None, task_name=None, conditional=None) -> 'MastAllTask':
        ...
    def start_any_task (self, labels='main', inputs=None, task_name=None, conditional=None) -> 'MastAnyTask':
        ...
    def start_fallback_task (self, labels='main', inputs=None, task_name=None, conditional=None) -> 'MastFallbackTask':
        ...
    def start_sequence_task (self, labels='main', inputs=None, task_name=None, conditional=None) -> 'MastSequenceTask':
        ...
    def start_task (self, label='main', inputs=None, task_name=None) -> 'MastAsyncTask':
        ...
    def tick (self):
        ...
class MastSequenceTask(object):
    """class MastSequenceTask"""
    def __init__ (self, main, labels, conditional) -> 'None':
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def active_label (self):
        ...
    def rewind (self):
        ...
    def run_event (self, event_name, event):
        ...
    def tick (self) -> 'PollResults':
        ...
class MatchStatementsRuntimeNode(MastRuntimeNode):
    """class MatchStatementsRuntimeNode"""
    def first_true (self, task: 'MastAsyncTask', node: 'MatchStatements'):
        ...
    def poll (self, mast, task, node: 'MatchStatements'):
        ...
class ParallelRuntimeNode(MastRuntimeNode):
    """class ParallelRuntimeNode"""
    def enter (self, mast, task, node: 'Parallel'):
        ...
    def poll (self, mast, task: 'MastAsyncTask', node: 'Parallel'):
        ...
class PollResults(IntEnum):
    """int([x]) -> integer
    int(x, base=10) -> integer
    
    Convert a number or string to an integer, or return 0 if no arguments
    are given.  If x is a number, return x.__int__().  For floating point
    numbers, this truncates towards zero.
    
    If x is not a number or if base is given, then x must be a string,
    bytes, or bytearray instance representing an integer literal in the
    given base.  The literal can be preceded by '+' or '-' and be surrounded
    by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
    Base 0 means to interpret the base from the string as an integer literal.
    >>> int('0b100', base=0)
    4"""
    FAIL_END : 100
    OK_ADVANCE_FALSE : 3
    OK_ADVANCE_TRUE : 2
    OK_END : 99
    OK_JUMP : 1
    OK_RUN_AGAIN : 4
    OK_YIELD : 5
class PushData(object):
    """class PushData"""
    def __init__ (self, label, active_cmd, data=None, resume_node=None):
        """Initialize self.  See help(type(self)) for accurate signature."""
class PyCodeRuntimeNode(MastRuntimeNode):
    """class PyCodeRuntimeNode"""
    def poll (self, mast, task: 'MastAsyncTask', node: 'PyCode'):
        ...
class ReturnIfRuntimeNode(MastRuntimeNode):
    """class ReturnIfRuntimeNode"""
    def poll (self, mast, task, node: 'ReturnIf'):
        ...
class TimeoutRuntimeNode(MastRuntimeNode):
    """class TimeoutRuntimeNode"""
    def poll (self, mast, task: 'MastAsyncTask', node: 'Timeout'):
        ...
class YieldRuntimeNode(MastRuntimeNode):
    """class YieldRuntimeNode"""
    def poll (self, mast, task, node: 'Yield'):
        ...
