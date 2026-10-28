import json
import sys

MINIMUM_ACCURACY = 0.85

with open("metrics.json", "r") as file:
    metrics = json.load(file)

accuracy = metrics["accuracy"]

print(f"Model accuracy: {accuracy:.2%}")
print(f"Minimum required accuracy: {MINIMUM_ACCURACY:.0%}")

if accuracy < MINIMUM_ACCURACY:
    print("QUALITY GATE FAILED")
    sys.exit(1)

print("QUALITY GATE PASSED")
