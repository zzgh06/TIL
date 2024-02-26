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


## 자바스크립트 function 문법

- function (일명 함수) 라는 문법이 있는데, 함수는 길고 더러운 코드 한 단어로 축약하고 싶을 때 쓰는 문법입니다.
- 간지나는 개발자말로 표현하면 특정 기능을 다음에도 쓰기 위해 모듈화해놓는 문법 

```javascript
function 자유롭게작명(){
  축약하고 싶은 긴 코드
}
```
1. function 키워드 쓰고 소괄호, 중괄호 붙이면 됩니다.
2. 그리고 소괄호 왼쪽에 작명하고
3. 긴 코드를 중괄호 안에 담으면 코드 축약 끝입니다.

`Alert 여는 코드 function으로 축약해보기`

```html
<button onclick="알림창열기()">알림창 여는 버튼</button>

<script>
  function 알림창열기(){
    document.getElementById('alert').style.display = 'block';
  }
</script>
```

## function에 사용가능한 파라미터 문법 

```javascript
function 알림창열기(구멍){
  document.getElementById('alert').style.display = 구멍;
}
```

- 지금 함수 내에 구멍을 뚫었습니다.
- 구멍을 뚫는 법은
  1. () 소괄호 내에 아무 글자나 적고

  2. {} 중괄호 내에도 같은 글자 아무데나 적으면 됩니다. 

- 구멍을 왜 뚫냐고요?
-> 구멍을 뚫으면 함수를 업그레이드해서 사용할 수 있습니다. 

- 구멍이 뚫려있으면 이제 함수를 쓸 때 그냥 쓰는게 아니라, 소괄호 내에 뭔가 문자나 숫자등을 입력해서 사용가능합니다

```javascript
function 알림창열기(구멍){
  document.getElementById('alert').style.display = 구멍;
}

알림창열기('안녕');
알림창열기('바보');
```
▲ 업그레이드 된 함수를 사용할 때는

- 소괄호 구멍자리에 뭔가 내가 원하는 문자를 입력해줄 수 있습니다.
- 문자를 입력하면 아까 그 {} 중괄호 내부의 '구멍'자리에 문자가 쇼옥하고 들어가게 됩니다. 
- 그럼 알림창열기('안녕') 이렇게 실행하면
`document.getElementById('alert').style.display = '안녕';`
이런 코드가 실행된다는 것입니다. 

```javascript
function 알림창열기(구멍){
  document.getElementById('alert').style.display = 구멍;
}

알림창열기('none'); //이거 실행하면 알림창열릴듯
알림창열기('block');  //얘는 닫힐듯 
```

▲ 좀 더 실용적인 사용예시를 들고왔습니다.

- 알림창열기('block') 이렇게 실행하면
`document.getElementById('alert').style.display = 'block';` 이런 코드가 실행됩니다.
- 그럼 알림창이 열리겠군요 

- 알림창열기('none') 이렇게 실행하면
`document.getElementById('alert').style.display = 'none';` 이런 코드가 실행됩니다.
- 그럼 알림창이 닫히겠군요 


## getElementsByClassName 셀렉터

- 어떤 html 요소를 찾고 변경할 때 id로 찾았었는데, 실은 class 같은걸로도 찾을 수 있습니다. 

```html
<p class="title1"> 테스트1 </p>
<p class="title1"> 테스트2 </p>
```
- 이런 html요소가 있다고 칩시다.
- 얘를 셀렉터로 찾고 변경하고 싶으면 class명이 title1인걸 찾아라~ 라고 명령줄 수도 있습니다.

```html
<p class="title1"> 테스트1 </p>
<p class="title1"> 테스트2 </p>
<script>
  document.getElementsByClassName('title1')[0].innerHTML = '안녕';
</script>
```
- 이러면 첫 <p> 태그 내용이 안녕으로 바뀝니다.
- getElementsByClassName('클래스명')[순서] 이렇게 쓰면 됩니다.

- [0] 이렇게 순서를 넣는 이유는
- getElementsByClassName 셀렉터는 일치하는 class가 들어있는 모든 html 요소를 찾아주기 때문입니다.

- 그래서 그 중에 몇번째 요소를 바꿀지 [순서]를 꼭 뒤에 붙여줘야합니다.
- [0] 이렇게 쓰면 찾은 것 중 위에서 부터 1번째 요소
- [1] 이렇게 쓰면 찾은 것 중 위에서 부터 2번째 요소
- [2] 이렇게 쓰면 찾은 것 중 위에서 부터 3번째 요소


## 이벤트 리스너
- 지금까진 버튼의 onclick=" " 안에 자바스크립트를 길게 짰는데 이것도 좀 더러워보입니다.
- 그게 보기싫으면 이벤트리스너 문법 사용하면 됩니다.
- 그럼 html 안에 자바스크립트 안적고도 똑같이 개발진행할 수 있습니다. 

- 이벤트 리스너는 이렇게 사용합니다.
```javascript
document.getElementById('어쩌구').addEventListener('click', function(){
    //실행할 코드 
});
```
- 이렇게 작성하면 'id가 어쩌구인 요소를 클릭하면 안의 코드를 실행해주세요~' 라는 뜻입니다.
- 이거 쓰면 버튼 같은 곳에 onclick 넣을 필요가 없겠군요 ㄷㄷ

```html
<div class="alert-box" id="alert">
  <p id="title">알림창임</p>
  <button id="close"> 닫기 </button>
</div>
```

    Q. alert 박스 내부에 닫기버튼이 있습니다.
    이걸 누르면 alert 창이 닫히도록 하려면 어떻게 기능개발을 해야할까요? 
    onclick 말고 addEventListener를 써봅시다.

```javascript
document.getElementById('close').addEventListener('click', function(){
    document.getElementById('alert').style.display = 'none'
});
```

### 더 배워볼 개념 1. event

