import pandas as pd
import re

data = {
    "Name": ["Alice", None, "Charlie", "David"],
    "Age": [24, None, 22, 35],
    "Salary": [50000, 60000, None, None],
}
df = pd.DataFrame(data)

df_dropped = df.dropna()
#     Name   Age   Salary
# 0  Alice  24.0  50000.0

df_filled = df.fillna({"Name": "Unknown", "Age": df["Age"].mean(), "Salary": 0})
#       Name   Age   Salary
# 0    Alice  24.0  50000.0
# 1  Unknown  27.0  60000.0
# 2  Charlie  22.0      0.0
# 3    David  35.0      0.0

# (\w+[\w\d\.\-]*)
# Must start with word (\w+)
# after that there can be something else
# Can have however many digits, letters, dashes, underscores or dots (* = 0 or more)
gmail = re.compile(r"(\w+[\w\d\.\-]*)@gmail.com")
search_target = "Boa-Dreamcode.public@gmail.com"

match = gmail.match(search_target)

# print(match.group()) ## or print(match.group(0))
# all expression
# Boa-Dreamcode.public@gmail.com

# print(match.group(1))
# just first group of parenthesis (\w+[\w\d\.\-]*)
# Boa-Dreamcode.public

new_search_target = "My email is Boa-Dreamcode.public@gmail.com, what is yours?"
match = gmail.search(new_search_target)
# print(match.group(1))
# Boa-Dreamcode.public

df = pd.DataFrame(
    {"phone_number": ["(123) 456-7890", "+1-555-123-4567", "555.456.7890"]}
)

#       phone_number
# 0   (123) 456-7890
# 1  +1-555-123-4567
# 2     555.456.7890

df["phone_number_clean"] = df["phone_number"].str.replace(r"\D", "", regex=True)

#       phone_number phone_number_clean
# 0   (123) 456-7890         1234567890
# 1  +1-555-123-4567        15551234567
# 2     555.456.7890         5554567890

df1 = pd.DataFrame(
    {
        "html_content": [
            "<p>This is a paragraph.</p>",
            "<div>Some <strong>bold</strong> text</div>",
        ]
    }
)

#                                  html_content
# 0                 <p>This is a paragraph.</p>
# 1  <div>Some <strong>bold</strong> text</div>

# Match any character (.), zero or more times (*), but be non-greedy (?)
# .*? is non-greedy (also called lazy), so it stops at the first possible match

df1["text_only"] = df1["html_content"].str.replace(r"<.*?>", "", regex=True)
# df1["text_only"] = df1["html_content"].str.replace(r"<.*?>", "", regex=True)
#                                  html_content             text_only
# 0                 <p>This is a paragraph.</p>  This is a paragraph.
# 1  <div>Some <strong>bold</strong> text</div>        Some bold text

df2 = pd.DataFrame(
    {
        "email": [
            "john.doe@example.com",
            "jane_smith@my-domain.org",
            "user123@anotherdomain.net",
        ]
    }
)

df2["domain"] = df2["email"].str.extract(r"@(\w+[\w\.-]*)")
#                        email             domain
# 0       john.doe@example.com        example.com
# 1   jane_smith@my-domain.org      my-domain.org
# 2  user123@anotherdomain.net  anotherdomain.net

# ?P<name> syntax is used in regular expressions to create named capturing groups.
series = pd.Series(["Tom-25-USA", "Anna-30-UK", "John-22-Canada"])
pattern = r"(?P<Name>\w+)-(?P<Age>\d+)-(?P<Country>\w+)"
result = series.str.extract(pattern)

#    Name Age Country
# 0   Tom  25     USA
# 1  Anna  30      UK
# 2  John  22  Canada

df3 = pd.DataFrame(
    {"email": ["test@example.com", "invalid-email", "hello.d@my.domain.org"]}
)
valid_emails = df3[df3["email"].str.contains(r"^\w+[\w\.-]+@\w+[\w\.-]+\.\w+$")]
#                    email
# 0       test@example.com
# 2  hello.d@my-domain.org

