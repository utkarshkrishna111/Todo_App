import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")

    # Create the destination directory if it doesn't exist
    pathlib.Path(dest_dir).mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    make_archive(filepaths=["Bonus_day8.py", "e2.py"], dest_dir="dest")