- 이벤트 리스너를 배웠는데 이벤트가 뭐냐고요?

- 유저가 웹페이지 접속해서 클릭, 스크롤, 키보드입력, 드래그 등을 할 수 있는데 이걸 전문용어로 이벤트라고 부릅니다.
- 어떤 요소 클릭시엔 click 이벤트
- 마우스갖다대면 mouseover 이벤트 
- 스크롤하면 scroll 이벤트
- 키입력하면 keydown 이벤트

- 그리고 이벤트가 일어나길 기다리는 친구가 이벤트 리스너입니다.
- 이벤트 리스너는 이벤트가 일어나면 내부 코드를 실행해주는 고마운 기본 문법입니다.  

`이벤트 종류는 수십가지가 있습니다.`
https://developer.mozilla.org/en-US/docs/Web/Events

▲ 이벤트 목록인데 이런거 미련하게 외우지 마시고 필요할 때 찾아쓰십시오.

### 더 배워볼 개념 2. 콜백함수
```javascript
셀렉터로찾은요소.addEventListener('scroll', function(){} );
```
- 이벤트 리스너 생김새를 잘 보면 함수같이 생겼습니다.
- 실은 뒤에 소괄호 붙으면 다 함수입니다.
- 근데 addEventListener() 함수에는 파라미터 자리에 2개의 자료를 집어넣죠?
- 맞습니다 자바스크립트 addEventListener 문법 만든 사람이 그렇게 쓰라고 해서 그렇게 쓸 뿐인데
- 둘째 파라미터로 함수가 들어가네요? 
- 저렇게 함수 파라미터자리에 들어가는 함수를 전문용어로 '콜백함수'라고 합니다.
- 콜백함수는 그냥 뭔가 순차적으로 실행하고 싶을 때 많이 보이는 함수형태며
- 그냥 함수안에 함수 넣으라고 하면 "아 저건 콜백함수구나~" 라는 반응만 보이면 됩니다.  
- 지금 코드짤 때는 우리가 콜백함수를 직접 작성하고 그럴 일은 없고
- 콜백함수 쓰라고 하는 자리가 있으면 잘 쓰기만 하면 됩니다. 


## classList 다루기

- 버튼누르면 등장하는 서브메뉴를 만들며
- 자바스크립트로 class 탈부착하는 문법을 배워봅시다.

```css
.list-group {
  display : none
}
.show {
  display : block
}
```
- css 파일 열어서 평소에 .list-group 붙은 요소는 숨겨놓도록 합시다. 
- 그리고 거기에 show라는 클래스를 부착하면 보여주는 식으로 개발해봅시다.
- 이제 버튼누르면 <ul class="list-group"> 에다가 show라는 클래스 부착하라고 코드짜면 서브메뉴 UI 완성임 
- 왜 이따구로 class를 부착해서 만드냐고요? 
- 나중에 display : block 말고 다른 스타일도 동시에 주고 싶을 경우 유용해서 그렇습니다.

### 버튼 클릭시 저기에 클래스명을 추가해주세요

- 버튼 눌렀을 때 show 라는 클래스를 저기에 추가해봅시다.
- class명을 원하는 요소에 추가하는 법은 
- 셀렉터로찾은요소.classList.add('클래스명') 이렇게 쓰면 됩니다.
- class명을 원하는 요소에서 제거하는 법은 
- 셀렉터로찾은요소.classList.remove('클래스명') 이렇게 쓰면 됩니다.
- 당연히 구글 검색해봐야 알지 생각해서 나오는 것들이 아닙니다. 

```javascript
document.getElementsByClassName('navbar-toggler')[0].addEventListener('click', function(){
  document.getElementsByClassName('list-group')[0].classList.add('show');
});
```
▲ 그래서 class="navbar-toggler" 가진 요소 클릭하면
class="list-group"인 요소에 show라는 클래스명 추가하라고 코드를 짰습니다.
이제 버튼누르면 서브메뉴가 잘 보이는군요. 

### 버튼 한 번 더 누르면 숨기기
- 버튼을 한 번 더 누르면 서브메뉴를 숨기고 싶은겁니다.
- 그럼 당연히 노예 컴퓨터에게 이렇게 명령내리면 됩니다.
- "버튼 한 번 더 누르면 show 클래스를 제거해주세요"
- 근데 이건 나중에 if문, 변수문법을 배우면 직접 만들어볼 수 있기 때문에
- 좀 쉬운 방법을 먼저 알려드리자면 

```javascript
document.getElementsByClassName('navbar-toggler')[0].addEventListener('click', function(){
  document.getElementsByClassName('list-group')[0].classList.toggle('show');
});
```
``.classList.toggle() 쓰면`
- 클래스명이 있으면 제거하고
- 클래스명이 없으면 붙여줍니다.
그래서 왔다갔다하는 UI 만들 때 유용하게 쓰면 되겠습니다.

### querySelector
getElementById()
getElementsByClassName()
이거 말고도 다른 방식으로 html 요소를 찾아주는 셀렉터도 있습니다.
`querySelector인데` 이거 쓰면 css 잘하는 분들은 편리하게 사용가능합니다. 

```html
<div class="test1">안녕하세요</div>
<div id="test2">안녕하세요</div>

<script>
  document.querySelector('.test1').innerHTML = '안녕';
  document.querySelector('#test2').innerHTML = '안녕';
</script>
```
- querySelector() 안에는 css 셀렉터 문법을 사용가능합니다.
- 다만 querySelector() 는 맨 위의 한개 요소만 선택해줍니다.

```html
<div class="test1">안녕하세요</div>
<div class="test1">안녕하세요</div>

<script>
  document.querySelectorAll('.test1')[1].innerHTML = '안녕';
