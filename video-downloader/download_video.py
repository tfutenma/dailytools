import os
from pytube import YouTube
from pytube.cli import on_progress


def download_video(url, format):
    yt = YouTube(url, on_progress_callback=on_progress)
    yt.register_on_progress_callback(on_progress)
    homedir = os.path.expanduser("~")

    if format == 'mp3':
        video = yt.streams.filter(only_audio=True).first()
        extension = 'mp3'
    else:
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        extension = 'mp4'

    if not os.path.exists(f'{homedir}/Downloads/videos'):
        os.mkdir(f'{homedir}/Downloads/videos')

    video.download(output_path=f'{homedir}/Downloads/videos', filename=f'{yt.title[:30]}.{extension}')
    print(f'Download successfully in {extension} format\n')

if __name__ == '__main__':
    url = input('Enter the YouTube URL: ')
    format = input('Enter the format (mp4/mp3): ')

    download_video(url, format)
