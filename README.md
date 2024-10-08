# Video Compressor

This Python script compresses video files using `ffmpeg` with GPU acceleration. It processes `.mp4` and `.mkv` files from the `files_to_compress` folder and outputs compressed files to the `compressed_files` folder.

## Features
- GPU-accelerated video compression using the `h264_nvenc` codec.
- Default video bitrate: 4M and audio bitrate: 128k.
- Supports `.mp4` and `.mkv` video formats.

## Requirements
- Python 3.x
- `ffmpeg` must be installed on your system. You can download it from [here](https://ffmpeg.org/download.html).
- Install the `ffmpeg-python` library:
  ```bash
  pip install ffmpeg-python
  ```

## Usage
1. Place your video files in the `files_to_compress` folder.
2. Run the script:
   ```bash
   python compress.py
   ```
3. Compressed videos will be saved in the `compressed_files` folder.

## Example
After running the script, the compressed files will appear with the prefix `compressed_` followed by the original filename in the `compressed_files` folder.

## Customization
You can adjust the video bitrate by modifying the `bitrate` parameter in the `compress_video` function:
```python
compress_video(input_path, output_path, bitrate="2M")
```
