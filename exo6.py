S = 0
moy = 0

for i in range(0, 5):
    N = float(input("\nEnter Note 1 : "))
    S += N

moy = S/5

print(f"\nLa somme est : {S}")
print(f"\nLa moyenne est : {moy}")
