from ctypes import c_double, c_int, CDLL, POINTER
from nnspy.device.component import connected_component
from nnspy.device.datasheet import datasheet
from nnspy.device.junction import junction
from nnspy.device.network import network_state, network_topology
from nnspy.device.wire import wire
from nnspy.interface.interface import interface
from nnspy.interface.MEA import MEA
from nnspy.util.point import point

nns = CDLL("libnns.so")

nns.create_network.argtypes = datasheet, POINTER(c_int), POINTER(c_int)
nns.create_network.restype = network_topology

nns.construe_circuit.argtypes = datasheet, network_topology
nns.construe_circuit.restype = network_state

nns.split_components.argtypes = datasheet, network_topology, POINTER(c_int), c_int
nns.split_components.restype = POINTER(connected_component)

nns.voltage_stimulation.argtypes = network_state, connected_component, interface, POINTER(c_double)
nns.voltage_stimulation.restype = c_int

nns.resistive_distance.argtypes = network_state, connected_component, c_int, c_int
nns.resistive_distance.restype = c_double

nns.connect_MEA.argtypes = datasheet, network_topology
nns.connect_MEA.restype = MEA

__all__ = [

    # CLASSES

    "junction", "wire", "point",

    "datasheet", "network_topology", "network_state", "connected_component",

    "interface", "MEA"

    # WRAPPER

    "nns"
]
