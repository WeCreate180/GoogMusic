from flask_ask import statement, audio
from googmusic import ask, music_queue, client

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
def skip():
    next_ids = music_queue.next()['nid']
    streams = client.get_stream_url(next_ids)
    return audio().play(streams)

@ask.intent("GoogMusicPrevIntent")
def prev():
    prev_ids = music_queue.prev()['nid']
    streamss = client.get_stream_url(prev_ids)
    return audio().play(streamss)

@ask.intent("GoogMusicThumbsDown")
def thumbsDown():
    sid = client.get_track_info(music_queue.current()['nid'])
    sid['rating'] = 1
    client.change_song_metadata(sid)

@ask.intent("GoogMusicThumbsUp")
def thumbsUp():
    sids = client.get_track_info(music_queue.current()['nid'])
    sids['rating'] = 5
    client.change_song_metadata(sids)

@ask.intent("GoogMusicThumbsNone")
def clearRating():
    sidss = client.get_track_info(music_queue.current()['nid'])
    sidss['rating'] = 0
    client.change_song_metadata(sidss)

@ask.on_playback_nearly_finished()
def nearly_finished():
    if len(music_queue) > 0:
        next_id = music_queue.next()['nid']

        stream = client.get_stream_url(next_id)

        return audio().enqueue(stream)
