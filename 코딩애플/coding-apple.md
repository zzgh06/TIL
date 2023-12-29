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