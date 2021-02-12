import subprocess

file = r"https://public-bucket-mine.s3.ap-south-1.amazonaws.com/Sasha+Belaya+vs+Oleksandra+Korashvili+new.mp4"

def get_thumbnail(input):
    output = r"/Users/Shreyas/Desktop/ffmpeg/thumb.png"
    cmd = f'ffmpeg -i "{input}" -ss 00:00:01.000 -vframes 1  -s 640x360  "{output}"'
    print(cmd)
    subprocess.check_output(cmd, shell=True)

get_thumbnail(file)
