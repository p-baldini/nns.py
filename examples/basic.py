from ctypes import *
from nnspy import *

ds = datasheet()
ds.wires_count      = 2000
ds.length_mean      = 14.0
ds.length_std_dev   = 40.0
ds.package_size     = 500
ds.generation_seed  = 1234

cc_count, n2c = c_int(0), (c_int *  ds.wires_count)()
nt = nns.create_network(ds, n2c, byref(cc_count))
ns = nns.construe_circuit(ds, nt)
ccs = nns.split_components(ds, nt, n2c, cc_count)[:cc_count.value]

cc = max(ccs, key=lambda x: int(x.ws_count))

print(f"Selected a CC with {cc.ws_count} nanowires")

mea = nns.connect_MEA(ds, nt)

mea.ct[0] = 1 # SOURCE
mea.ct[5] = 3 # LOAD
mea.ct[9] = 2 # GROUND
mea.ws[5] = 0.5

it = nns.mea2interface(mea)

for _ in range(100):
    ios = (c_double * 1)()
    ios[0] = 5.0

    nns.update_conductance(ns, cc)
    nns.voltage_stimulation(ns, cc, it, ios)

    print(ios[0] / 5, end=" ")
