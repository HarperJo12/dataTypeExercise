from datetime import datetime

# from datetime import date    
# today = date.today().isoformat()
# datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
years = input('what year were you born?')
now = datetime.today().strftime('%Y')
age = int(now) - int(years)
print(f'you were born in {years} \nyour age is {age}')