import pandas as pd

df = pd.read_csv(
    r'C:\Users\cengizhan.kose\Documents\Python\python-homework\question-4\Salaries.csv')
print("=====Entire List=====")
print(df.to_string())
print("=====First 5 Data=====")
print(df.head(5))
print("=====Last 5 Data=====")
print(df.tail(5))
print("=====Random 10 Data=====")
print(df.sample(n=10))
print("=====Summarize=====")
print(df.describe())
