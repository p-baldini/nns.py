from ctypes import c_int, c_void_p, POINTER, Structure
from nnspy.nns import nns

class connected_component(Structure):
    _fields_ = [
        ("ws_count",    c_int),
        ("js_count",    c_int),
        ("ws_skip",     c_int),
        ("js_skip",     c_int),
        ("Is",          POINTER(c_int))
    ]

nns.cccmp.argtypes = c_void_p, c_void_p
nns.cccmp.restype = c_int

__all__ = "connected_component", "nns"
