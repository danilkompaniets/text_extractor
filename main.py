import glob
import os
import shutil
from search_for_id import IDFinder
from unique_filename import UniqueFilenameGenerator
from scan_image import TextExtractor

custom_config = r"--oem 3 --psm 12"
images = glob.glob("./images/*")

# Create instances of IDFinder and UniqueFilenameGenerator
id_finder = IDFinder("./tables/CREATEK_CSV_UTF.csv")
filename_generator = UniqueFilenameGenerator()

for image_path in images:
    print(image_path)

    # Create an instance of TextExtractor
    text_extractor = TextExtractor()

    # Call extract_text_from_image method on the instance
    extracted_text = text_extractor.extract_text_from_image(image_path=image_path, config=custom_config, language="eng")
    search_query = str(extracted_text).upper()

    id_ = id_finder.get_id(search_query)

    if id_ is None:
        print(f"No matching ID found for {search_query}")
        continue

    new_file_name = f"{id_}.jpg"

    new_unique_filename = filename_generator.get_unique_filename(new_file_name)
    old_file_name = os.path.basename(image_path)

    old_file_path = os.path.join("./images/", old_file_name)
    new_file_path = os.path.join("./result/", new_unique_filename)

    # Copy the file to the result folder
    shutil.copyfile(old_file_path, new_file_path)

