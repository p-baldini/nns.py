from ctypes import c_double, c_int, POINTER, Structure
from nnspy.device.junction import junction
from nnspy.device.wire import wire

class network_topology(Structure):
    _fields_ = [
        ("Ws",          POINTER(wire)),
        ("js_count",    c_int),
        ("Js",          POINTER(junction))
    ]

class network_state(Structure):
    _fields_ = [
        ("Ys",          POINTER(c_double)),
        ("Vs",          POINTER(c_double))
    ]
