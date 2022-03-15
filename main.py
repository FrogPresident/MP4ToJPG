import argparse
import cv2
from pathlib import Path
from tqdm import tqdm


def main():
    args = get_arg_parser().parse_args()
    src: Path = args.src
    out: Path = args.out
    # cut the picture for each time
    timeF = 500
    c = 0
    progress = sorted(src.glob("**/*.mp4"))
    for mp4_file in progress:
        print(mp4_file)
        # read mp4 file
        vc = cv2.VideoCapture(str(mp4_file))
        num_frame = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))

        for i in tqdm(range(num_frame)):
            rval, frame = vc.read()
            if not rval:
                break
            if c % timeF == 0:
                # store converted object to jpg file
                cv2.imwrite(f"JPG/{c // timeF}.jpg", frame)
            c = c + 1


def get_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("src", type=Path)
    parser.add_argument("-o", "--out", default="out", type=Path)
    return parser


if __name__ == '__main__':
    main()