</script>
```
▲ 그래서 위처럼 test1이라는 클래스가 중복으로 여러개 있는데
X번째 요소를 선택하고 싶은 경우엔 querySelectorAll() 쓰면 됩니다.
querySelectorAll() 은 해당하는걸 다 찾아서 [] 안에 담아줍니다.
그래서 [숫자] 를 뒤에 붙여서 원하는 위치에 있는 요소 찾아쓰면 됩니다.


## jQuery 사용법 간단정리
jQuery 설치는 구글에 jQuery cdn 이런거 검색하면 나오는 사이트가 있습니다.
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js" integrity="sha512-894YE6QWD5I59HgZOGReFYm4dnWc1Qt5NtvYSaNcOP+u1T9qYdvdihz0PPSiiqn/+/3e7Jo4EaG7TubfWGUrMQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
```
이제 jQuery 설치한 곳 `하단에서` jQuery 문법을 사용가능합니다.

### jQuery 써서 html 변경하려면
```html
<p class="hello">안녕</p>

<script>
  $('.hello').html('바보'); 
</script>
```
- 이렇게 코드 양이 절반으로 줄어들어서 쓰는 것일 뿐입니다. 
- $ 이건 querySelector와 동일하게 사용하면 됩니다. 

### jQuery 써서 스타일 변경하려면

```html
<p class="hello">안녕</p>

<script>
  $('.hello').css('color', 'red');
</script>
```
- 이러면 css 스타일 변경이 가능합니다. 
- (주의) html 셀렉터로 찾으면 html 함수들을 뒤에 붙여야하고
- jQuery 셀렉터로 찾으면 jQuery 함수들을 뒤에 붙여야 잘됩니다. 

### jQuery 써서 class 탈부착하려면 
```html
<p class="hello">안녕</p>

<script>
  $('.hello').addClass('클래스명');
  $('.hello').removeClass('클래스명');
  $('.hello').toggleClass('클래스명');
</script>
```

### html 여러개를 바꾸려면
```html
<p class="hello">안녕</p>
<p class="hello">안녕</p>
<p class="hello">안녕</p>

<script>
  document.querySelectorAll('.hello')[0].innerHTML = '바보';
  document.querySelectorAll('.hello')[1].innerHTML = '바보';
  document.querySelectorAll('.hello')[2].innerHTML = '바보';
</script>
```
- <p> 태그 3개 내용을 일괄적으로 '바보'로 바꾸려면
- 그냥 자바스크립트는 저렇게 3줄 쓰면 됩니다.

```html
<p class="hello">안녕</p>
<p class="hello">안녕</p>
<p class="hello">안녕</p>

<script>
  $('.hello').html('바보');
</script>
```
- 그런데 $() 셀렉터는 그냥 querySelectorAll처럼 여러개가 있으면 전부 찾아줍니다.
- 그리고 거기에 [0] 이런 식으로 순서지정해줄 필요없이 냅다 .html() 붙이면
- 셀렉터로 찾은 모든 요소를 한 번에 조작하고 변경해줄 수 있습니다. 

### 이벤트리스너는
```html
<p class="hello">안녕</p>
<button class="test-btn">버튼</button>

<script>
  $('.test-btn').on('click', function(){
    어쩌구~
  });
</script>
```

### UI 애니메이션은
```html
<p class="hello">안녕</p>
<button class="test-btn">버튼</button>

<script>
  $('.test-btn').on('click', function(){
    $('.hello').fadeOut();
  });
</script>
```
- .hide() 는 사라지게, .fadeOut() 은 서서히 사라지게, .slideUp() 은 줄어들며 사라지게 만들어줍니다. 
- 간단한 애니메이션은 이런 식으로 쉽게 사용가능합니다. 
- 애니메이션을 반대로 주고 싶으면 show() fadeIn() slideDown() 이런게 있습니다. 
- 아니면 fadeToggle() 이런 것도 있음 


## 폼만들며 배워보는 if else

그럼 자바스크립트로 

    전송버튼누르면
    저기 <input>에 입력된 값이 공백이면 알림띄워주세요 

코드 짜면 되는데 "이런 경우에만 코드 실행해주세요~" 라는 표현법은 배우지 않았습니다.
이 경우엔 자바스크립트 if 문법쓰면 됩니다.

### 잠깐 문법수업 : if else 조건문

조건부로 코드를 실행하고 싶으면 if 문법을 쓰면 됩니다.

```javascript
if (조건식){
  실행할코드
}
```

### 간편한 alert 함수

- 간단한 알림팝업 띄우고 싶으면 alert('어쩌구') 쓰면 됩니다. 
- 사용자에게 간단한 안내문을 간편하게 띄울 수 있습니다.

### 전송버튼 누르면 공백체크하라던 숙제

- 태그는 그냥 태그명 그대로 작성
- jQuery 형태로 작성하니깐 안됐음
- $('#id').value == '' <= 요건 안됨
- jQuery에서는 val() 메서드를 사용하여 요소의 값을 가져올 수 있다
- if ($('#id').val() === '') 이런식으로 작성되어야 한다.
```javascript
$('form').on('submit', function(e){
  if (document.getElementById('id').value == ''){
    e.preventDefault();
    alert('아이디를 입력해주세요')
  } 
  
  if (document.getElementById('password').value == ''){
    e.preventDefault();
    alert('비밀번호를 입력해주세요')
  } 
  
  if (document.getElementById('password').value.length < 6){
    e.preventDefault();
    alert('비밀번호는 6자 이상입니다')
  }
});
```

## 변수문법

- 자료를 잠깐 저장하고 싶으면 변수문법을 씁시다.
- var 변수명 = 넣을값; 이러면 됩니다.

`그래서 변수 왜 쓰는 문법임?`
이라고 물어보면 답할 수 있어야 배운 것입니다. 

  1. 길고 복잡한 자료가 있으면 잠깐 변수에 저장해서 쓰면 편리합니다.
  2. 특정 값을 기록하고 싶으면 변수씁니다.


