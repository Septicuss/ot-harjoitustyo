# Software Engineering, practice work

Subject:
*A Python desktop application to batch-compress videos. Inspired by [8mb.video](https://8mb.video/)*

## Documentation

- [Specification](https://github.com/Septicuss/ot-harjoitustyo/blob/master/documentation/specification.md)
- [Time Tracking](https://github.com/Septicuss/ot-harjoitustyo/blob/master/documentation/timetracking.md)
- [Changelog](https://github.com/Septicuss/ot-harjoitustyo/blob/master/documentation/changelog.md)

## Installation

1. Install Poetry dependencies with

```
poetry install
```

2. Install ffmpeg if not present
```
sudo apt-get install ffmpeg
```

3. Start the application
```
poetry run invoke start
```

## Commands

### Start the application
```
poetry run invoke start
```

### Testing
```
poetry run invoke test
```

### Coverage report
```
poetry run invoke coverage-report
```