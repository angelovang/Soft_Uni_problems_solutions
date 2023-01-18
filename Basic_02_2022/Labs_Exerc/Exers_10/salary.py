tabs_count = int(input())
salary = float(input())
site = ''
fall  = 0
for x in range (tabs_count):
    site = input()
    if site == 'Facebook':
        fall = 150
    elif site == 'Instagram':
        fall = 100
    elif site == 'Reddit':
        fall = 50
    else:
        fall = 0
    salary -= fall
    if salary <= 0:
        print('You have lost your salary.')
        break
if salary >0:
    print(f'{int(salary)}')






'''Според отворения сайт в таба се налагат следните глоби:
    • "Facebook" -> 150 лв.
    • "Instagram" -> 100 лв.
    • "Reddit" -> 50 лв.
От конзолата се четат два реда:
    • Брой отворени табове в браузъра n - цяло число в интервала [1...10]
    • Заплата - число в интервала [500...1500]
След това n – на брой пъти се чете име на уебсайт – текст'''