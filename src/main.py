
"""
Command-line runner for the Music Recommender Simulation.

Loads song data, runs the recommendation algorithm,
and displays personalized recommendations with scores
and explanations.
"""

from pathlib import Path

try:
    from .recommender import load_songs, recommend_songs
except ImportError:
    from recommender import load_songs, recommend_songs


def main() -> None:
    """Load songs and display personalized music recommendations."""

    project_root = Path(__file__).resolve().parent.parent
    songs_path = project_root / "data" / "songs.csv"

    songs = load_songs(str(songs_path))
    print(f"Loaded songs: {len(songs)}")

    # Starter user profile
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8
    }

    print("\nMusic Recommender Simulation")
    print("----------------------------")
    print(f"Favorite genre: {user_prefs['genre']}")
    print(f"Favorite mood: {user_prefs['mood']}")
    print(f"Target energy: {user_prefs['energy']}")

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop 5 Recommendations:\n")

    if not recommendations:
        print("No recommendations available.")
        return

    for rank, (song, score, reasons) in enumerate(recommendations, start=1):
        print(f"{rank}. {song['title']}")
        print(f"   Score: {score:.2f}")

        if isinstance(reasons, list):
            for reason in reasons:
                print(f"   Because: {reason}")
        else:
            print(f"   Because: {reasons}")

        print()


if __name__ == "__main__":
    main()
