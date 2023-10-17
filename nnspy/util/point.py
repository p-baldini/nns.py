from ctypes import c_double, Structure

class position(Structure):
    _fields_ = [
        ("x", c_double),
        ("y", c_double)
    ]
