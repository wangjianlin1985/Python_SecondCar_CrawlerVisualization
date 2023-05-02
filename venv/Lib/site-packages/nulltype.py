import sys

_PY2 = sys.version_info[0] == 2

__all__ = "NullType NonNullType Null Nothing Empty".split()


class NullType(object):

    """
    A 'null' type different from, but parallel to, None. Core function
    is representing emptyness in a way that doesn't overload None.
    This helps create designated identifiers with specific meanings
    such as Passthrough, Prohibited, and Undefined.

    Instantiate to create desired null singletons. While they are
    singletons, depends on usage convention rather than strict
    enforcement to maintain their singleton-ness. This is a problem
    roughly 0% of the time.
    """

    def __init__(self, name):
        object.__setattr__(self, "__name", name)

    def __repr__(self):
        return object.__getattribute__(self, "__name")

    if _PY2:  # PY2
        def __nonzero__(self):
            """I am always False."""
            return False
    else: # PY3
        def __bool__(self):
            """I am always False."""
            return False

    def __iter__(self):
        return iter([])

    def __len__(self):
        return 0

    def __getitem__(self, index):
        return self

    def __getattr__(self, name):
        return self if name != '__name' else object.__getattr__(self, name)

    def __setitem__(self, name, value):
        pass

    def __setattr__(self, name, value):
        pass

    def __call__(self, *args, **kwargs):
        return self


Null = NullType('Null')
Nothing = NullType('Nothing')
Empty = NullType('Empty')


class NonNullType(object):

    """
    Like NullType, but truthy not falsey. Could be a subclass of NullType;
    while that would provide a tiny bit more code reuse, NonNullType as
    as NullType is ontologically suspect.
    """

    def __init__(self, name):
        object.__setattr__(self, "__name", name)

    def __repr__(self):
        return object.__getattribute__(self, "__name")


    if _PY2:
        def __nonzero__(self):
            """I am always True."""
            return True

    else: # PY3
        def __bool__(self):
            """I am always True."""
            return True

    def __iter__(self):
        """I always contain something. Myself. Beware recursion on this!"""
        return iter([self])

    def __len__(self):
        return 1

    def __getitem__(self, index):
        return self

    def __getattr__(self, name):
        return self if name != '__name' else object.__getattr__(self, name)

    def __setitem__(self, name, value):
        pass

    def __setattr__(self, name, value):
        pass

    def __call__(self, *args, **kwargs):
        return self