## 변수의 선언, 할당, 범위라는 개념

변수쓸 땐 선언과 할당이라는 용어가 있는데

- 변수만드는걸 선언
- 변수에 뭐 집어넣는걸 할당이라고 합니다.

```javascript
var 나이;
var 이름;
나이 = 20;
이름 = 'kim';
```
- 위의 2줄은 변수의 선언이라고 합니다.  
- 밑의 2줄은 할당이라고 합니다.
  - 저렇게 선언만 따로, 할당만 따로 할 수 있습니다. 
  - 이미 있는 변수를 재선언도 가능합니다.
  - 이미 들어있는 값을 등호로 재할당도 가능합니다.

```javascript
function 함수(){
  var 나이 = 20;
  console.log(나이); //가능
}

console.log(나이); //불가능
```
- 변수는 사용가능한 범위가 있습니다.
- 함수 안에서 변수를 만들었을 경우 함수 안에서만 사용가능합니다.
- 밖에선 사용불가능합니다. 밖에서 출력하면 변수가 정의 안되었다고 에러남
- 반대로 함수 바깥에서 만든 변수는 함수 안에서는 사용가능합니다.

### var let const 문법 전부 변수생성 가능

```javascript
let 거주지 = 'seoul';
const 가격 = 3000;
```
- var 대신 let, const 문법 써도 똑같이 변수생성이 가능합니다.
- 근데 let, const는 이런 기능을 제공합니다. 

```javascript
let 거주지 = 'seoul';
let 거주지; //에러내줌
```
- let, const는 재선언 불가능합니다. 재선언하면 에러를 내줍니다.  

Q. 장점이 뭐임 
- 여러분 코드 천줄 만줄 짜다보면 나중에 변수만든거 또 만들고 그런 실수가 있습니다.
- 그걸 미연에 방지해주는 고마운 변수생성 키워드입니다. 

```javascript
const 가격 = 3000;
가격 = 4000;  //에러내줌
```
const는 재할당도 불가능합니다. 재할당하면 에러를 내줍니다.

Q. 장점이 뭐임 
- 값을 수정하면 큰일나는 변수들을 만들고싶을 때 유용합니다.
- 나중에 값을 변경하는 실수를 방지하고 싶을 때 쓰면 됩니다.

```javascript
if (true) {
  let 이름 = 'kim';
}

console.log(이름); //없다고 나옴
```
- let과 const는 범위가 더 좁습니다. 모든 중괄호가 범위입니다.
- if, function, 나중에 배울 for 반복문 이런 것은 중괄호가 있습니다.
- 중괄호 안에서 만든 let const 변수의 경우 중괄호를 벗어나면 없다고 나옵니다.

  var 이름 = 'kim'; : 재선언 O 재할당 O 범위 function-scope
  let 이름 = 'kim'; : 재선언 X 재할당 O 범위 {block-scope}
  const 이름 = 'kim'; : 재선언 X 재할당 X 범위 {block-scope}

## setTimeout 타이머주는 법

기본 함수 중에 setTimeout() 이런게 있는데, 이거 쓰면 X초 후에 코드를 실행해줍니다.
```javascript
setTimeout(function(){ 실행할코드~ }, 기다릴시간);
```

위처럼 사용하면 됩니다.
시간은 ms 단위로 적으면 됩니다. (1ms는 1000분의 1초)

```javascript
setTimeout(function(){ 
  console.log('안녕')
}, 1000);
```
위처럼 쓰면 1초 후에 콘솔창에 '안녕'이 뜹니다.

`X초마다 코드를 실행하고 싶으면 setInterval()`

X초마다 코드를 실행하고 싶으면 setTimeout() 을 연달아서 여러개 쓰거나
```javascript
setInterval(function(){ 실행할코드~ }, 기다릴시간);
```

위처럼 setInterval 써도 됩니다.
그럼 X초마다 안에 있는 코드를 실행해줍니다. 

```javascript
setInterval(function(){ 
  console.log('안녕')
}, 1000);
```
위처럼 쓰면 1초 마다 콘솔창에 '안녕'이 뜹니다.


## 정규식으로 이메일형식 검증해보기

문자 검사하는 가장 쉬운 방법 
```javascript
'문자'.includes('찾을단어')
```
아무 문자나 뒤에 .includes() 붙일 수 있습니다.
그럼 문자에 찾을 단어가 들어있는지 검사해주고 있으면 true / 없으면 false 남겨줍니다.

하지만

- 한글이 들어있냐
- 영어가 들어있냐
- A로 끝나냐
- 마침표 다음에 영어가 있냐 

이런건 includes() 만으로 검사하기 어렵습니다. 

### 정규표현식 (regular expression)

줄여서 정규식은 문자를 검사하고 싶을 때 사용하는 식입니다. 

"어떤 문자에 'abc'라는 단어가 들어가있냐?" 라고 물어보고 싶을 때 쓰시면 됩니다.
자바스크립트로 정규식을 어떻게 표현하냐면 
```javascript
/abc/
```
이게 끝입니다.
그러면 이제 abc라는 단어가 있냐~? 라고 물어볼 준비가 된겁니다.

그럼 abcdef라는 문자에 abc라는 단어가 있는지 검사해보도록 합시다. 
```javascript
/abc/.test('abcdef')
```
/정규식/.test(정규식으로 검사해볼문자) 쓰면 됩니다.

진짜 들어있으면 true를 남기고 없으면 false를 남겨줍니다. 
```javascript
/[a-d]/.test('aefg')  //true
/[가-다]/.test('다라마바')  //true
```
[ ] 기호를 이용해서 문자 범위를 지정할 수 있습니다.
[a-z] 는 a부터 z까지 아무문자 하나를 의미합니다.

