# Copyright (C) Eduardo Araújo AKA Edu-MX < diaseduardo139@gmail.com

import globalPluginHandler
import api
import textInfos
import ui

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


text = Text()
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def script_Char(self, gesture):
        selected = text.selected_text()
        ui.message(selected)


    __gestures = {
        'kb:NVDA+W': 'Char'
    }