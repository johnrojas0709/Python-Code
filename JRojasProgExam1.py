"""The code for this project represents my own, independent work. I 
have neither given nor received help on this exam from other
students."""

# John Rojas
# Calculate amount of carbon dioxide (CO2) that would result from burning several chemical samples.

#Initial input
num_samples = int(input('How many samples are being burned? '))

# Define function to add total of each mco2
total = 0

# Loop asks information based on initial input. Calculates MCO2 each time. Adds to total.
for i in range(num_samples):
    atomic_mass = float(input(f'What is the atomic mass for sample {i + 1} (in Da)? ')) 
    carbon = int(input(f'How many carbon atoms does sample {i + 1} contain per molecule? '))
    mass = float(input(f'What is the mass of sample {i + 1} (in g)? '))
    mco2 = (44.01 * mass * carbon) / atomic_mass
    total += mco2

# Prints in exponential form, rounded to 2 decimal places.
print('These samples will release {:.2e}'.format(total) ,'g CO2 when burned.')