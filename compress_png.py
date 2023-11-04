import subprocess
import os
import shutil

def compress_png(directory, quality="65-80"):
    if not shutil.which("pngquant"):
        print("pngquant is not installed. Please install it and add it to your PATH.")
        return

    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return

    for filename in os.listdir(directory):
        if filename.lower().endswith('.png'):
            file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, "compressed_" + filename)
            command = ['pngquant', '--force', '--skip-if-larger', '--quality', quality, file_path, '--output', new_file_path]
            subprocess.run(command, check=True)
            print(f"Compressed {filename}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        compress_png(sys.argv[1])
    else:
        print("Usage: python compress_png.py <directory>")
