from sbs_utils.yaml.tokens import AliasToken
from sbs_utils.yaml.tokens import AnchorToken
from sbs_utils.yaml.tokens import BlockEndToken
from sbs_utils.yaml.tokens import BlockEntryToken
from sbs_utils.yaml.tokens import BlockMappingStartToken
from sbs_utils.yaml.tokens import BlockSequenceStartToken
from sbs_utils.yaml.tokens import DirectiveToken
from sbs_utils.yaml.tokens import DocumentEndToken
from sbs_utils.yaml.tokens import DocumentStartToken
from sbs_utils.yaml.tokens import FlowEntryToken
from sbs_utils.yaml.tokens import FlowMappingEndToken
from sbs_utils.yaml.tokens import FlowMappingStartToken
from sbs_utils.yaml.tokens import FlowSequenceEndToken
from sbs_utils.yaml.tokens import FlowSequenceStartToken
from sbs_utils.yaml.tokens import KeyToken
from sbs_utils.yaml.tokens import ScalarToken
from sbs_utils.yaml.tokens import StreamEndToken
from sbs_utils.yaml.tokens import StreamStartToken
from sbs_utils.yaml.tokens import TagToken
from sbs_utils.yaml.tokens import Token
from sbs_utils.yaml.tokens import ValueToken
from sbs_utils.yaml.error import MarkedYAMLError
class Scanner(object):
    """class Scanner"""
    def __init__ (self):
        """Initialize the scanner."""
    def add_indent (self, column):
        ...
    def check_block_entry (self):
        ...
    def check_directive (self):
        ...
    def check_document_end (self):
        ...
    def check_document_start (self):
        ...
    def check_key (self):
        ...
    def check_plain (self):
        ...
    def check_token (self, *choices):
        ...
    def check_value (self):
        ...
    def fetch_alias (self):
        ...
    def fetch_anchor (self):
        ...
    def fetch_block_entry (self):
        ...
    def fetch_block_scalar (self, style):
        ...
    def fetch_directive (self):
        ...
    def fetch_document_end (self):
        ...
    def fetch_document_indicator (self, TokenClass):
        ...
    def fetch_document_start (self):
        ...
    def fetch_double (self):
        ...
    def fetch_flow_collection_end (self, TokenClass):
        ...
    def fetch_flow_collection_start (self, TokenClass):
        ...
    def fetch_flow_entry (self):
        ...
    def fetch_flow_mapping_end (self):
        ...
    def fetch_flow_mapping_start (self):
        ...
    def fetch_flow_scalar (self, style):
        ...
    def fetch_flow_sequence_end (self):
        ...
    def fetch_flow_sequence_start (self):
        ...
    def fetch_folded (self):
        ...
    def fetch_key (self):
        ...
    def fetch_literal (self):
        ...
    def fetch_more_tokens (self):
        ...
    def fetch_plain (self):
        ...
    def fetch_single (self):
        ...
    def fetch_stream_end (self):
        ...
    def fetch_stream_start (self):
        ...
    def fetch_tag (self):
        ...
    def fetch_value (self):
        ...
    def get_token (self):
        ...
    def need_more_tokens (self):
        ...
    def next_possible_simple_key (self):
        ...
    def peek_token (self):
        ...
    def remove_possible_simple_key (self):
        ...
    def save_possible_simple_key (self):
        ...
    def scan_anchor (self, TokenClass):
        ...
    def scan_block_scalar (self, style):
        ...
    def scan_block_scalar_breaks (self, indent):
        ...
    def scan_block_scalar_ignored_line (self, start_mark):
        ...
    def scan_block_scalar_indentation (self):
        ...
    def scan_block_scalar_indicators (self, start_mark):
        ...
    def scan_directive (self):
        ...
    def scan_directive_ignored_line (self, start_mark):
        ...
    def scan_directive_name (self, start_mark):
        ...
    def scan_flow_scalar (self, style):
        ...
    def scan_flow_scalar_breaks (self, double, start_mark):
        ...
    def scan_flow_scalar_non_spaces (self, double, start_mark):
        ...
    def scan_flow_scalar_spaces (self, double, start_mark):
        ...
    def scan_line_break (self):
        ...
    def scan_plain (self):
        ...
    def scan_plain_spaces (self, indent, start_mark):
        ...
    def scan_tag (self):
        ...
    def scan_tag_directive_handle (self, start_mark):
        ...
    def scan_tag_directive_prefix (self, start_mark):
        ...
    def scan_tag_directive_value (self, start_mark):
        ...
    def scan_tag_handle (self, name, start_mark):
        ...
    def scan_tag_uri (self, name, start_mark):
        ...
    def scan_to_next_token (self):
        ...
    def scan_uri_escapes (self, name, start_mark):
        ...
    def scan_yaml_directive_number (self, start_mark):
        ...
    def scan_yaml_directive_value (self, start_mark):
        ...
    def stale_possible_simple_keys (self):
        ...
    def unwind_indent (self, column):
        ...
class ScannerError(MarkedYAMLError):
    """Common base class for all non-exit exceptions."""
class SimpleKey(object):
    """class SimpleKey"""
    def __init__ (self, token_number, required, index, line, column, mark):
        """Initialize self.  See help(type(self)) for accurate signature."""
