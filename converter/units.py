length_dict = {}  # m per one unit

length_dict['m'] = 1
length_dict['mm'] = 10 ** -3
length_dict['cm'] = 10 ** -2
length_dict['µm'] = 10 ** -6
length_dict['km'] = 10 ** 3
length_dict['in'] = 0.0254
length_dict['ft'] = 0.3048
length_dict['yd'] = 0.9144
length_dict['mi'] = 1609.344
length_dict['nmi'] = 1852

weight_dict = {}  # kg per one unit

weight_dict['kg'] = 1
weight_dict['g'] = 10 ** -3
weight_dict['mg'] = 10 ** -6
weight_dict['oz'] = 0.0283495
weight_dict['lb'] = 0.453592
weight_dict['st'] = 6.35029
weight_dict['t'] = 10 ** 3
weight_dict['tn'] = 907.185


def convert_length(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError('Value has to be a number')
    elif value < 0:
        raise ValueError('Value can\'t be negative')
    try:
        conversion_rate = length_dict[from_unit.lower(
        ).strip()] / length_dict[to_unit.lower().strip()]
    except KeyError:
        raise ValueError("Invalid unit(s)")
    return value * conversion_rate


def convert_weight(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError('Value has to be a number')
    elif value < 0:
        raise ValueError('Value can\'t be negative')

    try:
        conversion_rate = weight_dict[from_unit.lower(
        ).strip()] / weight_dict[to_unit.lower().strip()]
    except KeyError:
        raise ValueError("Invalid unit(s)")

    return value * conversion_rate
