card = input("Enter the credit card number: ")

test= card.split('-',maxsplit=3)

for i in test:    
    if len(i) == 4:
        pass
    else:
        print('No Válido')
        break
    try:
        int(i)
    except ValueError:
        print('No Válido')
        break
    if int(i)//1000 in range(1,10):
        pass
    else:
        print('No Válido')
        break

joined = ''.join(test)

for i in range(13):
    if int(joined[i : i+4]) % 1111 == 0:
        print('No Valido')
        break
