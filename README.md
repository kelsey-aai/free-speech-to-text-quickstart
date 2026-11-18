# Free speech-to-text quickstart (AssemblyAI-STT-3.7)

Companion code for [Best free speech-to-text APIs and open-source engines (2026)](https://www.assemblyai.com/blog/the-top-free-speech-to-text-apis-and-open-source-engines).

Transcribes a file with AssemblyAI-STT-3.7 (`assemblyai-stt-3-7`, 32 languages), falls back to Universal-2 for languages outside the 32, and prints speaker-labeled lines.

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export ASSEMBLYAI_API_KEY=your_api_key_here   # free tier, no credit card: https://www.assemblyai.com/dashboard/signup
python transcribe.py
```

Edit the URL in `transcribe.py` to point at your own audio file or a local path.

AssemblyAI-STT-3.7 returns verbatim transcripts by default. Add `disfluencies=False` to `TranscriptionConfig` for clean prose.

Docs: [model selection](https://www.assemblyai.com/docs/pre-recorded-audio/select-the-speech-model).
