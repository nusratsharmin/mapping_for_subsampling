import numpy as np
import nibabel as nib
from dipy.tracking import utils
from dipy.tracking.utils import length
from mapping_test import *
"""
Reading the track
"""
streams1,hdr1=nib.trackvis.read('/home/nusrat/dataset_trackvis/101.trk')
tracks = np.array([s[0] for s in streams1], dtype=np.object) 

"""
affine for converting the streamline cordinate with the voxel cordinate
"""
affine=utils.affine_for_trackvis(voxel_size=np.array([2,2,2]))

"""
length function from the dipy 
https://github.com/nipy/dipy/blob/master/dipy/tracking/_utils.py
"""
lengths = list(length(tracks)) 

"""
fiter the whole tractography--like we are not interested the track less than 10. 
"""
lengths=np.array(lengths)
l=np.where(lengths>10)[0]

"""
rearrange the tracktography
"""
tracks=tracks[l]

"""
checking is there any crossing bewtween them--calling the function that retrun the id of streamline those are not crossing
"""
idx= streamline_mapping_new_step(tracks, affine=affine)

