🎵 Music Recommender Simulation
Project Summary

This project is a small music recommendation system built in Python. It uses information about songs and a user's taste preferences to calculate recommendation scores. The system compares each song with the user's preferences and then ranks the songs from highest score to lowest score.

The recommender uses both categorical features, such as genre and mood, and numerical features, such as energy, valence, danceability, and acousticness. The goal is to create a simple version of how a real recommendation system can use data to predict what a user might enjoy.

How the System Works

Real-world recommendation platforms can use many types of user data, including likes, skips, listening history, playlists, and repeated plays. They can also use information about the content itself, such as genre, mood, tempo, and other audio features.

Two common approaches are collaborative filtering and content-based filtering.

Collaborative filtering looks at the behavior of other users with similar tastes. Content-based filtering looks at the features of items a user already likes and recommends other items with similar features.

My simulation mainly uses a content-based approach because it compares each song's attributes with a specific user taste profile.

Song Features

Each song in the system contains the following features:

id

title

artist

genre

mood

energy

tempo_bpm

valence

danceability

acousticness

User Preferences

The user profiles use the following preferences:

favorite_genre

favorite_mood

target_energy

target_valence

target_danceability

target_acousticness

The recommender scores every song in the catalog. It then sorts the songs from highest score to lowest score and returns the top 5 recommendations.

Algorithm Recipe

The original scoring system gave genre a larger weight and energy a smaller weight. I changed those weights as part of my experiment.

Current Scoring Rules

The version I tested uses:

Genre match: +1.0 point

Mood match: +1.0 point

Energy similarity: up to +3.0 points

Valence similarity: up to +1.0 point

Danceability similarity: up to +0.5 points

Acousticness similarity: up to +0.5 points

For numerical features, the system rewards songs that are closer to the user's preferred value.

The similarity calculation is based on the distance between the song's value and the user's target value. A value closer to the target receives more points.

For example, if a user wants an energy level of 0.90, a song with an energy level close to 0.90 receives a higher energy similarity score than a song with an energy level far away from 0.90.

A song does not automatically receive more points just because its numerical value is higher. It receives more points when its value is closer to the user's target.

Scoring and Ranking

The scoring rule judges one song.

The ranking rule applies that scoring rule to every song in the catalog, sorts the results by total score, and returns the highest-scoring songs.

Data Flow
User Preferences
       ↓
Score Every Song
       ↓
Calculate Feature Similarity
       ↓
Add Genre + Mood + Numerical Scores
       ↓
Sort Songs by Total Score
       ↓
Top 5 Recommendations

Getting Started
Setup

Create a virtual environment (optional but recommended):

python -m venv .venv


On Mac or Linux:

source .venv/bin/activate


On Windows:

.venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt

Run the Recommender

Run the program with:

python -m src.main

Running Tests

The project includes tests for the object-oriented recommender classes.

Run the tests with:

python -m pytest


The final test run completed successfully:

====================== 2 passed in 0.03s ======================


I also added src/__init__.py so that Python can correctly recognize src as a package when running the tests.

Dataset

The original dataset contained 10 songs. I expanded it to 15 songs to give the recommender more variety.

The additional songs include:

Velvet Nights — R&B / romantic

Wildfire Heart — metal / intense

Golden Fields — folk / peaceful

Neon Bounce — hip-hop / confident

Ocean Dreams — reggae / relaxed

The dataset contains a variety of genres, moods, energy levels, and other numerical audio features.

Sample Recommendation Output

The recommender was tested with three different user profiles:

High-Energy Pop

Chill Lofi

Deep Intense Rock

High-Energy Pop
Sunrise City - Score: 6.62
Because: genre match (+1.0), mood match (+1.0), energy similarity (+2.76), valence similarity (+0.96), danceability similarity (+0.45), acousticness similarity (+0.46)

Gym Hero - Score: 5.84
Because: genre match (+1.0), energy similarity (+2.91), valence similarity (+0.97), danceability similarity (+0.49), acousticness similarity (+0.47)

Rooftop Lights - Score: 5.41
Because: mood match (+1.0), energy similarity (+2.58), valence similarity (+0.99), danceability similarity (+0.46), acousticness similarity (+0.38)