```javascript
/[a-zA-Z]/.test('반가워요')  //false
/[a-zA-Z]/.test('반가워요a') //true
/[ㄱ-ㅎ가-힣ㅏ-ㅣ]/.test('반가워요')  //true
```
[a-zA-Z] 이건 아무 알파벳 하나라는 뜻입니다. 
[ㄱ-ㅎ가-힣ㅏ-ㅣ] 이건 아무 한글 하나라는 뜻입니다. 

```javascript
/\S/.test('abcde')   //true
```
백슬래시S 는 특수문자 포함 아무문자 1개라는 뜻입니다. 
자판의 원화기호가 백슬래시입니다.

```javascript
/^a/.test('abcde')   //true
/e$/.test('abcde') //true  
```
^a 라고 적으면 a로 시작하는지 검사할 수 있습니다.
e$ 라고 적으면 e로 끝나는지 검사할 수 있습니다.

```javascript
/(e|f)/.test('abcde')   //true
```
| 이건 or 기호입니다.
그래서 위 코드는 e 또는 f중 아무거나 한 문자가 있나 검사가능합니다.
정규식에선 괄호맘대로 칠 수 있습니다. 

```javascript
/a+/
```
+ 기호를 붙여주시면 뒤에 오는 글자들도 a와 일치하면 반복해서 쭉 찾아달라는 뜻입니다.
왜냐면 /a/는 a를 다 찾으라는게 아니라 a 한개를 찾으라는 뜻입니다.
aaaaa 이런걸 찾고 싶으면 /a+/ 쓰면 됩니다. 

### 간단히 작성해보는 이메일 정규식 

이메일은 어쩌구@어쩌구.어쩌구 이렇게 되어야합니다.
모든 문자 사이에 @ 그리고 .이라는 특수문자가 와야합니다. 

```javascript
/\S+@\S+\.\S+/
```
이렇게 쓰면 되겠습니다.

\. 이라는 기호는 왜 이렇게 썼냐면 마침표는 정규식에서 특수한 문법이기 때문에
마침표 문법을 쓰는게 아니라 진짜 마침표를 찾아달라라는 의미로 쓰려면 백슬래시를 앞에 붙여야합니다

## 함수의 return 문법 & 소수 다루기

함수 function 문법은

- 긴 코드 짧게 축약해서 쓸 수 있고 
- 파라미터로 기능업그레이드도 가능하다고 했습니다.
- 오늘 배울 return을 쓰면 함수를 쓰고나서 원하는 값을 그 자리에 퉤 뱉을 수도 있습니다.

### 함수안에서 쓸 수 있는 return 문법

- 함수 안에서 return이라는 문법을 사용할 수 있습니다.
- return 오른쪽에 아무거나 적으면 
- 함수가 실행되고난 자리에 return 오른쪽에 있던 값이 뾰로롱 남습니다. 

```javascript
function 함수(){
  return 123
}

console.log(함수()); // 123
```

```javascript
function 함수(){
  console.log('안녕');
  return 123
  console.log('반가워');
}

함수();
```

- 그리고 return 문법은 함수종료의 뜻도 가지고 있습니다.
- 함수안에 코드가 길면 위에서부터 한줄한줄 실행해주는데
- return을 만나면 함수가 바로 종료됩니다.
- 그래서 위 코드에선 console.log('반가워'); 이거 실행안됨


## 스크롤 이벤트로 만드는 재밌는 기능들

### 스크롤 이벤트리스너 

```javascript
window.addEventListener('scroll', function(){
  console.log('안녕')
});
```
- 스크롤바를 조작하면 scroll 이벤트가 발생합니다.

- 그래서 scroll 이벤트리스너를 전체 페이지에 달면 전체 - 페이지를 스크롤할 때마다 원하는 코드를 실행할 수 있습니다.

- 진짜 스크롤바 만질 때 마다 '안녕' 출력되나 봅시다.
- 참고로 window는 그냥 전체 페이지를 의미합니다.

- 실은 document도 전체 페이지입니다. window가 약간 더 큰 개념인데 scroll 이벤트리스너는 관습적으로 window에 붙임 

### 스크롤 관련 유용한 기능들

- 스크롤 이벤트리스너안에서 쓰는 유용한 기능들이 몇개 있습니다. 

```javascript
window.addEventListener('scroll', function(){
  console.log( window.scrollY )
});
```

- `window.scrollY` 사용하면 현재 페이지를 얼마나 위에서 부터 스크롤했는지 px 단위로 알려줍니다.

- `window.scrollX` 는 가로로 얼마나 스크롤했는지 알려줍니다. (가로 스크롤바가 있으면)

```javascript
window.scrollBy(0, 100)
```
- window.scrollBy(x, y) 실행하면 현재 위치에서부터 스크롤해줍니다.
- 위 코드는 현재 위치에서부터 +100px 만큼 스크롤해줍니다.

```javascript
$(window).on('scroll', function(){
  $(window).scrollTop();
})
```

jQuery 버전은 더 짧습니다.

- $(window).scrollTop() 이거 쓰면 아까처럼 현재 페이지 스크롤 양을 알려줍니다.
- 근데 간편한건 $(window).scrollTop(100) 이러면 페이지 강제이동도 해줌

### div 박스의 스크롤바 내린 양은 

박스를 셀렉터로 찾고 `.scrollTop` 붙이면 스크롤바를 위에서 부터 얼마나 내렸는지 알려줍니다.

```javascript
$('.lorem').on('scroll', function(){
  var 스크롤양 = document.querySelector('.lorem').scrollTop;
  console.log(스크롤양);
});
```

### div 박스 높이 구하는 법 

- 스크롤바가 생긴 박스의 경우 실제 높이같은게 궁금할 수 있습니다. 
- 박스에 스타일로 넣은 height : 100px 이거 말고 스크롤가능한 실제높이 말입니다.
- 그럴 땐 셀렉터로 찾아서 `.scrollHeight` 붙이면 나옵니다.

