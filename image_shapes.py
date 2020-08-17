from subprocess import Popen, PIPE
import os
import numpy as np
import argparse
import tqdm
import random


def image_shape_stats(root_dir, histogram, max_limit):
    widths = []
    heights = []
    all_files = []
    for root, dirs, files in os.walk(root_dir, topdown=True):
        for file in files:
            all_files.append(os.path.join(root, file))
    random.shuffle(all_files)

    for img_file in tqdm.tqdm(all_files[:max_limit]):
        try:
            file_stats = Popen(["file", img_file], stdout=PIPE)
            output = file_stats.communicate()[0]
            img_shape_str = output.decode("utf-8").split(',')[-2]
            img_shape_str = img_shape_str.replace(' ', '')
            width, height = [int(i) for i in img_shape_str.split('x')]
            widths.append(width)
            heights.append(height)
        except:
            continue
    print("Average of widths: {}".format(np.mean(widths)))
    print("Average of heights: {}".format(np.mean(heights)))

    if histogram:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        plt.hist(widths, bins=100, alpha=0.5, color="green")
        plt.hist(heights, bins=100, alpha=0.5, color="blue")
        plt.title('Width and height histogram of images in this directory')
        plt.legend(['heights', 'widths'], loc='upper right')
        plt.savefig(os.path.join(root_dir, 'width_and_height_histogram.png'), dpi=100)
        plt.gcf().clear()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image shape statistics')
    parser.add_argument('--root_dir', help='root dir from where to analyse image shape statistics', required=True)
    parser.add_argument('--histogram', default="True", action="store_true", help='Whether to save image shape histogram')
    parser.add_argument('--max', default=2e4, help='max limit of files to analyze', type=int)
    args = parser.parse_args()
    image_shape_stats(args.root_dir, args.histogram, args.max)

