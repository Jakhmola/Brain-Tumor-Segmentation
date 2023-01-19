import os

import keras
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from app import app

#generates segmentation mask given MRI file
def mask_generator(uploaded_file):
    SEGMENT_CLASSES = {
        0: 'NOT tumor',
        1: 'NECROTIC/CORE',  # or NON-ENHANCING tumor CORE
        2: 'EDEMA',
        3: 'ENHANCING'  # original 4 -> converted into 3 later
    }
    model = load_model('brats_3d.hdf5', compile=False)
    test_img = np.load(uploaded_file)
    test_img_input = np.expand_dims(test_img, axis=0)
    test_prediction = model.predict(test_img_input)
    test_prediction_argmax = np.argmax(test_prediction, axis=4)[0, :, :, :]
    # test_mask = np.load(os.path.join(app.config['UPLOAD_PATH'], uploaded_file.filename))
    # test_mask_argmax = np.argmax(test_mask, axis=3)
    # n_slice = random.randint(0, test_prediction_argmax.shape[2])
    for n_slice in range(0, test_img.shape[0]):
        fig = plt.figure(figsize=(24, 8))
        plt.subplot(121)
        plt.title('Testing Image', fontsize=18, weight='bold')
        plt.imshow(test_img[:, :, n_slice, 1], cmap='gray')
        plt.subplot(122)
        # plt.title('Testing Label')
        # plt.imshow(test_mask_argmax[:, :, n_slice])
        # plt.subplot(233)
        plt.title('Prediction on test image', fontsize=20, weight='bold')
        im = plt.imshow(test_prediction_argmax[:, :, n_slice])
        labels = list(SEGMENT_CLASSES.values())
        colors = [im.cmap(im.norm(value)) for value in [0, 1, 2, 3]]
        # create a patch (proxy artist) for every color
        patches = [mpatches.Patch(color=colors[i], label=f"{labels[i]}") for i in range(len(labels))]
        # put those patched as legend-handles into the legend
        plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title='Mask Labels', fontsize=18)
        # plt.show()
        fig.savefig(os.path.join(app.config['UPLOAD_PATH'], 'prediction'+str(n_slice)+'.png'), dpi=1000, transparent=True)
    return
