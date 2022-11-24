"""
Package for PostgressSQL API
"""

import asyncio
import app.db.models
from app.db.base import init_models


def run() -> None:
    asyncio.get_event_loop().run_until_complete(init_models())
