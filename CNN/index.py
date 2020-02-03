import os

import h5py
import numpy as np

from CNN.extract_cnn_vgg16_keras import VGGNet

'''
 Extract features and index the images
'''
'''
 Returns a list of filenames for all jpg images in a directory. 
'''


def get_imlist(path):
    fichier = []
    for root, dirs, files in os.walk(path):
        for i in files:
            if i.endswith('.jpg'):
                fichier.append(os.path.join(root, i))
    return fichier
    # return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


if __name__ == "__main__":

    db = img_paths = '../media/images'
    img_list = get_imlist(db)

    print("--------------------------------------------------")
    print("         feature extraction starts")
    print("--------------------------------------------------")

    feats = []
    names = []

    model = VGGNet()
    for i, img_path in enumerate(img_list):
        norm_feat = model.extract_feat(img_path)
        img_name = os.path.split(img_path)[1]
        img_name = img_path[3::]
        feats.append(norm_feat)
        names.append(img_name)
        print("extracting feature from image No. %d , %d images in total" % ((i + 1), len(img_list)))

    feats = np.array(feats)
    output = 'featureCNN.h5'

    print("--------------------------------------------------")
    print("      writing feature extraction results ...")
    print("--------------------------------------------------")

    h5f = h5py.File(output, 'w')
    h5f.create_dataset('dataset_feat', data=feats)
    names = [name.encode('utf8') for name in names]
    h5f.create_dataset('dataset_name', data=names)
    h5f.close()
