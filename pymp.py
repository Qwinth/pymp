import time, sys
from pygame import mixer
from multiprocessing import Process, Pipe
mixer.init()

def process(cc):
    music = cc.recv()[0]
    mixer.music.load(music)
    mtime = mixer.Sound(music).get_length()
    recv = cc.recv()
    if recv == ['play']:
        cc.send([])
        mixer.music.play()
        time.sleep(mtime)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    if sys.argv[1] == '-p' or sys.argv[1] == '--parallel':
        pc, cc = Pipe()
        Process(target=process, args=(cc,)).start()
        mixer.music.load(sys.argv[2])
        mtime = mixer.Sound(sys.argv[2]).get_length()
        pc.send([sys.argv[3]])
        pc.send(['play'])
        pc.recv()
        mixer.music.play()
        time.sleep(mtime)
       break
    
    else:
        mixer.music.load(sys.argv[1])
        mtime = mixer.Sound(sys.argv[1]).get_length()
        mixer.music.play()
        time.sleep(mtime)
