
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class MQTTClient:
    def _recv_len() -> None: ...
    def _send_str() -> None: ...
    def check_msg() -> None: ...
    def connect() -> None: ...
    def disconnect() -> None: ...
    def ping() -> None: ...
    def publish() -> None: ...
    def set_callback() -> None: ...
    def set_last_will() -> None: ...
    def subscribe() -> None: ...
    def wait_msg() -> None: ...
class Pin:
    def init() -> None: ...
    def irq() -> None: ...
    def off() -> None: ...
    def on() -> None: ...
    def value() -> None: ...
def main() -> None: ...
def sub_cb() -> None: ...
