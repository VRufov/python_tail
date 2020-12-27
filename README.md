## Installing

`pip install -r requirements.txt`

## Usage

Show help message
`python tail.py -h`

Print the last few number of lines (10 lines by default) of a certain file from the end
`python tail.py {filename}`

Print the specified number of lines of a certain file
`python tail.py -n {lines_number} {filename}`

Tail to loop forever, checking for new data at the end of the file(s). When new data appears, it will be printed.
`python tail.py -f {filename}`

Run tests from root directory
`python -m unittest -v tests.tests`