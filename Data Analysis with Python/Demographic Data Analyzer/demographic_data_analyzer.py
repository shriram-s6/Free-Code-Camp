import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men = df[df['sex'] == 'Male']
    average_age_men = round(men['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors = df[df['education'] == 'Bachelors']
    percentage_bachelors = (bachelors.shape[0] / df['education'].shape[0]) * 100
    percentage_bachelors = round(percentage_bachelors, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[(df['education'] == 'Masters') | (df['education'] == 'Doctorate') |
                          (df['education'] == 'Bachelors')]
    lower_education = df[(df['education'] != 'Masters') & (df['education'] != 'Doctorate') &
                         (df['education'] != 'Bachelors')]

    # percentage with salary >50K
    higher_edu_rich = higher_education[higher_education['salary'] == '>50K'].shape[0]
    lower_edu_rich = lower_education[lower_education['salary'] == '>50K'].shape[0]

    higher_education_rich = (higher_edu_rich / higher_education.shape[0]) * 100
    higher_education_rich = round(higher_education_rich, 1)
    lower_education_rich = (lower_edu_rich / lower_education.shape[0]) * 100
    lower_education_rich = round(lower_education_rich, 1)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == df['hours-per-week'].min()]
    min_workers_50k = num_min_workers[num_min_workers['salary'] == '>50K'].shape[0]

    rich_percentage = (min_workers_50k / num_min_workers.shape[0]) * 100
    rich_percentage = round(rich_percentage, 1)

    # What country has the highest percentage of people that earn >50K?
    countries = df[['native-country', 'salary']]
    countries_list = countries['native-country'].value_counts().index.to_list()
    countries_dict = {}
    count = 0
    for country in countries_list:
        countries_dict[country] = countries['native-country'].value_counts()[count]
        count += 1

    highest_earners = countries[countries['salary'] == '>50K']
    highest_earners_list = highest_earners['native-country'].value_counts().index.to_list()
    highest_earners_dict = {}
    counter = 0
    for earner in highest_earners_list:
        highest_earners_dict[earner] = highest_earners['native-country'].value_counts()[counter]
        counter += 1
    highest_earning_country_percentage = 0
    highest_earning_country = ''
    for country, count in highest_earners_dict.items():
        percentage = (highest_earners_dict[country] / countries_dict[country]) * 100
        percentage = round(percentage, 1)

        if percentage > highest_earning_country_percentage:
            highest_earning_country_percentage = percentage
            highest_earning_country = country


    # Identify the most popular occupation for those who earn >50K in India.
    highest_paid_india = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation']
    top_IN_occupation = highest_paid_india.value_counts().index.to_list()[0]

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
