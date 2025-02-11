import zipfile
import pathlib

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath,'r') as archive:
        archive.extractall(dest_dir)

        # Create the destination directory if it doesn't exist
    pathlib.Path(dest_dir).mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    extract_archive(r"C:\Users\utkar\PycharmProjects\PythonProject1\Bonus_Examples\compressed.zip",
                    r"C:\Users\utkar\PycharmProjects\PythonProject1")