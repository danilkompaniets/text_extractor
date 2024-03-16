import os


class UniqueFilenameGenerator:
    def __init__(self, folder="./result"):
        self.folder = folder

    def get_unique_filename(self, filename):
        """Generate a unique filename by appending a numerical index if it already exists."""
        base_name, extension = os.path.splitext(filename)
        index = 1
        new_filename = filename
        while os.path.exists(os.path.join(self.folder, new_filename)):
            new_filename = f"{base_name}_{index}{extension}"
            index += 1
        return new_filename
