# 🎧 Model Card: VibeMatch 1.0

## 1. Model Name

**VibeMatch 1.0 — Music Recommender Simulation**

VibeMatch is a Python-based music recommendation system that suggests songs based on a user's musical preferences.

## 2. Intended Use

I designed VibeMatch to simulate how music platforms recommend songs to users based on their interests. My program compares a user's favorite genre, mood, and preferred energy level with the attributes of songs in a dataset.

The purpose of this project is to understand how recommendation algorithms work and how they make decisions. This is an educational simulation created for my CodePath AI course, not a commercial music recommendation service.

The program assumes that the user has specific musical preferences and that songs matching those preferences will be more enjoyable.

## 3. How the Model Works

My program uses a content-based filtering algorithm. Instead of looking at what other people listen to, it focuses on the characteristics of individual songs.

I created a weighted scoring system that compares each song to a user's taste profile.

- **Genre match:** Adds 2 points when the song matches the user's favorite genre.
- **Mood match:** Adds 1 point when the song matches the user's preferred mood.
- **Energy similarity:** Adds up to 1 point depending on how close the song's energy is to the user's preference.
- **Acoustic preference:** In the class-based version, adds up to 0.5 points depending on whether the user prefers acoustic or non-acoustic music.

After calculating a score for every song, the program sorts the songs from highest to lowest and recommends the top five.

I improved the starter code by adding CSV data loading, numeric conversions, scoring logic, ranking, and explanations for each recommendation.

## 4. Data

My original dataset contained 10 songs. I expanded it to 20 fictional songs to give the recommender a wider variety of music to choose from.

The dataset includes genres such as pop, rock, metal, lofi, EDM, jazz, classical, hip-hop, R&B, reggae, and others.

Each song contains information about its title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness.

I wanted to include different types of music because not everyone enjoys the same genres or musical energy levels.

One limitation is that the catalog is small and uses simulated song attributes instead of real streaming data. It does not include a user's listening history, skips, likes, or playlists.

## 5. Strengths

One strength of my recommender is that it provides a clear explanation for why each song receives its score.

For example, someone who prefers high-energy rock should generally receive different recommendations from someone who prefers relaxing lofi music.

I also like that the scoring system considers energy similarity instead of automatically giving higher scores to songs with more energy.

This allows the program to recommend calmer music to users who prefer lower energy levels.

The ranking process is straightforward, and the weights can be adjusted to experiment with how recommendations change.

## 6. Limitations and Bias

One limitation I noticed in my scoring design is that genre receives more points than mood or energy, which can cause the recommender to favor a familiar genre even when another song has a better mood or energy match.

The system could create a filter bubble by repeatedly recommending music similar to what the user already likes, making it harder to discover different styles. Another limitation is that some genres only have one song in my dataset, so users who prefer those genres have fewer matching options.

My algorithm also does not use listening history or consider features such as tempo, valence, and danceability when ranking songs. These limitations mean the recommendations are useful for demonstrating the algorithm but do not fully represent a person's musical taste.

## 7. Evaluation

I designed three user profiles to evaluate how the recommender responds to different musical preferences:

- **High-Energy Pop:** Prefers pop music, a happy mood, and energy around 0.8.
- **Chill Lofi:** Prefers lofi music, a chill mood, and energy around 0.4.
- **Intense Rock:** Prefers rock music, an intense mood, and energy around 0.9.

I used these profiles to plan comparisons between energetic and relaxing music, along with differences between genre and mood preferences.

For the High-Energy Pop and Chill Lofi profiles, I expect the recommendations to differ because they prefer different genres and energy levels.

For the High-Energy Pop and Intense Rock profiles, both prefer energetic music, but their genre and mood preferences should change the rankings.

For the Chill Lofi and Intense Rock profiles, the difference in energy should strongly affect which songs receive higher similarity scores.

I also plan to experiment with lowering the genre weight and increasing the energy weight to see whether that produces more varied recommendations.

The program includes automated tests for recommendation order, explanation text, and the number of results returned. The final evaluation will include actual terminal results after running all three profiles.

## 8. Future Work

If I continued developing VibeMatch, I would improve it in three ways:

1. **Add listening history:** Track likes, skips, and previously played songs to learn more about user preferences.
2. **Improve recommendation diversity:** Include more songs and balance the results so the same genres do not dominate every recommendation.
3. **Include additional song features:** Use tempo, danceability, and valence to provide more detailed comparisons between songs.

I would also like to explore collaborative filtering, which could recommend songs based on what other users with similar tastes enjoy.

## 9. Personal Reflection

Working on this project helped me understand how recommendation systems can take information about a user and compare it with data to make personalized suggestions.

One of the biggest things I learned was how much a simple scoring formula can affect the final recommendations. Changing the importance of genre, mood, or energy can completely change which songs appear first.

I used AI to help me organize the Python functions, understand the scoring logic, and identify potential weaknesses in my approach. I also learned that I need to review the generated code and test it instead of assuming it works correctly.

What interested me most was realizing that even a basic algorithm can produce recommendations that feel personalized. It also made me think differently about platforms like Spotify and TikTok because the recommendations we see are influenced by the data and rules behind their systems.

If I expanded this project, I would like to make it more interactive and allow users to adjust their musical preferences to see how the recommendations change.