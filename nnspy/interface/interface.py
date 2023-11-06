from ctypes import c_double, c_int, CDLL, POINTER, Structure

nns = CDLL("libnns.so")

class interface(Structure):
    _fields_ = [
        ("sources_count",   c_int),
        ("sources_index",   POINTER(c_int)),
        ("grounds_count",   c_int),
        ("grounds_index",   POINTER(c_int)),
        ("loads_count",     c_int),
        ("loads_index",     POINTER(c_int)),
        ("loads_weight",    POINTER(c_double)),
    ]

nns.copy.argtypes = interface,
nns.copy.restype = interface

nns.destroy_interface.argtypes = interface,
