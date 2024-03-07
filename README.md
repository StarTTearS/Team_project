# Project ABC

* (간략히 프로젝트를 설명하고, 최종 목표가 무엇인지에 대해 기술)
* 주제: "오늘 뭐 먹지?"라는 질문을 했을 때 랜덤하게 음식의 이미지와 정보를 출력해주는 프로그램

* 이유1 : 세상에는 결정장애들이 생각보다 많음. 그들의 시간낭비를 줄여주기 위한 프로그램이 필요

* 이유2 : 운동하는 사람들이 많음. 당신들이 먹는 음식에 대한 칼로리 계산 및 추천 음식이 필요

* 이유3 : 당뇨병 환자들을 위한 건강관리 프로그램 등이 부족함. 그들을 위한 당 관리, 식단 관리 필요

* 주 타겟 : 결정장애 / 식단관리가 필요한 사람 / 20~30대 건강관리, 다이어트, 운동에 관심이 많은 일반인 / 당뇨병 환자

* 주기능 : 음식이름을 기입(텍스트) 또는 카메라로 이미지를 찍거나 비추었을 때, 그에 해당하는 음식의 정보를 출력

* 주기능2 : 오늘 뭐 먹지? 를 입력했을 때 랜덤으로 음식추천

* 부가 기능1 : 주식 / 디저트 / 음료 카테고리 생성

* 부가 기능2 : 오늘 먹은 음식에 대한 총 칼로리 계산 및 탄단지 비율 계산

* 부가 기능3 : 하루 남성 여성 기초 대사량 또는 평균 섭취 칼로리를 넘어가면 경고 표시 또는 사이렌을 울려서 그만 먹으라고 말하는 기능 추가

* 부가 기능4 : 만약 경고를 무시하고 계속 섭취할 경우 칼로리 소비를 위한 건강관리 프로그램 생성 추가

## High Level Design

* (프로젝트 아키텍쳐 기술, 전반적인 diagram 으로 설명을 권장)

## Clone code

* (각 팀에서 프로젝트를 위해 생성한 repository에 대한 code clone 방법에 대해서 기술)
  
* git clone https://github.com/brkim92/Team_project.git

## Prerequite

* (프로잭트를 실행하기 위해 필요한 dependencies 및 configuration들이 있다면, 설치 및 설정 방법에 대해 기술)

```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
* OpenCV
* otx
* CVAT
* Python
* Webcam
* GUI Framework

## Steps to build

* (프로젝트를 실행을 위해 빌드 절차 기술)

```shell
cd ~/xxxx
source .venv/bin/activate

make
make install
```

## Steps to run

* (프로젝트 실행방법에 대해서 기술, 특별한 사용방법이 있다면 같이 기술)

```shell
cd ~/xxxx
source .venv/bin/activate

cd /path/to/repo/xxx/
python demo.py -i xxx -m yyy -d zzz
```

## Output

* (프로젝트 실행 화면 캡쳐)

![./result.jpg](./result.jpg)

## Appendix

* (참고 자료 및 알아두어야할 사항들 기술)
