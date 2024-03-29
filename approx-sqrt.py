# Adapted from https://tour.golang.org/flowcontrol/8


def sqrt(x):
    # Initial guess
    z = 1.0

    # Keep getting a better estimate for the square root for x,
    # until within two decimal places.
    while abs(z * z - x) >= 0.01:
        # Get a better approximation for the square root.
        z -= (z * z - x) / (2 * z)

    # Return z
    return z


# Calculate the square root and print it.
z = sqrt(10.0)
print(z)

# Print the square of the square of z.
print(z * z)
