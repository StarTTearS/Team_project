# Data Preparation
* CVAT을 이용한 Data labeling 작업(360장의 images)
* Export dataset(coco 1.0)

<br>

# Train / Optimization / Deployment(1)
* OTX를 이용한 Dataset Train, Optimization, Deployment
```
   model 선택
  
   - YOLOX-TINY
     - 목적: 리소스가 제한된 환경(예: 모바일 장치, 엣지 컴퓨팅)에서 빠르고 경량의 객체 탐지를 위해 설계됨.
     - 특징: 비교적 낮은 연산 복잡도와 파라미터 수를 가짐. 실시간 성능을 위해 최적화됨.
     - 사용 사례: 실시간 애플리케이션, 모바일 장치, 빠른 처리 속도가 필요한 시나리오.
  
   - YOLOX-L (Large)
     - 목적: 높은 정확도를 요구하는 애플리케이션에서 사용하기 위해 설계됨.
     - 특징: 더 깊고 넓은 네트워크 구조를 가짐. 더 많은 연산 복잡도와 파라미터를 사용하여 정확도를 높임.
     - 사용 사례: 정확도가 중요한 서버 기반 애플리케이션, 고화질 비디오 분석, 안전 모니터링 시스템.
  
   - YOLOX-X (Extra Large)
     - 목적: 최대한의 정확도를 달성하기 위해 설계됨. 연구 목적이나 매우 높은 정확도를 요구하는 특수한 경우에 사용됨.
     - 특징: YOLOX 시리즈 중 가장 큰 모델로, 가장 많은 연산 복잡도와 파라미터를 가짐. 이는 또한 가장 높은 정확도를 제공하지만, 연산 비용 또한 가장 높음.
     - 사용 사례: 고성능 컴퓨팅 환경에서의 연구 및 개발, 고해상도 이미지나 비디오에서의 객체 탐지, 정밀 의료 영상 분석 등.
```
* dataset 수정과 retrain


 > -> 결과
 >
 > 1. YOLOX-X 와 YOLOX-L 는 성능은 좋으나 무거워서 지연 시간이 생김 (약 1.5 sec)
 > 2. YOLOX-TINY는 가볍지만 성능이 기대에 미치지 못함 (동그랗고 모여있으면 pizza로 인식, sweet and sour pork와 chicken을 잘 구별하지 못함, 붉은 계열의 음식들을 여러 label로 잡음)

<br>

# docker 설치한 후 CVAT으로 image 파일 추가 후 다시 labeling
* docker install  (https://opencv.github.io/cvat/docs/administration/basics/installation/)
* data add(search & save)
```   
  Add label name : 불고기, 삼겹살, 칼국수, 핫도그, 족발, 초밥, 카레, 삶은 고구마, 생선구이, 딸기, 바나나, 사과, 포도
```
* CVAT을 이용한 Data labeling 작업(1681장의 images)
* Export dataset(coco 1.0)

<br>

# Train / Optimization / Deployment(2)
* OTX를 이용한 Dataset Train, Optimization, Deployment

> -> 결과
 >
 > 1. YOLOX-TINY와 YOLOX-X의 AP가 너무 낮음
 > 2. Delay 약 5 sec

<br>

# labeling 보완

- rotate rectangle → rectangle로 고침(COCO 데이터셋에서 사용되는 객체 감지 모델은 회전한 직사각형 형태의 객체에 대한 라벨링을 지원하지 않음. COCO 데이터셋은 주로 사각형 형태의 바운딩 박스로 객체를 라벨링함)
- 불필요한  labeling 제거(경량화 작업)

<br>

# YOLOX-TINY로 train

- batch size 8 → 4로 변경해서 train 해봄(돌아가지만 accuracy가 좋지 않음)
- 다시 batch size 8로 변경

<br>

# 서버 cpu로 train 중→gpu로 train 해야함(train하기에 너무 무거움)
 > nvidia-smi
 > - Failed to initialize NVML: Driver/library version mismatch
 > NVML library version: 535.161

- 교수님 서버 : error로 인해 못해봄

- 다른 팀 서버 : gpu

  ![Screenshot from 2024-03-20 12-50-27](https://github.com/brkim92/Team_project/assets/154481519/139e8e4e-2e00-4479-a5f3-cd2dceb96d6b)


- 우리 팀 서버: cpu

  ![Screenshot from 2024-03-20 12-50-37](https://github.com/brkim92/Team_project/assets/154481519/da338715-178c-41f1-b426-b8ba82bd8989)


<br>

# New dataset
* train → export → optimize → deploy
* model: YOLOX-TINY
* 다른 조 서버(gpu)에서 training한 demo.py를 test함
 > -> 결과
 > 1. 육안상 보이는 delay는 거의 없음
 > 2. 인식은 첫 dataset보다 좋지는 않으나 사용은 가능한 수준(카메라를 image 가까이 가져가면 인식이 잘 되는 것으로 추정)

<br>

# hpo_config.yaml
```yaml
range:       # 학습률 값의 범위
- 2.0e-04   # 최소값(5 -> 4)
- 0.02        # 최대값(0.002 -> 0.02)
- 1.0e-04   # 증가값 (5 -> 4)
```
- mAP 0.640까지 도달
    - **gts**: 각 클래스에 대한 실제 객체의 수
    - **dets**: 모델이 검출한 객체의 수
    - **recall(재현율)**: 실제로 존재하는 객체 중에서 모델이 정확하게 검출한 객체의 비율
    - **ap(평균 정밀도)**: 모델이 검출한 객체의 정확도. 모델이 얼마나 정확하게 객체를 검출했는지를 나타내는 지표
                
        ![Screenshot from 2024-03-20 12-50-48](https://github.com/brkim92/Team_project/assets/154481519/d7501415-4279-4171-ab3e-1bb9cf56bf2e)

        > 김밥: 썰지 않은 줄로 된 김밥은 인식률 낮음      
        > 닭가슴살: 기본적인 흰 닭가슴살은 잘 인식하지만 색이 있는 유형은 치킨 또는 다른 라벨로 잡음        
        > 불고기: 야채가 많은 이미지는 샐러드로 잡음        
        > 칼국수: 붉은 색의 칼국수는 짬뽕으로 잡고, 간혹 파가 많이 올려있는 유형은 샐러드로 잡음        
        > 스시: 모듬 스시는 거의 잡지 못함        
        > 고구마: 달걀로 잡거나 불고기로 잡거나 누가 봐도 고구마 말고는 절대 고구마로 인식하지 않음

<br>

# model change
* YOLOX-L로 model을 바꾸고 train
* YOLOX-X로 model을 바꾸고 train
