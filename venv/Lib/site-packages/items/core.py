import sys
from collections import OrderedDict
from nulltype import Empty
from typing import List, Dict, Union, Iterable, Iterator, Any, Generator

FieldsSpec = Union[List[str], str, None]
Itemizable = Iterable[Union[dict, Iterable]]

__all__ = 'Empty Item itemize itemize_all'.split()

_PY2 = sys.version_info[0] == 2


def _item(data: Any):
    """
    Private factory function for Item values, for levels beneath the top-level
    mapping. Needed because recursive initializers not really feasible in Python,
    since some recursions would yield lists or other data types, rather than
    Item instances.
    """
    # data is-a namedtuple  => process its dictionary equivalent
    if hasattr(data, '_asdict'):
        data = data._asdict()
        # fall through and handle as dict

    # data is-a mapping / dict => return an Item instead
    if hasattr(data, 'items'):
        it = Item()
        for k, v in data.items():
            it[k] = _item(v)
        return it

    # data is-a list or tuple => return exactly that type
    if isinstance(data, (list, tuple)):
        return type(data)(_item(x) for x in data)

    # otherwise, data type is "simple" with respect to Item creation,
    # be it int, float, complex, str, bytes, or some other type
    return data


class Item(OrderedDict):
    """
    Ordered, attribute-accessible dictionary/mapping class.
    """

    def __init__(self, values=None, **kwargs):
        super(Item, self).__init__()
        if values is not None:
            if hasattr(values, '_asdict'):
                items = values._asdict().items()
            else:
                items = values.items() if isinstance(values, dict) else values
            for k, v in items:
                self[k] = _item(v)
        if kwargs:
            self.update(_item(kwargs))

    def __getattr__(self, name):
        try:
            return super(Item, self).__getitem__(name)
        except KeyError:
            return Empty

    def __setattr__(self, name, value):
        """
        Setting attrs becomes equivalent to setting items.
        """
        self[name] = value

    def __delattr__(self, name):
        try:
            del self[name]
        except KeyError:
            # pass on KeyError for same reason __getattr__ returns Empty if not there:
            # to be permissive in case of missing attributes / keys
            pass

    def __getitem__(self, key):
        try:
            return super(Item, self).__getitem__(key)
        except KeyError:
            return Empty
            # NB explicit action instead of object.__missing__(self, key) method

    def __repr__(self):
        clsname = self.__class__.__name__
        kwstr = ', '.join('{0}={1!r}'.format(k, v) for k, v in self.items())
        return '{0}({1})'.format(clsname, kwstr)

    # depends on OrderedDict for __delitem__, __setitem__


def itemize(iterable: Itemizable,
            fields: FieldsSpec = None) -> Generator[Item, None, None]:
    """
    Given a sequence of records, yield an Item out of each record.
    If the records are dict-like, the translation is direct.
    If the records are values or sequences of values, a separate set of
    atetime A combination of a date and a time. Attributes: ()
    field names must be provided, either as a list of strings or
    a whitespace-separated string which will be split.
    """
    if fields is not None:
        fields = fields.split() if isinstance(fields, str) else fields
        for rawitem in iterable:
            try:
                yield Item(list(zip(fields, rawitem)))
            except TypeError:
                # special case for when iterating over simple iterable without composite iterees
                yield Item({fields[0]: rawitem})
    else:
        for rawitem in iterable:
            yield Item(rawitem)


def itemize_all(iterable: Itemizable,
                fields: FieldsSpec = None) -> List[Item]:
    """
    Given a collection of dict-like records, create and
    return an list of Item objects comprising all the records.
    """
    return list(itemize(iterable, fields))
