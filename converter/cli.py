from converter.api import get_rate, convert_currency
from converter.units import convert_length, convert_weight


def convert_measurement(unit):
    unit_standard = unit.lower().strip()

    if unit_standard == 'length':
        return convert_length
    elif unit_standard == 'weight':
        return convert_weight
    elif unit_standard == 'currency':
        return convert_currency
    else:
        raise ValueError('Invalid measurement. Please try again.')


def run():
    while True:
        choice_tuple = ('length', 'weight', 'currency')
        choice = input(
            "Choose a measurement for conversion (length, weight, currency, quit): ").lower().strip()

        if choice == 'quit':
            break
        elif choice not in choice_tuple:
            print("Invalid choice. Please try again.")
            continue
        else:
            conversion_function = convert_measurement(choice)

        try:
            initial_amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount. Please try again.")
            continue

        from_unit = input("Enter measurement to convert from (abbr.): ")
        to_unit = input("Enter measurement to convert to (abbr.): ")

        try:
            final_amount = conversion_function(
                initial_amount, from_unit, to_unit)
        except (ValueError, RuntimeError, TypeError):
            print("Invalid inputs. Please try again.")
            continue

        print(f'{initial_amount} {from_unit} = {round(final_amount, 2)} {to_unit}')
