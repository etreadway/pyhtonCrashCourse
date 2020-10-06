def makeAlbum(artist, albumName, trackNumber=''):
    '''Createing a dictionary of album information'''
    album = {}
    album['artist'] = artist
    album['albumName'] = albumName
    if trackNumber:
        album['trackNumber'] = trackNumber
    
    return album

recordInfo = makeAlbum('nirvana', 'bleach', 11)
print(recordInfo)

recordInfo = makeAlbum('pixies', 'doolittle')
print(recordInfo)

recordInfo = makeAlbum('kendrick lamar', 'DAMN')
print(recordInfo)