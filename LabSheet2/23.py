import pandas as pd
from student_data import data

df = pd.DataFrame(data)
df['Bonus'] = 5
print(df)
