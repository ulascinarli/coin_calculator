import sys

def earnings():

    print('Ana Para Ne Kadar?')
    money = float(sys.stdin.readline())

    print('Tahmini Kazanc Yuzdesi Ne Kadar?')
    percent = float(sys.stdin.readline())

    print('Kac Hafta Surecek?')
    weeks = int(sys.stdin.readline())

    print('Ana Paraya Haftada Ne Kadar Ekleyeceksin?')
    add = float(sys.stdin.readline())

    weeks = weeks + 1

    for week in range (1, weeks):
        income = money + add + ((money + add) * percent)
        money = income
        print('Hafta: %s - Toplam Kazanc: %s' % (week, income))


while True:
    earnings()
    while True:
        print()
        answer = str(input('Tekrar hesapla? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("Gecersiz giris.")
    if answer == 'y':
        continue
    else:
        print("Ok Kib By")
        break
