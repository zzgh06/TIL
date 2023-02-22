# Web-Fundamentals of HTML and CSS
 
## Structuring the web

HTML(HyperText Markup Language)

    웹 페이지의 의미와 구조를 정의하는 언어
      - HyperText
        - 웹 페이지를 다른 페이지로 연결하는 링크
        - 참조를 통해 사용자가 한 문세에서 다른 문서로 즉시 접근할 수 있는 텍스트
      - Markup Language
        - 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
        - HTML, Markdown

**Structuring of HTML**
```html
HTML Element
<p>My Cat is very grumpy</p>

  1. <P> : opening tag
  2. </p> : Closing tag 
  3. My Cat is very grumpy : content
  4. <p>My Cat is very grumpy</p> : Element

- 하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성됨
- 닫는 태그는 태그 이름 앞에 슬래시가 포함되며 다는 태그가 없는 태그도 존재

HTML Attributes
<p class="editor-note">My Cat is very grumpy</p>
  class="editor-note" : Attribute

- 규칙
  - 요소 이름 다음에 바로 속성은 요소 이름과 속성 사이에 공백이 있어야 함
  - 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함
  - 속성 값은 열고 닫는 따옴표로 감싸야 함

- 목적
  - 니티내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
  - CSS가 해당 요소를 선택하기 위한 갑으로 활용됨
```

**HTML 문서의 구조**
```html
<!DOCTYPE html> : 해당문서가 html 문서하는 것을 나타냄
<html lang="en"> : 전체 페이지의 콘텐츠를 포함
<head> : HTML 문서에 관련된 설명, 설정 등(사용자에게 보이지 않음)
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title> : 브라우저 탭 및 즐겨찾기시 표시되는 제목으로 사용
</head>
<body> : 페이지의 표시되는 모든 곤텐츠
  
</body>
</html>
```

## Text Structure

HTML Text structure

    HTML의 주요 목적 중 하나는 텍스 구조와 의미를 제공하는 것
```html
<h1>Main Heading</h1>

예를 들어 <h1>은 단순히 텍스트를 크게 만드는 것이 아닌 해당 문서의 최상의 제목이라는 의미를 부여하는 것

대표적인 HTML Text structure
  - Heading & Paragraphs : h1~6, p
  - Lists : ol, ul, li
  - Emphasis & Importance : em, strong
```

## Styling the web

**CSS(Cascading Style Sheet)**

    웹 페이지의 디자인과 레이아웃을 구성하는 언어

```CSS
선택자(Selector)
h1 {
  color : blue; 선언(Declaration)
  font-size : 15px;
    속성       값
}
```

CSS Selectors : HTML 요소를 선택하여 스타일을 적용할 수 있도록 함

    CSS Selectors 종류
    - 기본 선택자
      - 전체(*) 선택자
      - 요소(tag) 선택자
      - 클래스(class) 선택자
      - 아이디(id) 선택자
      - 속성(attr) 선택자

    - 결합자(Combinators)
     - 자손 결합자(" "(space))
     - 자식 결합자(>)

    CSS Selectors 특징
      - 요소 선택자
        - 지정한 모든 태그를 선택

      - 클래스 선택자
        - 주어진 클래스 속성을 가진 모든 요소를 선택

      - 아이디 선택자
        - 주어진 아이디 속성을 가진 요소 선택
        - 문서에 주어진 아이디를 가진 요소가 하나만 있어야함
      
      - 자손 선택자(The" "(space)combinator)
        - 첫번째 요소의 자손 요소들 선택

      - 자식 선택자(The ">"combinator)
        - 첫번째 요소의 직계 자식만 선택

## Cascade & Specificity

**Cascade(계단식) & Specificity(우선순위)**

    동일한 요소에 적용 가능한 같은 스타일을 두 가지 이상 작성 했을 때 어떤 규칙이 이기는지 결정하는 것

    Cascade(계단식)
     - 동일한 우선순위를 같은 규칙이 적용될 때 CSS에서 마지막에 나오는 규칙이 사용
    
    Specificity(우선순위)
     - 선택자 별로 정해진 우선순위 점수에 따라 점수가 높은 규칙이 사용

    우선순위가 높은 순
      1. Importance
       - !important
        - Cascade의 구조를 무시하고 모든 우선순위 점수 계산을 무효화하는 가장 높은 우선순위. 
        - 반드시 필요한 경우가 아니면 절대 사용하지 않은 것을 권장

      2. 우선순위
       - 인라인 스타일 > id 선택자 > class 선택자 > 요소 선택자

      3. 소스코드 순서