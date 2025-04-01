import os
from time import sleep

from model.jobs import Job
from services.preset_service import PresetService
from concurrent.futures import ThreadPoolExecutor, as_completed

class JobService:

    def __init__(self):
        self.busy = False
        self.preset_service = PresetService()
        self.executor = ThreadPoolExecutor(max_workers=4 or os.cpu_count())

    def get_video_files(self, os_path: str) -> list[str]:
        files = []

        if not os.path.isdir(os_path):
            return files

        for root, _, filenames in os.walk(os_path):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                files.append(file_path)

    def process(self, job: Job):
        if self.busy:
            return

        self.busy = True

        files = self.get_video_files(job.path)
        futures = {}

        for file in files:
            future = self.executor.submit(self._process_file, file)
            futures[future] = file

        for future in as_completed(futures):
            file = futures[future]
            try:
                result = future.result()
                print(f"Successfully processed {file}")
            except Exception as e:
                print(f"Failed to process: {str(file)}")


    def progress(self):

        pass

    def _process_file(self, file: str):
        sleep(500)
        pass
