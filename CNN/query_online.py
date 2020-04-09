import h5py
import numpy as np
from keras import backend

from CNN.extract_cnn_vgg16_keras import VGGNet

MAX_RES = 5


def getMatches(url):
    # read in indexed images' feature vectors and corresponding image names
    h5f = h5py.File('./CNN/featureCNN.h5', 'r')
    feats = h5f['dataset_feat'][:]
    imgNames = h5f['dataset_name'][:]
    h5f.close()

    print("--------------------------------------------------")
    print("               searching starts")
    print("--------------------------------------------------")

    queryDir = url

    # init VGGNet16 model
    model = VGGNet()

    # extract query image's feature, compute simlarity score and sort
    queryVec = model.extract_feat(queryDir)
    scores = np.dot(queryVec, feats.T)
    rank_ID = np.argsort(scores)[::-1]
    rank_score = scores[rank_ID]

    # number of top retrieved images to show
    imlist = [imgNames[index] for i, index in enumerate(rank_ID[0:MAX_RES])]
    print("top %d images in order are: " % MAX_RES, imlist)

    # show top #maxres retrieved result one by one
    res = []
    for i in range(0, MAX_RES):
        resUrl = imgNames[rank_ID[i]].decode("utf-8")
        res.append(['media/images' + resUrl, rank_score[i]])
    backend.clear_session()
    return res
