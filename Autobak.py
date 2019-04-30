import sys
import time
import os

def updateMTime(files, oldtime, start):
    for f in files:
        stat = os.stat(f)
        oldtime.append( stat.st_mtime )

def isUpdate( file , oldtime):
    stat = os.stat(file)
    if stat.st_mtime > oldtime:
        return 1

    return 0

def main():
    home = os.path.expanduser('~')
    defaultBakpath = os.path.join(home, 'Dropbox/Linux/Autobak/')

    needBak = [
           os.path.join(home, '.vimrc'), 
           os.path.join(home, '.zshrc'), 
           os.path.join(home, '.zsh_history'), 
           os.path.join(home, '.ideavimrc'), 
           os.path.join(home, '.xprofile'), 
           os.path.join(home, '.tmux.conf'), 
           os.path.join(home, '.ssh'), 
           os.path.join('', '/etc/shadowsocks'),
           os.path.join(home, '.vim'),
            ]

    while(True):
        oldtime = []
        updateMTime(needBak, oldtime, 0)
        time.sleep(90)
        for i, f in enumerate(needBak):
            if isUpdate( f, oldtime[i] ):
                print('File %s changed' % f)
                print('Rsync files...')
                os.system('rsync -av '+ f + ' ' + defaultBakpath)
                print('Rsync finish')


    print('All done.', end='\n\n')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit
