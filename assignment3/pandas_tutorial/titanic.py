import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            # cspell:disable-next-line
            "Braund, Mr. Owen Harris",
            "Allen, Mr, William Henry",
            # cspell:disable-next-line
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

ages = pd.Series([22, 35, 58], name="Age")

max_age = df["Age"].max()
max_age2 = ages.max()
desc = df.describe()
# OUTPUT:
#              Age
# count   3.000000
# mean   38.333333
# std    18.230012
# min    22.000000
# 25%    28.500000
# 50%    35.000000
# 75%    46.500000
# max    58.000000

# titanic_data = pd.read_csv(
#     "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv",
#     skipinitialspace=True,
# )

# titanic_data.to_csv('titanic.csv', index=False)

titanic = pd.read_csv("./titanic.csv")
head8 = titanic.head(8)
titanic.dtypes

# Print Output:
# PassengerId      int64
# Survived         int64
# cspell:disable-next-line
# Pclass           int64
# Name            object
# Sex             object
# Age            float64
# SibSp            int64
# Parch            int64
# Ticket          object
# Fare           float64
# Cabin           object
# Embarked        object
# dtype: object
titanic.to_excel("./titanic.xlsx", sheet_name="passengers", index=False)
titanic["Age"].mean()
titanic[["Age", "Fare"]].median()
# print(titanic[["Age", "Fare"]].describe())

titanic_summary_age_fare = titanic.agg(
    {"Age": ["min", "max", "median", "skew"], "Fare": ["min", "max", "median", "mean"]}
)

titanic_grouped_sex_age = titanic[["Sex", "Age"]].groupby("Sex").mean()
titanic.groupby("Sex").mean(numeric_only=True)
titanic_grouped_sex_age_i = titanic.groupby("Sex")["Age"].mean()

print(titanic_grouped_sex_age)
print(titanic_grouped_sex_age_i)
