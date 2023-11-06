from ctypes import c_double, CDLL, Structure

nns = CDLL("libnns.so")

class point(Structure):
    _fields_ = [
        ("x", c_double),
        ("y", c_double)
    ]

nns.squared_distance.argtypes = point, point
nns.squared_distance.restype = c_double
