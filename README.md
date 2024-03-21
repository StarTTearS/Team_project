# 🍳 OPENCV와 딥러닝을 이용한 음식 추천 프로그램
![title1](https://github.com/brkim92/Team_project/assets/154492346/69df0c27-6a37-47a6-92b6-26cf3bcf7e91)

<br>

## Outline
* 프로젝트 주제: OPENCV와 딥러닝을 이용한 음식 추천 프로그램
* 프로젝트 수행자: 인텔 엣지AI SW개발자 아카데미/ 팀 뭐먹 (김보람, 김용제, 이경준, 천호진)
* 프로젝트 수행기간: 24/03/07 ~ 24/03/22

<br>

## Motivation

<br>

개발 동기는 아래와 같다.

![스크린샷 2024-03-19 11-13-45](https://github.com/brkim92/Team_project/assets/154478954/23dad1a6-e29c-480a-8de0-e318081b53cc)

![스크린샷 2024-03-19 11-00-33](https://github.com/brkim92/Team_project/assets/154478954/d0bff305-2664-4b51-9520-b92c6944a32c)

![스크린샷 2024-03-19 11-04-49](https://github.com/brkim92/Team_project/assets/154478954/fa9528b6-ac4a-4462-ab73-21fa4e106fe1)

```plain
* 세상에는 결정장애를 겪는 사람들이 예상보다 많고, 이들이 시간을 낭비하는 것을 줄여주기 위한 프로그램이 필요하다.
  또한, 건강에 대한 관심이 높아지면서 제로콜라 열풍과 같은 트렌드가 나타나고 있어, 개개인이 먹는 음식의 칼로리를
  계산하고 건강에 적합한 음식을 추천해주는 서비스가 필요하다. 이러한 요구에 부합하기 위해 주 타겟인 결정장애자부터
  다이어트 및 운동에 관심이 있는 20~30대 일반인 등 다양한 사용자를 대상으로 음식 정보 제공 및 랜덤 음식 추천 등의
  주요 기능을 갖춘 프로그램을 개발하고자 한다.
```

유스케이스 시나리오는 아래와 같다.

```
첫번째, 결정장애를 가지고 있는 사람이 있다.
두번째, 다이어트 및 운동에 관심이 있는 20~30대 일반인이 있다.

결정장애를 가진 사람이 식사를 무엇으로 선택할지 고민한다. 
'오늘 뭐 먹지?'에서 성별을 선택한다.
성별 선택을 기준으로 기초 대사량 계산한 뒤 적절한 식단인지 아닌지 판별하는 기준으로 삼는다. 
랜덤으로 음식을 추천하는 버튼을 누른다.
오늘의 음식 추천 기능/아침,점심,저녁 추천 기능을 제공하며 결정장애자의 결정을 도와준다.
만약 기초대사량이 넘는 식단이 나오면 경고 알람이 나오고 적절한 식단이 나오면 좋다는 알람이 나온다.
음성인식을 통해 랜덤으로 음식을 추천하는 버튼을 누른다.
음성인식 시작 버튼을 누른 후 2초 후 추천/일정이라는 단어를 말하면 추천은 오늘의 음식 추천 기능/일정은 아침,점심,저녁 추천 기능을 수행한다.
북마크 추천 모드 버튼을 누른다.
북마크에 저장된 음식 중에 자동으로 추천을 해준다.
카테고리 선택 버튼을 누른다.
카테고리를 정하면 그 카테고리에 있는 음식 중에서 추천을 해준다.
첫번째 사용자의 사용이 끝났다.

다이어트 및 운동에 관심이 있는 20~30대 일반인이 식사를 무엇으로 할지 고민한다.
카메라 인식 모드 버튼을 누른다.
자신의 식단을 카메라로 비추면 식단은 인식하고 식단에 포함된 음식 각각의 정보 뿐만 아니라 전체 음식의 정보도 보여준다.
두번째 사용자의 사용이 끝났다.
```
<br>

## 팀원 구성 및 역할 분담
### 💿김보람
- **ROLE**
    - 작업 내용 : 이미지 라벨링, 데이터셋 구성, 모델 선정, 학습된 모델 생성
    - 공통 작업 : 음식 이미지 찾기

<br>
    
### 👑김용제
- **ROLE**
    - 작업 내용 : 이미지 검출 기능 및 정보출력, 음식이미지 랜덤하게 출력, 음성 인식, 카테고리, 북마크 기능 코드 개발
    - 공통 작업 : 음식 이미지 찾기

<br>

### ⌨️이경준
- **ROLE**
    - 작업 내용 : 카메라에 비친 이미지 검출 기능 및 음식 정보 출력 코드 개발 
    - 공통 작업 : 음식 이미지 찾기

<br>

### 🖥️천호진

- **ROLE**
    - 작업 내용 : GUI 프레임워크 개발, PPT 제작
    - 공통 작업 : 음식 이미지 찾기
    
<br>

## 개발 환경
<br>

![system](https://github.com/brkim92/Team_project/assets/154492346/90a2fcb4-8a05-4ee0-96af-76e08e3bc6cf)


<br>

* OpenCV
* OTX
* CVAT
* Python
* Webcam
* GUI Framework

<br>

## Project Schedule
![Screenshot from 2024-03-20 17-21-55](https://github.com/brkim92/Team_project/assets/154481519/d9340ed4-fbd9-4012-87df-5eda7deb439a)

<br>

## Gantt Chart
![gantt chart](https://github.com/brkim92/Team_project/assets/154492346/cf77d33b-c21b-49b4-8bdb-745b406d9770)

<br>

## Sequence Diagram
![Sequence Diagram](https://github.com/brkim92/Team_project/assets/154492346/0124c87c-f0b8-4458-8b54-f5b6f18d0193)

<br>

## Module Diagram
![Module Diagram](https://github.com/brkim92/Team_project/assets/154492346/80306fa4-97f7-4919-bf8e-9475cc5099cf)

<br>

<img src="https://github.com/brkim92/Team_project/blob/64fa79c7b4b9a857b0be004f93cfb0df4f1fdb7e/PPT%20and%20Design%20Image/simple%20diagram.png" width="500" height="500"/>

<br>

## High Level Design

![Screenshot from 2024-03-19 09-18-18](https://github.com/brkim92/Team_project/assets/154481519/ef8418bb-77fa-4ebc-87fa-1dcb5bcf880d)

<br>

## Clone code

* (각 팀에서 프로젝트를 위해 생성한 repository에 대한 code clone 방법에 대해서 기술)
  
* git clone https://github.com/brkim92/Team_project.git

<br>

## Prerequite

* (프로젝트를 실행하기 위해 필요한 dependencies 및 configuration들이 있다면, 설치 및 설정 방법에 대해 기술)

* OTX Install
  >- OTX를 사용을 위한 가상환경 생성  
  > ```shell
  > python -m venv .otx_venv
  > source .otx_env/bin/activate
  > ```
  >- 필요한 Package Install
  > ```shell
  > pip install -U pip  #pip package manager를 최신 버전으로 Upgrade
  > pip install wheel  #wheel package install
  > pip install datumaro[default]  #기본 종속성과 함께 Datumaro package inatall
  > ```
  >- Pytorch & mmcv Install
  > ```shell
  > pip install torch==1.13.1 torchvision==0.14.1 --extra-index-url https://download.pytorch.org/whl/cu117  #CUDA 11.7와 호환
  > pip uninstall mmcv-full
  > pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu117/torch1.13.0/index.html  #CUDA 11.7 및 PyTorch 1.13.0과 호환
  > ```
  >- OTX Install
  > ```shell
  > pip install otx[full]
  > ```

<br>

* Docker Install
  
  ```shell
  https://opencv.github.io/cvat/docs/administration/basics/installation/
  ```
<br>

* Requirements.txt Install
  
  ```shell
  pip install -r requirements.txt
  ```  

<br>

* GUI Install
  
  ```shell
  pip install tkinter

  import tkinter as tk
  from tkinter import *
  from tkinter import ttk
  ```
  
<br>

* DroidCam
  ```shell
  cd /tmp/
  wget -O droidcam_latest.zip https://files.dev47apps.net/linux/droidcam_2.1.2.zip
  ' # sha1sum: d5eb769f249011fbfa0edef05ffd56949b63d470'
  unzip droidcam_latest.zip -d droidcam
  cd droidcam && sudo ./install-client

   ＊ wifi 아닐경우) 안드로이드 usb 드라이버 다운
  sudo apt-get install adb
  ```

<br>

## Steps to build

* (프로젝트를 실행을 위해 빌드 절차 기술)
* Model 선택 & 학습
  
  ```shell
  otx find --template --task DETECTION  #사용 가능한 Object Detection Model list
  otx build Object_Detection_YOLOX_L --train-data-root /annotations file이 있는 상위 경로  #Model 선택 후 학습 Data의 Root 경로를 지정하여 Mode을 Build
  cd otx-workspace-DETECTION/  #작업 Directory 변경
 
  otx train  #Model 학습
  otx export --load-weights ./outputs/latest_trained_model/models/weights.pth --output ./outputs/export  #학습된 모델의 가중치를 내보냄
  otx optimize --load-weights ./outputs/latest_trained_model/models/weights.pth --output ./outputs/oprimize/  #Model 최적화
  otx deploy --load-weights ./outputs/export/openvino.xml --output ./outputs/deploy/  #Model을 특정한 환경에 배포 가능한 형태로 변환하는 과정
  cd outputs/deploy/openvino/python/
  
  python3 demo.py -i 카메라 번호
  ```
  
* DroidCam Video Stream
  Droidcam 을 이용해 스마트폰을 웹캠으로 이용하여 음식 감지 편의성 높이기

  ```shell
  핸드폰)
  1) Droidcam 어플리케이션 다운
  2) wifi ip, port 번호 확인

  리눅스)
  1) 리눅스용 Droidcam 다운
  2) wifi 아닐경우) 안드로이드 usb 드라이버 다운
  3) Droidcam 실행
  4) 핸드폰에서 확인한 wifi ip 및 port 번호 입력 후 start
  ```
  
<br>

## Tree
```shell
.
├── Category.py
├── Food.py
├── Food_Nutrient.xlsx
├── Good.mp3
├── Police_Siren.mp3
├── Siren.py
├── Speech_recognition.py
├── TextOutput.py
├── TextOutput2.py
├── VoiceOutput.py
├── __pycache__
│   ├── Category.cpython-310.pyc
│   ├── Category.cpython-38.pyc
│   ├── Siren.cpython-310.pyc
│   ├── Speech_recognition.cpython-310.pyc
│   ├── Speech_recognition.cpython-38.pyc
│   ├── TextOutput.cpython-310.pyc
│   ├── TextOutput.cpython-38.pyc
│   ├── TextOutput2.cpython-310.pyc
│   ├── VoiceOutput.cpython-310.pyc
│   ├── VoiceOutput.cpython-38.pyc
│   ├── bookmark.cpython-310.pyc
│   ├── bookmark.cpython-38.pyc
│   ├── display_food_image.cpython-310.pyc
│   ├── display_food_image.cpython-38.pyc
│   ├── gets_nutrient.cpython-310.pyc
│   ├── gets_nutrient.cpython-38.pyc
│   ├── warn_good_image.cpython-310.pyc
│   └── warn_good_image.cpython-38.pyc
├── bookmark.py
├── demo.py
├── display_food_image.py
├── food.png
├── foodgui.py
├── gets_nutrient.py
├── imageresize.py
├── openvino
│   ├── README.md
│   ├── model
│   │   ├── config.json
│   │   ├── model.bin
│   │   └── model.xml
│   └── python
│       ├── LICENSE
│       ├── demo.py
│       ├── model_wrappers
│       │   ├── __init__.py
│       │   └── __pycache__
│       │       └── __init__.cpython-310.pyc
│       └── requirements.txt
├── openvino.zip
├── requirements.txt
├── title1.png
├── visualizer.py
└── warn_good_image.py

6 directories, 49 files
```

<br>

## Output
* (프로젝트 실행 화면 캡쳐)
  
![시연자료01](https://github.com/brkim92/Team_project/assets/154492346/f6b6b3bf-b2e6-4f8a-9c55-2ecf8b235f3d)

![시연자료02](https://github.com/brkim92/Team_project/assets/154492346/896e4009-3b6e-46ea-80d5-a35cdca22041)

![시연자료03](https://github.com/brkim92/Team_project/assets/154492346/5c9588a7-92ab-455b-9ed0-13550a41c194)

![시연자료04](https://github.com/brkim92/Team_project/assets/154492346/e45edfe7-e5d2-43b4-9496-eec2a4feb3e7)

<br>

## Demo Video
(아래 이미지를 클릭하시면 유튜브로 이동합니다.)

[![Video Label](http://img.youtube.com/vi/5kHoBU4CPGc/0.jpg)](https://youtu.be/5kHoBU4CPGc)

<br>

## Presentation Document
(아래 이미지를 클릭하시면 구글 드라이브로 이동합니다.)
[![프로젝트 발표자료](https://github.com/brkim92/Team_project/blob/0fb882f2bcb6af63c23c7927bebfb3ebf9024bda/PPT%20and%20Design%20Image/project_thumbnail.jpg)](https://docs.google.com/presentation/d/1L_pPFMZthQaw05bNle745C850yg6_qc9/edit?usp=sharing&ouid=115838414545194956375&rtpof=true&sd=true)

<br>

## Appendix
* [OPENVION 참고 자료](https://openvinotoolkit.github.io/training_extensions/stable/guide/explanation/algorithms/object_detection/object_detection.html) 
* [YOLOX 참고 자료](https://github.com/Megvii-BaseDetection/YOLOX)
* [OS.SYSTEM 함수 참고 자료](https://ctkim.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-os-%EB%AA%A8%EB%93%88)
* [음성파일 재생, pygame 모듈](https://www.jbmpa.com/pygame/10)
* [음성인식, speech_recognition](https://sanggi-jayg.tistory.com/entry/Python-%EC%9D%8C%EC%84%B1%EC%9D%B8%EC%8B%9DSpeech-Recognition-%EA%B3%BC-TTS-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0)

