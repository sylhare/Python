class AttributeDict(dict):
    """
    Dictionary subclass enabling attribute lookup/assignment of keys/values.
    For example::
        m = AttributeDict({'foo': 'bar'})
        m.foo and m['foo'] will return
            'bar'

    ``AttributeDict`` objects also provide ``.first()`` which acts like
    ``.get()`` but accepts multiple keys as arguments, and returns the value of
    the first hit, e.g.::
        m = AttributeDict({'foo': 'bar', 'biz': 'baz'})
        m.first('wrong', 'incorrect', 'foo', 'biz')
            'bar'
    """

    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            # to conform with __getattr__ spec
            raise AttributeError(key)
