import pandas as pd
from student_data import data

df = pd.DataFrame(data)
df["Rank"] = df["Marks"].rank(ascending=False).astype(int)
df["Grade"] = pd.cut(df["Marks"], bins=[-1, 59, 69, 79, 89, 100], labels=["D", "C", "B", "A", "A+"])
df["Result"] = df["Marks"].apply(lambda marks: "Pass" if marks >= 40 else "Fail")
merit_list = df[["Rank", "RollNo", "Name", "Department", "Marks", "Grade", "Result"]].sort_values("Marks", ascending=False)
print(merit_list)
merit_list.to_excel("student_merit_list.xlsx", index=False)
print("Saved as student_merit_list.xlsx")
