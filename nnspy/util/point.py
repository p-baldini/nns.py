from ctypes import c_double, Structure

class point(Structure):
    _fields_ = [
        ("x", c_double),
        ("y", c_double)
    ]
