import pandas as pd
import matplotlib as plt


def richest_person():
    df = pd.read_csv("Term 2.5\PandasProcessingData\Billionaires Statistics Dataset.csv")
    df_rp = df.loc[df["finalWorth"] == df["finalWorth"].max()]
    name = df_rp["personName"].to_string(index=False)
    worth = df_rp["finalWorth"].to_string(index=False)
    print(f"The richest person in the world is {name} with a final worth of ${worth}!")


def top_10():
    print("tt")

def best_country():
    print("bc")





def menu():
    print("#############\nMenu\n1. Richest Person 2. Top 10 3. Best Country")
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

        except:
            print("Please input a correct number.")


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