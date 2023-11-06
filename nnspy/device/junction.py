from ctypes import c_int, c_void_p, CDLL, Structure
from nnspy.util.point import point

nns = CDLL("libnns.so")

class junction(Structure):
    _fields_ = [
        ("first_wire",  c_int),
        ("second_wire", c_int),
        ("position",    point)
    ]

nns.jcmp.argtypes = c_void_p, c_void_p
nns.jcmp.restype = c_int