```javascript
$('.lorem').on('scroll', function(){
  var 스크롤양 = document.querySelector('.lorem').scrollTop;
  var 실제높이 = document.querySelector('.lorem').scrollHeight;
  console.log(스크롤양, 실제높이);
});
```

- 참고로 박스가 화면에 보이는 부분 높이는 .clientHeight 하면 나옵니다.
- document.querySelector('.lorem').clientHeight; 해보셈 

### 스크롤 다룰 때 주의점

- 1. 스크롤이벤트리스너 안의 코드는 1초에 60번 이상 실행됩니다. 그래서 스크롤 이벤트리스너는 많이 달면 성능저하가 일어나니 스크롤바 1개마다 1개만 씁시다.  

- 2. 스크롤이벤트리스너 안의 코드는 1초에 여러번 실행되다보니 바닥체크하는 코드도 여러번 실행될 수 있습니다. 

- 그걸 방지하고 싶으면 구글에 검색해보는 것도 나쁘지않습니다. 변수같은걸 활용하면 됩니다.(true / false)



### 페이지 내릴 때 마다 페이지를 얼마나 읽었는지 진척도를 알려주는 UI 같은건 어떻게 만들면 될까요?

```javascript
$(window).on('scroll', function(){
  // 유저의 스크롤양
  // const windowScroll = window.scrollY;
  const windowScroll = document.querySelector('html').scrollTop
  // 실제높이에서 눈에 보이는 나머지 값을 뺀 실질적인 스크롤 양
  const total = document.querySelector('html').scrollHeight - document.querySelector('html').clientHeight;
  // 실질적인 스크롤양에서 유저의 스크롤양을 나눈 뒤 * 100하여 백분율을 계산 
  const percentage = (windowScroll / total) * 100;
  $('.progress').css('width', percentage + '%')
})
```


## 이벤트 버블링과 이벤트관련 함수들

### 이벤트 버블링

- 어떤 HTML 태그에 이벤트가 발생하면 그의 모든 상위요소까지 이벤트가 실행되는 현상을 이벤트 버블링이라고 합니다. 

- click이라는 이벤트로 예를 들어보면, HTML 태그에 클릭이 발생하면 그의 모든 상위요소까지 자동으로 클릭된다는 말입니다. 

```html
<div>
  <div>
    <p>안녕</p>
  </div>
</div>
```
▲ 위의 코드에서 p태그 안녕이라는 글자를 클릭하면 브라우저는 사용자가 클릭을 총 3번 했다고 인지합니다.

- p랑 그 위의 div랑 그 위의 div랑 이렇게요.
- 이게 이벤트 버블링인데 브라우저는 원래 그렇게 동작하도록 되어있습니다.
- 이 사실을 모르고 코드짜다보면 가끔 이상한 현상이 발생할 수도 있습니다. 

### 이벤트리스너 안에서 쓰는 이벤트 함수들 

```javascript
document.querySelector('.black-bg').addEventListener('click', function(e){
  e.target;
  e.currentTarget;
  e.preventDefault();
  e.stopPropagation();
})
```

- 이벤트리스너의 콜백함수에 파라미터 아무거나 추가하면  이벤트관련 유용한 함수들을 사용가능합니다. 

- 파라미터 이름은 아무렇게나 작명하면 됩니다. 보통 대충 e라고 함.

- e.target은 실제 클릭한 요소 알려줌 (이벤트 발생한 곳)

- e.currentTarget은 지금 이벤트리스너가 달린 곳 알려줌 (참고로 this라고 써도 똑같음)

- e.preventDefault() 실행하면 이벤트 기본 동작을 막아줌

- e.stopPropagation() 실행하면 내 상위요소로의 이벤트 버블링을 중단해줌

- 몇개만 뽑아봤는데 필요할 때 가져다가 쓰면 됩니다. 

- e.target 이런거 출력해보십쇼 진짜 그게 맞나 

(참고2)

jQuery 셀렉터로 찾은 결과와
- querySelector 셀렉터로 찾은 결과는 다르게 생겼습니다.

- 출력해보면 전자는 이상한 object 이런게 나오고 후자는 <html> 이런게 나옵니다. 

- 그래서 e.target == $('.black-bg') 이건 사용불가능합니다.그리고 애초에 jQuery 셀렉터끼리 등호비교는 불가능합니다. 

- $('.black-bg').is($('.black-bg')) 이런 비교용 함수쓰든가 하면 됩니다.

- 위 예제에선 $(e.target).is($('.black-bg')) 이러면 됩니다.


그래서 오늘의 결론
1. 이벤트 버블링은 항상 일어난다

2. 이벤트 관련 유용한 함수들을 사용가능하다

잘 기억해두면 됩니다. 


## dataset 문법

```html
<div data-데이터이름="값"></div> 
```

- html 안에 유저 몰래 정보를 숨겨놓을 수 있습니다. 
- 데이터이름 아무렇게나 작명하고 값도 넣으면 됩니다.


```javascript
document.querySelector().dataset.데이터이름;
```

- 이러면 html 요소에 숨겨놨던 데이터가 이 자리에 남습니다.
- 출력해보면 진짜로 아까 숨겨놓은 값이 남습니다.


## 쓸만한 자바스크립트 라이브러리들

1. Swiper

https://swiperjs.com/get-started#use-swiper-from-cdn

- 캐러셀 (이미지슬라이드되는거) 만들고 싶으면 직접 코드 짜도 되겠지만
- 좀 이쁘게 아니면 쉽게 여러기능을 만들고 싶으면 Swiper 라이브러리 써도 됩니다.
- 호환 잘되고 이미지 lazy loading 이런 것도 되고 터치/드래그도 됩니다.


2. Animate On Scroll

- 스크롤 내리면 요소가 서서히 등장하는 애니메이션을 만들고 싶을 때 쓰면 좋습니다.

