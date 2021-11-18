# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.
Usage: demo.py <arg1> --arg2=<arg2> [--arg3=<arg3>]
Options:
<arg>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
[--arg4=<arg4>]   Takes any value (this is an optional option)
""" 

from docopt import docopt
opt = docopt(__doc__)

def main(opt,arg,arg2,arg3=NULL,arg4=NULL):
  print(opt)
  print(type(opt))
  print(arg4)

if __name__ == "__main__":
    main(opt["arg"], opt["--arg2"],opt["--arg3"], opt["--arg4"])
