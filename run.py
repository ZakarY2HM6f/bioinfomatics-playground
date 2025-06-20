import sys

imp = sys.argv[1]
exec(f"import pkg.{imp} as main")

main.main()
