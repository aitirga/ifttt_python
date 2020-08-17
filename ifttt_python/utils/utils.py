"""
Module containing general utility methods
"""

import logging
import os
logger = logging.getLogger(__name__)


def get_config_path():
    from pathlib import Path
    return Path(__file__).parent.parent / "config"


def get_output_path():
    from pathlib import Path
    os.makedirs(Path.cwd() / "output", exist_ok=True)
    return Path.cwd() / "output"


def get_root_path():
    from pathlib import Path
    return Path.cwd().parent
