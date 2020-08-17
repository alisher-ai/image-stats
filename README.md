# Image Stats
This packages extract the statistics of all images in the provided directory

## Install
`pip install image-stats`

## What it works?
Scan all files in the provided directory, and run shell command `file /path/to/image_file.png` to get file statistics. Parse the output and retrieve image dimensions from stdout. 

- Sample output of `file` command:
```JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 629x1005, frames 3```

- Image (spatial) shape: ```629x1005``` in `widthxheight` format


extract image stats in the directory
