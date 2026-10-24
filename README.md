# 🎵 Music Recommender Simulation — VibeMatch 1.0

## Project Summary

For my CodePath AI110 project, I developed VibeMatch 1.0, a Python-based music recommendation system that suggests songs based on a user's musical preferences.

My goal was to understand how platforms like Spotify and TikTok use data and algorithms to recommend content. I created a simplified content-based recommendation system that compares song characteristics with a user's preferred genre, mood, and energy level.

The program calculates a score for each song, ranks the songs from highest to lowest, and provides explanations for why certain songs were recommended.

I expanded the original music catalog from 10 to 20 fictional songs to include a wider variety of genres and moods. I also developed Python functions for loading the dataset, calculating recommendation scores, ranking songs, and explaining the results.

This project demonstrates how data can be transformed into personalized suggestions without requiring a complex machine learning model.

---

## How The System Works

My music recommender uses **content-based filtering**, which means it recommends songs by comparing their attributes to a user's preferences.

Unlike collaborative filtering, which uses the listening behavior of other users, my system focuses on the characteristics of individual songs.

### Song Features

Each `Song` object contains the following information:

- **ID:** A unique identifier for each song.
- **Title:** The song's name.
- **Artist:** The artist who created the song.
- **Genre:** The musical category, such as pop, rock, or jazz.
- **Mood:** The emotional feeling, such as happy, chill, or intense.
- **Energy:** The intensity of the song, measured from 0.0 to 1.0.
- **Tempo:** The speed of the music in beats per minute.
- **Valence:** How positive or negative the music sounds.
- **Danceability:** How suitable the music is for dancing.
- **Acousticness:** How acoustic the song is.

The initial scoring algorithm primarily uses genre, mood, and energy. Acousticness is also included when using the class-based `UserProfile`. The other numerical features are stored for possible future improvements.

### User Profile

The `UserProfile` class stores the following preferences:

- `favorite_genre`
- `favorite_mood`
- `target_energy`
- `likes_acoustic`

The command-line version uses a dictionary containing genre, mood, and energy.

For example, a user might prefer pop music, a happy mood, and an energy level of 0.8.

### My Algorithm Recipe

I designed a weighted scoring system to compare each song against the user's musical preferences.

| Feature | Scoring Rule |
|---|---|
| Genre | +2.0 points for an exact match |
| Mood | +1.0 point for an exact match |
| Energy | Up to +1.0 point based on similarity |
| Acousticness | Up to +0.5 points when the optional preference is supplied |

For energy similarity, I calculate the absolute difference between the song's energy and the user's target energy, then subtract that difference from 1.0.

For example, if a user prefers an energy level of 0.8 and a song has an energy level of 0.7, the energy similarity score is 0.9.

This is important because the algorithm rewards songs that are closer to the user's preferred energy rather than automatically favoring high-energy songs.

The maximum score is 4.0 using the three-feature command-line profile, or 4.5 when the optional acoustic preference is included.

### Recommendation Process

The program follows this process:

1. **Input:** Load the user's preferences and song information from `data/songs.csv`.
2. **Processing:** Compare each song against the user's preferences and calculate its score.
3. **Ranking:** Sort the songs from highest to lowest score.
4. **Output:** Display the top five songs with their scores and explanations.

The program uses two important functions:

- `score_song()` calculates the relevance score and returns explanations for an individual song.
- `recommend_songs()` evaluates every song, sorts the results, and returns the top recommendations.

I used `sorted()` instead of modifying the original list in place because I wanted to preserve the original song collection.

This modular structure makes it easier to change the scoring algorithm without rebuilding the entire program.

---

## Getting Started

### Setup

**1. Clone the GitHub repository**

```bash
git clone https://github.com/JoanneStars/ai110-module3show-musicrecommendersimulation-starter.git
cd ai110-module3show-musicrecommendersimulation-starter
```

This command assumes the repository has been forked under my GitHub account.

**2. Create a virtual environment**

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on macOS/Linux:

```bash
source .venv/bin/activate
```

**3. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

The requirements file contains pandas, pytest, and Streamlit. The current command-line recommender uses Python's built-in CSV module, while pytest supports automated testing.

**4. Run the music recommender**

```bash
python -m src.main
```

The program loads the song catalog, applies the default user preferences, and displays the highest-ranked recommendations.

### Running Tests

To run the automated tests:

```bash
python -m pytest tests/test_recommender.py -v
```

The drafted tests check:

- Whether matching songs appear higher in the ranking.
- Whether recommendations contain meaningful explanations.
- Whether the program respects the requested number of results.
- Whether requesting zero recommendations returns an empty list.

The tests must be run locally to confirm that they pass.

---

## Sample Recommendation Output

The following is the **calculated expected output** for the proposed 20-song dataset and default profile. It has not yet been verified against a local terminal run.

User preferences:

- Genre: pop
- Mood: happy
- Energy: 0.8

