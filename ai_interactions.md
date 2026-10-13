# AI Interactions Log

---

## Agentic Workflow (SF8)

**What task did you give the agent?**

Help me build and improve a music recommendation system in Python. I asked the AI to explain recommendation systems, suggest scoring logic, help debug Python issues, and generate example user profiles for testing.

**Prompts used:**

- Explain the difference between collaborative filtering and content-based filtering.
- How can I calculate similarity for musical features such as energy and valence?
- Help me create a scoring system for a music recommender.
- Why are my Python imports failing when running pytest?
- How can I explain recommendation results to users?

**What did the agent generate or change?**

- Suggested content-based recommendation logic.
- Suggested similarity scoring formulas.
- Helped create multiple user profiles.
- Helped generate recommendation explanations.
- Helped troubleshoot package and testing issues.

**What did you verify or fix manually?**

- Verified all generated code before using it.
- Adjusted recommendation weights for the experiment.
- Added additional songs manually.
- Fixed package setup by adding `src/__init__.py`.
- Ran and verified all tests manually.

---

## Design Pattern (SF10)

**Which design pattern did you use?**

Object-Oriented Design using Song, UserProfile, and Recommender classes.

**How did AI help you brainstorm or implement it?**

AI helped explain how different classes could separate song data, user preferences, and recommendation logic. This made the project easier to organize and maintain.

**How does the pattern appear in your final code?**

The project uses:

- `Song` class to represent music data.
- `UserProfile` class to represent user preferences.
- `Recommender` class to contain recommendation logic.

This separates responsibilities and keeps recommendation code organized.