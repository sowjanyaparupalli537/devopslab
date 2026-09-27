import soundfile as sf
import numpy as np


# ---------------------------------------
# ANALYZE GENERATED AUDIO
# ---------------------------------------

def analyze_audio(
    audio_file,
    text,
    voice_name
):

    # Read WAV file
    audio_data, sample_rate = sf.read(
        audio_file
    )


    # ---------------------------------------
    # AUDIO DURATION
    # ---------------------------------------

    duration = (
        len(audio_data) / sample_rate
    )


    # ---------------------------------------
    # CONVERT STEREO TO MONO
    # ---------------------------------------

    if audio_data.ndim > 1:

        audio_data = np.mean(
            audio_data,
            axis=1
        )


    # ---------------------------------------
    # VOLUME
    # ---------------------------------------

    rms = np.sqrt(
        np.mean(
            audio_data.astype(np.float64) ** 2
        )
    )

    volume_percentage = min(
        100.0,
        rms * 100
    )


    # ---------------------------------------
    # WORD COUNT
    # ---------------------------------------

    words = text.split()

    word_count = len(words)


    # ---------------------------------------
    # SPEECH SPEED
    # ---------------------------------------

    if duration > 0:

        words_per_second = (
            word_count / duration
        )

    else:

        words_per_second = 0


    words_per_minute = (
        words_per_second * 60
    )


    # ---------------------------------------
    # SPEED CATEGORY
    # ---------------------------------------

    if words_per_minute < 100:

        speed_description = "Slow"

    elif words_per_minute < 160:

        speed_description = "Normal"

    elif words_per_minute < 200:

        speed_description = "Fast"

    else:

        speed_description = "Very Fast"


    # ---------------------------------------
    # RETURN RESULTS
    # ---------------------------------------

    return {

        "voice": voice_name,

        "duration": duration,

        "volume": volume_percentage,

        "words_per_second": words_per_second,

        "words_per_minute": words_per_minute,

        "speed": speed_description
    }