import pygame


def Warning_Output():
    # 스크린 전체 크기 지정
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 500

    pygame.init()

    # 스크린 객체 저장
    SCREEN1 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("pygame sound")

    # wav, mp3, ogg 가능
    pygame.mixer.music.load('Police_Siren.mp3')

    # Music stream 무한 반복
    pygame.mixer.music.play(-1)

    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    v = pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(v + 0.1)
                    print("volume up")

                if event.key == pygame.K_DOWN:
                    v = pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(v - 0.1)
                    print("volume down")

                if event.key == pygame.K_LEFT:
                    pygame.mixer.music.pause()
                    print("일시 멈춤")

                if event.key == pygame.K_RIGHT:
                    pygame.mixer.music.unpause()
                    print("다시 재생")

                if event.key == pygame.K_a:
                    playing = False
                    pygame.quit()


def Good_Output():
    # 스크린 전체 크기 지정
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 500

    pygame.init()

    # 스크린 객체 저장
    SCREEN2 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("pygame sound")

    # wav, mp3, ogg 가능
    pygame.mixer.music.load('Good.mp3')

    # Music stream 무한 반복
    pygame.mixer.music.play(-1)

    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    v = pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(v + 0.1)
                    print("volume up")

                if event.key == pygame.K_DOWN:
                    v = pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(v - 0.1)
                    print("volume down")

                if event.key == pygame.K_LEFT:
                    pygame.mixer.music.pause()
                    print("일시 멈춤")

                if event.key == pygame.K_RIGHT:
                    pygame.mixer.music.unpause()
                    print("다시 재생")

                if event.key == pygame.K_a:
                    playing = False
                    pygame.quit()
