
positive_words = [
    "good", "great", "excellent", "amazing",
    "awesome", "love", "liked", "enjoyed",
    "fantastic", "nice", "wonderful", "best"
]

negative_words = [
    "bad", "worst", "terrible", "awful",
    "hate", "dislike", "boring", "poor",
    "sad", "waste", "pathetic", "ugly"
]

# Step 2: Input from User
print("----- AI SENTIMENT ANALYSIS SYSTEM -----")
review = input("Enter movie review: ")

# Step 3: Preprocessing (Lowercase conversion)
review = review.lower()

# Step 4: AI Analysis Logic
positive_count = 0
negative_count = 0

for word in review.split():
    if word in positive_words:
        positive_count += 1
    elif word in negative_words:
        negative_count += 1

# Step 5: AI Decision Making
print("\n----- AI RESULT -----")

if positive_count > negative_count:
    print("Sentiment: POSITIVE 😊")
elif negative_count > positive_count:
    print("Sentiment: NEGATIVE 😞")
else:
    print("Sentiment: NEUTRAL 😐")

# Step 6: Explanation (Optional for Viva)
print("\n----- AI ANALYSIS DETAILS -----")
print("Positive words count:", positive_count)
print("Negative words count:", negative_count)

print("\nThank you for using AI Sentiment Analyzer!")
