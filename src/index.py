from model.jobs import Job
from services.job_service import JobService

CLI_MODE = True

def main():

    service = JobService()

    path = "/home/videos"
    output = "/home/converted"
    preset = "test"
    output_format = "test.mp4"
    job = Job(path, output, preset, output_format)

    service.process(job)

    pass


if __name__ == '__main__':
    main()