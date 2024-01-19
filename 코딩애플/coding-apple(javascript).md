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