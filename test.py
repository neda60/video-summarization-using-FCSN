import numpy as np
import h5py

# with h5py.File('/Users/neda.ebrahimi/Documents/neda.ebrahimi/git/summe_dataset.h5', 'r') as hdf:
#with h5py.File('/Users/neda.ebrahimi/Documents/neda.ebrahimi/git/SinDongpytorch-vsumm-reinforce-master/utils/summe_dataset.h5', 'r') as hdf:
with h5py.File('log/summe-split0/result_test.h5', 'r') as hdf:

#with h5py.File('/Users/neda.ebrahimi/Documents/neda.ebrahimi/git/Video_Summary_using_FCSN-master/data/fcsn_tvsum0.h5', 'r') as hdf:
#with h5py.File('/Users/neda.ebrahimi/Documents/neda.ebrahimi/git/Video_Summary_using_FCSN-master/eccv16_dataset_summe_google_pool5.h5', 'r') as hdf:
# with h5py.File('/Users/neda.ebrahimi/Downloads/datasets/eccv16_dataset_youtube_google_pool5.h5', 'r') as hdf:
    ls = list(hdf.keys())
    print(ls)
    data = hdf.get('video_1')
    d1 = np.array(data)
    d1 = np.array(data['score'])
    print(d1)
    #print(data)
#
#
# # import os
# #
# # os.mkdir('f')
#
# d1 = np.random.random(size = (1000,20))
# d2 = np.random.random(size = (1000,200))
#
# hf = h5py.File('data.h5', 'w')
#
# hf.create_dataset('dataset_1', data=d1)
# hf.create_dataset('dataset_2', data=d2)
#
#
# print(hf.keys())
