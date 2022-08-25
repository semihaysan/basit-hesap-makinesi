
op = input("operator seciniz (+ | - | * | /) :")
sayi1 = int(input("birinci sayı giriniz :"))
sayi2 = int(input("ikinci sayıyı giriniz :"))
if op == '+':
    toplam = sayi1 + sayi2
    print(toplam)
elif op == '-':
    cikarma = sayi1 - sayi2
    print(+ cikarma)
elif op == '*':
    carpma = sayi1 * sayi2
    print(carpma)
elif op == '/':

    if sayi2 == 0 :
        print("2. sayi 0 olamaz")
    else:
        bolme = sayi1 / sayi2
        print(bolme)

else :
    print("私のディック、私は番号を入力すると言いました、あなたは何をしていますか?")
