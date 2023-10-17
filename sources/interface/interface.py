from ctypes import c_bool, c_double, c_int, POINTER, Structure

class interface(Structure):
    _fields_ = [
        ("mask_size",       c_int),
        ("sources_count",   c_int),
        ("sources_mask",    POINTER(c_bool)),
        ("grounds_count",   c_int),
        ("grounds_mask",    POINTER(c_bool)),
        ("loads_count",     c_int),
        ("loads_mask",      POINTER(c_bool)),
        ("loads_weight",    POINTER(c_double)),
    ]
