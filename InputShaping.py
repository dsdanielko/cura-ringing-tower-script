import json
import re

from ..Script import Script


class InputShaping(Script):
    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return json.dumps({
            'name': 'Input Shaping',
            'key': 'Input Shaping',
            'metadata': {},
            'version': 2,
            'settings': {
                "gcode": {
                    "label": "Motion planning type",
                    "description": "Use either M593 (ZV input shaping) or M493 (Fixed-time motion)",
                    "type": "enum",
                    "options": {
                        "is": "M593 (ZV Input Shaping)",
                        "ftm": "M493 (Fixed-Time Motion)"
                    },
                    "default_value": "is"
                },
                'start_f': {
                    'label': 'Start frequency',
                    'description': 'Ringing compensation frequency sweep start value',
                    'unit': 'Hz',
                    'type': 'int',
                    'default_value': 15
                },
                'end_f': {
                    'label': 'End frequency',
                    'description': 'Ringing compensation frequency sweep end value',
                    'unit': 'Hz',
                    'type': 'int',
                    'default_value': 60
                }
            }
        })

    def execute(self, data):
        gc = self.getSettingValueByKey('gcode')
        start_hz = self.getSettingValueByKey('start_f')
        end_hz = self.getSettingValueByKey('end_f')

        for i, layer in enumerate(data):
            lines = layer.split('\n')
            for j, line in enumerate(lines):
                if line.startswith(';LAYER:'):
                    layer = float(line.strip(';LAYER:'))
                    hz = 0 if layer < 2 else start_hz + (end_hz-start_hz) * (layer - 2) / 297
                    if gc == 'ftm':
                        if layer == 0:
                            lines[j] += '\n;TYPE:INPUTSHAPING\nM493 S11 D0 ;Enable ZVD Input Shaping'
                        lines[j] += '\n;TYPE:INPUTSHAPING\nM493 A%f ;(Hz) X Input Shaping Test' % hz
                        lines[j] += '\nM493 B%f ;(Hz) Y Input Shaping Test' % hz
                    if gc == 'is':
                        lines[j] += '\n;TYPE:INPUTSHAPING\nM593 F%f ;(Hz) Input Shaping Test' % hz
            data[i] = '\n'.join(lines)

        return data
