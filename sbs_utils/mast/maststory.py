from .mast import IF_EXP_REGEX, Mast, MastNode, PY_EXP_REGEX, OPT_COLOR, TIMEOUT_REGEX, BLOCK_START
from .mastsbs import MastSbs, EndAwait
import re
from .parsers import StyleDefinition
import logging

STYLE_REF_RULE = r"""(\s+style\s*=\s*((?P<style_name>\w+)|((?P<style_q>['"]{3}|["'])(?P<style>.*?)(?P=style_q))))"""
OPT_STYLE_REF_RULE = STYLE_REF_RULE+"""?"""


class Row(MastNode):
    rule = re.compile(r"""row"""+OPT_STYLE_REF_RULE)
    def __init__(self, style_name=None, style=None, style_q=None, loc=None):
        self.loc = loc
        self.style_def = None
        if style is not None:
            self.style_def = StyleDefinition.parse(style)
        elif style_name is not None:
            self.style_def = StyleDefinition.styles.get(style_name)
    
class Refresh(MastNode):
    rule = re.compile(r"""refresh\s*(?P<label>\w+)""")
    def __init__(self, label, loc=None):
        self.loc = loc
        self.label = label

    
class Hole(MastNode):
    rule = re.compile(r"""hole""")
    def __init__(self,  loc=None):
        self.loc = loc


class Text(MastNode):
    rule = re.compile(r"""((['"]{3,})(\n)?(?P<message>[\s\S]+?)(\n)?(['"]{3,}))"""+OPT_STYLE_REF_RULE+IF_EXP_REGEX)
    def __init__(self, message, if_exp, style_name=None, style=None, style_q=None, loc=None):
        self.loc = loc
        self.message = self.compile_formatted_string(message)
        if if_exp is not None:
            if_exp = if_exp.lstrip()
            self.code = compile(if_exp, "<string>", "eval")
        else:
            self.code = None
        self.style_def = None
        if style is not None:
            self.style_def = StyleDefinition.parse(style)
        elif style_name is not None:
            self.style_def = StyleDefinition.styles.get(style_name)

class AppendText(MastNode):
    rule = re.compile(r"""(([\^]{3,})(\n)?(?P<message>[\s\S]+?)(\n)?([\^]{3,}))"""+IF_EXP_REGEX)
    def __init__(self, message, if_exp, loc=None):
        self.loc = loc
        #TODO: This needs to be smart with the 'text: ' stuff
        self.message = self.compile_formatted_string(message)
        if if_exp is not None:
            if_exp = if_exp.lstrip()
            self.code = compile(if_exp, "<string>", "eval")
        else:
            self.code = None


class Face(MastNode):
    rule = re.compile(r"""face\s*(((['"]{3}|["'])(?P<face>[\s\S]+?)\3)|(?P<face_exp>[ \t\S]+)?)"""+OPT_STYLE_REF_RULE)
    def __init__(self, face=None, face_exp=None, style_name=None, style=None, style_q=None, loc=None):
        self.loc = loc
        self.face = face
        if face_exp:
            face_exp = face_exp.lstrip()
            self.code = compile(face_exp, "<string>", "eval")
        else:
            self.code = None
        self.style_def = None
        if style is not None:
            self.style_def = StyleDefinition.parse(style)
        elif style_name is not None:
            self.style_def = StyleDefinition.styles.get(style_name)

class Ship(MastNode):
    rule = re.compile(r"""ship\s+(?P<q>['"]{3}|["'])(?P<ship>[\s\S]+?)(?P=q)"""+OPT_STYLE_REF_RULE)
    def __init__(self, ship=None, q=None, style_name=None, style=None, style_q=None, loc=None):
        self.loc = loc
        self.ship= self.compile_formatted_string(ship)
        self.style_def = None
        if style is not None:
            self.style_def = StyleDefinition.parse(style)
        elif style_name is not None:
            self.style_def = StyleDefinition.styles.get(style_name)

class GuiContent(MastNode):
    rule = re.compile(r"""gui\s+(?P<gui>page|control)\s+(?P<var>\w+)\s+(?P<exp>("""+PY_EXP_REGEX+'|.*))'+OPT_STYLE_REF_RULE)
    def __init__(self, gui=None, var=None, exp=None, py=None, style_name=None, style=None, style_q=None, loc=None):
        self.loc = loc
        self.gui= gui
        self.var= var
        exp = exp.lstrip()
        if py:
            exp = exp[2:-2]
            exp = exp.strip()
        self.code = compile(exp, "<string>", "eval")
        self.style_def = None
        if style is not None:
            self.style_def = StyleDefinition.parse(style)
        elif style_name is not None:
            self.style_def = StyleDefinition.styles.get(style_name)


