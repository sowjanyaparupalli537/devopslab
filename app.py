import streamlit as st
import os

from text_processor import preprocess_text
from tts_engine import generate_speech, get_voices
from speech_analysis import analyze_audio


# ---------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------

st.set_page_config(
    page_title="Text-to-Speech Using NLP",
    page_icon="🔊",
    layout="centered"
)


# ---------------------------------------
# TITLE
# ---------------------------------------

st.title("🔊 Text-to-Speech Conversion Using NLP")

st.write(
    "Enter a sentence or paragraph and convert it into speech."
)


# ---------------------------------------
# TEXT INPUT
# ---------------------------------------

text = st.text_area(
    "Enter your text:",
    height=200,
    placeholder="Type your sentence or paragraph here..."
)


# ---------------------------------------
# CONVERT BUTTON
# ---------------------------------------

if st.button("🎙️ Convert to Speech"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:

        # ---------------------------------------
        # NLP PREPROCESSING
        # ---------------------------------------

        processed_text, tokens = preprocess_text(text)


        # ---------------------------------------
        # DISPLAY PROCESSED TEXT
        # ---------------------------------------

        st.subheader("📝 Processed Text")
        st.write(processed_text)


        # ---------------------------------------
        # DISPLAY TOKENS
        # ---------------------------------------

        st.subheader("🔤 Tokens")
        st.write(tokens)


        # ---------------------------------------
        # OUTPUT DIRECTORY
        # ---------------------------------------

        os.makedirs("output", exist_ok=True)

        output_file = "output/generated_speech.wav"


        # ---------------------------------------
        # GET TTS VOICE
        # ---------------------------------------

        voices = get_voices()

        if voices:

            selected_voice_id = voices[0]["id"]
            selected_voice_name = voices[0]["name"]

        else:

            selected_voice_id = None
            selected_voice_name = "Default System Voice"


        # ---------------------------------------
        # GENERATE SPEECH
        # ---------------------------------------

        try:

            generate_speech(
                processed_text,
                output_file,
                voice_id=selected_voice_id,
                rate=150,
                volume=1.0
            )


            st.success(
                "Speech generated successfully!"
            )


            # ---------------------------------------
            # AUDIO PLAYER
            # ---------------------------------------

            if os.path.exists(output_file):

                st.subheader("🔊 Generated Speech")

                st.audio(
                    output_file,
                    format="audio/wav"
                )


                # ---------------------------------------
                # SPEECH ANALYSIS
                # ---------------------------------------

                analysis = analyze_audio(
                    output_file,
                    processed_text,
                    selected_voice_name
                )


                st.subheader("📊 Speech Analysis")


                col1, col2 = st.columns(2)


                with col1:

                    st.metric(
                        "🎙️ Voice / Accent",
                        analysis["voice"]
                    )

                    st.metric(
                        "🔊 Volume",
                        f"{analysis['volume']:.2f}%"
                    )


                with col2:

                    st.metric(
                        "⚡ Speech Speed",
                        f"{analysis['words_per_minute']:.1f} WPM"
                    )

                    st.metric(
                        "⏱️ Duration",
                        f"{analysis['duration']:.2f} sec"
                    )


                st.write(
                    f"**Speed Category:** {analysis['speed']}"
                )


                # ---------------------------------------
                # DOWNLOAD
                # ---------------------------------------

                with open(
                    output_file,
                    "rb"
                ) as audio_file:

                    st.download_button(
                        label="⬇️ Download Speech",
                        data=audio_file,
                        file_name="generated_speech.wav",
                        mime="audio/wav"
                    )


        except Exception as e:

            st.error(
                f"Error generating speech: {e}"
            )