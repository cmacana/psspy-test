"""
Set of methods for Power System Analysis
"""


def to_pu(z_abs, baseVoltage, sn):
    """
    Convert an impendace from absolute values to p.u values
    `z_abs` Impedance in absolutes values
    `z_base` Base Impedance
    `baseVoltage` Base Voltage
    `sn` Base Apparent Power
    :return: Impedance in pu
    """
    z_base = baseVoltage ** 2 / sn
    z_pu = z_abs / z_base
    return z_pu


def per_length_to_impedance(length, z_per_length):
    """
    Compute an absulute impendace
    `length` Length of the line in km
    `z_per_length` Impedance per length in ohms/km
    :return: Impedance in ohms
    """
    return length * z_per_length


r_abs = per_length_to_impedance(0.1, 0.642)
x_abs = per_length_to_impedance(0.1, 0.083)
r_pu = to_pu(r_abs, baseVoltage=0.4, sn=0.4)
x_pu = to_pu(x_abs, baseVoltage=0.4, sn=0.4)
print r_pu
print x_pu