Neon Bounce - Score: 4.54
Because: energy similarity (+2.67), valence similarity (+0.88), danceability similarity (+0.49), acousticness similarity (+0.49)

Storm Runner - Score: 4.53
Because: energy similarity (+2.97), valence similarity (+0.68), danceability similarity (+0.38), acousticness similarity (+0.50)

Chill Lofi
Library Rain - Score: 6.96
Because: genre match (+1.0), mood match (+1.0), energy similarity (+3.00), valence similarity (+1.00), danceability similarity (+0.49), acousticness similarity (+0.47)

Midnight Coding - Score: 6.70
Because: genre match (+1.0), mood match (+1.0), energy similarity (+2.79), valence similarity (+0.96), danceability similarity (+0.49), acousticness similarity (+0.45)

Focus Flow - Score: 5.83
Because: genre match (+1.0), energy similarity (+2.85), valence similarity (+0.99), danceability similarity (+0.50), acousticness similarity (+0.49)

Spacewalk Thoughts - Score: 5.59
Because: mood match (+1.0), energy similarity (+2.79), valence similarity (+0.95), danceability similarity (+0.41), acousticness similarity (+0.44)

Coffee Shop Stories - Score: 4.75
Because: energy similarity (+2.94), valence similarity (+0.89), danceability similarity (+0.47), acousticness similarity (+0.46)

Deep Intense Rock
Storm Runner - Score: 6.75
Because: genre match (+1.0), mood match (+1.0), energy similarity (+2.88), valence similarity (+0.92), danceability similarity (+0.47), acousticness similarity (+0.47)

Wildfire Heart - Score: 5.88
Because: mood match (+1.0), energy similarity (+2.97), valence similarity (+0.95), danceability similarity (+0.46), acousticness similarity (+0.49)

Gym Hero - Score: 5.43
Because: mood match (+1.0), energy similarity (+2.94), valence similarity (+0.63), danceability similarity (+0.36), acousticness similarity (+0.50)

Night Drive Loop - Score: 4.16
Because: energy similarity (+2.40), valence similarity (+0.91), danceability similarity (+0.43), acousticness similarity (+0.42)

Neon Bounce - Score: 4.05
Because: energy similarity (+2.52), valence similarity (+0.72), danceability similarity (+0.34), acousticness similarity (+0.47)

Experiments You Tried

I tested three different user profiles:

High-Energy Pop

Chill Lofi

Deep Intense Rock

The results changed when the user profile changed. This shows that the same song catalog can produce different recommendations depending on what the user prefers.

High-Energy Pop

The High-Energy Pop profile ranked Sunrise City first. It matched the user's pop genre and happy mood while also having numerical features that were close to the user's targets.

Storm Runner also appeared in the top five even though it is not a pop song. Its energy level was extremely close to the user's target, which helped it receive a high score after the energy weight was increased.

Chill Lofi

The Chill Lofi profile ranked Library Rain first and Midnight Coding second. Both songs matched the lofi genre and chill mood preferences and also had strong numerical similarities.

Deep Intense Rock

The Deep Intense Rock profile ranked Storm Runner first because it matched the rock genre and intense mood while also having a very high energy similarity score.

Wildfire Heart also scored highly because its energy was very close to the user's target.

One interesting result was that Neon Bounce appeared in multiple profiles even though it did not match their preferred genres. This happened because its numerical features were reasonably close to several users' target values.

Weight Shift Experiment

I tested a weight shift experiment by:

Reducing the genre weight from 2.0 points to 1.0 point

Increasing the energy similarity weight from 1.5 points to 3.0 points

The purpose of this experiment was to see what would happen when energy became more important than genre.

Results

The results showed that energy became much more influential in the rankings.

For example, in the High-Energy Pop profile, Storm Runner ranked in the top five because its energy similarity was very high, even though it was a rock song instead of a pop song.

In the Deep Intense Rock profile, Storm Runner and Wildfire Heart scored very well because both had very high energy similarity.

The experiment demonstrated that changing feature weights can significantly change recommendation results.

The new weighting makes the recommender more sensitive to a user's desired energy level, but it also makes genre less important.

