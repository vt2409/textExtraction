import whisper

class TextExtract:
    @staticmethod
    def text_extraction(input_path):
        try:
            #Load the model tiny, base, medium, large according to requirements.
            model = whisper.load_model('base')

            #Transcribe the audio
            result = model.transcribe(input_path)
            print(f"✅ Text extracted successfully: {result}")
            return result
        except Exception as error:
            print(f"❌ Exception Occurred: {error}")
            return {}

# Creating an object of the class
obj = TextExtract()

# File paths
input_video_path = "../documents/sample_audio.mp3"

# Extract audio
output = obj.text_extraction(input_video_path)
print(f"✅ Extraction Successful: {output['text']}")




