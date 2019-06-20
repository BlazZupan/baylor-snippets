import os
from PIL.Image import open, LANCZOS

SAVE_PATH = "Desktop/tmp"  # directory that will store scaled images
RESIZE_WIDTH = 299
RESIZE_HEIGHT = 299

root_dir = os.path.expanduser('~')
save_dir = os.path.join(root_dir, SAVE_PATH)

if os.path.isdir(save_dir):
    print("Directory %s already exists.\nNothing saved." % save_dir)

else:
    os.mkdir(save_dir)

    data_dir = in_data.domain['image'].attributes['origin']

    if in_data.domain.has_discrete_class:
        for category in in_data.domain.class_var.values:
            cat_dir = os.path.join(save_dir, str(category))
            os.mkdir(cat_dir)

    for entry in in_data:
        local_dir = str(entry['image'])

        img_dir = os.path.join(data_dir, local_dir)
        new_dir = os.path.join(save_dir, local_dir)

        image = open(img_dir)
        image = image.resize((RESIZE_WIDTH, RESIZE_HEIGHT), LANCZOS)
        image.save(new_dir)

    print("%d images saved successfully." % len(in_data))
