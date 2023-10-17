from ctypes import c_double, Structure
from nnspy.util.point import point

class wire(Structure):
    _fields_ = [
        ("centroid",    point),
        ("start_edge",  point),
        ("end_edge",    point),
        ("length",      c_double)
    ]