This means the system may recommend songs from unexpected genres when their numerical features are a strong match.

Limitations and Risks

This recommender has several limitations.

Small Dataset

The dataset contains only 15 songs. A real recommendation system would use a much larger catalog and much more information about users.

Limited Features

The system does not understand lyrics, artist style, song meaning, listening history, or personal context. It only compares the features included in the dataset.

Genre Bias

The weight experiment reduced the genre score from 2.0 to 1.0. This means genre is now less influential than it was in the original version.

A song from a different genre can now outrank a genre match if its numerical features are much closer to the user's preferences.

Energy Bias

Because energy now has a maximum weight of 3.0 points, the recommender strongly favors songs that are close to the user's target energy.

This can sometimes cause songs with a very similar energy level to rank highly even when they do not match the user's favorite genre or mood.

Limited Understanding of Musical Taste

People do not always have consistent preferences. Someone might enjoy a specific song because of its lyrics, memories, artist, cultural background, or situation.

This simple system cannot understand those factors.

Evaluation

I evaluated the recommender by creating three different user profiles and comparing the resulting recommendation lists.

The profiles were:

High-Energy Pop

Chill Lofi

Deep Intense Rock

I looked for whether the recommendations made sense based on each profile's genre, mood, and numerical targets.

The recommendations generally matched the intended preferences.

For example:

High-Energy Pop ranked Sunrise City highly.

Chill Lofi ranked Library Rain and Midnight Coding highly.

Deep Intense Rock ranked Storm Runner first.

High-energy songs became more competitive after increasing the energy weight.

Songs could still appear in multiple profiles when their numerical features were similar to different users' targets.

I also ran the automated tests using python -m pytest.

The final test result was:

2 passed


This confirmed that the required object-oriented recommender classes passed the provided tests.

Strengths

The recommender has several strengths for a simple classroom simulation.

It is easy to understand because the scoring rules are explicit.

It gives an explanation for why each song received its score.

It uses multiple song features instead of relying on only genre.

Different user profiles produce different recommendation rankings.

The weights can be changed to experiment with how different preferences affect recommendations.

The system is deterministic, so the same inputs produce the same results.

The explanation feature is especially useful because users can see which characteristics contributed to a recommendation.

Future Work

If I continued the project, I would improve the recommender in several ways.

Add More Features

I could add tempo as a scoring feature because tempo can help distinguish different types of music.

I could also include additional audio features such as instrumentalness, speechiness, or loudness.

Add More Songs

A larger dataset would provide more variety and make the recommendations more useful.

Improve Recommendation Diversity

The recommender could prevent the top five results from being too similar to each other. This could help users discover different styles of music.

Better User Profiles

Users could have multiple preferences instead of one favorite genre and one favorite mood.

For example, a user might enjoy both pop and rock or have different preferences depending on the situation.

Collaborative Filtering

A future version could use listening behavior from multiple users and recommend songs based on patterns among users with similar tastes.

Better Explanations

The explanation system could provide more natural-language reasons for recommendations rather than only listing the numerical score contributions.

Personal Reflection

This project taught me that recommendation systems can be built from relatively simple rules.

My biggest learning moment was seeing how changing a user's target values changed the ranking of the songs. I learned that a recommender is not simply choosing songs randomly. It is turning user preferences and song data into scores and then using those scores to create a ranking.

The weight shift experiment was especially interesting because changing only two weights changed which songs became competitive. Increasing energy from 1.5 points to 3.0 points made high-energy songs much more important, while reducing genre from 2.0 points to 1.0 point allowed songs from other genres to rank higher.

Using AI tools helped me understand how to structure the scoring logic, debug Python errors, and think about different user profiles. I still needed to double-check the AI-generated code because small problems with indentation, variable names, dictionary keys, or package setup could stop the program from running.

I also learned that testing is important. After adding src/__init__.py, the automated tests successfully ran and both tests passed.

I was surprised that such a simple scoring system could still feel like a real recommendation engine. If I continued the project, I would add more songs, use more advanced similarity calculations, include tempo as a scoring feature, improve recommendation diversity, and eventually experiment with collaborative filtering.