class Blank(MastNode):
    rule = re.compile(r"""blank"""+OPT_STYLE_REF_RULE)
    def __init__(self, style_name=None, style=None, style_q=None, loc=None):
        self.loc = loc
        self.style_def = None
        if style is not None:
            self.style_def = StyleDefinition.parse(style)
        elif style_name is not None:
            self.style_def = StyleDefinition.styles.get(style_name)




class Section(MastNode):
    rule = re.compile(r"""section"""+OPT_STYLE_REF_RULE)
    def __init__(self, style_name=None, style=None, style_q=None, loc=None):
        self.loc = loc
        self.style_def = None
        if style is not None:
            self.style_def = StyleDefinition.parse(style)
        elif style_name is not None:
            self.style_def = StyleDefinition.styles.get(style_name)

class Clickable(MastNode):
    rule = re.compile(r"((section"+STYLE_REF_RULE+r"""\s*clickable\s*(?P<q>['"]{3}|["'])(?P<message>.*?)(?P=q)(\s*data\s*=\s*(?P<data>"""+PY_EXP_REGEX+r"""))?)\s*"""+BLOCK_START+r")|(?P<end>end_clickable)")
    stack = []
    def __init__(self, message, q, data=None, py=None, end=None, style_name=None, style=None, style_q=None, loc=None):
        #self.message = message
        self.loc = loc
        if message: #Message is none for end
            self.message = self.compile_formatted_string(message)
        self.end_node = None
        self.is_end = False
        
        if data:
            data = data.lstrip()
            if py:
                data = data[2:-2]
                data= data.strip()
            self.data_code = compile(data, "<string>", "eval")
        else:
            self.data_code = None

        if end is not None:
            Clickable.stack[-1].end_node = self
            self.is_end = True
            Clickable.stack.pop()
        else:
            Clickable.stack.append(self)

        
        self.style_def = None
        if style is not None:
            self.style_def = StyleDefinition.parse(style)
        elif style_name is not None:
            self.style_def = StyleDefinition.styles.get(style_name)
        
    @classmethod
    def dd_parse(cls, lines):
        mo = cls.rule.match(lines)

        if mo:
            span = mo.span()
            data = mo.groupdict()
            found = lines[span[0]:span[1]]
            return Mast.ParseData(span[0], span[1], data)
        else:
            return None

class Style(MastNode):
    rule = re.compile(r"""style\s+(?P<name>\.?\w+)\s*=\s*(?P<q>['"]{3}|["'])(?P<style>.*?)(?P=q)""")
    def __init__(self, name, style=None, q=None,loc=None):
        self.loc = loc
        style_def = StyleDefinition.parse(style)
        StyleDefinition.styles[name] = style_def

class AwaitGui(MastNode):
    rule = re.compile(r"await\s+gui"+TIMEOUT_REGEX)
    def __init__(self, assign=None,minutes=None, seconds=None, loc=None):
        self.loc = loc
        self.assign = assign
        self.seconds = 0 if  seconds is None else int(seconds)
        self.minutes = 0 if  minutes is None else int(minutes)
                
        self.buttons = []
        self.active = False
        self.nothing = False
        # just await gui
   
class Choose(MastNode):
    #d=r"(\s*timeout"+MIN_SECONDS_REGEX + r")?"
    #test = r"""await gui((((\s*(?P<choice>choice)(\s*set\s*(?P<assign>\w+))?)?):)?"""
    rule = re.compile(r"(await choice(\s*set\s*(?P<assign>\w+))?"+OPT_STYLE_REF_RULE+ r"\s*"+BLOCK_START+r")")
    def __init__(self, assign=None, style_name=None, style=None, style_q=None, loc=None):
        self.loc = loc
        self.assign = assign
        self.seconds = 0
        self.minutes = 0
                
        self.buttons = []
        self.active = False

        self.timeout_label = None
        self.fail_label = None
        self.end_await_node = None
        EndAwait.stack.append(self)

        self.style_def = None
        if style is not None:
            self.style_def = StyleDefinition.parse(style)
        elif style_name is not None:
            self.style_def = StyleDefinition.styles.get(style_name)

