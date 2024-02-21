def lazyproperty(f):
    """@lazyprop decorator.

    Decorated method will be called only on first access to calculate a cached property
    value. After that, the cached value is returned.
    """
    cache_attr_name = "_%s" % f.__name__  # like '_foobar' for prop 'foobar'
    docstring = f.__doc__

    def get_prop_value(obj):

        try:
            value = getattr(obj, cache_attr_name)
            return value
        except AttributeError:
            value = f(obj)
            setattr(obj, cache_attr_name, value)
            return value

    return property(get_prop_value, doc=docstring)


class MethodPropertyTest:
    @lazyproperty
    def test(self):
        """Test method to cache"""
        return 10 + 10


method = MethodPropertyTest()

# first time exception will raise and set the value after value will be get from the cache
print(method.test)  # set value form the AttributeError exception
print(method.test)