- 유저가 스크롤바를 ... div 박스 현재 y좌표만큼 내리면 애니메이션 보여달라고 코드짜면 되긴 하는데 귀찮으니까요 
 
https://github.com/michalsnik/aos

- 여기서 css파일, js 파일 cdn버전 찾아서 html 파일에 넣고
그 다음에 밑에 <script> 태그 열어서 

```javascript
<script>
  AOS.init();
</script>
```

https://michalsnik.github.io/aos/

그 다음에 위 사이트에서 예제 코드 따라서 복붙하면 구현 끝인듯요 


3. EmailJS

원래 이메일 전송은 서버가 해야하지만 Gmail 이런거 서버를 잠깐 빌리면

자바스크립트만으로 이메일 전송이 가능합니다. 
유저가 내 이메일 계정으로 이메일 전송도 가능하고 
내 이메일 계정으로 남에게 이메일 전송도 가능함 

https://www.emailjs.com/docs/introduction/how-does-emailjs-work/

이 사이트 가서 가입하고 계정만들고
튜토리얼 그대로 복붙하고 거기에 내가 방금 만든 EmailJS 계정아이디만 잘 채우면 됩니다. 


## Array 와 Object 자료형

### Array 자료형 

- 여러가지 자료를 한곳에 저장하고 싶을 때 사용하는 자료형입니다. 

```javascript
var car = ['소나타', 50000, 'white'];
console.log(car[1])
```

- array 자료에서 데이터 뽑을 땐 대괄호를 뒤에 붙이면 됩니다. [x] 라고 쓰면 x번째 자료를 출력해줍니다

```javascript
var car = ['소나타', 50000, 'white'];
car[1] = 60000;
console.log(car[1])
```
- array 자료를 수정하고 싶으면 등호 이용해서 수정하면 됩니다.
- 자료 추가도 됩니다.
- 그래서 결론은 여러 자료를 변수 하나에 저장하고 싶으면 array를 사용하면 편리합니다

### Object 자료형 

- 이것도  여러가지 자료를 한곳에 저장하고 싶을 때 사용하는 자료형입니다. 

```javascript
var car2 = { name : '소나타', price : 50000 };
```

- 중괄호를 열고 자료를 콤마로 구분해서 집어넣으면 됩니다.

- 그런데 자료 왼쪽에 자료의 이름을 붙여서 저장해야합니다.

- 멋진 말로 자료의 이름은 key, 실제 자료는 value라고 부릅니다.

- 그래서 object 자료형은 key : value 형태로 자료를 저장할 수 있습니다. 

```javascript
var car2 = { name : '소나타', price : 50000 };
console.log(car2['name']);
console.log(car2.name);
```

- array 자료에서 데이터 뽑을 땐 대괄호를 뒤에 붙이면 되는데
- [자료이름] 이렇게 써야합니다.
- .자료이름 이렇게 써도 가능합니다. 마음에드는거 쓰십쇼 

```javascript
var car2 = { name : '소나타', price : 50000 };
car2['name'] = '그랜저';
console.log(car2['name'])
```

- object 자료를 수정하고 싶으면 등호 이용해서 수정하면 됩니다. 자료 추가도 됩니다.

- 그래서 결론은 여러 자료를 변수 하나에 저장하고 싶으면 object 사용해도 편리합니다.

### Array/Object 차이 

- array는 순서개념이 있습니다. 왼쪽에 적을 수록 더 앞에 있는 자료임

- object는 순서개념이 없습니다. 가장 왼쪽에 적었다고 해도 1빠임을 보장해주지 않습니다.

- 그래서 array 자료는 순서개념이 있다보니

    - 가나다순 정렬
    - x번 자료부터 x번 자료까지 자르기
    - x번 자료 바꾸기
    - 맨 뒤, 맨 앞에 자료 넣기
    - 원하는 자료가 들어있나 검색

- 순서개념이 필요한 많은 것들을 할 수 있습니다. 

    - array자료.sort() 하면 가나다순 정렬되고
    - array자료.slice(x, y) 하면 x번부터 y번 전까지 자를 수 있고 
    - array자료.push(x) 하면 x를 맨 뒤에 입력할 수 있고

이런 기본함수들이 준비되어있습니다.

array 자료 조작이 필요할 때 검색해서 써보도록 합시다


## Select 인풋 다루기

```html
<form class="container my-5 form-group">
    <p>상품선택</p>
    <select class="form-select mt-2">
      <option>모자</option>
      <option>셔츠</option>
    </select>
</form>
```
- <select> 는 <input> 이랑 똑같은데
- 사용자가 고를 수 있는 선택지를 드랍다운 메뉴로 제공하는 <input> 입니다. 
- 선택지는 <option>으로 넣으면 됩니다. 
    - <select> 태그도 선택시 input, change 이벤트가 발생합니다.
    - <select> 태그도 .value로 유저가 입력한 값을 가져올 수 있습니다.

### 셔츠고르면 밑에 <select> 더 보여주기

Q. 유저가 셔츠를 선택하면 하단에 95, 100 을 선택할 수 있는 <select> 박스가 등장하려면 코드 어떻게 짜면 될까요?

```html
<form class="container my-5 form-group">
    <p>상품선택</p>
    <select class="form-select mt-2">
      <option>모자</option>
      <option>셔츠</option>
    </select>
    <select class="form-select mt-2 form-hide">
      <option>95</option>
      <option>100</option>
    </select>
</form>
```
- 미리 <select> 하나 더 추가했고 form-hide 클래스에는 display : none 주었습니다.
- 이제 "유저가 셔츠선택하면 form-hide 제거해주세요~" 라고 코드짜면 완성일듯요 

```javascript
<script>
  $('.form-select').eq(0).on('input', function(){

    var value = $('.form-select').eq(0).val();
    if (value == '셔츠') {
      $('.form-select').eq(1).removeClass('form-hide');
    }
  });
</script>
```


