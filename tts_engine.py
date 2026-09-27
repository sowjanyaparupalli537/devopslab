import pyttsx3


# ---------------------------------------
# GET AVAILABLE VOICES
# ---------------------------------------

def get_voices():

    engine = pyttsx3.init()

    voices = engine.getProperty("voices")

    voice_list = []

    for voice in voices:

        voice_list.append({
            "id": voice.id,
            "name": voice.name
        })

    engine.stop()

    return voice_list


# ---------------------------------------
# GENERATE SPEECH
# ---------------------------------------

def generate_speech(
    text,
    output_file,
    voice_id=None,
    rate=150,
    volume=1.0
):

    engine = pyttsx3.init()

    # Set voice
    if voice_id:

        engine.setProperty(
            "voice",
            voice_id
        )

    # Set speed
    engine.setProperty(
        "rate",
        rate
    )

    # Set volume
    engine.setProperty(
        "volume",
        volume
    )

    # Save audio
    engine.save_to_file(
        text,
        output_file
    )

    engine.runAndWait()

    engine.stop()

    return output_file