
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Logger:
    def _level_str() -> None: ...
    def critical() -> None: ...
    def debug() -> None: ...
    def error() -> None: ...
    def info() -> None: ...
    def log() -> None: ...
    def warning() -> None: ...
def basicConfig() -> None: ...
def debug() -> None: ...
def getLogger() -> None: ...
def info() -> None: ...