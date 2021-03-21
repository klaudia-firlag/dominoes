# Dominoes
A script for calculating positions of dominoes.
Dominoes' sequences are represented in a form of strings, where:

`|` - means a dominoe standing straight

`/` - means a dominoe falling to the right

`\ ` - means a dominoe falling to the left

Examples:
* `||//||\||/\|` after 1 forward iteration: `||///\\||/\|`
* `||////\\\|////|` after 2 backward iterations: `||//||||\|//|||`

## Tests
```shell
python -m unittest unittests.py
```

## Run
Arguments:
* `--in_sequence` - a string with a sequence of dominoes (constraints: a sequence must be at least 2 character long and contain only `/`, `|`, `\ ` characters)
* `--num_iter` - number of iterations - default: 1 (constraint: must be zero or a positive number)
* `--backward` - a flag for performing backward iterations
```shell
python run_dominoes.py --in_sequence '||////\\\|////|' --num_iter 2 --backward
```
