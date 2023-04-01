class Restaurants:
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    df = pd.read_csv(r"Nutrition_Value_Dataset.csv")
    result=[]
    df['Hunger Level'] = 0
    df['Protein Level'] = 0

    X = df[['Energy (kCal)']]  # Feature matrix
    y = df['Hunger Level']  # Target variable
    w = df[['Protein (g)']]
    z = df['Protein Level']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.95, random_state=2)
    w_train, w_test, z_train, z_test = train_test_split(w, z, test_size=0.95, random_state=2)

    y_train = [2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 3, 2, 1, 2, 3, 1, 3, 1, 1, 1, 2, 1, 1, 1, 3, 3]
    z_train = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3]

    lr = LinearRegression()

    # Train the model on the training set
    lr.fit(X_train, y_train)

    # Predict the hunger level for the test set
    y_pred = lr.predict(X_test)

    lr.fit(w_train, z_train)

    # Predict the Protein Level for the test set
    z_pred = lr.predict(w_test)

    y_pred = y_pred.round()

    y_pred = y_pred.astype('int')

    z_pred = z_pred.round()

    z_pred = z_pred.astype('int')

    df.loc[X_test.index, 'Hunger Level'] = y_pred
    df.loc[X_train.index, 'Hunger Level'] = y_train
    df.loc[w_test.index, 'Protein Level'] = z_pred
    df.loc[w_train.index, 'Protein Level'] = z_train

    def recommend_fast_food(self, a, b, c):
        self.df["Hunger Level"]=self.df["Hunger Level"].astype(str).astype(int)
        self.df["Protein Level"] = self.df["Protein Level"].astype(str).astype(int)
        return self.df
        # count = 0
        # t = self.df['Company']
        # p = self.df['Product']
        # for i in range(self.df.shape[0]):
        #     if t[i].lower() == a.lower() and b == 3 and self.y[i] >= 3 and self.z[i] >= 1 and c == "y":
        #         print(p[i])
        #         self.result.append(p[i])
        #         count += 1
        #     elif t[i].lower() == a.lower() and b == 3 and self.y[i] >= 3 and self.z[i] >= 0 and c == "n":
        #         print(p[i])
        #         self.result.append(p[i])
        #         count += 1
        #     elif t[i].lower() == a.lower() and self.y[i] == b and self.z[i] >= 0 and c == "n":
        #         print(p[i])
        #         self.result.append(p[i])
        #         count += 1
        #     elif t[i].lower() == a.lower() and self.y[i] == b and self.z[i] >= 1 and c == "y":
        #         print(p[i])
        #         self.result.append(p[i])
        #         count += 1
        # if count == 0:
        #     s = "No Meals available in "+a+" for given requirements."
        #     print(s)
        #     # self.result.append(s)
        # else:
        #     return self.result


# a = input("Enter Restaurant Name:")
# b = int(input("Enter Hunger Level (1 to 3):"))
# c = (input("Do you want to eat a high Protein Meal (y to n):"))


# print(a, "\nHunger Level:", b, "\nHigh Protein:", c, "\n\n")

