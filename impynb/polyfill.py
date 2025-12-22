__all__ = ["Unpack"]

try:
    # Python 3.11+
    from typing import Unpack  # type: ignore[attr-defined]
except ImportError:
    # Python < 3.11
    from typing_extensions import Unpack
