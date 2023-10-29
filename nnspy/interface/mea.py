from ctypes import c_int, Structure
from nnspy.util.point import point

class MEA(Structure):
    _fields_ = [
        ("Ps",      point * 16),
        ("e2n",     c_int * 16)
    ]
