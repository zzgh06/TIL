## CSS Selector
```css
  .profile { font-size : 20px }  /*클래스*/
  #special { font-size : 30px } /*아이디*/
  p { font-size : 16px } /*태그*/
```
CSS selector 라고 칭하는 것들입니다. 

- 클래스 selector는 .클래스명{ } 이렇게 적을 수 있고 모든 class="클래스명"을 가진 요소에 스타일을 적용가능.

- 아이디 selector는 #아이디명 { } 이렇게 적을 수 있고 모든 id="아이디명" 속성을 가진 요소에 스타일을 적용가능.

- 태그 selector는 p { 스타일~~ } 이렇게 적을 수 있고 모든 <p> 태그에 스타일을 적용가능.

### 셀렉터의 우선 순위
물론 class, id를 동시에 가지는 html 요소라면 스타일이 겹칠 수 있습니다. 그럴 경우 우선순위가 존재한다.

    style="" (1000점)
    #id (100점)
    .class (10점) 
    p (1점) 

정확한 카운트법은 아니지만 아무튼 이런 식, 점수가 높을 수록 더 우선적으로 적용된다. 

## float 속성
```html
<div>
  <div class="left-box"></div>
  <div class="right-box"></div>
</div>
```
```css
.left-box {
  width : 100px; 
  height : 100px;
  float : left;
}
.right-box {
  width : 100px; 
  height : 100px;
  float : left;
}
```
- 위의 코드는 박스 두개를 만들어 각각 왼쪽으로 정렬시킨다.

- 하지만 float를 쓰면 요소를 붕 띄우다보니 그 다음에 오는 HTML 요소들이 제자리를 찾지 못합니다. 

- (참고) float 속성으로 가로정렬할 땐, float 박스들을 싸매는 하나의 큰 div 박스를 만들고 폭을 지정해주는게 좋다. 그래야 모바일에서 안 흘러넘친다.

**float를 쓰고 나면 항상 clear 속성이 필요합니다**

```html
<div>
  <div class="left-box"></div>
  <div class="right-box"></div>
  <div class="footer"></div>
</div>
```
```css
.footer {
  clear : both
}
```
- clear 속성을 사용하면 float 다음에 오는 박스들이 제자리를 찾게된다.

- float썼으면 까먹지 말고 항상 넣는다, 안넣으면 내 의도와는 다른 레이아웃이 반겨준다. 

- 참고로 float : none 이것도 추가해주는게 나중에 생길 버그예방차원에서도 좋을 수 있다. 

## Table
기본적인 table HTML 구성 
```html
<table>
  <thead></thead>
  <tbody>
    <tr>
      <td>내용</td>
      <td>내용</td>
    </tr>
  </tbody>
</table>
```
- table태그 내에 tr은 row, td는 column을 의미. 

- 내가 원하는 만큼 row, column을 넣어주면 표가 완성. 

- tbody, thead는 그냥 헤드부분 영역구분을 위해 사용하며 td 대신 th 태그를 사용하면 기본적으로 제목처럼 굵게 처리된다. 

### 테이블 셀 내에서 상하정렬할 땐 vertical-align
```css
td, th {
  vertical-align : middle;
}
```
- vertical-align 속성을 이용해 테이블 내에서의 상하정렬을 할 수 있다.

- top, bottom, middle 사용가능


## nth-child 셀렉터
```css
.cart-table td:nth-child(2) {
  color: red;
} 
```
- 여러 요소를 찾은 다음, 원하는 n번째 요소만 스타일을 주고 싶으면 :nth-child(n) 이걸 뒤에 붙여주면 된다.

- 위의 코드는 그래서 .cart-table 안에 있는 모든 td를 찾은 다음, 2번째 나오는 td에만 color를 줄 수 있다. 

- 테이블에서 원하는 순서의 셀에 스타일줄 때 가끔 유용하게 사용한다.

```css
.cart-table td:nth-child(even) {
  color: red;
} 
```
- 이러면 짝수로 등장하는 td에만 스타일을 줄 수도 있고(odd라고 쓰면 홀수)

```css
.cart-table td:nth-child(3n+0) {
  color: red;
} 
```
- 이러면 3의 배수로 등장하는 3,6,9,12.. 번째 등장하는 요소에만 스타일을 줄 수 있다.

