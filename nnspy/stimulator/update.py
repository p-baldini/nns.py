from ctypes import CDLL
from nnspy.device.network import network_state
from nnspy.device.component import connected_component

nns = CDLL("libnns.so")

nns.update_conductance.argtypes = network_state, connected_component
