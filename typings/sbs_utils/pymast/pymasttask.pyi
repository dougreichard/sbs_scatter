from sbs_utils.engineobject import EngineObject
from sbs_utils.pymast.pollresults import PollResults
from sbs_utils.pymast.pymastcomms import PyMastComms
from sbs_utils.pymast.pymastscience import PyMastScience
from functools import partial
def get_task_id ():
    ...
def label (*dargs, **dkwargs):
    ...
class DataHolder(object):
    """class DataHolder"""
class PyMastTask(EngineObject):
    """class PyMastTask"""
    def __init__ (self, story, scheduler, label) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def _add (id, obj):
        ...
    def _delay (self, seconds=0, minutes=0, use_sim=False):
        ...
    def _remove (id):
        ...
    def _run_event (self, label, ctx, event):
        ...
    def _run_invert (self, label):
        ...
    def _run_sel (self, labels):
        ...
    def _run_seq (self, labels):
        ...
    def _run_until (self, poll_result, label):
        ...
    def await_comms (self, buttons, player=None, npc=None):
        ...
    def await_gui (self, buttons, timeout, on_message=None, test_refresh=None, test_end_await=None, on_disconnect=None):
        ...
    def await_science (self, scans, player=None, npc=None):
        ...
    def behave_invert (self, label):
        ...
    def behave_sel (self, *labels):
        ...
    def behave_seq (self, *labels):
        ...
    def behave_until (self, poll_result, label):
        ...
    def clear ():
        ...
    @property
    def client_id (self):
        ...
    def delay (self, seconds=0, minutes=0, use_sim=False):
        ...
    def do_jump (self):
        ...
    def end (self):
        ...
    def get (id):
        ...
    def get_as (id, as_cls):
        ...
    def get_gen (self, label):
        ...
    def get_objects_from_set (the_set):
        ...
    def get_role_object (link_name):
        ...
    def get_role_objects (role):
        ...
    def get_role_set (role):
        ...
    def has_inventory_list (collection_name):
        ...
    def has_inventory_set (collection_name):
        ...
    def has_links_list (collection_name):
        ...
    def has_links_set (collection_name):
        ...
    def jump (self, label):
        ...
    def on_event (self, ctx, event):
        ...
    def pop (self):
        ...
    def push (self, label):
        ...
    def push_jump_pop (self, label):
        ...
    def quick_push (self, func):
        ...
    def resolve_id (other: 'EngineObject | CloseData | int'):
        ...
    def resolve_py_object (other: 'EngineObject | CloseData | int'):
        ...
    def run_science (self, science):
        ...
    def tick (self, ctx):
        ...
    def watch_event (self, event_tag, label):
        ...
