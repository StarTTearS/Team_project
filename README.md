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
* 첫번째 결정장애자가 있다.
두번째 다이어트 및 운동에 관심이 있는 20~30대 일반인이 있다.


결정장애자가 식사를 무엇으로 할지 고민한다. 
'오늘 뭐 먹지?'에서 성별을 선택한다.
성별 선택을 기준으로 기초 대사량 계산한 뒤 적절한 식단인지 아닌지 판별하는 기준으로 삼는다. 
랜덤으로 음식을 추천하는 버튼을 누른다.
오늘의 음식 추천 기능/아침,점심,저녁 추천 기능을 제공하며 결정장애자의 결정을 도와준다. 만약 기초대사량이 넘는 식단이 나오면 경고 알람이 나오고 적절한 식단이 나오면 좋다는 알람이 나온다.
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
시나리오 작성
```
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
