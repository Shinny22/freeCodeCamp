import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    df.info(verbose=True)
    df.head()

    # Combien de chaque race sont représentés dans ce jeu de données? Il s'agit d'une série Pandas avec les noms des races comme étiquettes d'index.
    race_count = df["race"].value_counts()

   
    # What is the average age of men?
    average_age_men = df[df["sex"]=="Male"]["age"].mean()

    # Quel est le pourcentage de personnes qui ont un diplôme de Bachelor ?
    
    nombre_bachelors = df[df["education"]=="Bachelors"].shape[0]
    total = df.shape[0]
    percentage_bachelors = (nombre_bachelors / total) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?


    # with and without `Bachelors`, `Masters`, or `Doctorate`
    nbre_higher_education= df[df["education"].isin(["Bachelors", "Masters", "Doctorate"]) & (df["salary"] == ">50K")].shape[0]
    total = df.shape[0]
    higher_education = (nbre_higher_education / total) * 100
    lower_education = None

    # percentage with salary >50K
    higher_education_rich = higher_education
    lower_education_rich = None

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    rich_percentage = None

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

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