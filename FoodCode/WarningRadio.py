import subprocess


def play_warning_sound():
    # WAV 오디오 파일 경로
    sound_file = "/usr/share/sounds/freedesktop/stereo/complete.oga"
    # paplay 명령 실행하여 오디오 파일 재생
    subprocess.run(["paplay", sound_file])


# 경고음 재생
play_warning_sound()
