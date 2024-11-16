import random

# Function to generate a random temperature between 30 and 40 degrees Celsius
def generate_random_temperature():
    return random.uniform(30, 40)

# Example usage
random_temperature = generate_random_temperature()
print(f"Random Temperature: {random_temperature:.2f} °C")
