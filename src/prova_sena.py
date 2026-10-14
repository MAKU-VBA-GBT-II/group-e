import random
import os

os.makedirs('data', exist_ok=True)
sayilar = [random.randint(1, 100) for _ in range(10)]

with open('data/prova-sena.csv', 'w', encoding='utf-8') as f:
    f.write('deger\n')
    for s in sayilar:
        f.write(f'{s}\n')
print("İşte bu kadar!")