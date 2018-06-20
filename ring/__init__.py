""":mod:`ring` - Top-level interfaces for end users.
====================================================

Common ring decorators are aliased in this level as shortcuts.
"""
import ring.coder  # noqa
from ring.__version__ import __version__  # noqa
from ring.func import (
    dict, shelve, disk, memcache, redis)
try:
    import asyncio
    from ring.func_asyncio import aiomcache, aioredis
except ImportError:
    pass
else:
    del asyncio
try:
    import ring.django  # noqa
except ImportError:  # pragma: no cover
    pass


__all__ = (
    'dict', 'shelve', 'memcache', 'redis', 'disk',
    'aiomcache', 'aioredis')
