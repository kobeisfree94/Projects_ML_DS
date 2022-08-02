# COVID19 CT Image Classification

**Background**

2022년 4월 까지 대한민국 국민에 5명 중 1명은 코로나 확진 판정을 받은 적이 있습니다. 하지만 백신 접종률이 높아지면서 정부는 거리두기 정책을 완화하고, 실외에서는 마스크 안써도 되는 방안을 내놓으며, 
PCR검사도 자가긴단키트에서 양성 판정을 받은 사람들에게만 적용하는듯, 본격적으로 위드코로나 시대를 시작함을 알렸습니다. 이전에는 코로나 양성/음성 판정을 위해 PCR이라는 유전자 검사를 거의 모든 시민들에게 
공짜로 검사를 지급했다면 코로나가 팬대믹에서 엔대믹으로 넘어가면서 값비싼 PCR검사 가격을 국민에게 돌리고 있습니다. 

위드코로나 시대가 열리며 새로운 확진자 수가 줄었지만 이 시대에 새로운 문제 중 하나는 코로나 휴유증입니다. 실제로 어떤 BBC 기사에서는 코로나에 감염됬던 대략 80%에 사람들이 호흡곤란, 무기력증, 통증 등 후유증을 
겪었다고 보고했습니다. 미래에 PCR 유전자 검사를 딥러닝을 활요해 진단 할 수 있다면 진단 가격이 내려가며 긍정적인 효과를 보일 수도 있지만 어쩌면 위드코로나, 혹은 롱코비드 시대에 더 필요한 진단은 코로나가
신체에 끼친 데미지를 분석하고 후유증을 완화 할 수 있는 CT 나 X-Ray가 되지 않을까 예상 합니다.

그런 측면에서 Chest CT 사진을 딥러닝을 활용해 코로나 양성/음성 분류/진단을 하는 모델을 개발 하게 됐습니다. 


**1. Project Objective**
- Classify app. 1400 chest CT images using various ResNet models to determing COVID19 positivity
___
**2. Project Process**
- Load Data --> Data Preprocessing -—> ResNet —> Evaluate/Compare
___
**3. Data & EDA**
- Kaggle
- 1400 Chest CT images
- 1300 positive
- 100 negative
- Shape Resized to (224,224)
- Labels = 'inferred;
___
**4. Model**
- ResNet50, ResNet50V2, ResNet101, ResNet101V2, ResNet152, ResNet152V2
- ResNet Models already have the weights from ImageNet which gave high performances when performing CV problems with clear contrasts. 

**5. Conclusions**

![Screen Shot 2022-08-02 at 15 36 31](https://user-images.githubusercontent.com/60637777/182308125-19562d06-1933-4ffd-a4fd-ed7259bbc36d.png)

![Screen Shot 2022-08-02 at 15 35 50](https://user-images.githubusercontent.com/60637777/182308005-6f4f8f7e-e258-45b7-b48f-6a7719d0ed27.png)

![Screen Shot 2022-08-02 at 15 35 24](https://user-images.githubusercontent.com/60637777/182307923-8cb21ca7-d11a-4024-be64-bf1d6d7c521d.png)

![Screen Shot 2022-08-02 at 15 34 54](https://user-images.githubusercontent.com/60637777/182307850-bbcaa343-d428-4bdc-93c0-0f75e41e0523.png)

![Screen Shot 2022-08-02 at 15 34 27](https://user-images.githubusercontent.com/60637777/182307788-a9700519-5503-4138-93c8-80aa651792d1.png)

![Screen Shot 2022-08-02 at 15 33 43](https://user-images.githubusercontent.com/60637777/182307679-286e0b40-be47-40d7-beac-d0f12804c71d.png)

*- ResNet101V2 gave the best performance/accuracy with 98.84*


![Screen Shot 2022-08-02 at 15 33 16](https://user-images.githubusercontent.com/60637777/182307602-1ae340ef-a2ba-43ea-8518-5b511cd3654e.png)

6. Reflections
- 전체적으로 모든 모델들이 높은 성능을 보였다. ResNet을 사용한 이유도 위에 잠시 얘기했듯이 ImageNet이라는 pre-trained weight들이 있기 때문에 lines, shapes, color 등을 활요해 분류 하는데 좋은 성능을 보여서 이다. 
- 그 외에 이유에는 아무래도 양성 이미지와 음성 이미지에 큰 차이가 있는 부분이 분류를 더 쉽게 만들었지 않나 싶다. 
- 또 한 가지 변수는 음성 이미지가 양성에 비해 현저히 적었어서 class imbalance가 있었다. 이는 up-sizing으로 부족한 class에 이미지를 다시 학습 시키며 극복했다. 
- 원래는 바운딩 박스를 활용해서 좀 더 디테일한 라벨링을 활용해 분류를 진행해 보고 싶었다. 추후 계획은 좀 더 디테일한 부분을 라벨링 및 분석으로 CT이미지를 보고도 양성/음성 진단 이 외에 폐에 어떤 손상이 있는지 분석하는 모델로 만들고 싶다.
- 하지만 아무래도 라벨링에 의료 전문가에 소견이 필요하기에 쉽게 얻을 수 있는 데이터는 아닌거 같다. 
