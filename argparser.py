import argparse


parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("Quantity",help="Quantity of something",type=int,default=1)
parser.add_argument("Name",help="Name of something",type=str,default="NoName")
parser.add_argument("-g","--Group",help="group of something",type=str,choices=["Alpha","Beta","Charie"],required=True)
parser.add_argument("-o","--Others",help="other options of something",type=str,nargs="*")
args = parser.parse_args()

print(args.Quantity)
print(args.Name)
print(args.Group)
print(args.Others)


