def odd_nums(stop_value, start_value=1,step=2):
  current = start_value
  while current <= stop_value:
    yield current
    current += step

odd_to_15 = odd_nums(15)

for i in odd_to_15:
  print(i)

print(type(odd_to_15))
