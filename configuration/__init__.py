from Config import *
from Element import Element, ElementInterface
from Group import Group
from Property import Property, IntProperty, FloatProperty

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

    print(super_group.get_from_path('propGroup/floatProperty'))

    try:
        print(super_group.get_from_path('floatProperty'))
    except Exception as e:
        print(e.__class__.__name__, e)

    print(isinstance(super_group, Element))

    config = Config()
    config.add_child(super_group)
    config.add_child(IntProperty(None, 'newIntProp', 69))
    print(config.get_property('superGroup/intProp'))
    print(config.dump())
    print(config.serialize())