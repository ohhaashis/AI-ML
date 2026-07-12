import json

### Load the data

def loadData(filename):

    with open(filename,"r") as f:
        data = json.load(f)

    return data

data = loadData("Data/store_data.json")

# print(data)
# print(type(data))

### Clean & structure the Data

def cleanData(data):

    text_to_num = {"one":1,"two":2,"three":3,"four":4,"five":5}
    cleanedData = []
    uniqueUsers = set()

    for user in data :
        
        # Clear Ratings - DATA consistency
        rawRatings = str(user["rating"].strip().lower())
        if(rawRatings in text_to_num):
            rawRatings = text_to_num[rawRatings]

        user["rating"]= rawRatings

        # Handle missing values

        rawAge = user.get("age")
        if(rawAge == None):
            user["age"] = None

        # De-Duplication

        if(user["name"].strip() in uniqueUsers):
            continue

        uniqueUsers.add(user["name"])
        
        cleanedData.append(user)
        
    print(cleanedData)
    return cleanedData        

cleanData(data)