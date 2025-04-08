import os
from concurrent.futures import as_completed, ThreadPoolExecutor
from dataclasses import dataclass
from datetime import datetime
from threading import Lock
from time import time

import ffmpeg

TARGET_SIZE_MB = 8


@dataclass(frozen=True)
class Job:
    input_path: str
    output_path: str
    output_format: str


class JobService:

    def __init__(self):
        self.busy = False
        self.executor = ThreadPoolExecutor(max_workers=2)
        self.total_tasks = 0
        self.completed_tasks = 0
        self.failed_tasks = []
        self.lock = Lock()

    def get_video_files(self, os_path: str) -> list[str]:
        files = []

        if not os.path.isdir(os_path):
            return files

        for root, _, filenames in os.walk(os_path):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                files.append(file_path)

        return files

    def process(self, job: Job):
        print("processing job")

        if self.busy:
            return

        self.busy = True
        self.completed_tasks = 0
        self.total_tasks = 0

        files = self.get_video_files(job.input_path)
        futures = {}

        print("starting futures...")
        start = time()

        for file in files:
            filename, extension = os.path.splitext(file)
            creation_time = os.path.getctime(file)
            creation_date = datetime.fromtimestamp(creation_time).strftime('%d-%m-%Y %H-%M')

            formatted_name = (job.output_format
                              .replace("%file%", filename)
                              .replace("%ext%", extension.lstrip('.'))
                              .replace("%date%", creation_date)
                              )
            final_name = os.path.basename(formatted_name)
            output_path = os.path.join(job.output_path, final_name)

            future = self.executor.submit(_process_file, file, output_path)
            futures[future] = file

        print("found " + str(len(futures)) + " files!")
        print("starting tasks...")

        self.total_tasks += len(futures)

        for future in as_completed(futures.keys()):
            file = futures[future]
            filename = os.path.basename(file)
            with self.lock:
                self.completed_tasks += 1
            try:
                future.result()
                print(f"Successfully processed video ({self.completed_tasks}/{self.total_tasks})")
            except Exception as e:
                print(f"Failed to process video ({self.completed_tasks}/{self.total_tasks}), error: {e}")
                self.failed_tasks.append(file)
                pass

        end = time()
        print(f"Took {end - start:.2f} seconds")

        if len(self.failed_tasks) > 0:
            print("Failed files:")
            for file in self.failed_tasks:
                filename = os.path.basename(file)
                print(f"- {filename}")



def _process_file(file: str, output_file: str):
    target_size_bytes = TARGET_SIZE_MB * 1024 * 1024

    probe = ffmpeg.probe(file)
    duration = float(probe['format']['duration'])
    bitrate = int((target_size_bytes * 8) / duration)

    (
        ffmpeg
        .input(file)
        .output(
            output_file,
            **{
                'b:v': f'{bitrate}',
                'bufsize': f'{bitrate}',
                'maxrate': f'{bitrate}',
                'preset': 'medium',
                'c:v': 'libx264',
                'c:a': 'aac',
                'movflags': '+faststart'
            }
        )
        .overwrite_output()
        .run(quiet=True, capture_stdout=True, capture_stderr=True)
    )

    return output_file
