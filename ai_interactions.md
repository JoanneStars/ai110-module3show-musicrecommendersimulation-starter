# AI Interactions Log

This document describes how I used AI assistance while developing my CodePath AI110 Music Recommender Simulation.

## Agentic Workflow (SF8)

**Status: Not attempted as an autonomous agent workflow.**

### What task did you give the agent?

I used ChatGPT as a coding assistant to help develop my Python music recommendation system. I asked for help improving my existing project files, implementing recommendation logic, and understanding how to test the program.

I did not use an autonomous AI agent to independently edit files or run commands.

### Prompts used

Some of my requests included:

- Help me fix my `main.py` for the music recommendation project.
- Review my `recommender.py` and implement the missing scoring and ranking functions.
- Check whether my `test_recommender.py` works with the recommendation algorithm.
- Help me expand my `songs.csv` dataset to include more genres and moods.
- Help me complete my Model Card based on the project's actual implementation.

### What did the AI generate or change?

ChatGPT suggested code and documentation for the following files:

- `src/main.py` — Improved the command-line output to display recommendations, scores, and explanations.
- `src/recommender.py` — Generated CSV loading, weighted scoring, ranking, and explanation logic.
- `tests/test_recommender.py` — Suggested additional tests for recommendation limits and explanations.
- `data/songs.csv` — Suggested expanding the catalog from 10 songs to 20.
- `model_card.md` — Helped draft the model documentation, limitations, and reflection.
- `.gitignore` — Suggested exclusions for temporary Python files and local development settings.

These were code and documentation suggestions provided in chat, not autonomous changes made directly to my repository.

### What did you verify or fix manually?

I reviewed my project files and compared the suggestions with the CodePath assignment requirements.

The project still needs final verification through terminal commands and evaluation with multiple user profiles. I have not yet confirmed that all tests pass or that the scoring experiment is complete.

---

## Design Pattern (SF10)

**Status: Object-oriented structure implemented; formal design pattern stretch feature not yet completed.**

### Which design pattern did you use?

My recommender uses object-oriented programming with Python dataclasses and a `Recommender` class.

The `Song` class represents each song's attributes, and the `UserProfile` class stores the user's musical preferences.

The `Recommender` class organizes the process of ranking songs and explaining recommendations.

This is an object-oriented design, but I have not implemented a formal design pattern such as Strategy, Factory, or Observer.

### How did AI help you brainstorm or implement it?

ChatGPT helped me understand how to organize the recommendation logic into reusable functions and classes.

I used AI assistance to design a weighted scoring system that compares genre, mood, and energy similarity, along with an optional acoustic preference.

AI also helped me connect the object-oriented implementation to the same scoring logic used by the command-line application.

### How does the pattern appear in your final code?

The proposed code in `src/recommender.py` includes:

- `Song` — Stores information about an individual song.
- `UserProfile` — Stores a user's music preferences.
- `Recommender` — Manages song ranking and generates explanations.
- `score_song()` — Calculates relevance scores and returns reasons.
- `recommend_songs()` — Sorts songs by score and returns the top recommendations.

The program separates song data, user preferences, scoring, and ranking into different parts. This makes the system easier to maintain and allows the scoring logic to be modified without rewriting the entire application.

A future improvement would be implementing the **Strategy design pattern** so users could switch between different scoring algorithms, such as genre-focused or energy-focused recommendations.