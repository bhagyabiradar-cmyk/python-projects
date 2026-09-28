import pandas as pd

data = {
    "Name": ["Asha", "Rahul", "Priya", "Kiran", "Sneha"],
    "Marks": [85, 35, 91, 28, 72]
}

df = pd.DataFrame(data)

# Find Pass or Fail
df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

print(df)