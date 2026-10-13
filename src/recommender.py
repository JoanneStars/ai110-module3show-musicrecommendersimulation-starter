from typing import List, Dict, Tuple
from dataclasses import dataclass
import csv


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
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
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song\]:
        scored_songs = []

        for song in self.songs:
            score = 0

            if song.genre.lower() == user.favorite_genre.lower():
                score += 2

            if song.mood.lower() == user.favorite_mood.lower():
                score += 1

            score += (1 - abs(song.energy - user.target_energy))

            if user.likes_acoustic:
                score += song.acousticness

            scored_songs.append((song, score))

        scored_songs.sort(key=lambda item: item[1], reverse=True)

        return [song for song, score in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []

        if song.genre.lower() == user.favorite_genre.lower():
            reasons.append("genre match")

        if song.mood.lower() == user.favorite_mood.lower():
            reasons.append("mood match")

        reasons.append(
            f"energy similarity ({1 - abs(song.energy - user.target_energy):.2f})"
        )

        if user.likes_acoustic:
            reasons.append(
                f"acousticness contribution ({song.acousticness:.2f})"
            )

        return ", ".join(reasons)


def load_songs(csv_path: str) -> List[Dict\]:
    """
    Loads songs from a CSV file and converts numeric fields to numbers.
    """
    songs = []

    with open(csv_path, "r", newline="", encoding="utf-8") as file:
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


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]\]:
    """
    Scores one song based on genre, mood, and numerical similarity.
    """
    score = 0.0
    reasons = []

    # Genre match: reduced from 2.0 to 1.0 for experiment
    if song["genre"].lower() == user_prefs["favorite_genre"].lower():
        score += 1.0
        reasons.append("genre match (+1.0)")

    # Mood match
    if song["mood"].lower() == user_prefs["favorite_mood"].lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    # Energy similarity: increased from 1.5 to 3.0 for experiment
    energy_similarity = 1 - abs(
        song["energy"] - user_prefs["target_energy"]
    )
  energy_points = 3.0 * energy_similarity
