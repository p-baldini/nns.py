from ctypes import c_int, Structure
from nnspy.util.point import point

class junction(Structure):
    _fields_ = [
        ("first_wire",  c_int),
        ("second_wire", c_int),
        ("position",    point)
    ]
