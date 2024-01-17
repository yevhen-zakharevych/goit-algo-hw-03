import argparse
from pathlib import Path
import shutil


def parse_args():
    parser = argparse.ArgumentParser(description="Copy files")
    parser.add_argument("-s", "--source", type=Path, required=True, help="Source folder")
    parser.add_argument("-t", "--target", type=Path, default=Path("dist"), help="Target folder")

    return parser.parse_args()


def copy_files(source, target):
    if not Path.is_dir(source):
        print(f"{source} is not a directory")
        return

    for el in source.iterdir():
        if el.is_dir():
            copy_files(el, target)
        else:
            extension = Path(el.name).suffix[1:]
            dir_name = target / extension
            dir_name.mkdir(exist_ok=True, parents=True)
            shutil.copy(el, dir_name)


def main():
    args = parse_args()
    copy_files(args.source, args.target)


if __name__ == "__main__":
    main()