- 3n + 1 이렇게 작성하면 (3의배수 +1) 번째 등장하는 요소에만 스타일을 줄 수 있다.

## head 태그에 들어갈 내용 정리
1. 각종 CSS 파일들 

2. 스타일 태그

3. 사이트 제목

4. 여러가지 meta 태그

5. open graph
```html
<head>
  <meta property="og:image" content="/이미지경로.jpg">
  <meta property="og:description" content="사이트설명">
  <meta property="og:title" content="사이트제목">
</head>
```
- 링크 공유 시 뜨는 사이트 설명, 제목, 이미지를 커스터마이징하고 싶으면 저런 meta 태그를 따로 집어넣으면 된다. 

6. Favicon
```html
<head>
  <link rel="icon" href="아이콘경로.ico" type="image/x-icon">
</head> 
```
- 웹사이트 제목 옆에 뜨는 아이콘을 커스터마이징하려면 이렇게 link 태그로 첨부하면 된다.

- ico 대신 png 파일로 넣어도 됩니다. ico가 호환성은 가장 좋다. 

- 요즘은 32 x 32 사이즈로 제작하면 된다. 그리고 웹사이트를 바탕화면에 바로가기추가했을 경우 뜨는 아이콘도 커스터마이징 가능. 

`rel="apple-touch-icon-precomposed"` 

- 이런 식으로 rel 속성을 조정하면 되는데 OS마다 요구하는 rel 속성이 달라서 필요해지면 찾아 적용하시거나

- favicon generator 이런거 검색해서 한번 써보시면 OS별로 알아서 만들어준다. 

## CSS 덮어쓰기 방법 3개
1. 같은 클래스명이나 스타일을 하단에 작성

  - 하나의 CSS 파일일 경우,
  ```css
  .box {
    background : red;
  }

  .box {
    background : blue;
  }
  ```
  - 같은 class 명이라도 하단에 정의한 클래스 명과 스타일을 우선적으로 적용합니다. 

  ```html
  <link href="main.css" rel="stylesheet">
  <link href="main2.css" rel="stylesheet">
  ```
  - CSS파일이 여러개 첨부되어있을 때도 유효.

  - <link>를 하단에 사용할 수록 하단에 작성한 것과 똑같은 효과이기 때문에 main.css와 main2.css에 같은 class 명이 있더라도 main2.css에 있는 클래스 명을 우선적으로 적용합니다. 

2. id, style 등 우선순위를 높여 작성합니다.

  - tag < class < id < style="" 순으로 우선순위가 높다.

  - 점수로 따지자면 각각 1점 10점 100점 1000점이기 때문.

  - 그래서 class 스타일을 덮어쓰려면 id 써보고 안되면 style속성 열어보고 이렇게 수정하면 된다.

  - 속성 뒤에 !important라는걸 부여하면 모든 우선순위를 씹어먹고 최우선적으로 이 속성을 적용된다. 

  ```css
  .box {
  background : red !important;
  }

  .box {
    background : blue;
  }
  ```
  - 이렇게 사용하면 !important가 붙은 스타일은 최우선으로 적용된다.

  - 하지만 큰 힘으로 다른 힘을 억누르게 되면, 그걸 또 나중에 수정하려면 더 큰 힘으로 억눌러야하기 때문에 근본적인 해결방안이 아니다. 되도록이면 쓰지않는걸 추천. 

  - 특히 id 이런건 스타일링할 때 쓰지 맙시다. 프론트엔드 백엔드 기능개발하는 사람들도 id를 자주 사용하는데 그것과 겹치면 귀찮아진다. 

3. Specificity (구체성 점수) 높여서 작성하기 

  - 셀렉터를 여러개 나열하면 점수도 높아집니다.
  
  - 예를 들면 
  ```css
  div.container .box {
  color : red;
  }
  ```
  - 얘는 21점.

  - 왜냐면 10점짜리인 .class를 2개나 썼고 1점짜리인 div 태그셀렉터를 1개 썼기 때문. 

  - 저렇게 더 구체적으로 셀렉터를 작성할 수록 점수가 높아져서 저렇게 점수를 높여도 덮어쓰기가 가능합니다. 


