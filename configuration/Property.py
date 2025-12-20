from typing import Any
from Element import Element, ElementInterface
from Group import Group

from json import dumps

class Property(Element):
    """Base class for all configuration properties.
    Can be used as an untyped property, but it is not recommended."""
    _value_type = Any

    def __init__(self, parent: Group|None, name: str, value: _value_type|None = None, optional: bool = True):
        super().__init__(parent, name)
        self._optional = optional
        self.value = value

    def is_value_valid(self, value: _value_type) -> bool:
        return True

    @property
    def value(self) -> _value_type:
        return self._value

    @value.setter
    def value(self, value: _value_type|None):
        if (not self._optional) and value is None:
            raise ValueError(self, value)

        if self._value_type != Any and type(value) != self._value_type and not (self._optional and value is None):
            raise TypeError(self, value)

        if value is not None and not self.is_value_valid(value):
            raise ValueError(self, value)

        self._value = value

    @property
    def optional(self) -> bool:
        return self._optional
    
    @optional.setter
    def optional(self, optional: bool):
        self._optional = optional

    @property
    def parent(self):
        return self._parent
    
    @parent.setter
    def parent(self, parent: ElementInterface|None):
        if parent is not None and not isinstance(parent, Group):
            raise TypeError(self, parent)

        self._parent = parent
        if isinstance(parent, Group):
            parent.add_child(self)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}<{self._value_type.__name__}> {self.name}({repr(self.value)})'

    def dump(self) -> Any:
        return self.value

    def serialize(self) -> str:
        return dumps(self._value)

class IntProperty(Property):
    """A configuration property that stores an integer."""
    _value_type = int

    def __init__(self, parent: Group|None, name: str, value: _value_type|None = None, min: _value_type|None = None, max: _value_type|None = None, default: _value_type|None = None, optional: bool = True):
        """A configuration property that stores an integer.

        Args:
            parent (Group | None): The parent group. Must be set to None if it is a top-level property.
            name (str): The name of the property.
            value (int | None, optional): The (integer) value of the property. If set to None and the property isn't optional, will be discarded in favour of the default value instead.
            min (int | None, optional): The minimum value for the integer. Defaults to None.
            max (int | None, optional): The maximum value for the integer. Defaults to None.
            default (int | None, optional): The default value. Defaults to None.
            optional (bool): Whether a value is optional.
        """
        self._min = min
        self._max = max
        self._default = default
        super().__init__(parent, name, default if (value is None and not optional) else value, optional)

    @property
    def min(self):
        return self._min

    @property
    def max(self):
        return self._max

    @property
    def default(self):
        return self._default

    def is_value_valid(self, value: _value_type) -> bool:
        if self._min is not None and value < self._min:
            return False

        if self._max is not None and value > self._max:
            return False

        return True

class FloatProperty(Property):
    _value_type = float

    def __init__(self, parent: Group|None, name: str, value: _value_type|None = None, min: _value_type|None = None, max: _value_type|None = None, default: _value_type|None = None, optional: bool = True):
        """A configuration property that stores an integer.

        Args:
            parent (Group | None): The parent group. Must be set to None if it is a top-level property.
            name (str): The name of the property.
            value (int | None, optional): The (integer) value of the property. If set to None and the property isn't optional, will be discarded in favour of the default value instead.
            min (int | None, optional): The minimum value for the integer. Defaults to None.
            max (int | None, optional): The maximum value for the integer. Defaults to None.
            default (int | None, optional): The default value. Defaults to None.
            optional (bool): Whether a value is optional.
        """
        self._min = min
        self._max = max
        self._default = default
        super().__init__(parent, name, default if (value is None and not optional) else value, optional)

    @property
    def min(self):
        return self._min

    @property
    def max(self):
        return self._max

    @property
    def default(self):
        return self._default

    def is_value_valid(self, value: _value_type) -> bool:
        if self._min is not None and value < self._min:
            return False

        if self._max is not None and value > self._max:
            return False

        return True

if __name__ == '__main__':
    group = Group(None, "propGroup")

    prop = Property(None, "myProp")
    print(prop)

    prop.value = 3
    print(prop)

    prop._value_type = int
    print(prop)

    try:
        prop.value = 3.14
        print(prop)
    except Exception as e:
        print(e.__class__.__name__, e)

    print(Property(group, "lambda1"))
    print(Property(group, "lambda2").full_path())

    int_prop = IntProperty(group, "intProp", 879, min=0)
    print(int_prop)

    try:
        int_prop.value = 3.14
        print(int_prop)
    except Exception as e:
        print(e.__class__.__name__, e)

    try:
        int_prop.value = -1
        print(int_prop)
    except Exception as e:
        print(e.__class__.__name__, e)

    try:
        int_prop.value = None
        print(int_prop)
    except Exception as e:
        print(e.__class__.__name__, e)

    print(int_prop.min, int_prop.max, int_prop.default)

    float_prop = FloatProperty(group, "floatProperty", 3.14, optional=False)

    try:
        float_prop.value = None
        print(float_prop)
    except Exception as e:
        print(e.__class__.__name__, e)

    print(repr(float_prop.serialize()))
    print(group.serialize())

    super_group = Group(None, "superGroup")
    group.parent = super_group
    int_prop.value = 69
    int_prop.parent = super_group
    print(super_group.serialize())

    print(float_prop.full_path())