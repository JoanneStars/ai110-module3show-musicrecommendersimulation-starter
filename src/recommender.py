
"""
Music Recommender Simulation.

A content-based music recommendation system that scores
songs using genre, mood, energy, and acoustic preferences.
"""

import csv
from dataclasses import dataclass
from typing import List, Dict, Tuple


@dataclass
class Song:
    """Represent a song and its musical attributes."""
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """Represent a user's musical taste preferences."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


def load_songs(csv_path: str) -> List[Dict]:
    """Read songs from a CSV file and convert numeric values."""
    songs = []

    with open(csv_path, mode="r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])

            songs.append(row)

    return songs


def score_song(
    user_prefs: Dict, song: Dict
) -> Tuple[float, List[str]]:
    """Calculate song relevance and explain the score."""
    score = 0.0
    reasons = []

    # Genre match: 2 points
    preferred_genre = user_prefs.get(
        "genre", user_prefs.get("favorite_genre", "")
    )

    if song["genre"].lower() == preferred_genre.lower():
        score += 2.0
        reasons.append("Genre match (+2.0)")

    # Mood match: 1 point
    preferred_mood = user_prefs.get(
        "mood", user_prefs.get("favorite_mood", "")
    )

    if song["mood"].lower() == preferred_mood.lower():
        score += 1.0
        reasons.append("Mood match (+1.0)")

    # Energy similarity: up to 1 point
    target_energy = float(
        user_prefs.get(
            "energy", user_prefs.get("target_energy", 0.5)
        )
    )

    energy_gap = abs(target_energy - float(song["energy"]))
    energy_points = max(0.0, 1.0 - energy_gap)

    score += energy_points
    reasons.append(
        f"Energy similarity (+{energy_points:.2f})"
    )

    # Optional acoustic preference: up to 0.5 points
    if "likes_acoustic" in user_prefs:
        acousticness = float(song["acousticness"])

        if user_prefs["likes_acoustic"]:
            acoustic_points = 0.5 * acousticness
        else:
            acoustic_points = 0.5 * (1.0 - acousticness)

        score += acoustic_points
        reasons.append(
            f"Acoustic preference (+{acoustic_points:.2f})"
        )

    return round(score, 4), reasons


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5
) -> List[Tuple[Dict, float, List[str]]]:
    """Rank every song by relevance and return the top k."""
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored_songs.append((song, score, reasons))

    ranked_songs = sorted(
        scored_songs,
        key=lambda item: item[1],
        reverse=True
    )

    return ranked_songs[:max(0, k)]


class Recommender:
    """Provide object-oriented song recommendations."""

    def __init__(self, songs: List[Song]):
        """Store the available song catalog."""
        self.songs = songs

    def _preferences(self, user: UserProfile) -> Dict:
        """Convert a user profile into scoring preferences."""
        return {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic
        }

    def _score(self, user: UserProfile, song: Song):
        """Score a Song object using the shared algorithm."""
        return score_song(self._preferences(user), vars(song))

    def recommend(
        self, user: UserProfile, k: int = 5
    ) -> List[Song]:
        """Return the highest-ranked Song objects."""
        ranked = sorted(
            self.songs,
            key=lambda song: self._score(user, song)[0],
            reverse=True
        )

        return ranked[:max(0, k)]

    def explain_recommendation(
        self, user: UserProfile, song: Song
    ) -> str:
        """Explain why a song matches a user's preferences."""
        score, reasons = self._score(user, song)

        return (
            f"{song.title} scored {score:.2f} points because: "
            + "; ".join(reasons)
        )
