# Imports
import pandas as pd


# Dataset
df = pd.read_csv('Teen_Mental_Health_Dataset.csv')
print(df.head())



# This class will handle taking the username and information
class User:
    def __init__(self):
        self.username = username = input("Please enter your Name: " )
        self.email = email = input("Please enter your E-mail: " )
        self.contact = contact = input("Please enter your contact: " )

        return
    
# rrrrr = User()
# print(rrrrr.email)


class DataExploratory:

    # def
    # df.head()
    # print(df['author'].unique)
    # print(" ")
    # aaaa = df['category'].unique

    # aaaa.value_count()

    # # df.info() 

    pass
 


#  This class will handle cleaning of the dataset 
class Cleaning:

    pass
    


#  This class will handle analysisy of the cleaned dataset 
class Analysis:

    pass







def main():
    

    pass





if __name__ == "__main__":
    main()