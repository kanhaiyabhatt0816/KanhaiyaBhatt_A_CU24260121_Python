import pandas as pd
from student_data import data

df = pd.DataFrame(data)
print(df[df["Marks"] > 80])
