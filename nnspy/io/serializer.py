from ctypes import c_char, c_int, CDLL, POINTER
from nnspy.device.component import connected_component
from nnspy.device.datasheet import datasheet
from nnspy.device.network import network_topology, network_state

nns = CDLL("libnns.so")

nns.serialize_network.argtypes = datasheet, network_topology, POINTER(c_char), c_int

nns.serialize_state.argtypes = datasheet, network_topology, network_state, POINTER(c_char), c_int, c_int

nns.serialize_component.argtypes = connected_component, POINTER(c_char), c_int, c_int

nns.serialize_interface.argtypes = interface, POINTER(c_char), c_int, c_int
