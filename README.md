# 🍳 OPENCV와 딥러닝을 이용한 음식 추천 프로그램
![title1](https://github.com/brkim92/Team_project/assets/154492346/69df0c27-6a37-47a6-92b6-26cf3bcf7e91)

<br>

## Outline
* 프로젝트 주제: OPENCV와 딥러닝을 이용한 음식 추천 프로그램
* 프로젝트 수행자: 인텔 엣지AI SW개발자 아카데미/ 팀 뭐먹 (김보람, 김용제, 이경준, 천호진)
* 프로젝트 수행기간: 24/03/07 ~ 24/03/22

<br>

## Motivation
* 이유1 : 세상에는 결정장애들이 생각보다 많음. 그들의 시간낭비를 줄여주기 위한 프로그램이 필요

    + 이유2 : 운동하는 사람들이 많음. 당신들이 먹는 음식에 대한 칼로리 계산 및 추천 음식이 필요

      + 이유3 : 당뇨병 환자들을 위한 건강관리 프로그램 등이 부족함. 그들을 위한 당 관리, 식단 관리 필요

* 주 타겟 : 결정장애 / 식단관리가 필요한 사람 / 20~30대 건강관리, 다이어트, 운동에 관심이 많은 일반인 / 당뇨병 환자

* 주기능 : 음식이름을 기입(텍스트) 또는 카메라로 이미지를 찍거나 비추었을 때, 그에 해당하는 음식의 정보를 출력

    + 주기능2 : 오늘 뭐 먹지? 를 입력했을 때 랜덤으로 음식추천

* 부가 기능1 : 주식 / 디저트 / 음료 카테고리 생성

  + 부가 기능2 : 오늘 먹은 음식에 대한 총 칼로리 계산 및 탄단지 비율 계산

    + 부가 기능3 : 하루 남성 여성 기초 대사량 또는 평균 섭취 칼로리를 넘어가면 경고 표시 or 사이렌으로 그만 먹으라고 말하는 기능 추가

       + 부가 기능4 : 만약 경고를 무시하고 계속 섭취할 경우 칼로리 소비를 위한 건강관리 프로그램 생성 추가
<br>

## 팀원 구성 및 역할 분담
### 🍊김보람

- **UI**
    - 페이지 : 홈, 검색, 게시글 작성, 게시글 수정, 게시글 상세, 채팅방
    - 공통 컴포넌트 : 게시글 템플릿, 버튼
- **기능**
    - 유저 검색, 게시글 등록 및 수정, 게시글 상세 확인, 댓글 등록, 팔로워 게시글 불러오기, 좋아요 기능

<br>
    
### 👻김용제

- **UI**
    - 페이지 : 프로필 설정, 프로필 수정, 팔로잉&팔로워 리스트, 상품 등록, 상품 수정, 채팅 목록, 404 페이지
    - 공통 컴포넌트 : 탭메뉴, InputBox, Alert 모달, 댓글
- **기능**
    - 프로필 설정 및 수정 페이지 유저 아이디 유효성 및 중복 검사, 상품 등록 및 수정

<br>

### 😎이경준

- **UI**
    - 페이지 : splash 페이지, sns 로그인 페이지, 로그인, 회원가입
    - 공통 컴포넌트 : 상품 카드, 사용자 배너
- **기능**
    - splash 페이지, sns로그인 페이지, 로그인 유효성 및 중복 검사, 회원가입 유효성 및 중복 검사, 이메일 검증, 프로필 설정, 접근제한 설정

<br>

### 🐬천호진

- **UI**
    - 페이지 : 사용자 프로필 페이지
    - 공통 컴포넌트 : 탑배너, 하단 모달창
- **기능**
    - 팔로우 & 언팔로우, 로그아웃, 하단 모달창, 댓글 삭제, 게시글 삭제, 상품 삭제, 사용자 게시글 앨범형 이미지, 탑 배너 뒤로가기 버튼, Alert 모달
    
<br>

## 개발 환경
* OpenCV
* otx
* CVAT
* Python
* Webcam
* GUI Framework


## Project Schedule


## Gantt Chart
![gantt chart](https://github.com/brkim92/Team_project/assets/154492346/cf77d33b-c21b-49b4-8bdb-745b406d9770)

<br>

## Sequence Diagram
![Sequence Diagram](https://github.com/brkim92/Team_project/assets/154492346/0124c87c-f0b8-4458-8b54-f5b6f18d0193)
<br>

## Module Diagram
![Module Diagram](https://github.com/brkim92/Team_project/assets/154492346/80306fa4-97f7-4919-bf8e-9475cc5099cf)

<br>

## High Level Design

![Screenshot from 2024-03-19 09-18-18](https://github.com/brkim92/Team_project/assets/154481519/ef8418bb-77fa-4ebc-87fa-1dcb5bcf880d)
<br>

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

![시연자료01](https://github.com/brkim92/Team_project/assets/154492346/f6b6b3bf-b2e6-4f8a-9c55-2ecf8b235f3d)
![시연자료02](https://github.com/brkim92/Team_project/assets/154492346/896e4009-3b6e-46ea-80d5-a35cdca22041)
![시연자료03](https://github.com/brkim92/Team_project/assets/154492346/5c9588a7-92ab-455b-9ed0-13550a41c194)
![시연자료04](https://github.com/brkim92/Team_project/assets/154492346/e45edfe7-e5d2-43b4-9496-eec2a4feb3e7)
* (프로젝트 실행 화면 캡쳐)

![./result.jpg](./result.jpg)

## Appendix

* (참고 자료 및 알아두어야할 사항들 기술)
