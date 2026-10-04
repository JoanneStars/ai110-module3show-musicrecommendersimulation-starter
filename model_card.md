🎧 Model Card: Music Recommender Simulation
1. Model Name

VibeMatch Music Recommender 1.0

2. Intended Use

VibeMatch is a simple music recommendation system designed to recommend songs based on a user's stated music preferences.

The model assumes that a user has preferences for a favorite genre, favorite mood, and target values for features such as energy, valence, danceability, and acousticness.

This project is intended for classroom exploration rather than real-world users. It demonstrates how a recommendation system can use data and scoring rules to rank songs.

3. How the Model Works

The recommender compares each song with a user's preferences.

Each song contains information about its genre, mood, energy, tempo, valence, danceability, and acousticness. The user profile contains a favorite genre, favorite mood, and target values for several numerical features.

The model gives points when a song's genre or mood matches the user's preferences. It also gives similarity points when the song's numerical features are close to the user's target values.

My final scoring experiment reduced the genre weight from 2.0 points to 1.0 point and increased the energy similarity weight from 1.5 points to 3.0 points. This made energy level more important in the final rankings.

After calculating a score for every song, the model sorts the songs from highest score to lowest score and returns the top five recommendations.

4. Data

The dataset contains 15 songs.

The catalog includes a variety of genres, including:

Pop

Lofi

Rock

Ambient

Jazz

Synthwave

Indie pop

R&B

Metal

Folk

Hip-hop

Reggae

The dataset also contains different moods, including happy, chill, intense, relaxed, moody, focused, romantic, peaceful, and confident.

I expanded the original dataset from 10 songs to 15 songs by adding five songs:

Velvet Nights — R&B / romantic

Wildfire Heart — metal / intense

Golden Fields — folk / peaceful

Neon Bounce — hip-hop / confident

Ocean Dreams — reggae / relaxed

The dataset is still very small compared with a real music streaming service. It also does not include important information such as lyrics, listening history, skips, playlists, favorite artists, or the user's previous behavior.

5. Strengths

The recommender works well when a user's preferences are clearly represented by the available song features.

For example, the High-Energy Pop profile ranked Sunrise City highly because it matched the user's pop genre and happy mood while also having similar numerical features.

The Chill Lofi profile produced reasonable recommendations such as Library Rain, Midnight Coding, and Focus Flow because they matched the user's lofi preference and had appropriate energy levels.

The Deep Intense Rock profile ranked Storm Runner first because it matched both the rock genre and intense mood and had very high energy.

Another strength is that the explanations show why a song received its score. This makes the recommendations easier to understand than simply displaying a list of song titles.

6. Limitations and Bias

The biggest limitation is the small dataset. With only 15 songs, the model has a limited number of choices and cannot represent the full range of music preferences.

The model also does not understand lyrics, song meaning, artist style, cultural context, listening history, or personal experiences. It only uses the features included in the dataset.

The weight assigned to each feature can also create bias in the recommendations. In my final experiment, energy was given much more importance than genre. This caused high-energy songs from unexpected genres to move higher in the rankings.

For example, Storm Runner could rank highly for a user who prefers high-energy pop even though it is a rock song. This demonstrates how changing the scoring weights can unintentionally favor one feature over another.

Some genres and moods are also represented by only one song, while other genres such as pop and lofi have multiple songs. This can make the system more likely to recommend certain categories.

7. Evaluation

I evaluated the recommender using three different user profiles:

High-Energy Pop

Chill Lofi

Deep Intense Rock

I looked at whether the recommendations made sense based on each profile's genre, mood, and numerical preferences.

The results generally matched my expectations. The High-Energy Pop profile ranked Sunrise City first, the Chill Lofi profile ranked Library Rain first, and the Deep Intense Rock profile ranked Storm Runner first.

I also tested a weight-shift experiment. I reduced the genre weight from 2.0 to 1.0 and increased the energy similarity weight from 1.5 to 3.0.

This changed the recommendations noticeably. High-energy songs such as Storm Runner and Wildfire Heart became more competitive even when their genre did not match the user's favorite genre.

I also ran the automated tests for the recommender. The final test run completed successfully with 2 tests passed.

8. Future Work

If I continued developing this recommender, I would add more songs and more detailed user preferences.

I would add tempo as a scoring feature and allow users to specify their preferred tempo range. I would also consider favorite artists, listening history, skips, likes, and playlists.

Another improvement would be recommendation diversity. Instead of simply returning the five highest-scoring songs, the system could make sure the results are not too similar to one another.

The explanations could also be improved by clearly identifying the strongest reasons a song was recommended rather than listing every numerical similarity.

A more advanced version could combine content-based filtering with collaborative filtering. This could allow the system to learn from the behavior of users with similar musical tastes.

9. Personal Reflection

This project taught me that recommendation systems can be created using relatively simple scoring rules. I learned that a recommender takes user preferences and item data, converts them into scores, and then uses those scores to create a ranking.

One of the most interesting things I discovered was how much the recommendations changed when I changed the feature weights. Increasing the importance of energy caused high-energy songs from different genres to appear higher in the results. This helped me understand that the design of a recommendation algorithm can strongly affect what users see.

I also learned that debugging is an important part of building a program. I had to fix issues involving imports, indentation, variables, and dictionary keys before the program and tests worked correctly. The final result helped me understand how a simple recommendation system works and why real-world recommendation systems need much more data and more sophisticated methods.