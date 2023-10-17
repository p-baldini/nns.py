from ctypes import c_int, POINTER, Structure

class connected_component(Structure):
    _fields_ = [
        ("ws_count",    c_int),
        ("js_count",    c_int),
        ("ws_skip",     c_int),
        ("js_skip",     c_int),
        ("Is",          POINTER(c_int))
    ]
