import random
import math

# This signed weight is the neural value -- the "knowledge"
# At first we're Sgt Shultz: we know no-thing!
sign = 1 if (random.random() > 0.5) else -1
weight = 10000 * random.random() * sign

initial_weight = weight

# We seek a neuron that predicts a value 0f 0.8 for an input of 0.5
goal = 0.8

# Demo. Most neurons take an input array instead of a scalar.
input_value = 0.5

diff_fuzz = 1e-25

# This is the actual single-input neuron.
def neuron(input):
    return weight * input

# "Supervised" learning:
counter = 0
circuit_breaker = int(1e5)

for x in range(circuit_breaker):
    prediction = neuron(input_value)

    # Adjust weight using diff slope and sign
    diff = prediction - goal
    correction = diff * input_value
    weight -= correction

    counter += 1
    print(str(counter) + ". Prediction " + str(prediction) + " using weight " + str(weight) + ". Seeking goal " + str(goal))

    circuit_breaker -= 1
    if diff ** 2 < diff_fuzz:
        break


print("Initial weight: " + str(initial_weight))
print("Learned weight: " + str(weight))

print ("\nUse it: request outputs as function of fuzzy neural inputs")
counter = 0
vals = (0.9, 2.2, -10.0, 0.480, 0.485, 0.490, 0.495, 0.500, 0.550, 0.510, 0.515)
for x in range(0, len(vals)):
    counter += 1
    input = vals[x]
    print( str(counter) + ". Prediction " + str(neuron(input)) + " from input " + str(input) )

