from compression.jobs import Job, JobService

CLI_MODE = True


def main():
    service = JobService()
    job = Job(
        input_path="/mnt/c/Users/vbala/Videos/test",
        output_path="/mnt/c/Users/vbala/Videos/output",
        output_format="%file%.%ext%",
    )
    service.process(job)


if __name__ == '__main__':
    main()
