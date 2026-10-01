import pandas as pd

patients = {
    "Patient ID": [101, 102, 103, 104, 105],
    "Patient Name": ["Amit", "Riya", "Rahul", "Sneha", "Pooja"],
    "Age": [65, 45, 72, 58, 68],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Cold", "Blood Pressure"],
    "Medical Charges": [60000, 25000, 80000, 30000, 55000]
}

df = pd.DataFrame(patients)

print("Patients above 60:")
print(df[df["Age"] > 60])

print("\nAverage Medical Charge:")
print(df["Medical Charges"].mean())

print("\nMaximum Medical Charge:")
print(df["Medical Charges"].max())

print("\nPatients with charges greater than 50000:")
print(df[df["Medical Charges"] > 50000])