## Pseudo-element

  - :pseudo-class는 다른 상태일때 ex) hover, active 등
  - ::pseudo-element는 내부의 일부부만 스타일 줄때

  `Pseudo-element로 HTML 특정부분에 스타일링하기/글씨넣기`
  ```css
    .text::first-letter {
      color : red;
    }

    .text::first-line {
      color : red;
    }

    .text::after {
      content : '뻥이지롱';
      color : red;
    }

    .text::before {
      content : '뻥이지롱';
      color : red;
    }
  ```
    1. pseudo-element를 선택하려면 콜론 2개 :: 를 사용하면 됩니다. 

    2. ::first-letter라고 붙이면 안에 있는 글자 중 첫 글자만 스타일을 줄 수 있습니다.
    
    3. ::first-line이라고 붙이면 안에 있는 글자 중 첫 줄만 스타일을 줄 수 있습니다.
    
    4. ::after라고 붙이면 내부의 맨 마지막 부분에 특정 글자같은걸 추가해줄 수 있습니다.
    
    5. ::before라고 붙이면 내부의 맨 앞 부분에 특정 글자같은걸 추가해줄 수 있습니다.

## 쉽게 배우는 Sass 
### **SASS 문법 1 : 값을 저장해놓고 쓰는 '변수'**

- CSS로 색상 지정할 때 #2a4c6e 이런 이상한 칼라코드를 사용합니다.
- SASS 파일에선 이런 어려운 값들을 예쁜 한글로 치환해서 사용할 수 있습니다.

- 변수라는 문법을 쓰면 되는데 변수 문법은 어려운 값들을 이쁜 단어에 저장해서 쓸 수 있게 도와주는 문법입니다.

```css
$메인색상 : #2a4c6e;
$서브색상 : #333333;

.text {
  color: $메인색상
}
.box {
  background: $서브색상
} 
```

1. 우선 SASS 쓰려면 scss 파일 만들고 거기에 적어보십시오. SASS 파일은 항상 파일 확장자가 .scss로 끝나면 됩니다.
2. $기호를 사용하신 후 이쁜 이름을 작명하고, 거기에 저장할 더러운 값을 오른쪽에 적으시면 이제 $이쁜이름을 쓸 때마다 더러운 값이 그 자리에 남습니다.

위에선 #2a4c6e 라는 더러운 값을 $메인색상으로 저장했습니다. 
그럼 이제 #2a4c6e 이 색이 필요할 때 마다 귀찮게 #부터 적는게 아니라 $메인색상 이라고 깔끔하게 적을 수 있습니다.

훨씬 기억하기 쉽습니다. 이것이 Sass에서의 변수 문법입니다.

- 이거 말고도 width, font-size 등 자주 쓰지만 기억하기 어려운 값들을 넣으면 매우 편리합니다.

- $변수이름은 영어도 좋고 한글도 잘 먹습니다. 

- 많은 곳에서 공통적으로 사용하는 값들도 저기 넣으면 좋습니다. 


`사칙연산도 바로바로 가능합니다.`
```css
$기본사이즈 : 16px;

.box {
  font-size : $기본사이즈 + 2px;
  width : (100px * 2);
  height : (300px / 3)
}
```

그럼 진짜로 연산해줍니다. 

- 덧셈뺄셈은 px 단위는 px 단위끼리, % 단위는 % 단위끼리 이렇게 단위 맞춰주셔야하고
- 곱셈 나눗셈은 보통 뒤에 단위를 쓰지 않습니다. 쓰면 이상한 자료형이 됩니다. 
- 곱셈 나눗셈은 괄호 안에 작성해야 잘 먹습니다. 

- 파일 저장해보시면 CSS로 자동변환해준 파일에서 그 결과를 확인할 수 있을겁니다.


### **Sass 문법 2. 셀렉터 대신 쓰는 Nesting**


- 셀렉터를 많이 사용하다보면 코드 자체가 복잡해집니다.
- 예) div.container > div p.first > span::after
- 셀렉터 조금만 복잡해지면 처음 보는사람은 이거 보자마자 무슨 요소인지 제대로 파악조차 어렵습니다.
- 그래서 셀렉터의 외모를 개선할 수 있는 Nesting이라는 문법이 존재합니다.