class ButtonControl(MastNode):
    rule = re.compile(r"""((button\s+(?P<q>['"]{3}|["'])(?P<message>[\s\S]+?)(?P=q))(\s*data\s*=\s*(?P<data>"""+PY_EXP_REGEX+r"""))?"""+OPT_STYLE_REF_RULE+IF_EXP_REGEX+r"\s*"+BLOCK_START+")|(?P<end>end_button)")
    stack = []
    def __init__(self, message, q, data=None, py=None, if_exp=None, end=None,style_name=None, style=None, style_q=None, loc=None):
        #self.message = message
        self.loc = loc
        if message: #Message is none for end
            self.message = self.compile_formatted_string(message)
        self.end_node = None
        self.is_end = False
    
        if if_exp:
            if_exp = if_exp.lstrip()
            self.code = compile(if_exp, "<string>", "eval")
        else:
            self.code = None

        if data:
            data = data.lstrip()
            if py:
                data = data[2:-2]
                data= data.strip()
            self.data_code = compile(data, "<string>", "eval")
        else:
            self.data_code = None


        if end is not None:
            ButtonControl.stack[-1].end_node = self
            self.is_end = True
            ButtonControl.stack.pop()
        else:
            ButtonControl.stack.append(self)

        self.style_def = None
        if style is not None:
            self.style_def = StyleDefinition.parse(style)
        elif style_name is not None:
            self.style_def = StyleDefinition.styles.get(style_name)



FLOAT_VALUE_REGEX = r"[+-]?([0-9]*[.])?[0-9]+"

class SliderControl(MastNode):
    rule = re.compile(r"""(?P<is_int>intslider|slider|scrollbar)"""+
        r"""\s+(?P<var>\w+)"""+
        r"""\s+(?P<q>['"]{3}|["'])(?P<props>[\s\S]+?)(?P=q)"""+
        OPT_STYLE_REF_RULE)
    def __init__(self, is_int=None, var=None, q=None, props=None, style_name=None, style=None, style_q=None,loc=None):
        self.loc = loc
        self.var= var
        self.is_int = (is_int=="intslider")
        self.is_scroll = (is_int=="scrollbar")
        self.props = self.compile_formatted_string(props)
        
        self.style_def = None
        if style is not None:
            self.style_def = StyleDefinition.parse(style)
        elif style_name is not None:
            self.style_def = StyleDefinition.styles.get(style_name)
    
class CheckboxControl(MastNode):
    rule = re.compile(r"""checkbox\s+(?P<var>[ \t\S]+)\s+(?P<q>['"]{3}|["'])(?P<message>[\s\S]+?)(?P=q)"""+OPT_STYLE_REF_RULE)
    def __init__(self, var=None, message=None, q=None, style_name=None, style=None, style_q=None, loc=None):
        self.loc = loc
        self.var= var
        #self.message = message
        self.message = self.compile_formatted_string(message)

        self.style_def = None
        if style is not None:
            self.style_def = StyleDefinition.parse(style)
        elif style_name is not None:
            self.style_def = StyleDefinition.styles.get(style_name)

class RadioControl(MastNode):
    rule = re.compile(r"""(?P<radio>radio|vradio)\s+(?P<var>[ \t\S]+)\s+(?P<q>['"]{3}|["'])(?P<message>[\s\S]+?)(?P=q)"""+OPT_STYLE_REF_RULE)
    def __init__(self, radio, var=None, message=None, q=None, style_name=None, style=None, style_q=None, loc=None):
        self.loc = loc
        self.vertical = radio == "vradio"
        self.var= var
        self.message = self.compile_formatted_string(message)

        self.style_def = None
        if style is not None:
            self.style_def = StyleDefinition.parse(style)
        elif style_name is not None:
            self.style_def = StyleDefinition.styles.get(style_name)


class RerouteGui(MastNode):
    rule = re.compile(r"""reroute(\s+((?P<gui>server|clients)|(client\s+(?P<var>[_\w][\w]*))))?\s+(?P<label>[_\w][\w]*)""")
    def __init__(self, gui, var=None, label=None, loc=None):
        self.loc = loc
        self.gui = gui
        self.var = var
        self.label = label

        

class TextInputControl(MastNode):
    
    rule = re.compile(r"""input\s+(?P<var>[_\w][\w]*)(\s+(?P<q>['"]{3}|["'])(?P<label>[\s\S]+?)(?P=q))?"""+OPT_STYLE_REF_RULE)
    def __init__(self, var=None, label=None,q=None, style_name=None, style=None, style_q=None, loc=None):
        self.loc = loc
        self.var= var
        #print(f"node {label}")
        self.label = self.compile_formatted_string(label) if label is not None else None
        #print(f"self label {self.label}")

        self.style_def = None
        if style is not None:
            self.style_def = StyleDefinition.parse(style)
        elif style_name is not None:
            self.style_def = StyleDefinition.styles.get(style_name)



