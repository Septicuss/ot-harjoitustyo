## Week 3

- Project structure and basic model
  - `job_service` service, responsible for executing video processing jobs
  - `job` immutable model, which is passed forward to the job service
- Implement requirements; invoke tasks & test coverage

## Week 4

- Refactor application code completely to make it simpler
  - Compression backend now in one single package `compression`, which has simple files to manage file processing
- Implement a working, concurrent batch file processor with a 8 mb compression preset