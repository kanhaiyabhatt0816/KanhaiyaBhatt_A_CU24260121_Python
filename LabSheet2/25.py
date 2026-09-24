import pandas as pd
from student_data import data

df = pd.DataFrame(data)
df["Result"] = df["Marks"].apply(lambda marks: "Pass" if marks >= 40 else "Fail")
print(df[["Name", "Marks", "Result"]])
