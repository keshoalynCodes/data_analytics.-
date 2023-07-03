#checking if punkt package is up to date
import nltk
nltk.download("punkt")

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Read the UN Declaration of Human Rights text data
file_path = "data_analytics/natural_language_processing/projects/text_mining/datasets/un_declaration_hr_text_data.txt"
with open(r"C:\Users\kesho\Downloads\un_declaration_hr_text_data.txt") as file:
    text_data = file.read()

# Tokenize the text into individual words
stop_words = set(stopwords.words("english"))
words = word_tokenize(text_data.lower())
filtered_words = [word for word in words if word.isalpha() and word not in stop_words]

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(filtered_words))

# Create a bar plot of the top 25 frequent terms
word_counts = Counter(filtered_words)
top_words = dict(word_counts.most_common(25))
x_values = list(top_words.keys())
y_values = list(top_words.values())

# Plotting the bar plot
plt.figure(figsize=(12, 6))
plt.bar(x_values, y_values)
plt.xticks(rotation=90)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top 25 Frequent Terms in UN Declaration of Human Rights")
plt.tight_layout()

# Save the word cloud and bar plot images
output_folder = "data_analytics/natural_language_processing/projects/text_mining/output/"
wordcloud_path = output_folder + "word_cloud.png"
barplot_path = output_folder + "most_freq_terms.png"
wordcloud.to_file(wordcloud_path)
plt.savefig(barplot_path)

# Show the word cloud and bar plot
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