```text
Loaded songs: 20

Music Recommender Simulation
----------------------------
Favorite genre: pop
Favorite mood: happy
Target energy: 0.8

Top 5 Recommendations:

1. Sunrise City
   Score: 3.98
   Because: Genre match (+2.0)
   Because: Mood match (+1.0)
   Because: Energy similarity (+0.98)

2. Gym Hero
   Score: 2.87
   Because: Genre match (+2.0)
   Because: Energy similarity (+0.87)

3. Rooftop Lights
   Score: 1.96
   Because: Mood match (+1.0)
   Because: Energy similarity (+0.96)

4. Starlight Dance
   Score: 1.91
   Because: Mood match (+1.0)
   Because: Energy similarity (+0.91)

5. City Rhymes
   Score: 0.96
   Because: Energy similarity (+0.96)
```

These results illustrate how genre, mood, and energy influence the final rankings.

Sunrise City receives the highest score because it matches the preferred genre and mood and has an energy level close to the user's target.

Gym Hero ranks second because it matches the preferred genre, even though its mood is intense rather than happy.

This also demonstrates one possible limitation: the scoring system gives genre a greater influence than mood.

Before final submission, I will replace this calculated example with the actual terminal output.

---

## Experiments You Tried

### Experiment 1: Different Music Preferences

I selected three profiles to evaluate the behavior of the recommendation system.

| Profile | Genre | Mood | Target Energy |
|---|---|---|---|
| High-Energy Pop | pop | happy | 0.8 |
| Chill Lofi | lofi | chill | 0.4 |
| Intense Rock | rock | intense | 0.9 |

The purpose of this experiment is to observe how changes in musical preferences influence the ranking.

I expect the High-Energy Pop profile to favor upbeat pop songs, while the Chill Lofi profile should prefer slower and calmer songs.

The Intense Rock profile should favor songs with intense moods and higher energy levels.

Comparing these profiles will help determine whether the scoring logic distinguishes between different musical tastes.

### Experiment 2: Adjusting the Scoring Weights

My original scoring formula uses:

- Genre match: 2.0 points
- Mood match: 1.0 point
- Energy similarity: up to 1.0 point

For my planned experiment, I will reduce the genre weight to 1.0 point and increase the energy similarity weight to 2.0 points.

This change will test whether energy becomes more important than genre when ranking songs.

For example, a song from a different genre might move higher in the rankings if its energy is very close to the user's preference.

I will compare the original rankings against the modified rankings to determine whether the results become more varied or more appropriate for the user.

**Evaluation status:** The multiple-profile runs and weight-change experiment still need to be executed and their actual results documented.

---

## Limitations and Risks

One limitation of my project is that the dataset contains only 20 fictional songs. A real music platform has access to much larger catalogs and more detailed information about listening behavior.

My algorithm also does not learn from user interactions. It cannot track which songs a person skips, likes, repeats, or adds to playlists.

Another limitation is that genre receives more weight than mood or energy. This could cause the program to repeatedly recommend music from a user's preferred genre instead of introducing songs from different genres.

This behavior can contribute to a **filter bubble**, where users repeatedly encounter similar content and have fewer opportunities to discover different types of music.

The dataset also contains unequal numbers of songs from different genres. A genre represented by only one song has fewer opportunities to appear in the recommendations than a genre with several songs.

Finally, the algorithm loads tempo, valence, and danceability but does not currently use them to calculate rankings.

These limitations show that recommendation systems are influenced by both the quality of the data and the rules used to make decisions.

---

## Reflection

This project helped me understand how recommendation systems use information about users and content to generate personalized results. Before working on this project, I knew that platforms like Spotify suggested music based on what people enjoyed, but I did not fully understand how individual features could be compared mathematically. I learned how Python can load data from a CSV file, calculate weighted scores, rank results, and provide explanations for recommendations.

One of the most interesting things I learned was that a small change in the scoring formula can affect which songs appear at the top. It also helped me understand how algorithmic bias can develop, especially when one feature receives more importance than others. I used AI assistance to help organize my code, develop the scoring functions, and identify limitations, but I also learned the importance of reviewing the logic and verifying results through testing. If I continued working on this project, I would like to make the recommender interactive and allow users to adjust their musical preferences while exploring different genres.

For more detailed documentation, see my [Model Card](model_card.md).

---

## Technologies Used

- **Python:** Main programming language.
- **CSV module:** Reads and processes song data.
- **Python dataclasses:** Represents songs and user preferences.
- **Pytest:** Automated testing.
- **Git and GitHub:** Version control and project submission.
- **VS Code:** Development environment.
- **ChatGPT:** AI assistance for development, explanations, and documentation.

---

## Project Purpose

VibeMatch 1.0 was developed as part of the CodePath AI110 course to demonstrate the relationship between data, algorithms, recommendation rankings, and algorithmic bias.

It is an educational simulation and not a production-ready AI music platform.