```css
.navbar {
  ul {
    width : 100%;
  }
  li {
    color : black;
  }
}
/*위에건 SASS 문법*/

.navbar ul { 
  width : 100%; 
}
.navbar li { 
  color : black; 
}
/*밑에건 CSS 문법*/
```

- 위 두개의 코드는 같은 기능을 하는 코드입니다. 
- 중괄호 안에 또 셀렉터를 쓰시면 그것은 셀렉터상의 스페이스바 문법과 동일하게 작성가능합니다.
- 사용하는 이유는 이거 딱 하나입니다.
- "UI들을 뭉텅이로 관리할 수 있어서" 입니다.
- navbar 내부에 속한 요소들을 저렇게 정리해놓으면 나중에 관리가 편해지지 않을까요?
- navbar 내부에 있는 글자 하나 바꾸려고 하면 .navbar {} 중괄호만 뒤져보면 되잖아요.

참고. 그럼 :hover 같은거 붙이려면 어케해야해요?
```css
.navbar {
  :hover {
    color : blue;
  }
}

.navbar {
  &:hover {
    color : blue;
  }
}
```

- 위처럼 쓰면 .navbar :hover를 잡게 되고
- 밑처럼 쓰면 .navbar:hover를 잡게 됩니다.
- 밑에처럼 &기호를 붙여주시면 셀렉터를 스페이스바 없이 붙이실 수 있습니다.


### **Sass 문법 3. 이미 있는 클래스를 확장하는 @extend**

- 이미 존재하는 속성들을 복붙하지 않고 사용하실 수 있습니다.
- @extend 그리고 여러분이 복붙해야할 클래스 명을 뒤에 적어주시면 끝입니다.

```css
.btn {
  font-size : 16px;
  padding : 10px;
  background : grey;
}

.btn-green {
  @extend .btn;
  background : green;
}
```
- @extend를 사용하신 후 복붙할 클래스명을 뒤에 적으면 클래스명에 있던 모든 내용이 복붙됩니다. 
- 보통 비슷한 디자인의 요소들을 양산할 때 많이 사용합니다.
- % 기호는 .대신 쓸 수 있는 임시클래스인데 CSS파일에서 클래스로 컴파일하지 않고싶을 때 쓰는 기호입니다.
- 컴파일하고나면 %기호 안에 있는 것들은 흔적도 없이 사라집니다.

### **Sass 문법 4. 코드를 한단어로 축약하는 @mixin**

- @mixin은 스타일 여러줄을 한 단어로 치환해서 사용가능
```css
@mixin 버튼기본디자인() {
  font-size : 16px;
  padding : 10px;
}

.btn-green {
  @include 버튼기본디자인();
  background : green;
}
```
1. @mixin이라고 쓰고,

2. 이름을 하나 지어주고 ( ){ } 붙이고,

3. 한 단어로 치환할 값들을 중괄호 안에 쭉 나열하시면 됩니다.

- 그럼 이제 밑에서 자유롭게 @include mixin이름 으로 사용하면 mixin 안에 있던 코드가 그 자리에 복붙됩니다.

- mixin과 extend 문법은 유사, mixin만의 장점이 하나 있는데, 바로 내부에 묶어둔 속성들에 구멍을 하나 뿅 뚫어줄 수 있다는 것
```css
@mixin 버튼기본디자인($구멍) {
  font-size : 16px;
  padding : 10px;
  background : $구멍;
}
```
- 소괄호의 역할이 바로 구멍인데, 이제 버튼기본디자인()이라는 단어를 사용하실 때 소괄호구멍 안에 아무거나 값을 집어넣을 수 있습니다.

```css
@mixin 버튼기본디자인($구멍) {
  font-size : 16px;
  padding : 10px;
  background : $구멍;
}

.btn-green {
  @include 버튼기본디자인(#229f72);
}
```
- 그럼 응용하면 btn-green 말고도 파란버튼, 빨간버튼 자유자재로 만드실 수 있겠죠.
- 이것이 mixin의 장점이라고 보시면 됩니다.

1. 긴 코드를 한 단어로 축약할 수도 있고

2. 코드내부에 구멍을 뚫어 사용할 때마다 각각 다른 내용을 집어넣을 수 있습니다.


### **Sass 문법 5. @use와 언더바 파일**
CSS파일마다 맨위에 첨부하는 reset같은걸 자주 복붙하는 분들은 `import문법`을 사용하시길 바랍니다.

