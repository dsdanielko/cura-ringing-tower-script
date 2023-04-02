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
                'start_f': {
                    'label': 'Start frequency',
                    'description': 'Frequency sweep start value',
                    'unit': 'Hz',
                    'type': 'int',
                    'default_value': 15
                },
                'end_f': {
                    'label': 'End frequency',
                    'description': 'Frequency sweep end value',
                    'unit': 'Hz',
                    'type': 'int',
                    'default_value': 60
                }
            }
        })

    def execute(self, data):
        start_hz = self.getSettingValueByKey('start_f')
        end_hz = self.getSettingValueByKey('end_f')
        start_layer = self.getSettingValueByKey('start_l')

        for i, layer in enumerate(data):
            lines = layer.split('\n')
            for j, line in enumerate(lines):
                if line.startswith(';LAYER:'):
                    layer = float(line.strip(';LAYER:'))
                    hz = 0 if layer < 2 else start_hz + (end_hz-start_hz) * (layer - 2) / 297
                    lines[j] += '\n;TYPE:INPUTSHAPING\nM593 F%f' % hz
            data[i] = '\n'.join(lines)

        return data
