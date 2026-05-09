# log-colorizer

Colorize and filter log output in terminal with pattern matching.

## Features
- Auto-detect log levels (ERROR, WARN, INFO, DEBUG)
- Minimum level filtering
- Stream processing (pipe-friendly)

## Usage
```bash
tail -f app.log | python -m logcolor --level WARN
```

## License
MIT