## Select 2 : 자바스크립트로 html 생성하는 법

#### html 생성하는 법 

```html
<div id="test">
  
</div>

<script>
  var a = '<p>안녕</p>';
  document.querySelector('#test').insertAdjacentHTML('beforeend', a);
</script>
```

- 문자자료로 html을 만든 다음 
- insertAdjacentHTML() 안에 넣으면 됩니다.
- 'beforeend' 이건 안쪽 맨 밑에 추가하라는 뜻입니다. 싫으면 맘대로 변경가능 


```html
<div id="test">
  
</div>

<script>
  var a = '<p>안녕</p>';
  $('#test').append(a);
</script>
```

- 이래도 됩니다. 
- append는 안쪽 맨 밑에 추가하라는 뜻입니다. 

- Q. 저는 안쪽에 추가하는게 아니라 아예 바꾸고 싶은데요
- A. div찾아서 innerHTML = '<p></p>' 쓰셈, jQuery에선 .html() 입니다. 


### 바지옵션 누르면 다른 사이즈가 나와야하는데

```html
<form class="container my-5 form-group">
    <p>상품선택</p>
    <select class="form-select mt-2">
      <option>모자</option>
      <option>셔츠</option>
      <option>바지</option>
    </select>
    <select class="form-select mt-2 form-hide">
      <option>95</option>
      <option>100</option>
    </select>
</form>
``` 

- 첫 <select> 에 바지옵션을 추가해봅시다.
- 이거 누르면 28과 30 사이즈가 담긴 <select>가 
떠야합니다.

코드 어떻게 짜야하죠?
    - 당연히 html을 미리 만들어놨다가 보여줘도 되는데 실제 쇼핑몰의 경우 그렇게 만들어놓을 순 없습니다.
    - 바지 사이즈가 매일 달라지면 어떻게 합니까 매일 아침 html 수정할 것임?
    - 실제 서비스는 매번 서버에서 데이터를 받아와서 "데이터 갯수만큼 <option> 생성해주세요~" 라고 코드를 짜놓습니다.
    - 그래서 우리도 이를 대비하기 위해 html을 미리 만들어놓지말고 자바스크립트로 html을 생성해봅시다.

```html
<script>
  $('.form-select').eq(0).on('input', function(){

    var value = $('.form-select').eq(0).val();
    if (value == '셔츠') {
      $('.form-select').eq(1).removeClass('form-hide');
    }
    else if (value == '바지'){
      $('.form-select').eq(1).removeClass('form-hide');
      $('.form-select').eq(1).html('');
      var 템플릿 = `<option>28</option><option>30</option>`;
      $('.form-select').eq(1).append(템플릿)
    }

  });
</script>
``` 
그래서 유저가 바지를 선택하면

1. 일단 둘 째 <select> 보여주셈 
2. 둘 째 <select> 안에 비워주셈
3. html 만들어서 둘 째 <select> 안에 append 해주셈 

이라고 코드를 짰더니 진짜로 그렇게 해줍니다.
아니면 더 간단하게 할 수도 있을듯요 


## Select 3 : forEach, for in 반복문

- 서버에서 바지 사이즈 데이터 가져와서, 그 갯수만큼 <option>을 생성해봅시다. 
- 그래서 다음처럼 코드짜놓고 시작합시다. 

```html
<script>
  var pants = [28, 30, 32];
  $('.form-select').eq(0).on('input', function(){

    var value = $('.form-select').eq(0).val();
    if (value == '셔츠') {
      $('.form-select').eq(1).removeClass('form-hide');
    }
    else if (value == '바지'){
      $('.form-select').eq(1).removeClass('form-hide');
      $('.form-select').eq(1).html('');
      여기다 무슨 코드 짜야함 
    }
  });
</script>
```

- 맨 위에 pants 라는 변수를 하나 만들고 서버에서 보낸데이터라고 가정해봅시다.
- pants 데이터 갯수만큼 <option>을 생성하고싶으면 어떻게 해야할까요? 
- 반복문 쓰면 될 것 같은데요 

```javascript
$('#test').append(템플릿);

    var pants = [28, 30, 32, 34];
    var shirts = [90, 95, 100, 105];

    $('.form-select').eq(0).on('input', function(){
      var select = this.value;

      if (select == '셔츠'){
        $('.form-select').eq(1).removeClass('form-hide');
        $('.form-select').eq(1).html('');
        shirts.forEach(function(data){
          // .html() 메서드는 선택한 요소의 내용을 지우고 새로운 내용으로 대체(교체)합니다. 
          // .append() 메서드는 선택한 요소의 끝에 새로운 내용을 추가합니다.
          // 그래서 .html() 메서드를 사용하면 shirts 마지막 값인 105만 출력된다 
          $('.form-select').eq(1).append(`<option>${data}</option>`)
        })
      } else if (select == '모자'){
        $('.form-select').eq(1).addClass('form-hide');
      } else {
        $('.form-select').eq(1).removeClass('form-hide');
        $('.form-select').eq(1).html('');
        // forEach 반복문 : array에 붙일 수 있는 반복문
        // forEach 반복문의 콜백함수 파라미터에 작명을 하면 그 안에 array의 데이터가 차례대로 출력
        // forEach 안에 파라미터 2개 생성가능(첫째는 array 안의 데이터, 둘째는 0부터 1씩 증가하는 정수)
        pants.forEach(function(data, i){
          $('.form-select').eq(1).append(`<option>${data}</option>`);
        });

        // 콜백함수를 arrow function 으로 사용해도됨
        // 그러나 arrow function 쓰면 함수 안의 this 뜻이 달라질 수 있음
        // pants,forEach((data) => {
        //   $('.form-select').eq(1).append(`<option>${data}</option>`);
        // });
      }
```