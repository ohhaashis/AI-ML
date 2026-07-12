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
        
    #print(cleanedData)
    return cleanedData        

data = cleanData(data)


### Get meaningful insights from data 

def getInsights(data):

    # avg-rating

    tot_rating = 0

    for user in data:
        tot_rating+= float(user["rating"])
    print(f"Avg-Rating = {tot_rating/len(data)}")

    # percentage os user with poor ratings
    
    poor_ratings = 0

    for user in data:
        if(float(user["rating"])<(tot_rating/len(data))):
            poor_ratings += 1

    print(f"%age of users with poor rating is : {(poor_ratings/len(data))*100}%")

getInsights(data)

### Build recommendation Feature 

def getRecommendations(data):

    recommendations = []

    for user in data:

        curr_rec = {}
        curr_rec["name"] = user["name"]
        if(float(user["rating"])>=4):
            curr_rec["brand"] = "Apple"
        else:
            curr_rec["brand"] = "Samsung"

        recommendations.append(curr_rec)

        return recommendations

getRecommendations(data)