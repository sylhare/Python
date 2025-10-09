#!/usr/bin/env python3
"""
Image Optimization Script

This script optimizes image files (JPEG, PNG, GIF) to reduce file size while maintaining
acceptable quality. It uses external optimization tools to compress images and remove
unnecessary metadata.

Dependencies:
    Python 3.6+ (built-in modules only: os, subprocess, glob, argparse, sys, pathlib)
    
    External tools (must be installed separately):
    - jpegoptim: JPEG optimization
    - pngquant: PNG lossy compression  
    - optipng: PNG lossless optimization
    - ImageMagick (convert command): GIF optimization

Installation of external tools:
    macOS (with Homebrew):
        brew install jpegoptim pngquant optipng imagemagick
    
    Ubuntu/Debian:
        sudo apt-get install jpegoptim pngquant optipng imagemagick
    
    Windows (with Chocolatey):
        choco install jpegoptim pngquant optipng imagemagick

Usage:
    Basic usage:
        python optimize_images.py /path/to/image/folder
    
    Dry run (see what would be optimized without making changes):
        python optimize_images.py /path/to/image/folder --dry-run
    
    With custom quality settings:
        python optimize_images.py /path/to/images --jpeg-quality 70 --png-quality "60-85"
    
    Examples:
        python optimize_images.py ./my_photos
        python optimize_images.py /Users/username/Pictures --dry-run
        python optimize_images.py ../images --jpeg-quality 65  # More aggressive JPEG compression
        python optimize_images.py ../images --png-quality "50-80"  # More aggressive PNG compression

Features:
    - Supports JPEG, PNG, and GIF files
    - Preserves original filenames
    - Shows detailed progress and statistics
    - Dry run mode for testing
    - Automatic quality optimization
    - Metadata removal for smaller files

Note: This script overwrites original files. Make backups of important images first!
"""

import os
import subprocess
import glob
import argparse
import sys
from pathlib import Path

def get_file_size(file_path):
    """Get file size in bytes"""
    return os.path.getsize(file_path)

