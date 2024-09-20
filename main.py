# avec argparse aussi on peut lire la ligne de commande
# et c'est beaucoup plus puissant
from argparse import ArgumentParser

# on importe le module de calcul
from fibonacci import fibo_cached
from fibonacci import fibo

# acquisition du paramètre à partir de la ligne de commande
parser = ArgumentParser()
parser.add_argument("n", type=int)
# on utilise 1 si on veut cacher, 0 sinon
parser.add_argument("cache", type=int)
args = parser.parse_args()
n = args.n

cache = args.cache
# calcul et affichage
if cache == 1:
    print(f"fibo_cached({n}) = {fibo_cached(n)}")
else:
    print(f"fibo({n}) = {fibo(n)}")
