import pandas as pd
from student_data import data

df = pd.DataFrame(data)
print(df.nlargest(3, "Marks"))
