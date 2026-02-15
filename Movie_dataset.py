import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets
data = pd.read_csv('movies_dataset.csv')
# change release_date to datetime
data['release_date'] = pd.to_datetime(data['release_date'], errors='coerce')
# create a new column for release year
data['release_year'] = data['release_date'].dt.year

# count the number of movies by language
language_counts = data['original_language'].value_counts().head(10).reset_index()
language_counts.columns = ['language', 'Movie_Count']
# create a bar plot of the top 10 languages
plt.figure(figsize=(12, 7))
sns.barplot(data=language_counts, x='language', y='Movie_Count', palette='viridis')
plt.title('Top 10 Movie Languages in Dataset')

plt.tight_layout()
plt.savefig('top_languages.png')
plt.close()

# select only movies that have received a sufficient number of votes
plt.figure(figsize=(10, 6))
filtered_data = data[data['vote_count'] > 10]
# create a scatter plot of Popularity and Vote Average
sns.scatterplot(x='vote_average', y='popularity', data=filtered_data, alpha=0.5)
plt.title('Relationship between Popularity and Vote Average')

plt.tight_layout()
plt.savefig('popularity_vs_vote_average.png')
#plt.show()
plt.close()

# Count the number of films released each year since 2000
plt.figure(figsize=(12, 6))
yearly_growth = data[data['release_year'] >= 2000]['release_year'].value_counts().sort_index()
yearly_growth.plot(kind='line', marker='o', color='orange')
plt.title('Movies Released per Year Since 2000')
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.savefig('yearly_growth.png')
#plt.show()
plt.close()
