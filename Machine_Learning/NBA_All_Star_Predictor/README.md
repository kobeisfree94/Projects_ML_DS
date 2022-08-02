# NBA All-Star Predictor
___

**Background:**

미국에서 Fantasy Sport 시장은 2025년 까지 대략 $6.1 billion 더 성장 할 것 이라고 예측하고 있다. 예전에도 인기가 있었지만 비대면시대에 더 각광을 받는 시장이다. 
Fantasy Sport에 주요 메커니즘은 통계에 기반한 미래 예측이다. 선수들을 고르고 그 선수들의 실제 퍼포먼스에 따라 점수를 얻고 같은 리그에 있는 경쟁자들 보다 더 높은 랭킹을 얻는것이 목표이다. 

NBA에서 All-Star가 됬다는것은 선수 개인에게 가장 큰 영광 중 하나이다. 그리고 NBA All-Star Games 역시 시즌중 파이널 이외에 가장 큰 이벤트 중 하나이다. 
NBA All-Star Roster를 예측하는 패널과 쇼도 따로 있을 정도로 NBA에 홍보와 선수들의 커리어에 큰 비중을 차지하는 이벤트이다. 

그런 측면에서 MVP나 All-Star를 예측하는것은 팬들에게 큰 흥미를 가져다 줄 수 있을 뿐더러 스포츠 베팅 업체들이나 Fantasy Sports시장이 크게 관심을 가질만한 아이템이라고 생각한다. 
___

**1. Project Objective**
- To predict the NBA All-Star Roster of 24 players for the 2021-2022 season using player statistics from 1996-2021.
___

**2. Project Process**
- Data --> Data Preprocessing --> Random Forest Classifier --> Prediction/Evaluation
___

**3. Data & EDA**
- Database of player stats from 1996- 2021 constructed using SQLite (source: Basketball-Reference.com)
- Filled in Missing Values with 0
- Converted to appropriate data types for convenience
- Concatenated additional information (ex. all_star_2020 list)
- Feature Engineering
  - True Shooting Percengatge (TS%) = (Points/ (2*(Field Goals Attempted+0.44*Free Throws Attempted)))
___

**4. Model**
- Train = 1996-2020
- Test = 2021
- Features = ['PTS', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'TS%', '3PM']
- Target = ["Selected?"]
- Model = Random Forest Classifier
- Train Accuracy = 1.0
- Val Accuracy = 95.7
___

**5. Conclusions**
- 머신러닝 모델을 활용하여 25명의 2021-2022 NBA All-Star 로스터를 예측

![Screen Shot 2022-08-01 at 18 36 32](https://user-images.githubusercontent.com/60637777/182119827-e838be88-1ffa-4214-9fd5-7e68f0080900.png)

- 예측한 결과를 Pickle하여 Flask와 Heroku를 활용하여 API 애플리케이션으로 배포. 
___

*Update* 
- 위 프로젝트를 진행했을때 당시에는 NBA All-Star전이 진행되기 이전이 었기에 실제 리스트와 비교분석을 진행하지 못 했었지만 2022년 2월 21일 진행했던 실제 게임 로스터와 위 예측 모델의 성과를 비교했을때 결과는 아래와 같다. 

![Screen Shot 2022-08-01 at 19 15 48](https://user-images.githubusercontent.com/60637777/182127111-60cfcd1d-4a73-49ae-adb3-5437c48517c0.png)

- 예측 로스터와 실제 로스터의 일치도 = 74.07% 
___

**6. Reflections**
- 아래는 분석을 하면서 겪었던 변수들, 그리고 추후에 발전 할 수 있는 부분들을 정리했습니다. 

1. 팬투표/인기
- 실제 NBA All-Star 로스터는 전문가 50%, 팬 투표 50%를 기반으로 로스터가 결정 되기 때문에 통계를 기반한 quantitative 분석으로 만은 부족한 일치성을 보인다.
- 예를 들어 Draymond Green 같은 스타성은 높지만 평균 스탯은 좋지 않은 선수들, 혹은 Kobe Bryant나 Dirk Nowitzki 같이 NBA 레전드들은 은퇴 시즌에 스탯이 안 좋아도 발탁 되는 경우가 많다. 
- 추후에 Twitter나 팬 사이트 댓글을 가져와서 Sentiment Analysis를 통해 각 선수들의 인기 점수를 적용해서 예측 시스템에 넣으면 보다 높음 예측력을 보일거라고 예상해본다. 

2. 부상 
- All-Star에 이전에 출전 했었고 스타성이 있는 선수라도 부상을 당하면 실제 경기에 뛰지 못한다. 
- 단 부상은 단기와 장기부상 케이스로 나뉜다. 장기부상에 예를 들어 위 해에는 Paul George나 Klay Thompson이라는 스타선수들이 장기 부상을 당했기에 로스터 발탁이 불발됐다. 
- 하지만 Kevin Durant나 Draymond Green같은 케이스에서는 단기부상을 당했었기에 로스터에 발탁이 된 케이스다. 이런 상황에서는 사무국이 대채 선수를 발탁하기 때문에 팬 투표는 무의미 해지고 보통 그해에 라이징 스타, 혹은 핫한 신인을 (ex. LaMelo Ball) 발탁하는 경우가 많다. 
- 이와 같이 다양한 부상 케이스로 매해 마다 NBA All-Star 로스터에 포함되는 선수들의 수는 24-27명 사이로 나온다.
- 이 중에서 실제로 경기를 뛰는 선수들은 24명이지만 발탁 된것 자체가 영광이고 기록이기 때문에 이런 예외 케이스들이 발생된다. 
- 물론 부상을 예측할수는 없지만 NBA나 ESPN 처럼 매일 선수 상황을 업데이트 해주는 웹사이트에서 web scraping을 해온다면 부상이 얼마나 오래 지속됐는지에 따라 특정 선수를 예외처리 할 수 있지 않을까라는 생각이 든다.

3. Advanced Statistics
- 어떤 특정 선수들은 통계로 설명 안되는 선수들이 있다. 
- Draymond Green을 예를 들자면 점수, 리바운드, 스틸 들이 다 한자리 수일때가 많지만 도움 수비, 패싱 능력, BQ, 스크린 능력, 사기증가 등 다양한 방면에서 팀에게 플러스가 되는 선수들이 있다. 
- 반면 어떤 선수들은 득점은 많이 하지만 실수가 많고 팀에게 도움이 되기 보다는 자기 혼자만에 플레이로 승리를 놓치는 케이스들도 있다. 
- 전문가들은 이런 지표들까지 분석을 해서 Advanced Statistics라고 팀 기여도, 효율 등 분석할수 있는 지표들과 포뮬라를 만들어 놓았다. 추후에는 이런 Advancec Statistics도 포함해서 예측을 하면 더 높은 성능을 보일 수 있을거라고 생각한다. 

4. Flask/Heroku
- 처음으로 Flask을 사용해서 Web Application을 만들어 봤기에 보다 심플한 면이 있지만 일단 배포를 성공한것에 큰 의미를 두고 있다. 
- 추후에는 html/css파일은 더 업그레이드 시켜서 All-Star 뿐만 아니라 MVP까지 예측하는 모델을 만들어 서비스로 출시 해보고 싶다. 
