# Conversion factors
conversion_factors = {
    # Length Unit Conversion
    'cm': {
        'inches': 0.393701,
        'miles': 0.0000062137,
        'feet': 0.0328084,
        'meters': 0.01,
        'kilometers': 0.00001
    },
    'inches': {
        'cm': 2.54,
        'miles': 0.0000157828,
        'feet': 0.0833333,
        'meters': 0.0254,
        'kilometers': 0.0000254
    },
    'miles': {
        'cm': 160934.0,
        'inches': 63360.0,
        'feet': 5280.0,
        'meters': 1609.34,
        'kilometers': 1.60934
    },
    'feet': {
        'cm': 30.48,
        'inches': 12.0,
        'miles': 0.000189394,
        'meters': 0.3048,
        'kilometers': 0.0003048
    },
    'meters': {
        'cm': 100.0,
        'inches': 39.3701,
        'miles': 0.000621371,
        'feet': 3.28084,
        'kilometers': 0.001
    },
    'kilometers': {
        'cm': 100000.0,
        'inches': 39370.1,
        'miles': 0.621371,
        'feet': 3280.84,
        'meters': 1000.0
    },

    # Mass Unit Conversion
    'grams': {
        'kilograms': 0.001,
        'pounds': 0.00220462,
        'ounces': 0.035274,
        'metric_tonnes': 0.000001,
        'short_tons': 0.00000110231,
        'long_tons': 0.00000098421
    },
    'kilograms': {
        'grams': 1000,
        'pounds': 2.20462,
        'ounces': 35.274,
        'metric_tonnes': 0.001,
        'short_tons': 0.00110231,
        'long_tons': 0.000984207
    },
    'pounds': {
        'grams': 453.592,
        'kilograms': 0.453592,
        'ounces': 16,
        'metric_tonnes': 0.000453592,
        'short_tons': 0.0005,
        'long_tons': 0.000446429
    },
    'ounces': {
        'grams': 28.3495,
        'kilograms': 0.0283495,
        'pounds': 0.0625,
        'metric_tonnes': 0.0000283495,
        'short_tons': 0.00003125,
        'long_tons': 0.0000279018
    },
    'metric_tonnes': {
        'grams': 1000000,
        'kilograms': 1000,
        'pounds': 2204.62,
        'ounces': 35274,
        'short_tons': 1.10231,
        'long_tons': 0.984207
    },
    'short_tons': {
        'grams': 907185,
        'kilograms': 907.185,
        'pounds': 2000,
        'ounces': 32000,
        'metric_tonnes': 0.907185,
        'long_tons': 0.892857
    },
    'long_tons': {
        'grams': 1016050,
        'kilograms': 1016.05,
        'pounds': 2240,
        'ounces': 35840,
        'metric_tonnes': 1.01605,
        'short_tons': 1.12
    },

    # Temperature Unit Conversion
    'Celsius': {
        'Fahrenheit': lambda x: (x * 9/5) + 32,
        'Kelvin': lambda x: x + 273.15
    },
    'Fahrenheit': {
        'Celsius': lambda x: (x - 32) * 5/9,
        'Kelvin': lambda x: (x - 32) * 5/9 + 273.15
    },
    'Kelvin': {
        'Celsius': lambda x: x - 273.15,
        'Fahrenheit': lambda x: (x - 273.15) * 9/5 + 32
    }
}


# Conversion function
def convert(from_unit, to_unit, input_value):
    if from_unit == to_unit:
        output_value = input_value
    elif from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        factor = conversion_factors[from_unit][to_unit]
        if callable(factor):
            output_value = factor(input_value)
        else:
            output_value = input_value * factor
    else:
        raise ValueError(f"Cannot convert from {from_unit} to {to_unit}")
    return output_value

# Usage Example
'''
from_unit = "meters"
to_unit = "kilometers"
input_value = 32
text = convert(from_unit, to_unit, input_value)
print(text)
'''
