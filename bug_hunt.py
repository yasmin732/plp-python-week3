count = 1
total = 0
# BUG: The while statement was missing a colon, so I added one.
# BUG: Changed < to <= so that the loop includes 5 in the sum.
while count <=5:
    total = total + count
    count = count + 1

# BUG: total is an integer, so I used an f-string instead of joining it directly to a string.
print(f"Sum of 1 to 5 is: {total}")