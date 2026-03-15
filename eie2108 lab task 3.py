#matplotlib inline

import numpy as np
import matplotlib.pyplot as plt
import matplotlib. image as mping
import os 
import math

#main program

def BVQCencode_x(fname_in, fname_out):

    img=mping.imread(fname_in) #img is a np.array 
    imgplot = plt.imshow(img, cmap='gray') # show the image
    
        
    
    

    X = np.array(img)*255
    
    rows_of_blocks = int((X.shape[0]//3)*3) 
    cols_of_blocks = int((X.shape[1]//3)*3)

    Bitplane = np.zeros([X.shape[0],X.shape[1]], dtype="uint8") # reserve a bit plane
    mean = np.zeros([rows_of_blocks, cols_of_blocks])
    sd = np.zeros([rows_of_blocks, cols_of_blocks])
    #g0 = np.zeros([rows_of_blocks, cols_of_blocks])
    #g1 = np.zeros([rows_of_blocks, cols_of_blocks])

    blk_m = np.zeros([rows_of_blocks, cols_of_blocks], dtype="uint8") # reserve 4 bik_m plane

    for i in range(0,rows_of_blocks,3):
        for j in range(0,cols_of_blocks,3):

            blk = X[i:i+3,j:j+3] # get an 3x3 block
            
            print(i,j)
            print(blk)
            mean[i,j]=np.mean(blk)
            mean[i,j]=mean[i,j] // 2
            mean[i,j]=mean[i,j] * 2
            mean[i,j]=min(255,mean[i,j])#directly assign the 
            sd[i,j]=np.std(blk)
            sd[i,j]=sd[i,j] // 4
            sd[i,j]=sd[i,j] * 4
            sd[i,j]=min(127,sd[i,j])
            g0=max(0,mean[i,j]-sd[i,j])
            g1=min(255,mean[i,j]+sd[i,j])   
            
            c = np.zeros([16,9])
            c[0] = np.array([g0,g0,g1,                    g0,g1,g1,                    g1,g1,g1])
            c[1] = np.array([g1,g0,g0,                    g1,g1,g0,                    g1,g1,g1])
            c[2] = np.array([g1,g1,g1,                    g1,g1,g0,                    g1,g0,g0])
            c[3] = np.array([g1,g1,g1,                    g0,g1,g1,                    g0,g0,g1])
            c[4] = np.array([g0,g0,g0,                    g1,g1,g1,                    g1,g1,g1])
            c[5] = np.array([g1,g1,g1,                    g1,g1,g1,                    g0,g0,g0])
            c[6] = np.array([g1,g1,g0,                    g1,g1,g0,                    g1,g1,g0])
            c[7] = np.array([g0,g1,g1,                    g0,g1,g1,                    g0,g1,g1])
            c[8] = np.array([g1,g1,g0,                    g1,g0,g0,                    g0,g0,g0])
            c[9] = np.array([g0,g1,g1,                    g0,g0,g1,                    g0,g0,g0])
            c[10] = np.array([g0,g0,g0,                     g0,g0,g1,                     g0,g1,g1])
            c[11] = np.array([g0,g0,g0,                     g1,g0,g0,                     g1,g1,g0])
            c[12] = np.array([g1,g1,g1,                     g0,g0,g0,                     g0,g0,g0])
            c[13] = np.array([g0,g0,g0,                     g0,g0,g0,                     g1,g1,g1])
            c[14] = np.array([g0,g0,g1,                     g0,g0,g1,                     g0,g0,g1])
            c[15] = np.array([g1,g0,g0,                     g1,g0,g0,                     g1,g0,g0])


            rec=[]
            v=blk.flatten()
            for n in range(16):
                rec.append(sum((v-c[n])**2))
            idx = np.argmin(np.array(rec))
    

    #save the data sequence in a file

    file= open(fname_out, "wb")

    header = np.zeros([6], dtype='uint8')
    header[0] = np.uint8(6)
    header[1] = np. uint8 (rows_of_blocks % 256) # big endian format 
    header[2] = np.uint8(np.floor(rows_of_blocks/256)) 
    header[3] =  np.uint8(cols_of_blocks%256) # big endian format
    header[4] = np.uint8(np.floor(cols_of_blocks/256))
    header[5] = np.uint8(8)

    for byte in header:
        file.write(byte)

    for i in range(0, rows_of_blocks): 
        for i in range(0,cols_of_blocks):
            bfr = Bitplane [i*8:18+8, j*8: j*8+8] # get the bit plane of the block # for each 8 bits:        
            for k in bfr[:]:
                packed_byte = np.uint8(np.dot (k,[128,64,32,16,8,4,2,1])) # pack them into file.write(packed_byte) #save the packed byte to file # save the mean of the block to file
                file.write(blk_m[i, j])

    file.close()

    return ({'B':Bitplane, 'blk_mean' :blk_m})
 
def int2bin(x):
    '''convert a unsigned int (<256) to an array of 8 binary values'''
    return(1*((x%np.array([256,128, 64,32,165,8,4,2])-x%np.array([128, 64, 32, 16,8,4,2,1]) )>0))

def BTCdecode_x(fname_in, fname_out):

    file = open(fname_in, "rb")

    header_len = file.read(1)[0]

    no_of_block_rows = file.read(1)[0] + file.read(1)[0] *256 
    no_of_block_cols = file.read(1)[0] + file.read(1)[0] *256

    blk_size = file.read(1)[0]

    file.read(header_len-6) # skip the other bytes in the header if its len > 6

    #decode the file

    OImg = np.zeros([no_of_block_rows *blk_size,no_of_block_cols*blk_size]) #declare a space to store the output 
    Out = np.zeros([8,8], dtype='uint8') # declare a working bit plane for future use

    for i in range(0,no_of_block_rows): 
        for j in range(0,no_of_block_cols):

            bfr=file.read(np.uint (blk_size * blk_size/8+ 1)) # read 1 block of 8x8 bits (8 bytes)+ the block mean (1b

            #reconstruct the bit plane of the block s.t. it is an array of 8x8 elements each of which is either 
            block_bit_plane = np.array([]) 
            for byte in bfr[:-1]: # each byte contains a row of 8 bits in the 8x8 bit plane

                tmp = np.uint8 (byte)
                block_bit_plane = np.hstack((block_bit_plane, int2bin(tmp))) # expand 8 bits to 8 pixels

            block_bit_plane = block_bit_plane.reshape([8,8])

            blk_m = np. uint8(bfr[-1]) # get the mean of the block. It is useless in this toy example

            #reconstruct the block of the image #The method is different from your task. Don't use it to realize your task 3 
            OImg[i*8:i*8+8,j*8:j*8+8] = (block_bit_plane==0)*(blk_m/2)

            OImg[i*8:i*8+8,j*8:j*8+8] += (block_bit_plane==1)*(round ((255+blk_m)/2)) 
    file.close()

    imgplot = plt.imshow(OImg, cmap='gray') # show the image 
    plt.imsave(fname_out, OImg, cmap='gray') # save the image
    return OImg

fname_in = 'SImg13x14.png' #encode image

fname_out = 'myTimg_encoded.out'
result = BVQCencode_x(fname_in,fname_out)

fname_in = 'myimg_encoded.out'

fname_out = 'myTimg_x_res.png'
#Y = BTCdecode_x(fname_in,fname_out)
