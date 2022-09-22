from .quest import Quest
from .sbsquest import Target, Tell, Comms, Button, Near
from .questrunner import QuestRunner, PollResults, QuestRuntimeNode,  QuestAsync
import sbs
from ..spaceobject import SpaceObject
from ..consoledispatcher import ConsoleDispatcher
from ..gui import Gui
from .errorpage import ErrorPage

import traceback

class TellRunner(QuestRuntimeNode):
    def enter(self, quest:Quest, thread:QuestAsync, node: Tell):
        to_so:SpaceObject = thread.inputs.get(node.to_tag)
        self.face = ""
        self.title = ""
        if to_so:
            self.to_id = to_so.get_id()
        else:
            thread.runtime_error("Tell has invalid TO")            
        from_so:SpaceObject = thread.inputs.get(node.from_tag)
        if from_so:
            self.from_id = from_so.get_id()
            self.title = from_so.comm_id(thread.main.sim)
        else:
            thread.runtime_error("Tell has invalid from")            

    def poll(self, quest:Quest, thread:QuestAsync, node: Tell):

        if self.to_id and self.from_id:
            msg = node.message.format(**thread.get_symbols())
            sbs.send_comms_message_to_player_ship(
                self.to_id,
                self.from_id,
                "white",
                self.face, self.title, msg)
            return PollResults.OK_ADVANCE_TRUE
        else:
            PollResults.OK_ADVANCE_FALSE

class CommsRunner(QuestRuntimeNode):
    def enter(self, quest:Quest, thread:QuestAsync, node: Comms):
        self.timeout = node.minutes*60+node.seconds
        if self.timeout == 0:
            self.timeout = None

        self.tag = None
        self.buttons = node.buttons
        self.button = None
        self.thread = thread
        self.color = node.color if node.color else "white"

        to_so:SpaceObject = thread.inputs.get(node.to_tag)
        if to_so:
            self.to_id = to_so.get_id()
        from_so:SpaceObject = thread.inputs.get(node.from_tag)
        if from_so:
            self.from_id = from_so.get_id()
            self.comms_id = from_so.comm_id(thread.main.sim)
            ConsoleDispatcher.add_select(self.from_id, 'comms_targetUID', self.comms_selected)
            ConsoleDispatcher.add_message(self.from_id, 'comms_targetUID', self.comms_message)
            self.set_buttons(self.from_id, self.to_id)
            # from_so.face_desc

    def comms_selected(self, sim, an_id, event):
        to_id = event.origin_id
        from_id = event.selected_id
        self.set_buttons(from_id, to_id)

    def set_buttons(self, from_id, to_id):
        # check to see if the from ship still exists
        if from_id is not None:
            sbs.send_comms_selection_info(to_id, "", self.color, self.comms_id)
            for i, button in enumerate(self.buttons):
                value = True
                color = "blue" if button.color is None else button.color
                if button.code is not None:
                    value = self.thread.eval_code(button.code)
                if value and button.should_present((from_id, to_id)):
                    sbs.send_comms_button_info(to_id, color, button.message, f"{i}")

    def comms_message(self, sim, message, an_id, event):
        ### These are opposite from selected??
        from_id = event.origin_id
        to_id = event.selected_id

        self.button = int(event.sub_tag)
        this_button: Button = self.buttons[self.button]
        this_button.visit((from_id, to_id))


    def leave(self, quest:Quest, thread:QuestAsync, node: Comms):
        ConsoleDispatcher.remove_select(self.from_id, 'comms_targetUID')
        ConsoleDispatcher.remove_message(self.from_id, 'comms_targetUID')
        sbs.send_comms_selection_info(self.to_id, "", self.color, self.comms_id)
        

    def poll(self, quest:Quest, thread:QuestAsync, node: Comms):

        if len(node.buttons)==0:
            # clear the comms buttons
            return PollResults.OK_ADVANCE_TRUE

        if self.button is not None:
            jump = self.buttons[self.button].jump 
            
            thread.jump(jump)
            return PollResults.OK_JUMP

        if self.timeout:
            self.timeout -= 1
            if self.timeout <= 0:
                thread.jump(node.time_jump)
                return PollResults.OK_JUMP
            else:
                PollResults.OK_ADVANCE_FALSE

        return PollResults.OK_RUN_AGAIN

class TargetRunner(QuestRuntimeNode):
    def enter(self, quest:Quest, thread:QuestAsync, node: Target):
        to_so:SpaceObject = thread.inputs.get(node.to_tag)
        self.to_id = to_so.get_id() if to_so else None
        from_so:SpaceObject = thread.inputs.get(node.from_tag)
        self.from_id = from_so.get_id() if from_so else None


    def poll(self, quest, thread, node:Target):
        if self.to_id:
            obj:SpaceObject = SpaceObject.get(self.from_id)
            obj.target(thread.main.sim, self.to_id, not node.approach)
        else:
            obj:SpaceObject = SpaceObject.get(self.from_id)
            obj.clear_target(thread.main.sim)

        return PollResults.OK_ADVANCE_TRUE


class NearRunner(QuestRuntimeNode):
    def enter(self, quest:Quest, thread:QuestAsync, node: Near):
        self.timeout = node.minutes*60+node.seconds
        if self.timeout==0:
            self.timeout = None
        self.tag = None

        to_so:SpaceObject = thread.inputs.get(node.to_tag)
        if to_so:
            self.to_id = to_so.get_id()
        from_so:SpaceObject = thread.inputs.get(node.from_tag)
        if from_so:
            self.from_id = from_so.get_id()

    def poll(self, quest:Quest, thread:QuestAsync, node: Near):
        # Need to check the distance
        dist = sbs.distance_id(self.to_id, self.from_id)
        if dist <= node.distance:
            if node.jump:
                thread.jump(node.jump)
                return PollResults.OK_JUMP
            else:
                return PollResults.OK_ADVANCE_TRUE

        if self.timeout is not None:
            self.timeout -= 1
            if self.timeout <= 0:
                thread.jump(node.time_jump)
                return PollResults.OK_JUMP
            else:
                PollResults.OK_ADVANCE_FALSE

        return PollResults.OK_RUN_AGAIN


over =     {
        "Comms": CommsRunner,
        "Tell": TellRunner,
        "Near": NearRunner,
        "Target": TargetRunner
    }

class SbsQuestRunner(QuestRunner):
    def __init__(self, quest: Quest, overrides=None):
        if overrides:
            super().__init__(quest, over|overrides)
        else:
            super().__init__(quest,  over)

    def run(self, sim, label="main", inputs=None):
        self.sim = sim
        inputs = inputs if inputs else {}
        super().start_thread( label, inputs)

    def tick(self, sim):
        self.sim = sim
        super().tick()

    def runtime_error(self, message):
        sbs.pause_sim()
        message += traceback.format_exc()
        Gui.push(self.sim, 0, ErrorPage(message))

