import sys

LEVEL_COLORS = {
    "ERROR": "\033[91m",
    "WARN": "\033[93m",
    "INFO": "\033[92m",
    "DEBUG": "\033[90m",
}
RESET = "\033[0m"

class Colorizer:
    def __init__(self, min_level=None):
        self.min_level = min_level
        self._levels = ["DEBUG", "INFO", "WARN", "ERROR"]

    def _detect_level(self, line):
        for lvl in self._levels:
            if lvl in line.upper():
                return lvl
        return None

    def _should_show(self, level):
        if not self.min_level:
            return True
        return self._levels.index(level) >= self._levels.index(self.min_level)

    def colorize(self, line):
        level = self._detect_level(line)
        if level and not self._should_show(level):
            return None
        if level and level in LEVEL_COLORS:
            return f"{LEVEL_COLORS[level]}{line}{RESET}"
        return line

    def process_stream(self, stream=None):
        stream = stream or sys.stdin
        for line in stream:
            result = self.colorize(line.rstrip())
            if result is not None:
                print(result)
