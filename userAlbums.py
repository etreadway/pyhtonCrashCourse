def makeAlbum(artist, albumName, trackNumber=''):
    '''Createing a dictionary of album information'''
    album = {}
    album['artist'] = artist
    album['albumName'] = albumName
    if trackNumber:
        album['trackNumber'] = trackNumber
    
    return album

while True:
    print('Type "q" at any time to quit')
    newArtist = input('Type the name of the artist: ')
    if newArtist == 'q':
        break
    newAlbumName = input('Type the name of the album: ')
    if newAlbumName == 'q':
        break
    newTrackNumber = input('Type the number of tracks (or leave blank and ENTER): ')
    if newTrackNumber == 'q':
        break
    newRecord = makeAlbum(newArtist, newAlbumName, newTrackNumber)
    print(newRecord)