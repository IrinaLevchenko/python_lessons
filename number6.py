km_day1 = 2     # столько км спортсмен пробежал в первый день
km_day_last = 3 # узнать нужно на какой день спортсмен пробежит столько км
day = 1

while km_day1 <= km_day_last:
    km_day1 *= 1.1
    day = day + 1
print(day)
