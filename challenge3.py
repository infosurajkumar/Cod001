# Experiment with different ranges and slices to get a feel for how they work.
# Remember that you can print the range as well as iterating through it to print
# its values , to check that your ranges are what you expected
# you may also want to include things like:

o = range(0, 100, 4)
O = list(o)
print(O)
for value in O:
    print(value)
print("=" * 50 )
p = o[::5]
print(p)
for i in p:
    print(i)

# and see if you can work out what will be printed before running the programme
# if you are unsure , use a for loop to print out values of o to see why p returnss
#  what it does