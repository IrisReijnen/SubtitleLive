# import sounddevice as sd
# import numpy as np
# import whisper
# import queue
# import threading
#
# # Load the Whisper model
# model = whisper.load_model("base")
#
# # Set up parameters for audio capture
# sampling_rate = 16000  # Whisper works well with 16kHz
# block_duration = 2     # Block duration in seconds
# audio_queue = queue.Queue()
#
# # Callback function to capture audio chunks
# def audio_callback(indata, frames, time, status):
#     if status:
#         print(status)
#     audio_queue.put(indata.copy())
#
# # Function to process and transcribe the audio
# def transcribe_audio():
#     while True:
#         audio_data = audio_queue.get()
#         # Convert the numpy audio data to a format Whisper can process
#         audio_as_float32 = np.float32(audio_data).flatten()
#         result = model.transcribe(audio_as_float32, fp16=False, language='en')
#         print("Transcription:", result['text'])
#
# # Set up live audio stream
# def start_stream():
#     # Create a thread to process the audio transcription
#     transcription_thread = threading.Thread(target=transcribe_audio, daemon=True)
#     transcription_thread.start()
#
#     # Start capturing audio
#     with sd.InputStream(samplerate=sampling_rate, channels=1, callback=audio_callback, blocksize=int(sampling_rate * block_duration)):
#         print("Recording... Press Ctrl+C to stop.")
#         sd.sleep(int(60 * 60 * 1000))  # Keep running for an hour
#
# # Start the transcription process
# start_stream()
