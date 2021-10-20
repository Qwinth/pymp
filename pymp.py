import time, os
import argparse
from pygame import mixer
from multiprocessing import Process, Pipe
mixer.init()
def process(cc):
    music = cc.recv()[0]
    mixer.music.load(music)
    mtime = mixer.Sound(music).get_length()
    While = cc.recv()[0]
    while True:
        recv = cc.recv()
        if recv == ['play']:
            cc.send([])
            mixer.music.play()
            time.sleep(mtime)
            if While == False:
                break
        


if __name__ == '__main__':
    #multiprocessing.freeze_support() uncomment this line if you use pyinstaller or cx_Freeze
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--parallel', action='store_true')
    parser.add_argument('-l', '--loop', action='store_true')
    parser.add_argument('path', nargs='+')
    args = parser.parse_args()
    if args.loop: While = True
    else: While = False
    if args.parallel:
        pc, cc = Pipe()
        Process(target=process, args=(cc,)).start()
        mixer.music.load(args.path[0])
        mtime = mixer.Sound(args.path[0]).get_length()
        pc.send([args.path[1]])
        pc.send([args.loop])
        while True:
            pc.send(['play'])
            pc.recv()
            mixer.music.play()
            time.sleep(mtime)
            if While == False:
                break
        
    else:
        if os.path.isfile(args.path[0]):
            mixer.music.load(args.path[0])
            mtime = mixer.Sound(args.path[0]).get_length()
            while True:
                mixer.music.play()
                time.sleep(mtime)
                if While == False:
                    break
        
        elif os.path.isdir(args.path[0]):
            dirlist = os.listdir(args.path[0])
            num = 0
            while True:
                while True:
                    try:
                        if dirlist[num].split('.')[-1] == 'mp3' or dirlist[num].split('.')[-1] == 'ogg':
                            mixer.music.load(args.path[0] + dirlist[num])
                            mtime = mixer.Sound(args.path[0] + dirlist[num]).get_length()
                            mixer.music.play()
                            time.sleep(mtime)
                            num += 1
                    except IndexError:
                        num = 0
                        break
                
                if While == False:
                    break
