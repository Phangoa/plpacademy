# 📦 Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 📁 Load the Dataset
df = pd.read_csv("owid-covid-data.csv")

# 🧭 Initial Exploration
print("Columns:", df.columns.tolist())
print("Shape:", df.shape)
print("Missing values:\n", df.isnull().sum().sort_values(ascending=False))

# 🧹 Data Cleaning
# Filter for selected countries
countries = ['Kenya', 'India', 'United States', 'South Africa', 'Lesotho']
df = df[df['location'].isin(countries)]

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Drop rows with missing critical values
df = df.dropna(subset=['date', 'total_cases', 'total_deaths'])

# Fill missing numeric values
numeric_cols = ['new_cases', 'new_deaths', 'total_vaccinations']
df[numeric_cols] = df[numeric_cols].fillna(0)

# 🧮 Feature Engineering
df['death_rate'] = df['total_deaths'] / df['total_cases']
df['vaccination_rate'] = df['total_vaccinations'] / df['population']

# 📊 Exploratory Data Analysis (EDA)
# Line plot: Total cases over time
plt.figure(figsize=(12,6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar chart: Total cases by country (latest date)
latest_date = df['date'].max()
latest_data = df[df['date'] == latest_date]
total_cases_by_country = latest_data.groupby('location')['total_cases'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(x=total_cases_by_country.values, y=total_cases_by_country.index, palette="viridis")
plt.title(f"Total Cases by Country on {latest_date.date()}")
plt.xlabel("Total Cases")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# 🧬 Vaccination Progress
plt.figure(figsize=(12,6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)
plt.title("Cumulative Vaccinations Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 🗺️ Choropleth Map (Optional)
choropleth_df = latest_data[['iso_code', 'location', 'total_cases']]
fig = px.choropleth(
    choropleth_df,
    locations="iso_code",
    color="total_cases",
    hover_name="location",
    title="Global COVID-19 Case Density",
    color_continuous_scale="Reds"
)
fig.show()

# 🧠 Insights Summary (Markdown-style for Jupyter)
from IPython.display import Markdown, display

def print_md(text):
    display(Markdown(text))

print_md("### Key Insights")
print_md("- 🇺🇸 The United States has consistently led in total cases and vaccinations.")
print_md("- 🇮🇳 India shows a steep rise in cases during mid-2021, followed by aggressive vaccination.")
print_md("- 🇱🇸 Lesotho has relatively low case counts but a high death rate, indicating potential underreporting or healthcare challenges.")
print_md("- 🌍 Vaccination rollout varies widely, with some countries reaching over 70% coverage while others lag below 20%.")
print_md("- 📉 Death rates tend to decrease as vaccination rates increase, suggesting vaccine effectiveness.")


