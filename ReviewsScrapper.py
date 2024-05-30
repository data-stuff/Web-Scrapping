# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:11:30 2024

@author: Wairimu Kariba
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# interested variables
user_names = []
num_stars_list = []
review_dates = []
review_texts = []

# Set user-agent string
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"

# Set options for Chrome webdriver with user-agent
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent}")

# URL of the TripAdvisor page with reviews
url = "https://italiarecensioni.com/piemont/rock-burger-san-salvario-1033863"

# Initialize Chrome webdriver with options
driver = webdriver.Chrome(options=options)

# Maximize window
driver.maximize_window()

# Open the URL
driver.get(url)
time.sleep(10)

try:
    # Wait for the cookie consent banner to appear (adjust timeout and locator as needed)
    cookie_banner = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "fc-choice-dialog"))
    )

    # Find the "OK" button and click it to accept cookies
    ok_button = cookie_banner.find_element(By.XPATH, "//button[@aria-label='OK']")
    ok_button.click()

except:
    # If there's no cookie consent banner, continue scraping directly
    pass

# Find all review containers on the page
review_containers = driver.find_elements(By.CLASS_NAME, "review")

# Loop through each review container
for review_element in review_containers:
    try:
        # Extract user info
        user_info = review_element.find_element(By.CLASS_NAME, "user-txt-info")
        user_name = user_info.find_element(By.TAG_NAME, "span").text
    except:
        user_name = "User info not found"

    try:
        # Extract stars
        stars_element = review_element.find_element(By.CLASS_NAME, "stars-row")
        star_icons = stars_element.find_elements(By.CSS_SELECTOR, "i.fa-star")
        num_stars = len(star_icons)
    except:
        num_stars = "Stars not found"

    try:
        # Extract review date
        review_date = review_element.find_element(By.CLASS_NAME, "reviewdate").text
    except:
        review_date = "Review date not found"

    try:
        # Extract review text
        review_text = review_element.find_element(By.CLASS_NAME, "review-data").text
    except:
        review_text = "Review text not found"

    # Append the extracted data to the respective lists
    user_names.append(user_name)
    num_stars_list.append(num_stars)
    review_dates.append(review_date)
    review_texts.append(review_text)

# Close the WebDriver
driver.quit()

# Print the stored data
print("User Names:", user_names)
print("Num Stars:", num_stars_list)
print("Review Dates:", review_dates)
print("Review Texts:", review_texts)

import pandas as pd

# Create a dictionary with the scraped data
data_rb = {
    "User Names": user_names,
    "Num Stars": num_stars_list,
    "Review Dates": review_dates,
    "Review Texts": review_texts
}

# Create a DataFrame
df = pd.DataFrame(data_rb)

# Print the DataFrame
print(df)

import numpy as np

# Define the placeholders
placeholders = ["User info not found", "Stars not found", "Review date not found", "Review text not found"]

# Replace placeholders with NaN
cleaned_df = df.replace(placeholders, np.nan)

# Print the cleaned DataFrame
print(cleaned_df)

excel_file_path = r'C:\Users\Wairimu Kariba\Downloads\sansa.df.xls'
cleaned_df.to_excel(excel_file_path, index=False)
