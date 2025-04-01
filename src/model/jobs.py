class Job:

    def __init__(self, path: str, output_path: str, preset:str, output_format: str):
        self.path = path
        self.output_path = output_path
        self.preset = preset
        self.output_format = output_format