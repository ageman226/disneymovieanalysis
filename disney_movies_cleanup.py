import pandas as pd

# Read in the data
df = pd.read_csv('disney_movies.csv')

# Capitalize the first letter of each word in the movie_title column
df['movie_title'] = df['movie_title'].str.title().str.strip()

# Change the release_date column to a datetime object
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

#Fills in the missing values in the genre column with 'Unknown' and capitalizes the first letter of each word
df['genre'] = df['genre'].fillna('Unknown').str.capitalize()

# Fills in the missing values in the mpaa_rating column with 'Unknown' and capitalizes the first letter of each word
df['mpaa`_rating'] = df['mpaa_rating'].fillna('Not Rated', inplace=True)

#Changes the total_gross column to a numeric type and removes the commas then rounds the values to 2 decimal places
df['total_gross'] = pd.to_numeric(df['total_gross'])
df['total_gross'] = df['total_gross'].round(2)

#Changes the inflation_adjusted_gross column to a numeric type and removes the commas then rounds the values to 2 decimal places
df['inflation_adjusted_gross'] = pd.to_numeric(df['inflation_adjusted_gross'])
df['inflation_adjusted_gross'] = df['inflation_adjusted_gross'].round(2)

df.drop('mpaa`_rating', axis=1, inplace=True)

print(df.head())

df.to_csv('disney_movies_cleaned_best.csv', index=False)