```css
@use 'reset.scss';
```
- 이러면 reset.scss 파일을 해당 SCSS파일에 전부 복붙할 수 있습니다.
- 파일이 다른 폴더 안에 있다면 '폴더명/reset.scss' 이런 식으로 경로를 잘 써주시면 됩니다.

```css
@use '_reset.scss';
```
- scss 파일명을 작명할 때 언더바를 파일명 맨 앞에 붙이는 경우가 있습니다.
- 언더바 _기호를 파일명 맨앞에 사용하시면 "이 파일은 CSS파일로 따로 컴파일하지 말아주세요" 라는 의미입니다.
- 그냥 첨부용 파일이라는 것이지요.

```css
@use '_reset.scss';

reset.$변수명;  /* 다른 파일의 변수쓰는법 */
@include reset.mixin이름();  /* 다른 파일의 mixin쓰는법 */
```

- @use 해온 다른 파일에 있던 $변수와 @mixin을 가져다 쓸 수도 있습니다.
- 이 경우엔 그냥 쓰는게 아니라 꼭 파일명을 앞에 붙여야합니다. 
- 응용하면 다른 파일에서 자주 사용할법한 _button.scss _navbar.scss 이런 파일들을 미리 다 만들어놓고 멋지게 첨부식으로 CSS를 개발할 수 있습니다.


## transform & animation 으로 매끄러운 애니메이션 만들기
### transform 관련 CSS 속성들 
```css
.box {
  transform : rotate(10deg); 
  transform : translate(10px, 20px);
  transform : scale(2);
  transform : skew(30deg);
  
  /*transform 두개 이상을 한꺼번에 쓰려면*/
  transform : rotate(10deg) translateX(30px);
}
```
- transform 은 어떤 요소를 독립적으로 움직이게 만들고 싶을 때 사용합니다.
- 본인 원래 위치에서 자유롭게 (다른 요소에 영향 없이) 이동하게 됩니다.
- rotate는 회전, translate는 좌표이동, scale은 확대축소, skew는 비틀기 입니다.

### 복잡한 애니메이션 구현법
1. 가장 먼저 @keyframes 를 정의합니다.
```css
@keyframes 움찔움찔{
  0% {
    transform : translateX(0px); /* 애니메이션이 0%만큼 동작시 */
  }
  50% {
    transform : translateX(-20px); /* 애니메이션이 50%만큼 동작시 */
  }
  100% {
    transform : translateX(20px); /* 애니메이션이 100%만큼 동작시 */
  }
}
```
- `@keyframes는` 커스텀 애니메이션을 정의하기 위한 공간이라고 생각하시면 됩니다.
- '움찔움찔'이라는 애니메이션을
- 0% 진행했을 때의 CSS,
- 50% 진행했을 때의 CSS,
- 100% 진행했을 때의 CSS를 각각 작성합니다.
- (% 수치는 맘대로 변경, 추가 가능합니다)

2. keyframes를 원하는 곳에 첨부합니다.
```css
.box:hover {
  animation-name : 움찔움찔;
  animation-duration : 1s;
}
```
- animation 속성을 이용하시면 애니메이션을 동작시킬 수 있습니다 .
- 꼭 필요한 속성은 name과 duration이고
- 애니메이션 이름을 name에
- 애니메이션 동작시간을 duration에 넣으면 됩니다.
- 그럼 진짜 마우스 올렸을 때 움찔움찔 애니메이션이 동작합니다. 

3. 애니메이션 세부조정하기
```css
.box:hover {
  animation-name : 움찔움찔;
  animation-duration : 1s;
  animation-timing-function : linear; /*베지어 주기*/
  animation-delay : 1s; /*시작 전 딜레이*/
  animation-iteration-count : 3; /*몇회 반복할것인가*/
  animation-play-state : paused;  /*애니메이션을 멈추고 싶은 경우 자바스크립트로 이거 조정*/
  animation-fill-mode: forwards;  /*애니메이션 끝난 후에 원상복구 하지말고 정지*/
}
```

### margin, width, left, 이런거 말고 transform 쓰라는 이유 

