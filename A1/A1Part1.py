import sys
import os
import matplotlib
import numpy
import scipy

sys.path.append("/home/aspma/aspma-course/sms-tools/software/models")
from utilFunctions import wavread

"""
A1-Part-1: Reading an audio file

Write a function that reads an audio file and returns 10 consecutive samples of the file starting from 
the 50001th sample. This means that the output should exactly contain the 50001th sample to the 50010th 
sample (10 samples). 

The input to the function is the file name (including the path) and the output should be a numpy array 
containing 10 samples.

If you use the wavread function from the utilFunctions module the input samples will be automatically 
converted to floating point numbers with a range from -1 to 1, which is what we want. 

Remember that in python, the index of the first sample of an array is 0 and not 1.

If you run your code using piano.wav as the input, the function should return the following 10 samples:  
array([-0.06213569, -0.04541154, -0.02734458, -0.0093997 ,  0.00769066,	0.02319407,  0.03503525, 
0.04309214, 0.04626606,  0.0441908], dtype=float32)
"""
def readAudio(inputFile):
    """
    Input:
        inputFile: the path to the wav file      
    Output:
        The function should return a numpy array that contains 10 samples of the audio.
    """
    import sys
    import os
    import matplotlib
    import numpy
    import scipy
    
    sys.path.append("/home/aspma/aspma-course/sms-tools/software/models")
    from utilFunctions import wavread
    #f_s = 44100.
    
    (fs, a) = scipy.io.wavfile.read(inputFile)
    print "fs",fs
    f_s = fs 
    def grabMySamples(objSParray, startSample, endSample, lengthSamples= -1.):
        """     
             mode 1:
                 arg1:      <input Object SciPy Audio   [obj] >
                 arg2:      <starting sample            -flt- >
                 arg3:      <end sample                 -flt- >
             mode 2:
                 arg1:      <input Object SciPy Audio   [obj] >
                 arg2:      <starting sample            -flt- >
                 arg3:      <  ANY NUMBER               -flt- >
                 arg4:      < length in samples         -int- >
             -----------------------------------------------------
             returns :      <       [SciPy Wav Array]         >
        """
        import matplotlib.pyplot as plt
        
        #unpack
        fs = float(objSParray[0])
        a = objSParray[1]
        lenSmpl = a.size * 1.0
        lenSec  =lenSmpl / fs
        
        verbose = False
        if verbose:
            
            print lengthSamples
            plt.plot(a)
            plt.show()
        
        if lengthSamples < 0:
        #    for i in range[ startSample, endSample ]:
            endingSample = endSample
        else:
        #    print startSample, startSample + lengthSamples
            endingSample = int(startSample + lengthSamples)
        return a[ startSample : endingSample]


    print "hello, whales."
    a = scipy.io.wavfile.read(inputFile) #  samplingFq , amplitudes
    #os.system("play "+ inputFile)
    #print len(a)
    #print a[1].max()
    smpl = grabMySamples(a, 50000, 10, 10)
    
    verbose = False
    if verbose:
        
        print lengthSamples
        plt.plot(smpl)
        plt.show()

    return smpl
    
class Odio:
    import sys
    import os
    import matplotlib
    import numpy
    import scipy
    
    def __init__(self,in_sF):
        
        self.pathInFile = in_sF
        
        (fs, a) = scipy.io.wavfile.read(in_sF)
        
        self.fs = float(objSParray[0])
        self.a = objSParray[1]
        self.lenSmpl = a.size * 1.0
        self.lenSec  =lenSmpl / fs   
        
    def grabMySamples(objSParray, startSample, endSample, lengthSamples= -1.):
        """     
             mode 1:
                 arg1:      <input Object SciPy Audio     [obj]       >
                 arg2:      <starting sample              -flt-       >
                 arg3:      <end sample                   -flt-       >
             mode 2:
                 arg1:      <input Object SciPy Audio     [obj]       >
                 arg2:      <starting sample              -flt-       >
                 arg3:      <  ANY NUMBER                 -flt-       >
                 arg4:      < length in samples           -int-       >
        """

        

        
        verbose = False
        if verbose:
            import matplotlib.pyplot as plt
            print lengthSamples
            plt.plot(a)
            plt.show()
        
        
        if lengthSamples < 0:
        #    for i in range[ startSample, endSample ]:
            endingSample = endSample
        else:
        #    print startSample, startSample + lengthSamples
            endingSample = int(startSample + lengthSamples)
        return a[ startSample : endingSample]    


    
    def writeOut(self,outputPathFile):
        pass
    
    #def max(self):
    
    #def sum(self):
    
    
    
    
    
if __name__ == "__main__":
    sF = "hmpback4_441.wav"
    odioF = sys.path[0]+os.sep+sF
    #os.system("play "+sF)
    out = readAudio(odioF)
    print len(out)
    for samples in out:
        print samples
    
    
