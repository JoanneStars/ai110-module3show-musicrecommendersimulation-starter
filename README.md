## What I Changed, What I Found Out, and What Worked

### What I Changed

During this project, I expanded the original music recommendation system and performed several experiments to better understand how recommendation systems work.

I expanded the dataset from 10 songs to 15 songs by adding:

- Velvet Nights
- Wildfire Heart
- Golden Fields
- Neon Bounce
- Ocean Dreams

The additional songs increased the diversity of genres, moods, and audio feature values available to the recommender.

I also modified the scoring system. The original version placed more emphasis on genre and less emphasis on energy. As part of my experiment, I changed the weights:

Original Weights

- Genre: 2.0
- Energy: 1.5

Modified Weights

- Genre: 1.0
- Energy: 3.0

I also created three user profiles to test how different preferences affect recommendations:

- High-Energy Pop
- Chill Lofi
- Deep Intense Rock

Finally, I added recommendation explanations so users could see how each recommendation score was calculated.

### What I Found Out

The most interesting discovery was that recommendation results can change significantly when feature weights are changed.

When energy became more important than genre, songs with energy levels close to a user's preferred value became much more competitive in the rankings.

For example, Storm Runner appeared in the High-Energy Pop recommendations even though it is a rock song. Its energy level was very close to the user's target value, which helped it receive a high score.

Another finding was that recommendations changed when user preferences changed.

The High-Energy Pop profile ranked Sunrise City first.

The Chill Lofi profile ranked Library Rain first.

The Deep Intense Rock profile ranked Storm Runner first.

This demonstrated that the recommender adapts to different user preferences rather than producing identical recommendations for every user.

I also found that some songs appeared in multiple recommendation lists. Neon Bounce appeared in several profiles because its numerical feature values were reasonably close to multiple users' target preferences even though its genre did not always match.

### What Worked

Several parts of the project worked successfully.

The scoring system was able to combine:

- Genre
- Mood
- Energy
- Valence
- Danceability
- Acousticness

into a single recommendation score.

The recommendation explanation feature worked well because it showed users how the final score was generated.

Creating multiple user profiles was also successful because it allowed me to evaluate whether recommendations changed based on user preferences.

Expanding the dataset added more variety and produced more interesting recommendation results.

The automated tests also passed after adding the required package configuration.

Final test result:

```text
====================== 2 passed ======================
```

### Challenges

One challenge was configuring Python imports so that the automated tests could locate the source files correctly.

To solve this issue, I added:

```text
src/__init__.py
```

This allowed Python to recognize the src directory as a package and enabled pytest to execute successfully.

Another challenge was balancing recommendation weights. Increasing energy importance improved personalization for energetic users, but it also allowed songs from different genres to rank highly. This demonstrated how feature weighting can introduce bias into recommendation systems.

### Key Takeaway

The biggest lesson from this project was that recommendation systems do not randomly choose content. They convert user preferences and item features into numerical scores and then rank the results.

Even small changes to feature weights can significantly change recommendation outcomes. This helped me understand why recommendation system design decisions are important and how different priorities can influence what users ultimately see.