from typing import List, Dict, Tuple, Optional
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

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"


def load_songs(csv_path: str) -> List[Dict]:
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

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
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
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    # Valence similarity
    if "target_valence" in user_prefs:
        valence_similarity = 1 - abs(
            song["valence"] - user_prefs["target_valence"]
        )
        valence_points = 1.0 * valence_similarity
        score += valence_points
        reasons.append(f"valence similarity (+{valence_points:.2f})")

    # Danceability similarity
    if "target_danceability" in user_prefs:
        dance_similarity = 1 - abs(
            song["danceability"] - user_prefs["target_danceability"]
        )
        dance_points = 0.5 * dance_similarity
        score += dance_points
        reasons.append(f"danceability similarity (+{dance_points:.2f})")

    # Acousticness similarity
    if "target_acousticness" in user_prefs:
        acoustic_similarity = 1 - abs(
            song["acousticness"] - user_prefs["target_acousticness"]
        )
        acoustic_points = 0.5 * acoustic_similarity
        score += acoustic_points
        reasons.append(f"acousticness similarity (+{acoustic_points:.2f})")

    return score, reasons

def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """
    Scores every song and returns the top k songs ranked by score.
    """
    recommendations = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)

        recommendations.append((song, score, explanation))

    recommendations.sort(key=lambda item: item[1], reverse=True)

    return recommendations[:k]


    
