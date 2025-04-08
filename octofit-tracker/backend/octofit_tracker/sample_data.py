def get_test_data():
    return {
        "users": [
            {"_id": "1", "username": "john_doe", "email": "john_doe@example.com", "password": "password123"},
            {"_id": "2", "username": "jane_smith", "email": "jane_smith@example.com", "password": "password123"}
        ],
        "teams": [
            {"_id": "1", "name": "Team Alpha"},
            {"_id": "2", "name": "Team Beta"}
        ],
        "activities": [
            {"_id": "1", "activity_type": "Running", "duration": "01:00:00"},
            {"_id": "2", "activity_type": "Cycling", "duration": "02:00:00"}
        ],
        "leaderboard": [
            {"_id": "1", "score": 100},
            {"_id": "2", "score": 200}
        ],
        "workouts": [
            {"_id": "1", "name": "Morning Run", "description": "A quick morning run to start the day."},
            {"_id": "2", "name": "Evening Yoga", "description": "Relaxing yoga session in the evening."}
        ]
    }