class DropdownControl(MastNode):
    
    rule = re.compile(r"""(dropdown\s+(?P<var>[ \t\S]+)\s+(?P<q>['"]{3}|["'])(?P<values>[\s\S]+?)(?P=q)"""+BLOCK_START+""")|(?P<end>end_dropdown)"""+OPT_STYLE_REF_RULE)
    stack = []
    def __init__(self, var=None, values=None, q=None,end=None, style_name=None, style=None, style_q=None, loc=None):
        self.loc = loc
        self.is_end = False
        self.end_node = None
        self.loc = loc
        if end is not None:
            DropdownControl.stack[-1].end_node = self
            self.is_end = True
            DropdownControl.stack.pop()
        else:
            DropdownControl.stack.append(self)
            self.var= var
            self.values = self.compile_formatted_string(values)
        
        self.style_def = None
        if style is not None:
            self.style_def = StyleDefinition.parse(style)
        elif style_name is not None:
            self.style_def = StyleDefinition.styles.get(style_name)

class ImageControl(MastNode):
    rule = re.compile(r"""image\s*(?P<q>['"]{3}|["'])(?P<file>[\s\S]+?)(?P=q)"""+OPT_STYLE_REF_RULE)
    def __init__(self, file, q, style_name=None, style=None, style_q=None, loc=None):
        self.loc = loc
        self.file = self.compile_formatted_string(file)
        
        self.style_def = None
        if style is not None:
            self.style_def = StyleDefinition.parse(style)
        elif style_name is not None:
            self.style_def = StyleDefinition.styles.get(style_name)



class WidgetList(MastNode):
    #rule = re.compile(r'tell\s+(?P<to_tag>\w+)\s+(?P<from_tag>\w+)\s+((['"]{3}|["'])(?P<message>[\s\S]+?)(['"]{3}|["']))')
    #(\s+color\s*["'](?P<color>[ \t\S]+)["'])?
    rule = re.compile(r"""widget_list\s+((?P<clear>clear)|(?P<console>['"]\w+['"])(\s*(?P<q>['"]{3}|["'])(?P<widgets>[\s\S]+?)(?P=q)))""")
    def __init__(self, clear, console, widgets, q, loc=None):
        self.loc = loc
        if clear == "clear":
            self.console = ""
            self.widgets = ""
        else:
            self.console = console
            self.widgets = widgets

class Console(MastNode):
    #rule = re.compile(r'tell\s+(?P<to_tag>\w+)\s+(?P<from_tag>\w+)\s+((['"]{3}|["'])(?P<message>[\s\S]+?)(['"]{3}|["']))')
    #(\s+color\s*["'](?P<color>[ \t\S]+)["'])?
    rule = re.compile(r"""console\s+(?P<console>\w+)""")
    def __init__(self,  console, loc=None):
        self.loc = loc
        self.var = False
        widgets = None
        match console:
            case "helm":
                console =  "normal_helm"
                widgets = "3dview^2dview^helm_movement^throttle^request_dock^shield_control^ship_data^text_waterfall^main_screen_control"
            case "weapons":
                console =  "normal_weap"
                widgets = "2dview^weapon_control^weap_beam_freq^ship_data^shield_control^text_waterfall^main_screen_control"
            case "science":
                console =  "normal_sci"
                widgets = "science_2d_view^ship_data^text_waterfall^science_data^science_sorted_list"
            case "engineering":
                console =  "normal_engi"
                widgets = "ship_internal_view^grid_object_list^grid_face^grid_control^text_waterfall^eng_heat_controls^eng_power_controls^ship_data"
            case "comms":
                console =  "normal_comm"
                widgets = "text_waterfall^comms_waterfall^comms_control^comms_face^comms_sorted_list^ship_data"
            case "mainscreen":
                console =  "normal_main"
                widgets = "3dview^ship_data^text_waterfall"
            case "clear":
                console = ""
                widgets = ""
            case _:
                self.var = True

        self.console = console
        self.widgets = widgets


class MastStory(MastSbs):
    nodes = [
        # sbs specific
        Row,
            Text,
            AppendText,
            Face,
            Ship,
            GuiContent,
            Blank,
            Hole,
            Clickable,
            Section,
            Style,
        Choose,
        AwaitGui,
        ButtonControl,
        RerouteGui,
        SliderControl,
        CheckboxControl,
        RadioControl,
        DropdownControl,
        ImageControl,
        TextInputControl,
        WidgetList,
        Console,
        Refresh
    ] + MastSbs.nodes 
