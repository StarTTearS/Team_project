import speech_recognition as sr  # 음성인식 모듈


def recognize_speech(duration=1):
    # 음성 인식 객체 생성
    recognizer = sr.Recognizer()

    # 마이크에서 음성을 수집
    with sr.Microphone() as source:
        print("음성을 입력하세요...")
        recognizer.adjust_for_ambient_noise(
            source, duration=duration)  # 주변 소음 조절
        audio = recognizer.listen(source, phrase_time_limit=3)

        # Write audio to a WAV file
        with open("microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())

    audio_file_path = '/home/kyj/FoodCode/microphone-results.wav'
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)  # 전체 오디오 파일을 읽어옴
        text = recognizer.recognize_google(audio, language='ko-KR')
        return text

    # while True:
    # 음성을 텍스트로 변환하여 반환
    # text = recognizer.recognize_google(audio, language='ko-KR')
