import os


def upload_images(folder_path, image_names, element):

        # Example of fiel_path and images_name
        # folder_path = 'assets/season'
        # image_names = ['image1.jpg', 'image2.jpg', 'image3.jpg']

        # folder_path = 'assets/season'

        # Create full file paths for each image in the list
        image_paths = [os.path.abspath(os.path.join(
            folder_path, image_name)) for image_name in image_names]

        # Send each file path to the file input element one by one
        for image_path in image_paths:
            element.send_keys(image_path)
