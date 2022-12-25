from .mast import IF_EXP_REGEX, TIMEOUT_REGEX, OPT_COLOR, Mast, MastNode, EndAwait,BLOCK_START
import re


class Target(MastNode):
    """
    Creates a new 'task' to run in parallel
    """
    rule = re.compile(r"""have\s*(?P<from_tag>[\w\.\[\]]+)\s*(?P<cmd>target|approach)(\s*(?P<to_tag>[\w\.\[\]]+))?""")
    def __init__(self, cmd=None, from_tag=None, to_tag=None, loc=None):
        self.loc = loc
        self.from_tag = from_tag
        self.to_tag = to_tag
        self.approach = cmd=="approach"

        
class Tell(MastNode):
    #rule = re.compile(r'tell\s+(?P<to_tag>\w+)\s+(?P<from_tag>\w+)\s+((['"]{3}|["'])(?P<message>[\s\S]+?)(['"]{3}|["']))')
    rule = re.compile(r"""have\s*(?P<from_tag>\*?\w+)\s+tell\s+(?P<to_tag>\*?\w+)\s+((['"]{3}|["'])(?P<message>[\s\S]+?)\4)"""+OPT_COLOR)
    def __init__(self, to_tag, from_tag, message, color=None, loc=None):
        self.loc = loc
        self.to_tag = to_tag
        self.from_tag = from_tag
        self.message = self.compile_formatted_string(message)
        self.color = color if color is not None else "#fff"

class Broadcast(MastNode):
    #rule = re.compile(r'tell\s+(?P<to_tag>\w+)\s+(?P<from_tag>\w+)\s+((['"]{3}|["'])(?P<message>[\s\S]+?)(['"]{3}|["']))')
    rule = re.compile(r"""have\s*(?P<to_tag>\*?\w+)\s+broadcast\s+(?P<q>['"]{3}|["'])(?P<message>[\s\S]+?)(?P=q)"""+OPT_COLOR)
    def __init__(self, to_tag, message, color=None, q=None,loc=None):
        self.to_tag = to_tag
        self.loc = loc
        self.message = self.compile_formatted_string(message)
        self.color = color if color is not None else "#fff"


class Comms(MastNode):
    rule = re.compile(r"""await\s*(?P<from_tag>\w+)\s*comms\s*(?P<to_tag>\w+)(\s*set\s*(?P<assign>\w+))?(\s+color\s*["'](?P<color>[ \t\S]+)["'])?"""+TIMEOUT_REGEX+'\s*'+BLOCK_START)
    def __init__(self, to_tag, from_tag, assign=None, minutes=None, seconds=None, time_pop=None,time_push="", time_jump="", color="white", loc=None):
        self.loc = loc
        self.to_tag = to_tag
        self.from_tag = from_tag
        self.assign = assign
        self.buttons = []
        self.seconds = 0 if  seconds is None else int(seconds)
        self.minutes = 0 if  minutes is None else int(minutes)
        self.color = color

        self.timeout_label = None
        self.fail_label = None
        self.end_await_node = None
        EndAwait.stack.append(self)

class Button(MastNode):
    rule = re.compile(r"""(?P<button>\*|\+)\s+(?P<q>["'])(?P<message>.+?)(?P=q)"""+OPT_COLOR+IF_EXP_REGEX+r"\s*"+BLOCK_START)
    def __init__(self, button, message,  color, if_exp, q=None, loc=None):
        self.message = self.compile_formatted_string(message)
        self.sticky = (button == '+' or button=="button")
        self.color = color
        self.visited = set() if not self.sticky else None
        self.loc = loc
        self.await_node = EndAwait.stack[-1]
        self.await_node.buttons.append(self)

        if if_exp:
            if_exp = if_exp.lstrip()
            self.code = compile(if_exp, "<string>", "eval")
        else:
            self.code = None

    def visit(self, id_tuple):
        if self.visited is not None:
            self.visited.add(id_tuple)
    
    def been_here(self, id_tuple):
        if self.visited is not None:
            return (id_tuple in self.visited)
        return False

    def should_present(self, id_tuple):
        if self.visited is not None:
            return not id_tuple in self.visited
        return True


