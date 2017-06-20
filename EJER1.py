import argparse

if __name__ == '__main__':

parser=argparse.ArgumentParser()
parser.add_argument('nombre')
parser.add_argument('edad')
parser.add_argument('curso')

args=parser.parse_args()

print(args.nombre)
print(args.edad)
print(args.curso)

print(args.nombre,args.edad,args.curso)
