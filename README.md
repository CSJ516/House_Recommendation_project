# House Recommendation project :house_with_garden:


본 프로젝트에서는 2030 세대를 위해 서울시 전월세 부동산을 추천해주는 웹 사이트를 구현했습니다.

jupyter notebook, QGIS, PostgreSQL, Django 등의 프로그램을 사용하였으며, 진행 순서는 다음과 같습니다.


### 1. 데이터 수집
- 국토교통부 실거래가 공개시스템에서 5년치 부동산 실거래가 데이터 수집
- 공공 데이터 포털에서 각종 편의시설 데이터 수집
- 서울 열린 데이터 광장에서 편의시설 및 지하철역 데이터 수집
- 카카오 API 로 위도, 경도 데이터 수집
- BeautifulSoup 로 네이버 부동산 매물 데이터 수집

### 2. 데이터 저장
- QGIS 로 공간 정보 데이터 가시화
- PostgreSQL 에 데이터 저장
#### :star2: 데이터를 연동하는 자세한 방법은 https://blog.naver.com/dalgoon02121/222233313663 참고 :star2:

### 3. Django 로 웹 사이트 구현
- 사용자가 부동산 유형, 전/월세, 예산, 직장주소, 편의시설 조건 선택
- SQL 구문으로 조건에 따른 부동산 매물별 점수 계산
- 점수가 높은 부동산 및 주변 편의시설, 관련 네이버 매물을 지도상으로 표시

<img width="720" alt="바로방" src="https://user-images.githubusercontent.com/60870945/131973301-8c2c31e8-71e0-47a7-80cd-0246db704556.png">
