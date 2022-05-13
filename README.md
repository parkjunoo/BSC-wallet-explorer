## 팀 이름
---

- 팀명 : 제네시스 BNB
- Github Repository : [https://github.com/codestates/BTC2nd-06](https://github.com/codestates/BTC2nd-06)
- 팀원 :
    - 안재윤
    - 박준수
    - 박준하
- 개발 프로젝트
    - Genesis BNB 지갑

## 깃 레포

---

[https://github.com/codestates/BTC2nd-06](https://github.com/codestates/BTC2nd-06)

# 1. 선정 코인 소개

## 개요

바이낸스 스마트 체인(BSC)는 바이낸스 체인과 병렬로 실행되는 블록체인입니다. 스마트 콘트랙트 기능 및 이더리움 가상 머신(EVM)과 호환이 되고 높은 처리량을 유지하며 BNB 통화를 기반으로 두고 있는 바이낸스 체인의 단점을 보완합니다. 기존의 바이낸스 체인은 프로그래밍 관점에서 다른 블록체인보다 유연하지 못하다는 단점을 가지고 있었지만 바이낸스 스마트 체인의 등장으로 고성능 탈중앙 애플리케이션을 개발할수 있게 되었습니다. 바이낸스 스마트 체인은 바이낸스 체인과 크로스체인 호환을 위해 구축 되었으며, 사용자는 두 블록체인 모두에서 혜택을 누릴 수 있습니다. 

## 특징

### 합의

바이낸스 스마트 체인은 지분 권위 증명 또는 PoSA 합의 알고리즘을 통해 ~3초 블록 시간을 달성합니다. 참여자는 검증자가 되기 위해 BNB를 스테이킹할수 있고 유효 블록을 제시할 경우, 트랜잭션에 포함된 트랜잭션 수수료를 지급받습니다. 

### **크로스체인 호환**

듀얼 체인 구조를 사용하여 사용자는 바이낸스 블록체인 간에 자유롭게 자산을 전송할 수 있습니다. 바이낸스 체인상의 빠른 트레이딩 기능을 사용하는 동시에, 바이낸스 스마트 체인상에 강력 탈중앙 앱을 구축할 수 있습니다. 바이낸스 체인의 BEP-2와 BEP-8 토큰은 바이낸스 스마트 체인에서 도입된 새로운 표준인 BEP-20 토큰으로 스왑할 수 있습니다. 

익스플로러

![explorer.gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/94c4a625-9c0b-45b9-a218-9b97fa22ebc4/explorer.gif)

회원가입하기

![May-13-2022 18-48-01.gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c533034c-b6fc-4156-a048-5ae72810939c/May-13-2022_18-48-01.gif)

코인전송

![bnb.gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/990e7bfc-014c-4bf7-91c6-d5752f31e9c5/bnb.gif)

코인 거래기록

![May-13-2022 19-gggg.gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b017fe82-9804-4508-acbe-e3d8d6f27047/May-13-2022_19-gggg.gif)

# 2. 프로젝트 소개

## 개요

Genesis BNB 프로젝트는 바이낸스 스마트 체인 (BSC) 에서 서비스를 지원하는 합니다. 블록체인 지갑, 익스플롤러, 데몬 구현을 하여 플랫폼에 적용하고 네트워크에서 다양한 기능을 지원합니다. 

## 핵심 기능

### 지갑

- 중앙 서버 통제 없이 사용자가 지갑보유
- 지갑 및 계정 발급
- 계정 활동 내역 확인
- 코인 전송 및 잔액 확인
- 토큰 전송 및 잔액 확인

### 익스플로러

- 네트워크 상의 최신 블록을 기준으로 내용 표시
- 최신블록에 담긴 트랜잭션 내용 표시
- 블록번호 / 트렌잭션해시 값으로 검색 기능 구현

### 데몬

- BSC 네트워크의 최신 생성 블록의 트랜잭션을 실시간 스캔하여 지갑 앱에 등록된 계정과 관련된 트랜잭션을  DB에 저장

# 3. 프로젝트 상세

## 지갑 (Wallet)

### 1. 지갑 기능

Genesis BNB 지갑은 BSC 네트워크 지갑 관리를 지원합니다. 지갑은 니모닉 구문을 이용하여 생성되도록 설계되었습니다. 

1. 니모닉 구문 발급
    1. lightwallet library 을 이용하여 니모닉 구문 생성
2. 계정 생성
    1. HDWalletProvider를 이용하여 계정생성
3. 계정 불러오기
    1. web3.eth.getAccounts()를 호출하여 계정 확인

### 2. 코인 관리

1. 코인 전송
    1. web3.eth.sendTransaction()를 호출하여 코인 전송
2. 코인 잔액 확인
    1. web3.eth.getBalance(address)를 호출하여 잔액 확인
3. 적정 가스비 제안
    1. web3.eth.getGasPrice() 와 web3.eth.estimateGas()를 호출하여 gas limit 과 gas price 확인

### 3. 토큰 관리

1. 스마트 컨트랙트 배포
    1. solc library를 사용하여 compile 된 스마트 컨트랙트(SimpleToken.sol)를 바이낸스 스마트 블록체인(BSC) 네트워크에 배포
2. 토큰 전송
    1. contract method중 transfer method를 사용하여 토큰 전송
3. 토큰 잔액 확인
    1. contract method중 balanceOf method를 사용하여 토큰 잔액 확인

## 익스플로러 (Explorer)

BSC 테스트넷 네트워크 상의 가장 최신 Block을 기준으로 Block내 정보들과 Tx의 정보를 수집하여 가져옵니다. 

### 기능

- 최근 이어진 블록을 기준으로 7개의 리스트를 보여줍니다.
    - 블록 높이, 시간, 트랜잭션의 수 등 10종의 블록 정보들 표시
- 가장 최근에 생성된 블록이 담고 있는 Tx 표시
    - 트랜잭션 해쉬, 수신자, 발신자, value 등 6가지 Tx 정보들을 표시
- Block Number / Tx Hash 값을 기준으로 탐색 기능 제공

## 데몬 (Daemon)

### 기능

- systemd service 데몬으로 동작하는 Python 스크립트
- 일정 confirm depth를 만족하는 최신 생성 블록 안의 트랜잭션 목록을 조회하여 DB에 등록된 지갑 계정 주소와 관련이 있는 트랜잭션의 목록을 필터링
- 해당 트랜잭션 레코드를 DB에 생성 후 지갑 계정과 Foreign Key로 연결
- DB에 저장된 트랜잭션 레코드는 지갑 앱의 ‘계정 트랜잭션 조회' API를 통해 조회 가능

 

# 4. Lessons Learned

## 지갑 (Wallet)

- 코인 전송하는 API를 개발하는데 어려움이 있었습니다. 처음에 lightwallet library를 이용하여 니모닉 코드 생성후 hooked-web3-provider 사용하여 개발을 진행했었는데 library 자체가 프론트에서 사용되도록 설계되 있는 부분이 있어서 백엔드에서 사용하려면 모듈 수정이 필요했습니다. 시행착오 끝에 lightwallet library는 니모닉 코드만 생성하는 용도로 쓰고 HDWalletProvider를 provider로 써서 개발하였습니다.
- SimpleToken.sol contract를 solc로 compile 한 후 배포하는 과정에서 매번 abi 와 bytecode를 받아오는 시간이 생각보다 오래 걸렸습니다. 매번 compile 하는 대신 compile한 파일을 build 폴더에 저장해서 필요할 때 읽어오는 형식으로 바꿔서 진행하였습니다.
- Contract 배포후 method 호출시 abi가 잘못됐다는 에러가 계속 발생하였습니다. Contract는 배포된걸 확인할 수 있었고 에러를 디버깅하는데 시간이 많이 소요됐습니다. 알고 보니 contract instance 만들 때 contract address 대신에 account address를 이용하여 method를 호출해서 에러가 난 것을 확인하였습니다.

## 익스플로러 (Explorer)

- Web3js BN에 대한 이슈
    
    Web3 라이브러리를 사용하다 **Number can only safely store up to 53 bits** 애러를 발견하게 되었습니다. 해당이슈는 가스비에대한 BN가 JS에서 정수 값 최대 bit를 초과하여 발생하는 경우로 많은 시간을 잡아먹게 되었습니다. 해당 이슈를 추적한 결과 임시로 Web3js에 함수를 expend하여 해결한 것을 보고 해결 할 수 있었습니다.
    
- 블록체인 네트워크에 대한 성능적인 측면에서 생각보다 많이 느리다는걸 알 수 있었습니다. 프론트의 경우 비동기처리시 반드시 UI적인 처리가 필수임을 알 수 있었고 성능에대한 고민이 좀 더 필요했습니다.
- BSCscan에는 생각보다 쓸 수 있는게 별루 없다.
- Chrome Extenstion을 개발하는 방법을 배울 수 있었습니다.

## 데몬 (Daemon)

- BSC 체인은 새로운 블록이 생성되는 데 1~2초가 소요되어 블록 생성 속도가 비교적 빠릅니다. 그에 비해 테스트넷 web3 프로바이더를 이용하여 API 메서드 호출 시 간헐적으로 응답 리턴이 상당히 지연되는 현상이 있었습니다. (getBlock() 메서드 응답 리턴에 짧게는 0.1초부터 길게는 18초까지 소요) 이런 이유로 블록 생성 속도와 web3 통신 및 백엔드 로직(DB row 저장) 처리 속도의 균형을 맞추는 것이 어려웠습니다.
- 다행히 적은 컴퓨팅 파워의 EC2/RDS 서버로도 백엔드 로직 처리에서의 시간 지연이 거의 없었기에, web3 API 메서드의 리턴이 느린 경우 최신 블록을 실시간으로 검사하는 대신 데몬에서 마지막으로 처리한 블록 넘버를 추적하며 블록을 스캔한 결과 BSC Scan 페이지와 비교하였을 때 최신 블록의 트랜잭션을 아주 적은 시간 지연으로 스캔할 수 있었습니다.
- web3 프로바이더와의 통신 등 외부 통신 API에 의존하는 로직을 처리할 경우 응답 시간을 고려한 조치가 필요하다는 것을 배울 수 있었습니다.
- 또한, 무한루프의 형태로 동작하는 데몬이 의도치 않은 동작으로 멈추는 것을 방지하기 위해 web3 API 응답 결과에 따른 Exception 처리를 적절히 해주는 등의 고민을 해볼 수 있었습니다.
- DB에 저장된 지갑 계정의 수가 매우 많을 경우 데몬과 백엔드 로직의 실행을 분산 병렬 처리하고, 로드가 큰 작업, 외부 API 통신 등을 비동기 처리하는 방향으로 개선할 수 있을 것으로 기대합니다.
