# 🏏 IPL Data Analysis

# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('IPL_Matches.csv')

# Display first few rows
print("📄 Dataset Preview:")
print(df.head())

# Basic info
print("\n📊 Dataset Info:")
print(df.info())

# Check for missing values
print("\n🔍 Missing Values:")
print(df.isnull().sum())

# --- Data Analysis ---

# 1️⃣ Most successful teams
top_teams = df['winner'].value_counts().head(5)
print("\n🏆 Top 5 Teams by Wins:")
print(top_teams)

plt.figure(figsize=(8,5))
sns.barplot(x=top_teams.values, y=top_teams.index, palette='coolwarm')
plt.title('Top 5 Teams by Wins')
plt.xlabel('Number of Wins')
plt.ylabel('Team')
plt.show()

# 2️⃣ Toss decision impact
toss_decision = df['toss_decision'].value_counts()
plt.figure(figsize=(6,4))
sns.barplot(x=toss_decision.index, y=toss_decision.values, palette='viridis')
plt.title('Toss Decision Analysis')
plt.xlabel('Decision')
plt.ylabel('Count')
plt.show()

# 3️⃣ Matches won by toss winners
toss_winner_wins = df[df['toss_winner'] == df['winner']].shape[0]
total_matches = df.shape[0]
percentage = (toss_winner_wins / total_matches) * 100
print(f"\n🎯 Matches won by toss winners: {percentage:.2f}%")

# 4️⃣ Most Player of the Match awards
top_players = df['player_of_match'].value_counts().head(5)
print("\n⭐ Top 5 Players of the Match Awards:")
print(top_players)

plt.figure(figsize=(8,5))
sns.barplot(x=top_players.values, y=top_players.index, palette='mako')
plt.title('Top 5 Players with Most MOM Awards')
plt.xlabel('Awards')
plt.ylabel('Player')
plt.show()

print("\n✅ IPL Analysis Completed Successfully!")
