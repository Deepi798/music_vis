import pandas as pd
import matplotlib.pyplot as plt

# Data dictionary
data = {
    'song_name': [
        'Euphoria', 'Still With You', 'My Time', 'Dreamers', '3D', 
        'Standing Next to You', 'Seven', 'Stay Alive', 'Closer to You', 'Begin'],
    'Artist(s)_name': ['Jungkook'] * 10,
    'Artist_count': [1] * 10,
    'lanuched_year': [2018, 2020, 2020, 2022, 2023, 2023, 2023, 2022, 2023, 2016],
    'lanuched_month': [8, 6, 3, 11, 10, 9, 7, 2, 9, 11],
    'lanuched_day': [24, 4, 9, 20, 6, 18, 14, 11, 5, 9],
    'in_spotify_ranking': [1, 5, 7, 6, 3, 4, 2, 9, 8, 10],  
    'in_spotify_streams': [
        1800000000, 1200000000, 1100000000, 800000000, 700000000, 
        600000000, 1500000000, 500000000, 350000000, 450000000],  
    'in_apple_ranking': [2, 4, 5, 8, 3, 6, 1, 10, 12, 9],  
    'in_apple_streams': [
        1900000000, 1400000000, 1200000000, 850000000, 900000000, 
        750000000, 1300000000, 400000000, 350000000, 800000000], 
    'in_deezer_ranking': [6, 9, 10, 12, 5, 8, 4, 11, 13, 10],  
    'in_deezer_streams': [
        800000000, 600000000, 500000000, 400000000, 350000000, 
        300000000, 450000000, 250000000, 200000000, 500000000],  
    'in_shazam_ranking': [3, 2, 5, 7, 4, 6, 1, 8, 9, 4],
    'in_shazam_streams': [
        500000, 400000, 350000, 300000, 250000, 200000, 600000, 150000, 100000, 180000],
    'in_youtube_ranking': [1, 2, 3, 5, 7, 8, 2, 10, 9, 4],
    'in_youtube_streams': [
        2500000000, 2000000000, 1800000000, 1300000000, 1100000000,
        1000000000, 2300000000, 800000000, 600000000, 850000000], 
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate total streams by summing all platforms
df['total_streams'] = df['in_spotify_streams'] + df['in_apple_streams'] + df['in_deezer_streams'] + df['in_shazam_streams'] + df['in_youtube_streams']

# Sort the DataFrame by total streams in descending order
df = df.sort_values(by='total_streams', ascending=False)

# Create a bar plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot bars for each platform with different colors
ax.bar(df['song_name'], df['in_spotify_streams'], label='Spotify Streams', alpha=0.6, color='green', width=0.15, align='center')
ax.bar(df['song_name'], df['in_apple_streams'], label='Apple Music Streams', alpha=0.6, color='blue', width=0.15, align='edge')
ax.bar(df['song_name'], df['in_deezer_streams'], label='Deezer Streams', alpha=0.6, color='purple', width=0.15, align='edge')
ax.bar(df['song_name'], df['in_shazam_streams'], label='Shazam Streams', alpha=0.6, color='orange', width=0.15, align='edge')
ax.bar(df['song_name'], df['in_youtube_streams'], label='YouTube streams', alpha=0.6, color='red', width=0.15, align='edge')

# Labels and title
ax.set_xlabel('Song Name')
ax.set_ylabel('Streams')
ax.set_title("Jungkook's Famous Solo Album Songs")
ax.legend()

# Annotate stream counts above each bar
for i, song in enumerate(df['song_name']):
    ax.text(i, df['in_spotify_streams'].iloc[i] + 0.05 * max(df['in_spotify_streams']), f'{df["in_spotify_streams"].iloc[i]:,.0f}', ha='center', color='black', fontsize=10)
    ax.text(i, df['in_apple_streams'].iloc[i] + 0.05 * max(df['in_apple_streams']), f'{df["in_apple_streams"].iloc[i]:,.0f}', ha='center', color='black', fontsize=10)
    ax.text(i, df['in_deezer_streams'].iloc[i] + 0.05 * max(df['in_deezer_streams']), f'{df["in_deezer_streams"].iloc[i]:,.0f}', ha='center', color='black', fontsize=10)
    ax.text(i, df['in_shazam_streams'].iloc[i] + 0.05 * max(df['in_shazam_streams']), f'{df["in_shazam_streams"].iloc[i]:,.0f}', ha='center', color='black', fontsize=10)
    ax.text(i, df['in_youtube_streams'].iloc[i] + 0.05 * max(df['in_youtube_streams']), f'{df["in_youtube_streams"].iloc[i]:,.0f}', ha='center', color='black', fontsize=10)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Make the plot layout tight to avoid overlapping
plt.tight_layout()

# Show the plot
plt.show()
