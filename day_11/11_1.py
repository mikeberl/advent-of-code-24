with open('input.txt', 'r') as file:
    numeri = list(map(int, file.read().split()))
print(numeri)

for _ in range(25):
    i = 0
    while i < len(numeri):
        if numeri[i] == 0:
            numeri[i] += 1
        elif len(str(abs(numeri[i]))) % 2 == 0:
            numero_str = str(numeri[i])
            meta = len(numero_str) // 2
            primo = int(numero_str[:meta])
            secondo = int(numero_str[meta:])

            numeri[i:i+1] = [primo, secondo]
            i +=1
        else:
            numeri[i] *= 2024

        i += 1
    print(f'Dopo {_} cicli abbiamo {len(numeri)} diversi blocchi')

# print(numeri)
print(len(numeri))