- 크롬같은 웹브라우저들은 html css를 2D 그래픽으로 바꿔주는 간단한 프로그램입니다.
- 근데 html css를 그래픽으로 바꿀 때
- layout 잡기 -> 색칠하기 -> transform 적용하기 순서로 동작합니다.  
- layout이 바뀌면 layout 부터 transform 까지 쭉 다시 렌더링해야하는데
- transform이 바뀌면 transform 부분만 다시 렌더링하면 됩니다. 
- 그래서 뭔가 이동시키고 싶으면 margin 쓰는 것 보다 transform 쓰는게 빠르게 동작합니다.


## CSS Grid 레이아웃

### 간단한 Grid 레이아웃 만들기 

Grid 레이아웃은 말그대로 격자를 만드는 레이아웃입니다. 

```html
<div class="grid-container">
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
</div>
```
```css
.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-template-rows: 100px 100px 100px;
  grid-gap: 10px;
}
```
- 부모<div>에 display : grid를 주면 자식 <div>들은 전부 격자처럼 진열됩니다. 
- grid-template-columns는 격자의 열 너비와 갯수
- grid-template-rows는 격자의 행 높이와 갯수를 설정하는 속성입니다.
- fr이라는 단위는 몇배만큼 차지할지를 나타내는 값입니다.
- 그런데 격자를 왜 만드냐고요? 격자 그려놓으면 레이아웃 만들기 편해질 수 있으니까요. 

### Grid로 레이아웃 만드는 법 1. 자식 div 높이와 폭을 조정하기 

grid로 레이아웃 만드는 법은 두개가 있습니다. 

첫째 방법은 직접 자식에게 명령을 주어, 몇 칸을 차지할지를 정해주는 겁니다. 
```html
<div class="grid-container">
    <div class="grid-nav">헤더</div>
    <div class="grid-sidebar">사이드바</div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
</div>
```
```css
.grid-nav {
  grid-column : 1 / 4;
  grid-row : 2 / 4;
}
```
- 자식 div박스 한개를 조금 크게 키우고 싶다면,
- 자식이 몇개의 컬럼과 row를 차지할지 표시해주시면 됩니다.  
- grid-column은 몇개의 컬럼을 차지할지
- grid-row는 몇개의 row를 차지할지 설정해주는 속성입니다.
- grid-column : 1 / 4 라고 쓰시면 1부터 4까지를 다 차지해라~ 라는 명령인데
- 1부터 4가 뭔소리냐면
- grid-column : 1 / 4 여기서의 숫자는
- grid의 column에 존재하는 세로선들을 의미합니다.
- 왼쪽 세로선부터 1,2,3 ...이라고 생각하면 됩니다. 
- 그럼 grid-column : 1 / 4 이건 세로선 1부터 4까지 차지하라는 말입니다.
- 그래서 박스가 사진처럼 저렇게 늘어납니다.
- grid-row도 비슷하게 동작합니다. 가로선에 번호매겨 생각하면 됩니다. 

### Grid로 레이아웃 만드는 법 2. 자식에게 이름쓰고 부모가 배치하기 

- 자식에 이름을 써놓고 부모가 자식을 자유롭게 배치할 수 있습니다. 
```html
<div class="grid-container">
    <div class="grid-nav">헤더</div>
    <div class="grid-sidebar">사이드바</div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
</div>
```
```css
.grid-nav {
  grid-area: 헤더;
}

.grid-sidebar {
  grid-area: 사이드;
}
```
- grid-area라는 속성을 이용해 자식에게 '헤더' 와 '사이드' 라는 멋진 이름을 붙여줍니다. 

▼ 그리고 부모에게 이런 속성을 하나 추가해줍니다. 
```css
.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-template-rows: 100px 100px 100px;
  grid-gap: 10px;
  grid-template-areas: 
    "헤더 헤더 헤더 헤더"
    "사이드 사이드 . ."
    "사이드 사이드 . ."
}
```
- grid-template-areas라는 속성이 있는데 이건 뭐냐면
- 자식중에 '헤더'라는 이름을 가진 애가 있다면 첫 행에 저렇게 4칸을 차지하게 해주시고
- 자식중에 '사이드바'라는 애가 있으면 둘째 행에 저렇게 2칸을 차지하게 하고
- 셋째 행 2칸도 차지하게 해주세요
- 라고 명령내리는 속성입니다.