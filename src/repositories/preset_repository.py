
from model.preset import Preset

class PresetRepository:

    def __init__(self):
        self._presets = {}

    def put(self, preset_name: str, preset: Preset):
        self._presets[preset_name] = preset

    def remove(self, preset_name: str):
        del self._presets[preset_name]

    def get(self, preset_name: str):
        return self._presets[preset_name]

    def all(self):
        return self._presets.values()