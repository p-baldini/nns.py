from ctypes import c_double, c_int, CDLL, POINTER, Structure
from nnspy.device.datasheet import datasheet
from nnspy.device.junction import junction
from nnspy.device.wire import wire

nns = CDLL("libnns.so")

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

nns.create_network.argtypes = datasheet, POINTER(c_int), POINTER(c_int)
nns.create_network.restype = network_topology

nns.construe_circuit.argtypes = datasheet, network_topology
nns.construe_circuit.restype = network_state

nns.destroy_topology.argtypes = network_topology,

nns.destroy_state.argtypes = network_state,
