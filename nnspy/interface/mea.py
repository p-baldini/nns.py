from ctypes import c_double, c_int, Structure
from nnspy.util.point import point

class MEA(Structure):
    _fields_ = [
        ("Ps",      point * 16),
        ("e2n",     c_int * 16),
        ("ct",      c_int * 16),
        ("ws",      c_double * 16)
    ]
