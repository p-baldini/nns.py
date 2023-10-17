from ctypes import c_int, Structure
from nnspy.util.point import position

class junction(Structure):
    _fields_ = [
        ("first_wire",  c_int),
        ("second_wire", c_int),
        ("position",    position)
    ]
