import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
!wget https://sds-platform-private.s3-us-east-2.amazonaws.com/uploads/P14-Convolutional-Neural-Networks.zip
import zipfile as zf
files = zf.ZipFile("P14-Convolutional-Neural-Networks.zip", 'r')
files.extractall('directory to extract')
files.close()
