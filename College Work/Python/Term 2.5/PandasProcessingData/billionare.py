import pandas as pd
import matplotlib as plt


def richest_person():
    df = pd.read_csv("Term 2.5\PandasProcessingData\Billionaires Statistics Dataset.csv")
    df_rp = df.loc[df["finalWorth"] == df["finalWorth"].max()]
    name = df_rp["personName"].to_string(index=False)
    worth = df_rp["finalWorth"].to_string(index=False)
    print(f"The richest person in the world is {name} with a final worth of ${worth}!")

def create_list(b):
    c=[]
    for a in b:
        c.append(a)
    return c

def top_10():
    df = pd.read_csv("Term 2.5\PandasProcessingData\Billionaires Statistics Dataset.csv")
    t10 = df.head(11)
    names = create_list(t10["personName"])
    worths = create_list(t10["finalWorth"])
    for x in range(1,11):
        print(f"{x}. {names[x]} \n   Worth: {worths[x]}\n")

def best_country():
    df = pd.read_csv("Term 2.5\PandasProcessingData\Billionaires Statistics Dataset.csv")
    country_finalvalue = {}

    for country in df["country"].unique():
        df_country = df.loc[df["country"] == country]
        total_worth = df_country["finalWorth"].sum()
        country_finalvalue[country] = total_worth

    best_country = max(country_finalvalue, key=country_finalvalue.get)
    print(f"The best country is {best_country} with a total wealth of {country_finalvalue[best_country]}")





def menu():
    print("#############\nMenu\n1. Richest Person \n2. Top 10 \n3. Best Country\n#############\n")
    while True:
        try:
            # Enter user choice
            user_choice = input("Enter choice: ")
            user_choice = int(user_choice)
            # Process user choice
            if user_choice == 1:
                richest_person()
                break
            elif user_choice == 2:
                top_10()
                break
            elif user_choice == 3:
                best_country()
                break
            else:
                print("Please input a correct option.")

        except ValueError as error:
            print(f"ERROR: {error}")

def main():
    menu()
    while True:
        user_choice = input("Run again? (y/n) ")
        if user_choice == "y":
            menu()
        elif user_choice == "n":
            break
        else:
            print("Incorrect option please choose y or n.")

if __name__ == "__main__":
    main()