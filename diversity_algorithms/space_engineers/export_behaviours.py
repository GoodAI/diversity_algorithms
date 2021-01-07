import argparse
import os
import glob
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("input_folder_path", help="Folder with run results.")
parser.add_argument("output_path", help="Path to the output file.")
args = parser.parse_args()

# Find all "archive_all_gen*.npz" files, ordered by date
files = sorted(glob.glob(os.path.join(args.input_folder_path, "archive_all_gen*.npz")), key=os.path.getmtime)

with open(args.output_path, 'w') as output_file:
    for file in files:
        archive = np.load(file)
        size = archive["size"]

        # Go through individual behaviour descriptors and save them as "x,y"
        behaviour_descriptors = []
        for i in range(0, size):
            bd = archive[f"ind_{i}"]
            behaviour_descriptors.append(f"{bd[0]},{bd[1]}")

        # Join all behaviour descriptors into a single line, each entry separated by ;
        line = ';'.join(behaviour_descriptors)

        # Write the line to the output file
        output_file.write(line)
        output_file.write("\n")