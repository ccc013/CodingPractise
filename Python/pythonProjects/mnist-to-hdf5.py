
import numpy as np
import lmdb, h5py
import sys
sys.path.append('../../python')
import caffe
from caffe.proto.caffe_pb2 import Datum

def mnist_lmdb_to_h5(src, tgt):
    with lmdb.open(src, map_size=1099511627776, readonly=True) as lmdb_env:
        numSamples = int(lmdb_env.stat()['entries'])
        with lmdb_env.begin(write=False) as txn:
            with txn.cursor() as cur:
                with h5py.File(tgt, 'w') as fd:
                    fd.create_dataset('data', (numSamples, 1, 28, 28), dtype=np.float32)
                    fd.create_dataset('label', (numSamples,), dtype=np.float32)
                    for key, val in cur:
                        d = Datum.FromString(val)
                        img = np.array(np.fromstring(d.data, dtype=np.uint8).reshape(1, 28, 28), dtype=np.float32) / 255.0
                        index = int(key)
                        fd['data'][index, :, :, :] = img
                        fd['label'][index] = float(d.label)

mnist_lmdb_to_h5('./mnist_test_lmdb', './mnist_test.h5')
mnist_lmdb_to_h5('./mnist_train_lmdb', './mnist_train.h5')

