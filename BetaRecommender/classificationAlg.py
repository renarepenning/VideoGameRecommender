# %matplotlib inline
#!pip3 install openpyxl  # package to open xlsx files
#!pip3 install xlrd
#!pip3 install sklearn
import matplotlib.pyplot as plt
from scraping_igdb import get_token
from User import User
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
'''implement classification alg - KNN classifier'''
# will need code to translate game's name to id

features = ["name", "id", "involved_companies",
            "platforms", "key_words", "similar_games"]

# Get user name and ratings
new_user = User()
new_user.printUser()
userFeature = new_user.series

# open excel file --> EXCEL READING NOT WORKING?? ## allGames = pd.read_excel("IGDB_games_beta.xlsx")
allGames = pd.read_csv("IGDB_games_beta.csv")
allGames.columns = ["id", "name", "category", "genres", "themes",
                    "involved_companies", "platforms", "key_words", "similar_games", "release_dates", ]
# allGames.reindex("")
print(allGames)
# .head() wont work # https://stackoverflow.com/questions/62624980/vscode-python-pandas-dataframe-intellisense-doesnt-show-attributes-method

# Borrowed from CMPS3160 Lab08+09
X_train_dict = allGames[features].to_dict(orient="records")
X_new_dict = [{
    'name': new_user.name,
    'category': new_user.categories,
    'genre': new_user.genres,
    'console': new_user.platforms,
    'key_words': new_user.key_words,
}]
y_train = allGames["similar_games"]

# sci-kit preprocessing
vec = DictVectorizer(sparse=False)  # training dict --> vector
vec.fit(X_train_dict)
X_train = vec.transform(X_train_dict)
X_new = vec.transform(X_new_dict)

scaler = StandardScaler()  # scale training data
scaler.fit(X_train)
X_train_sc = scaler.transform(X_train)
X_new_sc = scaler.transform(X_new)

# Fit a 10-nearest neighbors model.
model = KNeighborsRegressor(n_neighbors=10)
model.fit(X_train_sc, y_train)
# Calculate the model predictions on the training data.
y_train_pred = model.predict(X_new_sc)
print("Prediction", y_train_pred)


'''# scraping IGDB
headers = get_token()
query = requests.post('https://api.igdb.com/v4/games', headers=headers)
'''
