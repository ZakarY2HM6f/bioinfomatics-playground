import sys
assert(len(sys.argv) == 2)

imp = sys.argv[1]
exec(f"import pkg.{imp} as main")

main.main()
