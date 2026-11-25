# Unit & Currency Converter

A command-line converter for currencies, lengths, and weights. Currency rates are fetched live from the [Frankfurter API](https://frankfurter.dev), and unit conversions are calculated locally.

## Features

- Live currency conversion between any currencies Frankfurter supports
- Length and weight conversions
- Input validation with clear error messages (bad units, negative or non-numeric amounts, no internet connection)
- Menu loop, so you can run several conversions in one session

## Requirements

- Python 3.x (CHECK: run `python --version` and put your version here)
- The libraries in `requirements.txt` (`requests`)
- An internet connection for currency conversions

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/izetherdic/unit_currency_converter.git
   cd unit_currency_converter
   ```
2. Create and activate a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   On Windows, activate with `.venv\Scripts\activate` instead.
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the program from the project root:

```
python main.py
```

Choose a measurement type, then enter the amount and the units to convert from and to. Type `quit` at the menu to exit.

Example session (CHECK: replace with real output from your own run):

```
Choose a measurement for conversion (length, weight, currency, quit): length
Enter amount: 5
Enter measurement to convert from (abbr.): mi
Enter measurement to convert to (abbr.): km
Initial length: 5.0
Final length: 8.04672
```

## Supported units

CHECK: update this list to match the keys in `units.py`.

| Type | Units |
|------|-------|
| Length | `mm`, `cm`, `m`, `km`, `in`, `ft`, `yd`, `mi`, `nmi` |
| Weight | `mg`, `g`, `kg`, `oz`, `lb`, `st`, `t` (metric tonne), `tn` (US ton) |
| Currency | 3-letter codes such as `USD`, `EUR`, `GBP`, `JPY` |

Unit names are not case-sensitive.

## Project structure

```
unit_currency_converter/
├── main.py              # entry point
├── requirements.txt
├── README.md
└── converter/
    ├── __init__.py
    ├── api.py           # fetches exchange rates and converts currency
    ├── units.py         # length and weight conversions
    └── cli.py           # menu loop and input handling
```

## How it works

- **Currency:** `api.py` requests the exchange rate for a currency pair and multiplies it by the amount.
- **Units:** `units.py` stores each unit as a factor relative to a base unit (meters for length, kilograms for weight) and converts through that base.
- **Errors:** the conversion functions raise `ValueError`, `TypeError`, or `RuntimeError`, and `cli.py` catches them so the program keeps running.

## Possible improvements

- Temperature conversions
- More units (volume, speed, area)
- Automated tests with pytest
- Caching exchange rates to reduce API calls
