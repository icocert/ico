import contextlib

import sys


@contextlib.contextmanager
def maybe_open(path, *args, **kwargs):
    if not path:
        yield sys.stdout
    else:
        f = open(path, *args, **kwargs)
        try:
            yield f
        finally:
            f.close()
