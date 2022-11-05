# FormatMyCode
Anything related to formatting written code.

## TCL formatting
Use the format_my_code.py and format your TCL files.

### Usage

1. Clone the repository:
```
git clone https://github.com/FabriceCh/FormatMyCode
```

2. Install required python packages with pip:
```
pip install -r FormatMyCode/requirements.txt
```

3. Run the formatter:
```
python format_my_code.py -f <path_to_tcl_file> [-r <lines>]
```
Ex:
```
python format_my_code.py -f code.tcl -r 100-200,250-300
```