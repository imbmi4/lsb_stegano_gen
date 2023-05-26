# lsb_stegano_gen

## 반갑습니다 ㅋㅋ
그.. LSB 스테가노그래피 탐지하는 건 많아도 만드는건 없길래 만들어봤습니다.

사실 저만 쓰려고 이전 컴퓨터 화면 기준으로만 프로그램을 짜서 크기 같은 건 깨지지만 기능들은 잘 작동하네요. ㅎㅅㅎ
혹시나 이걸 보시는 분들은 그래도 LSB 스테가노그래피가 뭔지 아실 분들 같으니 설명은 생략하겠습니다.

일단 필요한 라이브러리 : 
PyQt5, pillow, requests, beautifulsoup5
입니다.

뒤에 두 개는 심심해서 그냥 보안뉴스 크롤링해오는 거 해놔서 필요한거에용. LSB 스테가노하고는 거리가 좀 멀어서 죄송하네용..

어쨌든 대충 사용법입니다.

<img width="348" alt="image" src="https://github.com/imbmi4/lsb_stegano_gen/assets/92718171/225a09da-34cf-4ccc-808e-556663b28d91">

이게 메인 화면인데 Detect는 인터넷에 흔한 탐지기고

<img width="335" alt="image" src="https://github.com/imbmi4/lsb_stegano_gen/assets/92718171/c26f2277-2a53-49d9-bd57-7c41032bcd53">

왼쪽 밑에 버튼 누르셔서 사진 가져온다음 화살표 누르시면 넘어갑니다.(다른것들이랑 비슷해요)

<img width="471" alt="image" src="https://github.com/imbmi4/lsb_stegano_gen/assets/92718171/08aa4f1e-fd97-41dd-a09c-5ecad666b0c2"> 

두 번째로 이게 젤 중요한 만들기입니다.
왼쪽에 있는 Load Hidden Image로 숨겨질 사진 가져오시고 오른쪽에 있는 Load Covering Image로 이걸 덮을 사진을 가져옵니다.
당연히 오른쪽 사진(덮을 사진)의 크기가 왼쪽 사진(숨겨질 사진)보다 커야합니다. (하나라도 작으면 생성 안되게 해놨습니다.)
그리고 중간에 어느 RGB의 몇 번째 비트에 숨길지 정하고 화살표를 클릭하면 result.png가 생성이 됩니답.


### 사용 제약
1. 덮을 사진과 숨겨질 사진 모두 bmp 파일이어야 합니다.
2. LSB 스테가노 특성상 숨겨질 사진은 무조건 검은색, 흰색으로만 이루어진 사진이어야 합니다.

### 사용 예시

<img width="492" alt="image" src="https://github.com/imbmi4/lsb_stegano_gen/assets/92718171/1a2caaff-9a97-4918-86e8-7193f354d7f6">

왼쪽 사진을 오른쪽 사진의 Red plnae 0에 맞추고 화살표를 누르면

<img width="488" alt="image" src="https://github.com/imbmi4/lsb_stegano_gen/assets/92718171/624ae10a-f11d-4f1b-af08-82644b80095f">

밑에 complete result.png에 결과 저장됨이라는 문구가 뜹니다.

됐는지 확인하기 위해 Detect 메뉴로 가서 로딩해보면

<img width="332" alt="image" src="https://github.com/imbmi4/lsb_stegano_gen/assets/92718171/b439d22c-f44b-4e8c-9f90-5a09683b8195">

옹.. 잘 숨겨진걸 확인할 수 있습니다.

## 추후 개선사항
1. 이전 컴 디스플레이 기준이라 UI가 다 깨지네요 나중에 반응형으로 바꿔놓겠습니답!
2. 너무너무너무너무너무너무 느립니다. 나중에 쓰레딩을 사용해서 이미지를 미리 다 따놓든 하겠습니다.
