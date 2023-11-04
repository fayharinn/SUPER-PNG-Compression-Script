# SUPER PNG Compression Script

This script uses `pngquant` to compress PNG files in a specified directory, reducing file size with minimal quality loss.

## Prerequisites

Make sure you have `pngquant` installed on your system:

- For macOS: `brew install pngquant`
- For Linux: Install `pngquant` using your distribution's package manager.
- For Windows: Download the `pngquant` binary from the official site and add it to your PATH.

## Usage

To use the script, navigate to the directory containing `compress_png.py` and run:

```bash
python compress_png.py path_to_your_png_directory
```

Replace `path_to_your_png_directory` with the path to the directory containing your `.png` files.

## What It Does

The script will create a compressed copy of each `.png` file in the specified directory. The new files will be prefixed with 'compressed_' to distinguish them from the originals.

## Customization

You can adjust the quality of compression by changing the `quality` parameter within the script. The default is set to "65-80", which balances compression with quality.

## Disclaimer

Please ensure you have backups of your original PNG files. This script will create compressed versions, but it's always good to have a backup.

Enjoy your newly optimized images!
