# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

VibeMatch Music Recommender 1.0

---

## 2. Intended Use

VibeMatch is a simple music recommendation system designed to recommend songs based on a user's stated music preferences.

The model assumes that a user has preferences for a favorite genre, favorite mood, and target values for features such as energy, valence, danceability, and acousticness.

This project is intended for classroom exploration rather than real-world users. It demonstrates how a recommendation system can use data and scoring rules to rank songs.

---

## 3. How the Model Works

The recommender compares each song with a user's preferences.

Each song contains information about its genre, mood, energy, tempo, valence, danceability, and acousticness. The user profile contains a favorite genre, favorite mood, and target values for several numerical features.

The model gives points when a song's genre or mood matches the user's preferences. It also gives similarity points when the song's numerical features are close to the user's target values.

### Final Scoring Rules

- Genre match: +1.0 point
- Mood match: +1.0 point
- Energy similarity: up to +3.0 points
- Valence similarity: up to +1.0 point
- Danceability similarity: up to +0.5 points
- Acousticness similarity: up to +0.5 points

My final scoring experiment reduced the genre weight from 2.0 points to 1.0 point and increased the energy similarity weight from 1.5 points to 3.0 points.

This made energy level more important in the final rankings.

After calculating a score for every song, the model sorts the songs from highest score to lowest score and returns the top five recommendations.

---

## 4. Data

The dataset contains 15 songs.

The catalog includes a variety of genres including:

- Pop
- Lofi
- Rock
- Ambient
- Jazz
- Synthwave
- Indie Pop
- R&B
- Metal
- Folk
- Hip-Hop
- Reggae

The dataset also contains different moods including:

- Happy
- Chill
- Intense
- Relaxed
- Moody
- Focused
- Romantic
- Peaceful
- Confident

I expanded the original dataset from 10 songs to 15 songs by adding:

- Velvet Nights — R&B / romantic
- Wildfire Heart — metal / intense
- Golden Fields — folk / peaceful
- Neon Bounce — hip-hop / confident
- Ocean Dreams — reggae / relaxed

The dataset is still very small compared with a real music streaming service. It does not include lyrics, user listening history, skips, playlists, favorite artists, or long-term user behavior.

---

## 5. Strengths

The recommender works well when a user's preferences are represented by the available song features.

Examples:

### High-Energy Pop

The recommender ranked Sunrise City first because it matched the user's preferred genre and mood while also closely matching the numerical target values.

### Chill Lofi

The recommender ranked Library Rain and Midnight Coding highly because both songs matched the user's preferred genre, mood, and energy level.

### Deep Intense Rock

The recommender ranked Storm Runner first because it matched the user's rock preference, intense mood preference, and target energy level.

Another strength is that recommendation explanations are provided for every result. Users can see exactly how each recommendation score was calculated rather than receiving a list of unexplained recommendations.

The system is also deterministic, meaning the same inputs always produce the same outputs.

---

## 6. Limitations and Bias

The biggest limitation is the small dataset. With only 15 songs, the recommender cannot represent the wide variety of music available in real-world music services.

The system only uses:

- Genre
- Mood
- Energy
- Valence
- Danceability
- Acousticness

It does not understand:

- Lyrics
- Artist style
- Personal memories
- Cultural context
- Listening history
- Favorite artists
- Playlist behavior

### Energy Bias

My weight experiment increased energy importance from 1.5 points to 3.0 points.

Because of this change, songs with similar energy values may rank highly even when they belong to a different genre.

Example:

Storm Runner can appear in High-Energy Pop recommendations even though it is a rock song.

### Dataset Bias

Some genres and moods are represented by only one song while other categories contain multiple songs.

This can make the system more likely to recommend some categories than others.

### Feature Selection Bias

The model assumes that the chosen numerical features are sufficient for representing music taste.

In reality, listeners often choose music based on factors that cannot be captured by simple numerical audio features.

---

## 7. Evaluation

I evaluated the recommender using three user profiles:

### High-Energy Pop

Preferences:

- Favorite Genre: Pop
- Favorite Mood: Happy
- High target energy

Result:

- Sunrise City ranked first.

### Chill Lofi

Preferences:

- Favorite Genre: Lofi
- Favorite Mood: Chill
- Low target energy

Result:

- Library Rain ranked first.
- Midnight Coding ranked second.

### Deep Intense Rock

Preferences:

- Favorite Genre: Rock
- Favorite Mood: Intense
- Very high target energy

Result:

- Storm Runner ranked first.
- Wildfire Heart ranked highly.

### Weight Shift Experiment

I reduced genre importance and increased energy importance:

Original:

- Genre = 2.0
- Energy = 1.5

Modified Version:

- Genre = 1.0
- Energy = 3.0

Results:

- High-energy songs became much more competitive.
- Storm Runner ranked highly for users outside the rock genre.
- Wildfire Heart moved higher in recommendation rankings.
- Recommendation results became more sensitive to energy preferences.

### Automated Testing

I also validated the implementation using the provided automated tests:

```bash
python -m pytest
```

Final result:

```text
======================
2 passed
======================
```

This confirmed that the object-oriented recommender classes functioned correctly.

---

## 8. Future Work

If I continued this project, I would improve the recommender in several ways.

### Add More Features

Additional features could include:

- Tempo weighting
- Instrumentalness
- Speechiness
- Loudness

### Expand User Profiles

Users could define:

- Multiple favorite genres
- Multiple moods
- Favorite artists
- Listening history

### Improve Recommendation Diversity

Future versions could intentionally avoid recommending songs that are too similar to one another.

### Better Explanations

The recommender could generate natural-language explanations that focus on the strongest reasons for each recommendation.

### Collaborative Filtering

A future version could incorporate collaborative filtering by learning from user behavior patterns and recommending songs liked by users with similar tastes.

---

## 9. Personal Reflection

This project taught me that recommendation systems can be created using relatively simple scoring rules.

My biggest learning experience was seeing how user preferences and feature weights affect recommendation rankings. Small changes to the scoring formula had a noticeable impact on which songs were recommended.

The weight-shift experiment was especially interesting because changing only two weights substantially altered the rankings. Increasing energy importance caused songs from different genres to become more competitive when their energy levels closely matched the user's preferences.

I also learned the importance of testing and debugging. During development I resolved issues involving imports, package structure, variable names, dictionary access, and project configuration. Adding `src/__init__.py` allowed Python to correctly recognize the project structure and run pytest successfully.

Using AI tools helped me explore recommendation system concepts, build scoring logic, generate user profiles, debug errors, and compare experimental results. However, I still needed to manually verify recommendations, test the code, adjust weights, and confirm that the outputs matched my expectations.

Overall, this project helped me better understand how recommendation systems transform user preferences and item features into scores, rankings, and personalized recommendations.