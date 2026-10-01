import pandas as pd

ages = {
    101: 65,
    102: 45,
    103: 72,
    104: 58,
    105: 68
}

s = pd.Series(ages)

print("Patient Ages:")
print(s)

print("\nAverage Age:")
print(s.mean())

print("\nOldest Patient:")
print(s.idxmax(), s.max())

print("\nYoungest Patient:")
print(s.idxmin(), s.min())

print("\nPatients above 60 years:")
print(s[s > 60])