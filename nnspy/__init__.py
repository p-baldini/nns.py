from ctypes import c_double, c_int, CDLL, POINTER
from nnspy.device.component import connected_component
from nnspy.device.datasheet import datasheet
from nnspy.device.junction import junction
from nnspy.device.network import network_state, network_topology
from nnspy.device.wire import wire
from nnspy.interface.interface import interface
from nnspy.util.point import point

nns = CDLL("libnns.so")

nns.create_network.argtypes = datasheet, POINTER(c_int), POINTER(c_int)
nns.create_network.restype = network_topology

nns.construe_circuit.argtypes = datasheet, network_topology
nns.construe_circuit.restype = network_state

nns.split_components.argtypes = datasheet, network_topology, network_state, POINTER(c_int), c_int
nns.split_components.restype = POINTER(connected_component)

nns.voltage_stimulation.argtypes = network_state, connected_component, interface, POINTER(c_double)

__all__ = [

    # CLASSES

    "junction", "wire", "point",

    "datasheet", "network_topology", "network_state", "connected_component",

    "interface",

    # WRAPPER

    "nns"
]
