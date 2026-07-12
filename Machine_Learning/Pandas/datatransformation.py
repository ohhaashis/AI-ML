# Transforming Data ( Feature Engineering )

# apply()
# map()
# assign()
# replace(old,new)

## Feature engineering

# df2 = df.copy()

# df2["Tax"] = df2["income"].apply(lambda x : "20%" if x>= 50000 else "10%")

# print(df2)


# gender_map = {"Male":"M", "Female":"F" , "Unknown":"U"}

# df2 = df2["gender"].map(gender_map)

# print(df2)

# df2.assign(new_income = df2["income"]*1.1)

# df2["country"].replace("USA","US")

