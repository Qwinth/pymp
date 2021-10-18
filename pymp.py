import sys
from pygame import mixer
from multiprocessing import Process, Pipe
mixer.init()
def process(cc):
    mixer.music.load(cc.recv()[0])
    recv = cc.recv()
    if recv == ['play']:
        cc.send([])
        mixer.music.play()
        while True:
            if mixer.music.get_busy() == 0:
                break
    
        


if __name__ == '__main__':
    multiprocessing.freeze_support()
    if sys.argv[1] == '-p' or sys.argv[1] == '--parallel':
        pc, cc = Pipe()
        Process(target=process, args=(cc,)).start()
        mixer.music.load(sys.argv[2])
        pc.send([sys.argv[3]])
        pc.send(['play'])
        pc.recv()
        mixer.music.play()
        while True:
            if mixer.music.get_busy() == 0:
                break
    else:
        mixer.music.load(sys.argv[1])
        mixer.music.play()
        while True:
            if mixer.music.get_busy() == 0:
                break
