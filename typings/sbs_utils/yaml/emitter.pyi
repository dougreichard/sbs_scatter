from sbs_utils.yaml.events import AliasEvent
from sbs_utils.yaml.events import CollectionEndEvent
from sbs_utils.yaml.events import CollectionStartEvent
from sbs_utils.yaml.events import DocumentEndEvent
from sbs_utils.yaml.events import DocumentStartEvent
from sbs_utils.yaml.events import Event
from sbs_utils.yaml.events import MappingEndEvent
from sbs_utils.yaml.events import MappingStartEvent
from sbs_utils.yaml.events import NodeEvent
from sbs_utils.yaml.events import ScalarEvent
from sbs_utils.yaml.events import SequenceEndEvent
from sbs_utils.yaml.events import SequenceStartEvent
from sbs_utils.yaml.events import StreamEndEvent
from sbs_utils.yaml.events import StreamStartEvent
from sbs_utils.yaml.error import YAMLError
class Emitter(object):
    """class Emitter"""
    def __init__ (self, stream, canonical=None, indent=None, width=None, allow_unicode=None, line_break=None):
        """Initialize self.  See help(type(self)) for accurate signature."""
    def analyze_scalar (self, scalar):
        ...
    def check_empty_document (self):
        ...
    def check_empty_mapping (self):
        ...
    def check_empty_sequence (self):
        ...
    def check_simple_key (self):
        ...
    def choose_scalar_style (self):
        ...
    def determine_block_hints (self, text):
        ...
    def dispose (self):
        ...
    def emit (self, event):
        ...
    def expect_alias (self):
        ...
    def expect_block_mapping (self):
        ...
    def expect_block_mapping_key (self, first=False):
        ...
    def expect_block_mapping_simple_value (self):
        ...
    def expect_block_mapping_value (self):
        ...
    def expect_block_sequence (self):
        ...
    def expect_block_sequence_item (self, first=False):
        ...
    def expect_document_end (self):
        ...
    def expect_document_root (self):
        ...
    def expect_document_start (self, first=False):
        ...
    def expect_first_block_mapping_key (self):
        ...
    def expect_first_block_sequence_item (self):
        ...
    def expect_first_document_start (self):
        ...
    def expect_first_flow_mapping_key (self):
        ...
    def expect_first_flow_sequence_item (self):
        ...
    def expect_flow_mapping (self):
        ...
    def expect_flow_mapping_key (self):
        ...
    def expect_flow_mapping_simple_value (self):
        ...
    def expect_flow_mapping_value (self):
        ...
    def expect_flow_sequence (self):
        ...
    def expect_flow_sequence_item (self):
        ...
    def expect_node (self, root=False, sequence=False, mapping=False, simple_key=False):
        ...
    def expect_nothing (self):
        ...
    def expect_scalar (self):
        ...
    def expect_stream_start (self):
        ...
    def flush_stream (self):
        ...
    def increase_indent (self, flow=False, indentless=False):
        ...
    def need_events (self, count):
        ...
    def need_more_events (self):
        ...
    def prepare_anchor (self, anchor):
        ...
    def prepare_tag (self, tag):
        ...
    def prepare_tag_handle (self, handle):
        ...
    def prepare_tag_prefix (self, prefix):
        ...
    def prepare_version (self, version):
        ...
    def process_anchor (self, indicator):
        ...
    def process_scalar (self):
        ...
    def process_tag (self):
        ...
    def write_double_quoted (self, text, split=True):
        ...
    def write_folded (self, text):
        ...
    def write_indent (self):
        ...
    def write_indicator (self, indicator, need_whitespace, whitespace=False, indention=False):
        ...
    def write_line_break (self, data=None):
        ...
    def write_literal (self, text):
        ...
    def write_plain (self, text, split=True):
        ...
    def write_single_quoted (self, text, split=True):
        ...
    def write_stream_end (self):
        ...
    def write_stream_start (self):
        ...
    def write_tag_directive (self, handle_text, prefix_text):
        ...
    def write_version_directive (self, version_text):
        ...
class EmitterError(YAMLError):
    """Common base class for all non-exit exceptions."""
class ScalarAnalysis(object):
    """class ScalarAnalysis"""
    def __init__ (self, scalar, empty, multiline, allow_flow_plain, allow_block_plain, allow_single_quoted, allow_double_quoted, allow_block):
        """Initialize self.  See help(type(self)) for accurate signature."""
