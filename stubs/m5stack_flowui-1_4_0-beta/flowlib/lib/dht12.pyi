
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class DHT12:
    def humidity() -> None: ...
    def measure() -> None: ...
    def temperature() -> None: ...
class DHTBaseI2C:
    def measure() -> None: ...