def optimize_jpeg(file_path, dry_run=False, quality=75):
    """Optimize JPEG files using jpegoptim"""
    try:
        original_size = get_file_size(file_path)
        
        if dry_run:
            # Estimate potential savings (rough approximation)
            estimated_savings = int(original_size * 0.20)  # Assume 20% reduction
            return True, estimated_savings, 20.0
        
        result = subprocess.run([
            'jpegoptim', 
            f'--max={quality}',  # Set quality (default 75% for better compression)
            '--strip-all',  # Remove metadata
            '--force',  # Overwrite original
            file_path
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            new_size = get_file_size(file_path)
            savings = original_size - new_size
            savings_percent = (savings / original_size) * 100 if original_size > 0 else 0
            return True, savings, savings_percent
        else:
            return False, 0, 0
    except Exception as e:
        print(f"Error optimizing JPEG {file_path}: {e}")
        return False, 0, 0

def optimize_png(file_path, dry_run=False, quality_range="65-90"):
    """Optimize PNG files using pngquant and optipng"""
    try:
        original_size = get_file_size(file_path)
        
        if dry_run:
            # Estimate potential savings (rough approximation)
            estimated_savings = int(original_size * 0.30)  # Assume 30% reduction
            return True, estimated_savings, 30.0
        
        # First use pngquant for lossy compression
        temp_file = file_path + '.tmp'
        result1 = subprocess.run([
            'pngquant', 
            f'--quality={quality_range}',  # More aggressive quality range
            '--force',
            '--output', temp_file,
            file_path
        ], capture_output=True, text=True)
        
        if result1.returncode == 0 and os.path.exists(temp_file):
            # Replace original with optimized version
            os.replace(temp_file, file_path)
        
        # Then use optipng for lossless optimization
        result2 = subprocess.run([
            'optipng',
            '-o7',  # Higher optimization level (was -o2)
            '-quiet',
            file_path
        ], capture_output=True, text=True)
        
        new_size = get_file_size(file_path)
        savings = original_size - new_size
        savings_percent = (savings / original_size) * 100 if original_size > 0 else 0
        return True, savings, savings_percent
        
    except Exception as e:
        print(f"Error optimizing PNG {file_path}: {e}")
        return False, 0, 0

def optimize_gif(file_path, dry_run=False):
    """Optimize GIF files using ImageMagick"""
    try:
        original_size = get_file_size(file_path)
        
        if dry_run:
            # Estimate potential savings (rough approximation)
            estimated_savings = int(original_size * 0.10)  # Assume 10% reduction
            return True, estimated_savings, 10.0
        
        # Use ImageMagick to optimize GIF
        result = subprocess.run([
            'convert',
            file_path,
            '-strip',  # Remove metadata
            '-coalesce',  # Handle animation properly
            '-layers', 'optimize',  # Optimize layers
            file_path
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            new_size = get_file_size(file_path)
            savings = original_size - new_size
            savings_percent = (savings / original_size) * 100 if original_size > 0 else 0
            return True, savings, savings_percent
        else:
            return False, 0, 0
    except Exception as e:
        print(f"Error optimizing GIF {file_path}: {e}")
        return False, 0, 0

def main():
    parser = argparse.ArgumentParser(
        description="Optimize image files (JPEG, PNG, GIF) to reduce file size",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python optimize_images.py /path/to/images
  python optimize_images.py ./images --dry-run
  python optimize_images.py /Users/user/Documents/images
        """
    )
    
    parser.add_argument(
        'path',
        help='Path to directory containing images to optimize'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be optimized without making changes'
    )
    
    parser.add_argument(
        '--jpeg-quality',
        type=int,
        default=75,
        help='JPEG quality (1-100, default: 75)'
    )
    
    parser.add_argument(
        '--png-quality',
        type=str,
        default='65-90',
        help='PNG quality range (e.g., "65-90", default: "65-90")'
    )
    
    args = parser.parse_args()
    
    img_dir = os.path.abspath(args.path)
    
    if not os.path.exists(img_dir):
        print(f"Error: Image directory not found: {img_dir}")
        sys.exit(1)
    
    if not os.path.isdir(img_dir):
        print(f"Error: Path is not a directory: {img_dir}")
        sys.exit(1)
    
    # Get all image files
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif']
    image_files = []
    
    for ext in image_extensions:
        image_files.extend(glob.glob(os.path.join(img_dir, ext)))
        image_files.extend(glob.glob(os.path.join(img_dir, ext.upper())))
    
    mode_text = "DRY RUN - " if args.dry_run else ""
    print(f"Found {len(image_files)} images to {mode_text.lower()}optimize")
    print("=" * 60)
    
    total_original_size = 0
    total_new_size = 0
    optimized_count = 0
    failed_count = 0
    
    for i, file_path in enumerate(image_files, 1):
        filename = os.path.basename(file_path)
        file_ext = os.path.splitext(filename)[1].lower()
        
        print(f"[{i}/{len(image_files)}] Processing: {filename}")
        
        original_size = get_file_size(file_path)
        total_original_size += original_size
        
        success = False
        savings = 0
        savings_percent = 0
        
        if file_ext in ['.jpg', '.jpeg']:
            success, savings, savings_percent = optimize_jpeg(file_path, args.dry_run, args.jpeg_quality)
        elif file_ext == '.png':
            success, savings, savings_percent = optimize_png(file_path, args.dry_run, args.png_quality)
        elif file_ext == '.gif':
            success, savings, savings_percent = optimize_gif(file_path, args.dry_run)
        else:
            print(f"  Skipping unsupported format: {file_ext}")
            continue
        
        if success:
            new_size = original_size - savings
            total_new_size += new_size
            optimized_count += 1
            action_text = "Would optimize" if args.dry_run else "Optimized"
            print(f"  ✓ {action_text}: {savings_percent:.1f}% reduction ({savings:,} bytes saved)")
        else:
            total_new_size += original_size
            failed_count += 1
            action_text = "Would fail to optimize" if args.dry_run else "Failed to optimize"
            print(f"  ✗ {action_text}")
    
    # Summary
    total_savings = total_original_size - total_new_size
    total_savings_percent = (total_savings / total_original_size) * 100 if total_original_size > 0 else 0
    
    print("\n" + "=" * 60)
    summary_title = "DRY RUN SUMMARY" if args.dry_run else "OPTIMIZATION SUMMARY"
    print(summary_title)
    print("=" * 60)
    print(f"Total images processed: {len(image_files)}")
    print(f"Successfully {'would be ' if args.dry_run else ''}optimized: {optimized_count}")
    print(f"Failed to {'would fail to ' if args.dry_run else ''}optimize: {failed_count}")
    print(f"Original total size: {total_original_size:,} bytes ({total_original_size/1024/1024:.1f} MB)")
    print(f"{'Estimated ' if args.dry_run else ''}New total size: {total_new_size:,} bytes ({total_new_size/1024/1024:.1f} MB)")
    print(f"{'Estimated ' if args.dry_run else ''}Total space saved: {total_savings:,} bytes ({total_savings/1024/1024:.1f} MB)")
    print(f"{'Estimated ' if args.dry_run else ''}Overall reduction: {total_savings_percent:.1f}%")
    
    if args.dry_run:
        print("\nNote: This was a dry run. No files were actually modified.")
        print("Run without --dry-run to perform actual optimization.")

if __name__ == "__main__":
    main()

