# Web - Semantic Web

## 1. 개요

**Semantic Web**

    웹 데이터를 의미론적으로 표현하고 연결하는 개념
    for 컴퓨터가 데이터의 내용과 문잭을 더 효율적으로 이해하고 더 지능적으로 활용

## 2. Semantic in HTML

**HTML Semantic Element**

    기본적인 모양과 기능 이외에 의미를 가지는 HTML 요소
    검색엔진 및 개발자가 웹 페이지의 콘텐츠를 이해하기 쉽게 만들어줌

    페이지 구조화를 위한 대표적인 Semantic Element
     - header
     - nav
     - main
     - article
     - section
     - aside
     - footer

## 3. Semantics in CSS

**OOCSS**

    Object-Oriented CSS : 객체 지향적 접근법을 적용하여 CSS를 구성하는 방법론

**BEM**

    Block Element Modifier : 블록, 요소, 수정자를 사용해 클래스 이름을 구조화하는 방법론

    BEM 구성
      - Block
        - 문단 전체에 적용된 요소 또는 요소를 담고 있는 컨테이너
        - 재사용 가능한 독립적 블록, 가장 바깥쪽 상위요소
        - 재사용을 위해 margin 또는 padding을 적용하지 않음

      - Element
        - block이 포함하고 있는 한 조각
        - 블록을 구성하는 종속적인 하위요소

      - Modifier
        - block 또는 element의 속성

```CSS
.block {}
.block__element {}
.block--modifier {}
```

## **참고**
    의미론적인 마크업의 이점
      - 검색 엔진이 해당 웹 사이트를 분석하기 쉽게 만들어 검색 순위에 영향을 줌
      - 시각 장애 사용자가 스크린 리더기로 웹 페이지를 사용할 때, 추가적으로 도움
    
    클래스 이름이 너무 길어지는 건 아닐까? 
      - 클래스를 만들 때 가장 중요한 부분은 클래스 이름이 무엇을 나타내는지 분명하게 전달할 수 있는가에 대한 것
      - 각각의 명명법은 개인적인 취향에 따라 다르지만, 빠르고 명확한 표기를 우선적으로 해야 함

    OOCSS & BEM의 목적
      - 재사용 가능한 모듈로 분리함으로써 유지보수성과 확장성을 향상
      - 개발자 간의 협력이 향상되어 공통 언어와 코드 이해를 확립