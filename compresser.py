import os
import ffmpeg

input_folder = 'files_to_compress'
output_folder = 'compressed_files'

def compress_video(input_file, output_file, bitrate="4M"):
    try:
        (
            ffmpeg
            .input(input_file)
            .output(output_file, video_bitrate=bitrate, vcodec='h264_nvenc', audio_bitrate='128k')
            .run()
        )
        print(f'File compressed using GPU: {output_file}')
    except ffmpeg.Error as e:
        print(f'Compression error: {e.stderr.decode()}')

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith('.mp4') or filename.endswith('.mkv'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, 'compressed_' + filename)

        compress_video(input_path, output_path)
