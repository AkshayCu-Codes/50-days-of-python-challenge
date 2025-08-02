import pandas as pd

# Define the data as a dictionary
data = {
    'Year': [2009, 2002, 2009, 2010, 2009],
    'Title': ['Brothers', 'Spider-Man', 'WatchMen', 'Inception', 'Avatar'],
    'Genre': ['Drama', 'Sci-fi', 'Drama', 'Sci-fi', 'Fantasy']
}

# Create the DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)