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

    def text_to_html(self, text):
        text = text.strip() \
        .split("\n")
        new_text = [line for line in text if not self.line_is_null(line)]
        columns = [column.strip() for column in new_text[0].split("|")]
        new_text.pop(0)
        columns.pop(-1)
        columns.pop(0)
        html_columns = [f"<th>{column}</th>\n" for column in columns]
        html_fields = []
        for text in new_text:
            trusted_fields = [field.strip() for field in text.split("|")]
            trusted_fields.pop(-1)
            trusted_fields.pop(0)
            trusted_fields = [f"<td>{field}</td>\n" for field in trusted_fields]
            refined_fields = f'''
            <tr>
            {"".join(trusted_fields)}
            </tr>\n
            '''
            html_fields.append(refined_fields)


        html = f'''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accessible Output Spark 🎲</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Output Spark</h1>
        <table class="table table-striped table-bordered">
            <thead>
                <tr>
                    {"".join(html_columns)}
                </tr>
            </thead>
            <tbody>
            {"".join(html_fields)}
            </tbody>
        </table>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
        '''
        return html


text = Text()
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def script_Char(self, gesture):
        selected = text.selected_text()
        webpage = text.text_to_html(selected)
        



    __gestures = {
        'kb:NVDA+W': 'Char'
    }