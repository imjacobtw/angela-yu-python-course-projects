from bs4 import BeautifulSoup
import os
import pandas as pd
import requests

PAYSCALE_REPORT_BASE_URL = (
    "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
)
PAYSCALE_CSV_FILE_NAME = "payscale_salaries_by_college_major.csv"
SALARY_COLUMNS = ["Early Career Pay", "Mid-Career Pay"]


def get_page_data(url):
    page_table = pd.read_html(url)
    page_df = page_table[0]

    for column in page_df.columns:
        page_df[column] = page_df[column].str.removeprefix(f"{column}:")

        if column in SALARY_COLUMNS:
            page_df[column] = (
                page_df[column].replace("[$,]", "", regex=True).astype(int)
            )

    return page_df


# Scrape data on the initial run and read cached data on subsequent runs.
if not os.path.isfile(f"./{PAYSCALE_CSV_FILE_NAME}"):
    df = get_page_data(PAYSCALE_REPORT_BASE_URL)
    response = requests.get(PAYSCALE_REPORT_BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    last_page = int(soup.select(".pagination__btn")[-2].text)

    for page in range(2, last_page + 1):
        url = f"{PAYSCALE_REPORT_BASE_URL}/page/{page}"
        page_df = get_page_data(url)
        df = pd.concat([df, page_df], ignore_index=True)

    df.dropna()
    df.to_csv(PAYSCALE_CSV_FILE_NAME)

df = pd.read_csv(PAYSCALE_CSV_FILE_NAME)

# What college major has the highest mid-career salary?
highest_mid_career_salary_row_index = df["Mid-Career Pay"].idxmax()
highest_mid_career_salary_major = df["Major"][highest_mid_career_salary_row_index]
print(highest_mid_career_salary_major)

# How much do graduates with this major earn?
highest_mid_career_salary = df["Mid-Career Pay"].max()
print(highest_mid_career_salary)

# Which college major has the lowest starting salary?
lowest_early_career_salary_row_index = df["Early Career Pay"].idxmin()
lowest_early_career_salary_major = df["Major"][lowest_early_career_salary_row_index]
print(lowest_early_career_salary_major)

# How much do graduates of that major earn after university?
lowest_early_career_salary = df["Early Career Pay"].min()
print(lowest_early_career_salary)

# Which college major has the lowest mid-career salary?
lowest_mid_career_salary_row_index = df["Mid-Career Pay"].idxmin()
lowest_mid_career_salary_major = df["Major"][lowest_mid_career_salary_row_index]
print(lowest_mid_career_salary_major)

# How much can people expect to earn with this degree?
lowest_mid_career_salary = df["Mid-Career Pay"].min()
print(lowest_mid_career_salary)

# What ius the average mid-career salary of all bachelor's degrees?
average_salary_by_degree_type = df.groupby("Degree Type").mean(numeric_only=True)
bachelors_average_salary = int(
    average_salary_by_degree_type["Mid-Career Pay"]["Bachelors"]
)
print(bachelors_average_salary)
