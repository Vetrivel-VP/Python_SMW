message = " Hello "
# length
print(len(message))

# strip()
print(len(message.strip()))

# lower()
print(message.lower())

# upper()
print(message.upper())
message.strip()

# replace()
print(message.replace("Hello", "WORLD"))

# split()
message = "Hello, World, welcome"
print(message.split(','))

# format

a = "Its my book, I been taking care of this {0} for past {1} years"
print(a.format("book", 20))

print(message + a)
