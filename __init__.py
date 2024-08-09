# Copyright (C) Eduardo Araújo AKA Edu-MX < diaseduardo139@gmail.com
import re
import globalPluginHandler
import api
import textInfos
import ui

pattern = r"^\+(\-+\+)+$"

class Text:
    def __init__(self):
        self.recent_text_view = ''


    def selected_text(self):
        obj=api.getCaretObject()
        try:
            info=obj.makeTextInfo(textInfos.POSITION_SELECTION)
            if info or not info.isCollapsed:
                return info.text
        except (RuntimeError, NotImplementedError):
            return None

        def line_is_null(self, line):
            return re.match(pattern, line) is not None

        def text_to_dict(self, text):
            # tratamento de string
            new_text = text.strip()


-


text = Text()
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def script_Char(self, gesture):
        selected = text.selected_text()
        ui.message(text.text_to_dict(selected))


    __gestures = {
        'kb:NVDA+W': 'Char'
    }