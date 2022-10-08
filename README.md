This script tries to immitate Sublime Text's arithmetic command.

![showcase of the script](https://gist.githubusercontent.com/CyborgSquirrel/4a83b65f6a55862d72f45d38c31f56a5/raw/c50f5bcf8335e4feaa7e827f73714fffa87f0f23/arithmetic-kak.gif)

To install, either clone the repo and source the script inside your `kakrc`, or use `plug.kak`.

To use the script, select one or more numbers (using multiple selections), then run `:arithmetic`, then type in your desired expression.

Inside an expression, you may use:
- `x` - the selected number
- `i` - the index of the selected number
- functions from python's `math` and `random` libraries.
