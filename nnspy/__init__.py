from ctypes import c_double, c_int, CDLL, POINTER

from nnspy.device.component import connected_component
from nnspy.device.datasheet import datasheet
from nnspy.device.junction import junction
from nnspy.device.network import network_state, network_topology
from nnspy.device.wire import wire
from nnspy.interface.interface import interface
from nnspy.interface.mea import MEA
from nnspy.util.point import point

nns = CDLL("libnns.so")

__all__ = [

    # CLASSES

    "junction", "wire", "point",

    "datasheet", "network_topology", "network_state", "connected_component",

    "interface", "MEA",

    # WRAPPER

    "nns"
]
