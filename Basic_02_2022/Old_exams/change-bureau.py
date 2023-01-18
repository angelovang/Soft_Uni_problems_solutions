cnt_bitcoin = int(input())
china_uan = float(input())
tax = float(input())

euro_lv = 1.95
usd_lv = 1.76
china_usd = 0.15
bitc_lv = 1168

total_sum = (cnt_bitcoin * bitc_lv)/euro_lv + ((china_uan*china_usd)*usd_lv)/euro_lv
total_sum = total_sum - total_sum*tax/100

print(f'{total_sum:.2f}')

