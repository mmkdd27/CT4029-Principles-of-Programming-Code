from datetime import date
import time
import sys

print("welcome !")
print("""
my name is mohammad 
this is principles of programing 
it teaches programming """)
print("footballs are cool but you know whats cooler? basketballs!    ,michael  jordan probably ")
print(10 * 304)
today = date.today()
print("Today's date:", today)


def progress_bar(iteration, total, bar_length=50):
    progress = (iteration / total)
    # this is for knowing which part of the current bar are we in
    arrow = '=' * int(round(bar_length * progress))
    # the progress
    spaces = '#' * (bar_length - len(arrow))
    # whats left
    # *********
    sys.stdout.write(f'\r[{arrow + spaces}] {int(progress * 100)}%')
    sys.stdout.flush()
    # this uses the stdout object to give the output of the function instead of print to avoid printing a new line  for every iteration of the progress bar
    # ******


total_iterations = 55
for i in range(total_iterations):
    time.sleep(0.1)  # Simulate some work
    progress_bar(i + 1, total_iterations)

def progress_bar_print(iteration, total, bar_length=50):
    progress = (iteration / total)
    # this is for knowing which part of the current bar are we in
    arrow = '=' * int(round(bar_length * progress))
    # the progress
    spaces = '#' * (bar_length - len(arrow))
    # whats left

    print(f'\r[{arrow + spaces}] {int(progress * 100)}%')
 #here is a version with print
total_iterations = 55
for i in range(total_iterations):
    time.sleep(0.1)  # Simulate some work
    progress_bar_print(i + 1, total_iterations)
