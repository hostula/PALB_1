# scores tuple
scores = (
    ('Hyun', 88, 95, 90),
    ('John', 90, 85, 88),
    ('Alice', 92, 90, 91),
    ('Bob', 85, 87, 84)
)

# unpack using zip
names, english, math, science = zip(*scores)

# extract math scores
math_scores = math

# calculate average
average_math = sum(math_scores) / len(math_scores)

print("Math scores:", math_scores)
print("Average math score:", average_math)