class ButtonSet(MastNode):
    rule = re.compile(r"""(button_set\s+use\s+(?P<use>\w+))|(button_set\s*(?P<name>\w+)"""+BLOCK_START+""")|(end_button_set)""")
    lookup = {}
    def __init__(self, use=None, name=None, loc=None):
        self.loc = loc
        self.buttons = []
        self.use = use
        self.end = None
        if use is not None:
            EndAwait.stack[-1].buttons.extend(self.buttons)
        elif name is None:
            EndAwait.stack[-1].end = self
            EndAwait.stack.pop(-1)
        else:
            ButtonSet.lookup[name] = self
            EndAwait.stack.append(self)
    



class Near(MastNode):
    rule = re.compile(r'await\s*(?P<from_tag>\w+)\s+near\s+(?P<to_tag>\w+)\s*(?P<distance>\d+)'+TIMEOUT_REGEX+"\s*"+BLOCK_START)
    def __init__(self, to_tag, from_tag, distance, minutes=None, seconds=None, loc=None):
        self.loc = loc
        self.to_tag = to_tag
        self.from_tag = from_tag
        self.distance = 0 if distance is None else int(distance)
        
        self.seconds = 0 if  seconds is None else int(seconds)
        self.minutes = 0 if  minutes is None else int(minutes)

        self.timeout_label = None
        self.fail_label = None
        self.end_await_node = None
        EndAwait.stack.append(self)
    

class Simulation(MastNode):
    """
    Handle commands to the simulation
    """
    rule = re.compile(r"""simulation\s+(?P<cmd>pause|create|resume)""")
    def __init__(self, cmd=None, loc=None):
        self.loc = loc
        self.cmd = cmd

class Role(MastNode):
    """
    Handle commands to the simulation
    """
    rule = re.compile(r"""have\s+(?P<name>\w+)\s+(?P<cmd>add|remove)\s+(role|roles)\s*(?P<q>["'])(?P<roles>.+?)(?P=q)""")
    def __init__(self, name, roles, cmd=None, q=None, loc=None):
        self.loc = loc
        self.cmd = cmd
        self.name = name
        self.roles = [x.strip() for x in roles.split(',')]

class Find(MastNode):
    """
    
    """
    """ships = find all "Station" near artemis by 700  filter(lambda score: score >= 70)"""
    rule = re.compile(r"""(?P<assign>\w+)\s*=\s*all\s*(?P<q>["'])(?P<role>.+?)(?P=q)(\s*near\s+(?P<name>\w+)(\s+by\s+(?P<max>\d+))?)?(\s+filter\s*\((?P<the_filter>.*\)))?(\s*include\s+(?P<inc_dist>distance))?""")
    def __init__(self, assign, name, role,max, the_filter, inc_dist, q=None, loc=None):
        self.loc = loc
        self.all = all is not None
        self.name = name
        self.assign = assign
        self.role = role.strip()
        self.max = None if max is None else int(max)
        self.the_filter = the_filter
        self.inc_dist = inc_dist

class Closest(MastNode):
    """
    
    """
    """ships = find all "Station" near artemis by 700  filter(lambda score: score >= 70)"""
    rule = re.compile(r"""(?P<assign>\w+)\s*=\s*closest\s*(?P<q>["'])(?P<role>.+?)(?P=q)(\s*near\s+(?P<name>\w+)(\s+by\s+(?P<max>\d+))?)?(\s+filter\s*\((?P<the_filter>.*\)))?""")
    def __init__(self, assign, name, role,max, the_filter, q=None, loc=None):
        self.loc = loc
        self.all = all is not None
        self.name = name
        self.assign = assign
        self.role = role.strip()
        self.max = None if max is None else int(max)
        self.the_filter = the_filter



class MastSbs(Mast):
    nodes =  [
        # sbs specific
        Target,
        Tell,
        Broadcast,
        Comms,
        Button,
        ButtonSet,
        Near,
        Simulation,
        Role,
        Find,
        Closest
    ] + Mast.nodes 
    