from datetime import date
import time
import sys

print("welcome !")
print("""
my name is mohammad 
this is principles of programing 
it teaches programming """)
print("footballs are cool but you know whats cooler? basketballs!    ,michael  jordan probably ")
print(10*304)
today = date.today()
print("Today's date:", today)

def progress_bar(iteration, total, bar_length=50):
    progress = (iteration / total)
    arrow = '=' * int(round(bar_length * progress))
    spaces = ' ' * (bar_length - len(arrow))
    sys.stdout.write(f'\r[{arrow + spaces}] {int(progress * 100)}%')
    sys.stdout.flush()

total_iterations = 55
for i in range(total_iterations):
    time.sleep(0.1) # Simulate some work
    progress_bar(i + 1, total_iterations)