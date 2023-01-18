exam_h = int(input())
exam_m = int(input())
arrival_h = int(input())
arrival_m = int(input())

exam_time_m = exam_h * 60 + exam_m
arrival_time = arrival_h * 60 + arrival_m
diff = arrival_time - exam_time_m

if -30 <= diff <= 0 :
    print('On time')
    if diff < 0 :
        print(f'{abs(diff)} minutes before the start')
elif diff < -30:
    print ('Early')
    if diff > -60 :
        print(f'{abs(diff)} minutes before the start')
    else:
        hours = abs(diff) // 60
        minutes = abs(diff) % 60
        print(f'{hours}:{minutes:02d} hours before the start')
elif 0 < diff :
    print ('Late')
    if diff < 60:
        print(f'{diff} minutes after the start')
    else :
        hours = diff // 60
        minutes = diff % 60
        print(f'{hours}:{minutes:02d} hours after the start')




