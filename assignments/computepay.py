def computepay(h, r):
    if h > 40:
        return (40 * r) + ((h - 40) * (r * 1.5))
    else:
        return h * r
    
h = input("Enter Hours: ")
r = input("Enter Rate: ")

# Convert to float
h = float(h)
r = float(r)

print("Pay", computepay(h, r))