import sounddevice as sd
import numpy as np
import whisper
import queue
import threading

# Load the Whisper model (use a smaller model for faster performance)
model = whisper.load_model("tiny")  # "tiny" is faster, you can also use "base"

# Set up parameters for audio capture
sampling_rate = 16000
block_duration = 2  # Process audio blocks every 2 seconds
max_audio_buffer = 5  # Only keep 5 seconds of recent audio
audio_queue = queue.Queue()

# Callback function to capture audio chunks
def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    audio_queue.put(indata.copy())

# Function to process and transcribe the audio, limiting buffer size
def transcribe_audio():
    audio_buffer = np.zeros((0,), dtype=np.float32)  # Initialize buffer as float32
    while True:
        # Get new audio chunk from the queue
        audio_data = audio_queue.get()

        # Ensure audio data is in float32 format
        audio_data = audio_data.astype(np.float32)

        # Append new audio data to the buffer
        audio_buffer = np.concatenate((audio_buffer, audio_data.flatten()))

        # Only keep the last 'max_audio_buffer' seconds of audio
        if len(audio_buffer) > max_audio_buffer * sampling_rate:
            audio_buffer = audio_buffer[-max_audio_buffer * sampling_rate:]

        # Transcribe the most recent audio chunk
        result = model.transcribe(audio_buffer, fp16=False, language='en')
        print("Transcription:", result['text'])

# Set up live audio stream
def start_stream():
    transcription_thread = threading.Thread(target=transcribe_audio, daemon=True)
    transcription_thread.start()

    # Start capturing audio
    with sd.InputStream(samplerate=sampling_rate, channels=1, callback=audio_callback, blocksize=int(sampling_rate * block_duration)):
        print("Recording... Press Ctrl+C to stop.")
        sd.sleep(int(60 * 60 * 1000))  # Keep running for an hour

# Start the transcription process
start_stream()
