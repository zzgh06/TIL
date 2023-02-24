# Web-The box Model

## 구성요소
CSS BOX Model : 모든 HTML 요소를(사각형) 박스로 표현

    박스에 대한 크기, 여백, 테두리 등의 스타일을 지정하는 디자인 개념
    BOX의 구성
      - Margin : 박스와 다른 요소 사이의 공백, 가장 바깥쪽 영역
      - Border : 콘텐츠와 패딩을 감싸는 테두리 영역
      - Padding : 콘텐츠 주위에 위치하는 공백 영역
      - Content : 콘텐트가 표시되는 영역

    width & height 속성
      - 요소의 너비와 높이를 지정
      - 이때 지정되는 요소의 너비와 높이는 콘텐츠 영역을 대상으로 함

    box-sizing 속성
      - 요소의 너비와 높이를 계산하는 방법을 지정

```css
/* content-box의 경우 콘테츠 값에 패딩 값까지 포함되어 계산되어 원하는 값 이상의 결과가 나타남*/
* {
  box-sizing: content-box;
}
/* 주로 border-box로 지정해줘야 원하는 값만큼 너비와 높이를 지정할 수 있음 */
* {
  box-sizing: border-box;
}
``` 

## 박스타입

Block & Inline

    block 타입 특징
      - 항상 새로운 행으로 나뉨
      - width와 height 속성을 사용하여 너비와 높이를 지정할 수 있음
      - 기본적으로 width 속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간을 모두 차지함
      - 대표적인 block 타입 태그 : h1~6, p, div

    inline 타입 특징
      - 새로운 행으로 나뉘지 않음
      - width와 height 속성을 사용할 수 없음
      - 수직 방향 : padding, margins, borders가 적용되만 다른 요소를 밀어낼 수는 없음
      - 수평 방향 : padding, margins, borders가 적용되어 다른 요소를 밀어낼 수 있음
      - 대표적인 inline 타입 태그 : a, img, span

    display : inline-block
      - inline과 block 요소 사이의 중간 지점을 제공하는 display 값
      - 요소가 줄 바꿈 되는 것을 원하지 않으면서 너비와 높이를 적용하고 싶은 경우에 사용
      - block 요소의 특징을 가짐
        - 너비 및 높이 속성이 준수
        - 패딩, 여백 및 테두리로 인해 다른 요소가 상자에서 밀려남
```css
 .index {
  display: block;
 }
 - block 요소는 기본적으로 부모 요소의 너비 100%를 차지하며, 자식 콘텐츠의 최대 높이를 취한다
 - block 요소의 총 너비와 총 높이는 content + padding + border width/height다
 - block 요소는 서로 margin로 구분된다

.index {
  display: inline;
 }
 - inline 요소는 자체 콘텐츠의 너비와 높이만 차지한다. 그리고 inline 요소는 width 나 height 속성을 지정할 수 없다.
 - 이미지도 인라인 요소이다. 단, 이미지는 다른 inline 요소와 달리  width 나 height로 크기를 조정할 수 있다.
 - 만약 inline 요소의 크기를 제어하려면 block 요소로 변경하거나 inline-block 요소로 설정해주어야 한다
```



