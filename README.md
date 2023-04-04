# Disney Movies Data Analysis

This project takes a CSV of Disney movies and cleans up the data using Python's Pandas library, then creates visualizations using Tableau to explore the relationships between movie genre, MPAA rating, and release year with their respective gross earnings.

## Code

The `disney_movies_cleaning.py` script reads in the `disney_movies.csv` file, cleans the data using various Pandas methods, and outputs a cleaned CSV file named `disney_movies_cleaned_best.csv`. The script includes the following cleaning steps:

- Capitalizes the first letter of each word in the `movie_title` column, then strips the whitespace from the end of each string
- Changes the `release_date` column to a datetime object
- Fills in the missing values in the `genre` column with 'Unknown' and capitalizes the first letter of each word
- Fills in the missing values in the `mpaa_rating` column with 'Not Rated' and capitalizes the first letter of each word
- Changes the `total_gross` and `inflation_adjusted_gross` columns to numeric type and removes commas, then rounds the values to 2 decimal places
- Drops the `mpaa_rating` column (since it was replaced with a cleaned version)

The cleaned data is then ready for visualization in Tableau.

## Visualization

The visualizations created in Tableau explore the relationships between movie genre, MPAA rating, and release year with their respective gross earnings. 

The visualizations:

![alt text](https://public.tableau.com/static/images/Di/DisneyMovies_16805966484460/Dashboard1/1_rss.png)

These visualizations provide insights into the Disney movies data and can help inform business decisions related to movie production and marketing.

## Conclusion

Overall, this project demonstrates how Python's Pandas library and Tableau can be used together to clean and visualize data in a meaningful way. The cleaned data and visualizations can be used to gain insights and make informed business decisions.
