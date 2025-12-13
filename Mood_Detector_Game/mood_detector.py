text = input("Enter a sentence: ").lower()
if "happy" in text or "good" in text or "great" in text:
    print("Mood: Happy 😊")
elif "sad" in text or "bad" in text or "angry" in text:
    print("Mood: Sad 😔")
else:
    print("Mood: Neutral 😐")
