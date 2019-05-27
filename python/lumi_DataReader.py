import pandas as pd
import h5py


COLNAMES = ["fillnum","runnum","lsnum","nbnum","timestampsec","timestampmsec","totsize","avgraw","avg",
            "bxraw","bx","maskhigh","masklow"]

                   
           

def BrilReader(filename, key, columns=COLNAMES):
    '''
    columns are listed as following.
    one row of data includes 4 nibbles, or 1e14 orbits,
        "fillnum"          +0    native unsigned int
        "runnum"           +4    native unsigned int
        "lsnum"            +8    native unsigned int
        "nbnum"            +12   native unsigned int
        "timestampsec"     +16   native unsigned int
        "timestampmsec"    +20   native unsigned int
        "totsize"          +24   native unsigned int
        "publishnnb"       +28   native unsigned char
        "datasourceid"     +29   native unsigned char
        "algoid"           +30   native unsigned char
        "channelid"        +31   native unsigned char
        "payloadtype"      +32   native unsigned char
        "calibtag"         +33   32-byte null-terminated ASCII string
        "avgraw"           +65   native float
        "avg"              +69   native float
        "bxraw"            +73   [3564] native float
        "bx"               +14329 [3564] native float
        "maskhigh"         +28585 native unsigned int
        "masklow"          +28589 native unsigned int
    '''
    f = h5py.File(filename, 'r')
    dset = f[key]
    
    n = len(dset)
    df = pd.DataFrame()
    for c in columns:
        df[c] = [i for i in dset[:,c]]
    return df
    