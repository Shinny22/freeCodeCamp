import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    df.info(verbose=True)
    df.head()

    # How many of each race are represented in this dataset? 
    # Answer: 
    race_count = df["race"].value_counts()

   
    # What is the average age of men? 
    # Answer: 
    average_age_men = df[df["sex"]=="Male"]["age"].mean()

    # What percentage of people have a Bachelor's degree? 
    # Answer: 
    nombre_bachelors = df[df["education"]=="Bachelors"].shape[0]
    total = df.shape[0]
    percentage_bachelors = (nombre_bachelors / total) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) earn more than 50K? 
    # Answer: 
    # What percentage of people without advanced education earn more than 50K? 
    # Answer: 
    nbre_higher_education= df[df["education"].isin(["Bachelors", "Masters", "Doctorate"]) & (df["salary"] == ">50K")].shape[0]
    total = df.shape[0]
    higher_education = (nbre_higher_education / total) * 100
    lower_education = None

    # percentage with salary >50K
    higher_education_rich = higher_education
    lower_education_rich = None

    # What is the minimum number of hours a person works per week (hours-per-week function)? 
    # Answer: 
    min_work_hours = df["hours-per-week"].min()

    # What percentage of people who work the minimum number of hours per week have a salary of >50K? 
    # Answer: 
    num_min_workers = df[df["hours-per-week"] == min_work_hours].shape[0]
    rich_percentage = (num_min_workers / df.shape[0]) * 100

    # Which country has the highest percentage of people earning >50K? 
    # Answer: 
    highest_earning_country = df[df["salary"] == ">50K"]["native-country"].value_counts().index[0]
    highest_earning_country_percentage = (df[(df["salary"] == ">50K") & (df["native-country"] == highest_earning_country)].shape[0] / df[df["native-country"] == highest_earning_country].shape[0]) * 100

    # Identify the most popular profession for those earning >50K in India. 
    # Answer: 
    top_IN_occupation = df[(df["salary"] == ">50K") & (df["native-country"] == "India")]["occupation"].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelor's degrees: {percentage_bachelors}%")
        print(f"Percentage with advanced education earning >50K: {higher_education_rich}%")
        print(f"Percentage without advanced education earning >50K: {lower_education_rich}%")
        print(f"Minimum work hours: {min_work_hours} hours/week")
        print(f"Percentage of rich among those working the least hours: {rich_percentage}%")
        print("Country with the highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich in the country: {highest_earning_country_percentage}%")
        print("Most popular professions in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


calculate_demographic_data()