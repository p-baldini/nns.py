from ctypes import c_char, c_int, CDLL, POINTER
from nnspy.device.component import connected_component
from nnspy.device.datasheet import datasheet
from nnspy.device.network import network_topology, network_state

nns = CDLL("libnns.so")

nns.deserialize_network.argtypes = POINTER(datasheet), POINTER(network_topology), POINTER(c_char), c_int

nns.deserialize_state.argtypes = datasheet, network_topology, POINTER(network_state), POINTER(c_char), c_int, c_int

nns.deserialize_component.argtypes = POINTER(connected_component), POINTER(c_char), c_int, c_int, c_int

nns.deserialize_interface.argtypes = POINTER(interface), POINTER(c_char), c_int, c_int