orders = [
    "Order 1: 2x Cheddar, 1x Gouda",
    "Order 2: 3x Stilton, 2x Rye Crackers",
    "Order 3: 2x Saltines",
    "Order 4: 1x Camembert, 2x Jahrlsberg",
    "Order 5: 2x Gouda, 2x Rye Crackers",
    "Order 6: 1x Ritz, 1x Jahrlsberg",
    "Order 7: 1x Parmesan, 1x Brie",
    "Order 8: 3x Saltine Crackers",
    "Order 9: 2x Rye Crackers",
    "Order 10: 2x Mozzarella, 1x Cheddar",
    "Order 11: 1X Water Crackers" "Order 12: 3x Blue Cheese",
    "Order 13: 1x Triscuits",
    "Order 14: 1x Butter Crackers, 2x Multigrain Crackers",
    "Order 15: 1x Feta",
    "Order 16: 1x Havarti",
    "Order 17: 2x Wheat Crackers",
    "Order 18: 1x Ricotta",
    "Order 19: 1x Garlic Herb Crackers",
]
orders = pd.Series(orders)
favored_cheeses = orders.str.contains(
    r"Cheddar|" r"Stilton|" r"Camembert|" r"Jahrlsberg|" r"Gouda",
    case=False,
    regex=True,
)
favored_crackers = orders.str.contains(
    r"Ritz|" r"Triscuit|" r"Rye Crackers|" r"Multigrain Crackers|" r"Water Crackers",
    case=False,
    regex=True,
)

# print(orders[favored_cheeses & favored_crackers])
# print(orders[~favored_cheeses])
# 1    Order 2: 3x Stilton, 2x Rye Crackers
# 4      Order 5: 2x Gouda, 2x Rye Crackers
# 5         Order 6: 1x Ritz, 1x Jahrlsberg
# dtype: object
# 2                                  Order 3: 2x Saltines
# 6                         Order 7: 1x Parmesan, 1x Brie
# 7                          Order 8: 3x Saltine Crackers
# 8                              Order 9: 2x Rye Crackers
# 10    Order 11: 1X Water CrackersOrder 12: 3x Blue C...
# 11                               Order 13: 1x Triscuits
# 12    Order 14: 1x Butter Crackers, 2x Multigrain Cr...
# 13                                    Order 15: 1x Feta
# 14                                 Order 16: 1x Havarti
# 15                          Order 17: 2x Wheat Crackers
# 16                                 Order 18: 1x Ricotta
# 17                    Order 19: 1x Garlic Herb Crackers
# dtype: object

df4 = pd.DataFrame(
    {"col_2021": [1, 2, 3], "col_2022": [4, 5, 6], "col_other": [7, 8, 9]}
)
# Select columns that end with digits
df_year = df4.filter(regex=r"\d+$")
#    col_2021  col_2022
# 0         1         4
# 1         2         5
# 2         3         6

data = {
    "Name": ["Alice", "Bob", "Alice", "David"],
    "Age": [24, 27, 24, 35],
    "Salary": [50000, 60000, 50000, 80000],
}
df5 = pd.DataFrame(data)

df_no_duplicates = df5.drop_duplicates()

# DataFrame with duplicates removed:
#     Name  Age  Salary
# 0  Alice   24   50000
# 1    Bob   27   60000
# 3  David   35   80000

data = {"Color": ["Red", "Blue", "Green", "Blue", "Red"]}
df5 = pd.DataFrame(data)

# Label encoding: Convert categories to numbers
df5["Color_Label"] = df5["Color"].map({"Red": 1, "Blue": 2, "Green": 3})

# One-Hot Encoding: Create binary columns for each category
df_encoded = pd.get_dummies(df5["Color"], prefix="Color")

#    Color_Blue  Color_Green  Color_Red
# 0       False        False       True
# 1        True        False      False
# 2       False         True      False
# 3        True        False      False
# 4       False        False       True

data = {"City": ["New York", "new york", "San Francisco", "San fran"]}
df6 = pd.DataFrame(data)

# Standardize text data (convert to lowercase and strip spaces)
df6["City"] = df6["City"].str.lower().str.strip()

# Use Regex to replace shorthand names
df6["City"] = df6["City"].replace({"san fran": "san francisco"})
#             City
# 0       new york
# 1       new york
# 2  san francisco
# 3  san francisco

data = {"Age": [24, 35, 30, 45, 60]}
df7 = pd.DataFrame(data)

# Binning Age into age groups
bins = [0, 30, 60, 100]
labels = ["Young", "Middle-Aged", "Old"]
df7["Age_Group"] = pd.cut(df7["Age"], bins=bins, labels=labels)
