from ctypes import c_double, c_int, Structure

class datasheet(Structure):
    _fields_ = [
        ("wires_count",     c_int),
        ("length_mean",     c_double),
        ("length_std_dev",  c_double),
        ("package_size",    c_int),
        ("generation_seed", c_int)
    ]

__all__ = "datasheet",
