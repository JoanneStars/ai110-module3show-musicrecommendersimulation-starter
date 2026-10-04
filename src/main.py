from .recommender import load_songs, recommend_songs


def main():
    songs = load_songs("data/songs.csv")

    profiles = {
        "High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.90,
            "target_valence": 0.80,
            "target_danceability": 0.90,
            "target_acousticness": 0.10,
        },
        "Chill Lofi": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.35,
            "target_valence": 0.60,
            "target_danceability": 0.60,
            "target_acousticness": 0.80,
        },
        "Deep Intense Rock": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.95,
            "target_valence": 0.40,
            "target_danceability": 0.60,
            "target_acousticness": 0.05,
        },
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, 5)

        print()
        print("=" * 50)
        print(profile_name)
        print("=" * 50)

        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
