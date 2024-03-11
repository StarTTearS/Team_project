import torch
import torchvision
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.transforms import functional as F
from PIL import Image, ImageDraw, ImageFont

# 사전 학습된 Faster R-CNN 모델 불러오기
model = fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

# 객체 감지 및 정보 표시 함수 정의


def detect_and_display(image_path):
    # 이미지 불러오기
    image = Image.open(image_path).convert("RGB")
    # 모델 예측
    with torch.no_grad():
        prediction = model([F.to_tensor(image)])
    # 이미지에 박스 및 정보 표시
    draw = ImageDraw.Draw(image)
    font_size = 24  # 원하는 글꼴 크기로 설정
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # 사용할 폰트 경로
    font = ImageFont.truetype(font_path, size=font_size)
    for score, label, box in zip(prediction[0]["scores"], prediction[0]["labels"], prediction[0]["boxes"]):
        if score > 0.7:  # 임계값 설정 가능
            # 박스 그리기
            draw.rectangle([(box[0], box[1]), (box[2], box[3])],
                           outline="red", width=3)
            # 정보 표시
            label_text = f"Class: {label.item()}, Score: {score.item():.2f}"
            draw.text((box[0], box[1]), label_text, fill="red", font=font)
    # 이미지 출력
    image.show()


# 치킨이 감지된 이미지 경로 설정
image_path = "/home/kyj/Final_Project/Team_project/Food/FastFood/chicken/chicken1.jpg"

# 함수 호출
detect_and_display(image_path)
