import cmptcomplexity.aprox as aproximator
import sys
setup = sys.argv[1]
proper = sys.argv[2]


a= aproximator.count_it(proper,setup, timeout=36)
a.show()


