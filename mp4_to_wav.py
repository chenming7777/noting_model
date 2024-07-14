import ffmpeg

def mp4_to_wav(input_file, output_file):
    try:
        # Extract audio from video and convert to wav format using ffmpeg
        ffmpeg.input(input_file).output(output_file, format='wav').run(overwrite_output=True)
        print(f"Successfully converted {input_file} to {output_file}")
    except ffmpeg.Error as e:
        # Capture both stdout and stderr from ffmpeg
        print(f"Error occurred: {e}")
        print(f"stdout: {e.stdout.decode('utf-8')}")
        print(f"stderr: {e.stderr.decode('utf-8')}")

# Example usage
mp4_to_wav('test.mp4', 'output_audio.wav')
