from flask_ask import statement, audio
from googmusic import ask, music_queue, client, musicman

@ask.intent('AMAZON.CancelIntent')
def cancel():
    return audio().stop()

@ask.intent("AMAZON.PauseIntent")
def pause():
    return audio('Pausing').stop()

@ask.intent("AMAZON.ResumeIntent")
def resume():
    return audio('Resuming').resume()

@ask.intent("GoogMusicSkipIntent")
def googSkip():
    next_ids = music_queue.next()['nid']
    streams = client.get_stream_url(next_ids)
    return audio().play(streams)

@ask.intent("AMAZON.NextIntent")
def amznSkip():
    next_ids = music_queue.next()['nid']
    streams = client.get_stream_url(next_ids)
    return audio().play(streams)

@ask.intent("AMAZON.PreviousIntent")
def amznPrev():
    prev_ids = music_queue.prev()['nid']
    streamss = client.get_stream_url(prev_ids)
    return audio().play(streamss)

@ask.intent("GoogMusicPrevIntent")
def googPrev():
    prev_ids = music_queue.prev()['nid']
    streamss = client.get_stream_url(prev_ids)
    return audio().play(streamss)

@ask.intent("GoogMusicThumbsDown")
def thumbsDown():
    sid = client.get_track_info(music_queue.current()['nid'])
    sid['rating'] = 1
    client.change_song_metadata(sid)
    next_ids = music_queue.next()['nid']
    streams = client.get_stream_url(next_ids)
    return audio("Disliked.").play(streams)

@ask.intent("GoogMusicThumbsUp")
def thumbsUp():
    sids = client.get_track_info(music_queue.current()['nid'])
    sids['rating'] = 5
    client.change_song_metadata(sids)
    return audio("Liked.")

@ask.intent("GoogMusicThumbsNone")
def clearRating():
    sidss = client.get_track_info(music_queue.current()['nid'])
    sidss['rating'] = 0
    client.change_song_metadata(sidss)
    return audio("Rating cleared.")

@ask.intent("GoogMusicTitle")
def googMusicTitle():
    preSetup = client.get_track_info(music_queue.current()['nid'])
    title = preSetup['title']
    print(title)
    return audio(title)

@ask.intent("GoogMusicArtist")
def googArtistTitle():
    prePreSetup = client.get_track_info(music_queue.current()['nid'])
    artist = prePreSetup['artist']
    print(artist)
    return audio(artist)

@ask.intent("GoogMusicLoopMode")
def googLoopMode():
    if not music_queue.loop():
        return audio('Loop mode on.')
    else:
        return audio('Loop mode off.')
    
@ask.intent("AMAZON.LoopOffIntent")
def amznLoopOff():
    if not music_queue.loop():
        music_queue.loopOn()
        return audio('Loop mode on.')
    else:
        music_queue.loopff()
        return audio('Loop mode off.')
    
@ask.intent("AMAZON.LoopOnIntent")
def amznLoopOn():
    if not music_queue.loop():
        music_queue.loopOn()
        return audio('Loop mode on.')
    else:
        music_queue.loopOff()
        return audio('Loop mode off.')
    
@ask.intent("AMAZON.StartOverIntent")
def restartIntent():
    restart_id = client.get_track_info(music_queue.current()['nid'])
    artist = restart_id['artist']
    title = restart_id['title']
    song = musicman.get_song(title, artist)
    reStream = client.get_stream_url(song['storeId'])
    return audio.play(reStream)

@ask.on_playback_nearly_finished()
def nearly_finished():
    if music_queue.loop():
        if len(music_queue) > 0:
            next_id = music_queue.next()['nid']

            stream = client.get_stream_url(next_id)

            return audio().enqueue(stream)
