"""
Task 4: Pocket Money Records
You're building a small tracker for your younger sibling's weekly pocket money.
The amounts (in naira) for the past 5 weeks are stored like this:
money = [1000, 1200, 800, 1500, 1100]

1. Calculate and display the total amount received so far.
2. A mistake was made in the third week's entry (800). It should have been 1000. Fix it.
3. Display the list in reverse order to check most recent payments first.

→ Perform the corrections and computations, and print all results.
"""

# Initial weekly records
money = [1000, 1200, 800, 1500, 1100]


total_before_correction = sum(money)
money[2]=1000
reversed_money = list(reversed(money))
total_after_correction = sum(money)
print(total_before_correction)
print(money)
print(reversed_money)
print(total_after_correction)

