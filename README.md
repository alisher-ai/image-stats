# Image Stats
This packages extract the statistics of all images in the provided directory

## Install
`pip install image-stats`

## What it works?
Scan all files in the provided directory, and run shell command `file /path/to/image_file.png` to get file statistics. Parse the output and retrieve image dimensions from stdout. 

- Sample output:
  - Sample output of `file` command:
  ```JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 629x1005, frames 3```

  - Image (spatial) shape: ```629x1005``` (in `widthxheight` format)

- Skips (continue) if anything goes wrong within the for loop

## Arguments
- **root_dir**: root directory from where to extract the file statistics

- **histogram**: plot histogram of widths and heights to the `os.path.join(root_dir, width_and_height_histogram.png)`

- **max**: max limit for the number of files to be processed

## How to use:

image-stats --root_dir /path/to/the/root/dir --histogram --max 10000


