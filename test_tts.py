import pyttsx3


# Initialize TTS engine
engine = pyttsx3.init()


# Test text
text = "Hello. This is my Text to Speech Conversion Using NLP project."


# Set speech speed
engine.setProperty("rate", 150)


# Set volume
engine.setProperty("volume", 1.0)


# Generate speech
engine.say(text)

engine.runAndWait()


print("Speech generated successfully!")

# Close engine
engine.stop()