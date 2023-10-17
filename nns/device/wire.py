from ctypes import c_double, Structure
from sources.util.point import position

class wire(Structure):
    _fields_ = [
        ("centroid",    position),
        ("start_edge",  position),
        ("end_edge",    position),
        ("length",      c_double)
    ]
