# pip install assemblyai
import os

from assemblyai import TranscriptStatus
from assemblyai.prerecorded.v2 import Transcriber, TranscriptionConfig

config = TranscriptionConfig(
    speech_models=["assemblyai-stt-3-7", "universal-2"],  # 32 languages, Universal-2 covers the rest of 99
    language_detection=True,
    speaker_labels=True,
)
transcriber = Transcriber(api_key=os.environ["ASSEMBLYAI_API_KEY"], config=config)
transcript = transcriber.transcribe("https://assembly.ai/wildfires.mp3")

if transcript.status == TranscriptStatus.error:
    raise RuntimeError(f"Transcription failed: {transcript.error}")

for utterance in transcript.utterances:
    print(f"Speaker {utterance.speaker}: {utterance.text}")
