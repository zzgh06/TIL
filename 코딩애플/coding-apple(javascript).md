# javascript

- 자바스크립트는 HTML 조작을 위해 사용합니다.

  `왜 조작을 하냐고요?`
    - 탭, 모달 등 웹페이지 UI 만들 수 있음
    - 유저가 입력한 데이터를 검사할 수도 있음
    - 유저가 버튼누르면 서버로 데이터 요청할 수도 있음 
    - 이런 기능들을 개발할 수 있습니다. 

- html 조작, 변경하려면
```html
<h1 id="hello">안녕하세요</h1>

<script>
  document.getElementById('hello').innerHTML = '안녕';
</script> 
```
- document -> 문서인데 여기선 html 웹문서겠죠
- 마침표 -> ~의 
- getElementById('어쩌구') -> 아이디가 '어쩌구'인 html 요소 (일명 element) 를 찾으셈 
- innerHTML -> 딱봐도 그냥 내부 HTML이라는 뜻인듯 
- = -> 등호는 프로그래밍에서 오른쪽에 있는걸 왼쪽에 대입하라는 뜻입니다. 
- '바보' -> 바보라는 문자 (큰따옴표, 작은따옴표안에 담겨있으면 항상 문자입니다.)

```html
<script>
  document.getElementById('???').??? = '???'; 
</script> 
```
- 여기 물음표만 맘대로 바꿔주면 html의 모든걸 변경하고 조작할 수 있습니다. 

```html
<script>
  document.getElementById('???').src = 'profile.jpg'; 
</script> 
```
- 이러면 원하는 요소에 src="profile.jpg"를 추가할 수 있고

```html
<script>
  document.getElementById('???').style.color = 'red';
</script> 
```
- 이러면 원하는 요소에 style="color : red"를 추가할 수 있고
- 아무튼 그렇습니다 수백가지 바꿀 수 있습니다

(참고)
- .getElementById()는 셀렉터라고 부릅니다. html 요소를 찾기 위해 사용합니다.
- .innerHTML / .style / .color 이렇게 점찍는데 괄호없는건 메소드(또는 함수) 라고 부릅니다.
- html 요소의 어떤 속성을 변경할지 결정하기 위해 사용합니다.

## 기본적인 UI 만드는 법칙

1. HTML CSS 로 미리 UI 디자인을 해놓고 필요하면 평소엔 숨김
2. 버튼을 누르거나할 경우 UI를 보여달라고 자바스크립트 코드짬