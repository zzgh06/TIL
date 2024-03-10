# React

## 리액트에서 레이아웃 만들 때 쓰는 JSX 문법 3개


### JSX 문법 1. html에 class 넣을 땐 className

- 스타일을 주기 위한 class명을 넣을 때 class=" " 가 아니라 className=" " 입니다.
- 왜냐면 실은 App.js에 짜고 있는건 html이 아니라 JSX라고 부르는 언어이기 때문.
- 원래 리액트환경에서 <div>하나 만들고 싶으면 자바스크립트로 React.createElement('div', null) 

이딴 식으로 어렵게 코드짜야합니다. 
근데 그러면 유저들 다 도망가기 때문에 JSX라는 언어를 대신 사용합니다.



### JSX 문법 2. 변수를 html에 꽂아넣을 때는 {중괄호}

자바스크립트 변수같은 곳에 있던 자료를 html 중간에 꽂아서 보여주고 싶을 때가 많습니다. 

```jsx
function App(){

  let post = '강남 우동 맛집';
  return (
    <div className="App">
      <div className="black-nav">
        <div>블로그임</div>
        <div>여기에 저 변수에 있던거 꽂고 싶으면?</div>
      </div>
    </div>
  )
}
```

- 저 let post 안에 있던 자료를 <div>안에 꽂아넣고 싶으면 어떻게하죠?
- 옛날 자바스크립트 문법을 쓴다면 document.getElementById().innerHTML = ?? 이런 식이었겠지만
- 리액트에서는 더 쉽게 데이터를 꽂아넣을 수 있습니다. 

```jsx
function App(){

  let post = '강남 우동 맛집';
  return (
    <div className="App">
      <div className="black-nav">
        <div>블로그임</div>
        <div>{ post }</div>
      </div>
    </div>
  )
}
```

- 중괄호안에 데이터바인딩하고 싶은 변수명만 담으시면 됩니다.



### JSX 문법 3. html에 style속성 넣고싶으면 

- <div style="color : blue"> 이런걸 넣고 싶으면
- JSX 상에서는 style={ } 안에 { } 자료형으로 집어넣어야합니다. 

```jsx
<div style={ {color : 'blue', fontSize : '30px'} }> 글씨 </div>
```

이렇게 넣어야합니다.

- { 속성명 : '속성값' } 이렇게 넣으면 됩니다. 
- 근데 font-size 처럼 속성명에 대쉬기호를 쓸 수 없습니다.

대쉬기호 대신 모든 단어를 붙여써야합니다. 붙여쓸 땐 앞글자를 대문자로 치환해야합니다. 


## 중요한 데이터는 변수말고 state에 담습니다


### state 만드는 법 

- 이전 강의에서는 그냥 let posts = '어쩌구' 이렇게 변수에 데이터를 저장했었는데
- 리액트에선 변수 말고 state를 만들어서 데이터를 저장해둘 수 있습니다. 
- 이번엔 state를 이용해 데이터를 잠깐 저장해보도록 합시다.

```jsx
import { useState } from 'react';
import './App.css'

function App(){
 
  let [a,b] = useState('남자 코트 추천');
  let posts = '강남 우동 맛집';
  return (
    <div className="App">
      <div className="black-nav">
        <div>개발 blog</div>
      </div>
      <div className="list">
        <h4>글제목</h4>
        <p>2월 17일 발행</p>
        <hr/>
      </div>
    </div>
  )
}
```

- 맨 윗줄에 import {useState} from 'react' 하고 
- 원하는 곳에서 useState('보관할 자료') 쓰면 state에 자료를 잠깐 저장할 수 있습니다.

그리고 저장한 자료를 나중에 쓰고 싶으면

- let [a,b] = useState('남자 코트 추천');
- a 자리에 state 이름을 자유롭게 작명한 다음 나중에 자유롭게 사용하면 됩니다. 



### 변수 말고 state에 데이터 저장해서 쓰는 이유

- state는 변동사항이 생기면 state쓰는 html도 자동으로 재렌더링해줍니다.

```jsx
function App(){
  let post = '강남 우동 맛집'

  return (
    <h4>{ post }</h4>
  )
}
```
`▲ let post 변수에 있던걸 {post} 이렇게 데이터바인딩 해놨다고 가정해봅시다. `

- 근데 갑자기 post 변수에 있던걸 '강남 우동 맛집'  ->  '강남 고기 맛집' 이렇게 바꿨습니다. 
- 그 변경사항도 html에 반영되게 하고 싶으면 어떻게하죠?
- 직접 여러분이 "변수내용 바뀌었으니까 html도 고쳐주세요" 라고 귀찮게 코드짜면 됩니다. 
- 쌩자바스크립트는 원래 그래야함 

```jsx
function App(){
  let [글제목, b] = useState('남자 코트 추천');

  return (
    <h4>{ 글제목 }</h4>
  )
}
```
`▲ 이번엔 state를 하나 만들어서 {글제목} 이렇게 데이터바인딩 해놨다고 가정해봅시다.`

- 근데 갑자기 state에 있던걸 '남자 코트 추천'  -> '여자 코트 추천' 이렇게 바꿨습니다. 
- 그 변경사항도 html에 반영되게 하고 싶으면 어떻게 하냐고요? 
- state자료는 그럴 필요 없습니다. 여러분이 개입 안해도 자동으로 html도 바뀝니다.  
- state는 변경이 일어나면 state가 포함된 html을 자동으로 재렌더링 해줘서 그렇습니다. 


`그럼 뭐가 좋겠습니까`
- 그리고 UI 기능 개발도 매우 편리해지고
- OT강의에서 설명드렸던 사이트처럼 스무스하게 동작하는 것임 


## 버튼에 기능개발을 해보자 & 리액트 state변경하는 법


### 좋아요 버튼 만들기 

버튼을 누르면 좋아요 갯수가 1씩 증가하는 기능을 만들어봅시다.

```jsx
function App(){
  
  let [따봉] = useState(0);
  return (
     <h4> { 글제목[0] } <span>👍</span> { 따봉 }</h4>
  )
}
```
- 그냥 useState() 쓰고 왼쪽에 작명만 잘하면 state 만들기 끝입니다.
- useState() 왼쪽에 작명은 2개 해야하지만 귀찮으면 저처럼 1개만 해도 됩니다. 



### onClick 사용법

```jsx
<div onClick={실행할함수}>
```
`JSX에서는 이렇게 합니다.`

1. Click이 대문자인거
2. {} 중괄호 사용하는거
3. 그냥 코드가 아니라 함수를 넣어야 잘 동작한다는거 
를 기억해주십시오. 



### (매우중요) state 변경하는 법

아무튼 좋아요 버튼 누르면 따봉이라는 state를 +1 해주고 싶으면 코드 어떻게 짜죠? 

그냥 여러분 잘하는 간단한 자바스크립트 문법 쓰면 됩니다. 

```jsx
function App(){
  
  let [ 따봉 ] = useState(0);
  return (
    <h4> { 글제목[0] } <span onClick={ ()=>{ 따봉 = 따봉 + 1 } } >👍</span> { 따봉 }</h4>
  )
}
```
변수에 +1 해주고 싶으면 변수 = 변수+1 해주면 끝입니다.

근데 안타깝게도 저건 변수가 아니라 state입니다. 
`state는 state변경함수를 써서 state를 변경`해야합니다. 

안그러면 큰일남 (html 재렌더링 안됨) 

```jsx
let [ 따봉, 따봉변경 ] = useState(0); 
```
state만들 때 2개까지 작명할 수 있댔는데
두번째 작명한건 state 변경을 도와주는 함수입니다. 

그거 써야 state 변경이 가능합니다. 

사용법은
`따봉변경(새로운state) `
이렇게 쓰면 됩니다. 

왜냐면 state 변경함수는 ( ) 안에 넣은걸로 state를 갈아치워주는 함수라 그렇습니다.

- 따봉변경(1) 이라고 사용하면 따봉이라는 state가 1로 변경됩니다.
- 따봉변경(100) 이라고 사용하면 따봉이라는 state가 100으로 변경됩니다.
- 알겠죠? 따봉변경( 따봉 = 따봉 + 1 ) 이딴거 안됩니다. 깔끔하게 새로운 state만 집어넣으시면 됩니다. 



### 좋아요를 눌렀을 때 따봉이라는 state를 1 증가하려면 

```jsx
function App(){
  
  let [ 따봉, 따봉변경 ] = useState(0);
  return (
      <h4> { 글제목[0] } <span onClick={ ()=>{ 따봉변경(따봉 + 1) } } >👍</span> { 따봉 }</h4>
  )
}
```
따봉이라는 기존 state에 1을 더한 값을 따봉변경 함수에 집어넣었습니다.

그럼 버튼을 누를 때 마다 그 값으로 대체됩니다.

`오늘 배운 내용 정리하면`

1. 클릭시 뭔가 실행하고 싶으면 onClick={함수} 이렇게 이벤트 핸들러를 달아서 사용합니다.
2. state를 변경하시려면 state 변경함수를 꼭 이용하십시오.

state변경함수는 ( ) 안에 입력한걸로 `기존 state를 갈아치워줍니다.`


## array, object state 변경하는 법


### 일단 글수정 버튼 만들기 

```jsx
function App(){
  
  let [글제목, 글제목변경] = useState( ['남자코트 추천', '강남 우동맛집', '파이썬 독학'] );  
  
  return (
      <button onClick={ ()=>{ ??? } }> 수정버튼 </button>
  )
}
```

대충 아무데나 버튼하나 만들고 이거 누르면 첫 글이 수정되는 기능을 만들어봅시다.

저기 물음표안에 뭘 넣어야하죠? 

```jsx
function App(){
  
  let [글제목, 글제목변경] = useState( ['남자코트 추천', '강남 우동맛집', '파이썬 독학'] );  
  
  return (
    <button onClick={ ()=>{ 
      글제목변경(['여자코트 추천', '강남 우동맛집', '파이썬 독학'])
    } }> 수정버튼 </button>
  )
}
```
이러면 숙제 끝입니다. 버튼누르면 첫 글제목 바뀜 

state 변경함수는 ( ) 안에 넣은걸로 기존 state를 갈아치워주니까 저렇게 집어넣으면 됩니다.



### 약간 프로그래머 스타일로 다시만들어보면

지금 코드는 확장성이 부족합니다. 

- [ ] 안에 글이 3개밖에 없어서 망정이지 글이 100개 들어있으면 어쩔 것임, onClick 안의 코드도 매우 길어지겠군요.
- 그러니까 기존 state를 다 복붙하지말고
- 기존 state를 첫 글만 살짝 바꿔서 state변경함수에 집어넣는 식으로 개발해봅시다.

```jsx
function App(){
  
  let [글제목, 글제목변경] = useState( ['남자코트 추천', '강남 우동맛집', '파이썬 독학'] );  
  
  return (
    <button onClick={ ()=>{ 
      let copy = [...글제목];
      copy[0] = '여자코트 추천';
      글제목변경(copy)
    } }> 수정버튼 </button>
  )
}
```

- array, object 자료 다룰 때는 원본 데이터를 직접 조작하는 것 보다는 기존값은 보존해주는 식으로 코드짜는게 좋은관습입니다. 
- (왜냐면 원본 막 바꿔버렸을 때 갑자기 원본이 필요해지면 어쩔 것임)
- 그래서 let copy 같은 변수에다가 기존 array를 복사해놓고 
그걸 조작하는 식으로 코드짜면 조금 더 안전합니다. 



### state 변경함수 동작원리 

- state 변경함수를 쓸 때, 기존state === 신규state 이렇게 먼저 검사해봅니다.
- 그래서 같으면 state 변경을 해주지 않습니다. 
- 그래서 위 코드에서도 글제목변경(copy) 해도
- copy라는 변수가 기존state와 같아서 변경을 안해준 것입니다. 


Q. 잉 copy라는 변수랑 기존 state랑 안에 있는 자료가 다른데 왜 같다고함 
- 기존 state는 '남자코트 추천'
- copy에는 '여자코트 추천'이 들어있지만
- 실은 기존state === copy 비교해보면 같다고 나옵니다.

왜냐고요? 



### array/object 동작원리 

1. 자바스크립트는 array/object 자료를 하나 만들면

예를 들어서 let arr = [1,2,3] 이렇게 만들면 
[1,2,3] 자료는 램이라는 가상공간에 몰래 저장이 되고
let arr 변수엔 그 자료가 어디있는지 가리키는 `화살표만 담겨있습니다.`

2. 그래서 array/object 자료를 복사하면 이상한 일이 일어나는데  

예를 들면 
```jsx
let data1 = [1,2,3];
let data2 = data1;  
```

이런 식으로 사용하면 복사가 됩니다.
- data1에 있던 자료를 data2에 복사한다는 뜻임 

- 그럼 data2 출력해보면 [1,2,3] 이게 잘 나옵니다. 
- 근데 data1과 data2는 각각 [1,2,3]을 별개로 저장하는게 아니라 data1과 data2는 똑같은 값을 공유합니다.
- data1을 변경하면 data2도 자동으로 변경되고 그렇습니다. (충격)

왜냐면 변수에는 화살표만 저장된다니까요
- 그래서 방금 님들 화살표를 복사한 것임 
- 그래서 data1, data2는 똑같은 화살표를 가지게 됩니다. 같은 자료를 가리킴 

3. 그래서 같은 화살표를 가지고 있는 변수끼리는 
등호로 비교해도 똑같다고 나옵니다. 

```jsx
let data1 = [1,2,3];
let data2 = data1;  //복사
data2[0] = 1000;  //data2 내부 변경
console.log(data2 === data1)   //true 나올듯 
```

```jsx
let copy = 글제목;
copy[0] = '여자코트 추천';
글제목변경(copy)
```
- 그래서 아까처럼 이렇게하면
- 컴퓨터는 copy와 기존 글제목 state는 똑같다고 생각하기 때문에 (화살표가 똑같아서)
- state 변경을 안해줍니다. 

```jsx
let copy = [...글제목];
copy[0] = '여자코트 추천';
글제목변경(copy)
```
이러면 잘됩니다. 화살표가 달라지는 문법이라 그렇습니다.

`오늘의 정리`
- 리액트에서 array/object state를 수정하고 싶으면 독립적인 카피본을 만들어서 수정하는게 좋습니다. 

[...기존state] 
{...기존state} 

이렇게 하면 독립적인 카피가 하나 생성됩니다.


## Component : 많은 div들을 한 단어로 줄이고 싶으면


### 복잡한 html을 한 단어로 치환할 수 있는 Component 문법

- 리액트는 긴 HTML을 한 단어로 깔끔하게 치환해서 넣을 수 있는 문법을 제공합니다.
- `Component라고 합니다.`
- 이걸 이용하면 함수 만들듯, 변수 만들듯 HTML을 깔끔하게 한 단어로 치환해서 원하는 곳에 꽂아넣을 수 있습니다.

```jsx
function App (){
  return (
    <div>
      (생략)
      <Modal></Modal>
    </div>
  )
}

function Modal(){
  return (
    <div className="modal">
      <h4>제목</h4>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  )
}
```
▲ 이렇게 하시면 원하는 HTML을 한 단어로 줄일 수 있습니다.

줄이는 법은
1. function을 이용해서 함수를 하나 만들어주고 작명합니다. 
2. 그 함수 안에 return () 안에 축약을 원하는 HTML을 담으면 됩니다.
3. 그럼 원하는 곳에서 <함수명></함수명> 사용하면 아까 축약한 HTML이 등장합니다.

- 이렇게 축약한 HTML 덩어리를 Component 라고 부릅니다. 
- 앞으로 HTML 깔끔하게 축약해서 쓰고싶으면 Component 이런 식으로 많이 만들어 쓰십시오.
- <div> 뭉텅이보다 깔끔하게 <Modal> 이렇게 되어있으니
- 남이 봤을 때 & 미래의 내가 봤을 때 레이아웃을 바로 파악이 가능하니 나중에 관리하기도 좋겠죠?



### Component 만들 때 주의점 

1. component 작명할 땐 영어대문자로 보통 작명합니다.
2. return () 안엔 html 태그들이 평행하게 여러개 들어갈 수 없습니다.
3. function App(){} 내부에서 만들면 안됩니다. 
왜냐면 function App(){} 이것도 다시보니 컴포넌트 생성문법이죠?
component 안에 component 를 만들진 않습니다. 
4. <컴포넌트></컴포넌트> 이렇게 써도 되고 <컴포넌트/> 이렇게 써도 됩니다. 



### arrow function 써도 됩니다

```jsx
function Modal(){
  return ( <div></div> )
}

let Modal = () => {
  return ( <div></div>) 
}
```



### 어떤 HTML들을 Component 만드는게 좋을까

기준은 없습니다만 관습적으로 어떤 부분을 주로 Component화 하냐면

- 사이트에 반복해서 출현하는 HTML 덩어리들은 Component로 만들면 좋습니다.
- 내용이 매우 자주 변경될 것 같은 HTML 부분을 잘라서 Component로 만들면 좋습니다.
- 다른 페이지를 만들고 싶다면 그 페이지의 HTML 내용을 하나의 Component로 만드는게 좋습니다.
- 또는 다른 팀원과 협업할 때 웹페이지를 Component 단위로 나눠서 작업을 분배하기도 합니다. 



### Component의 단점

- 일단 HTML 깔끔하게 쓰려고 Component를 수백개 만들면 그것 만으로도 관리가 힘듭니다.



## 리액트 환경에서 동적인 UI 만드는 법 (모달창만들기)


### 리액트에서 동적인 UI 만드는 step

1. html css로 미리 UI 디자인을 다 해놓고
2. UI의 현재 상태를 state로 저장해두고
3. state에 따라서 UI가 어떻게 보일지 조건문 등으로 작성


### step 1. html css로 미리 디자인해놓기

### step 2. UI의 현재 상태를 state로 저장

state 하나 만들고
거기에 `현재 UI의 상태정보를 저장`해두라는 소리입니다

```jsx
let [modal, setModal] = useState(false);
```

- 저는 modal이라고 작명했습니다.
- 영어로 작명시 state변경함수는 set을 앞에 붙이는게 관습입니다. 

- state에 무슨 자료를 넣어야되냐면 정말 맘대로 하면 됩니다.
- 그냥 현재 모달창의 상태만 표현할 수 있으면 됩니다.
- 모달창은 열림/닫힘 이 두개 상태밖에 없기 때문에 그거 2종류만 표현할 수 있는 자료형이면 됩니다. 

```jsx
let [modal, setModal] = useState('닫힘');
let [modal, setModal] = useState(0);
```
- '닫힘'/'열림
- 0/1
- 아무렇게나 표현해도 상관없습니다. 저는 true/false로 표현해볼 것임
(true false는 참 거짓을 담을 수 있는 boolean이라는 자료형입니다)


### step 3. state에 따라서 UI가 어떻게 보일지 작성

```jsx
function App (){

  let [modal, setModal] = useState(false);
  return (
    저 state가 true면 <Modal></Modal>
    false면 아무것도 보여주지마세요
  )
}
```
- 이렇게 코드짜라는 소리입니다. 
- 프로그래밍할 때 "이 경우엔 이렇게 해주세요~" 라고 코드짜고 싶으면 if 조건문을 사용합니다. 


### JSX에서 조건문 쓰는 법

- 조건문은 if / else 문법을 쓰면 되는데 
- JSX 안에서는 if else 문법을 바로 사용할 수 없습니다.
- 하지만 if 문법 대신 삼항연산자라는건 JSX 중괄호 안에서 사용가능합니다.

```jsx
조건식 ? 조건식 참일 때 실행할 코드 : 조건식 거짓일 때 실행할 코드 
```
- 이렇게 if문 대신 쓸 수 있는 문법이 삼항연산자입니다. 

```jsx
3 > 1 ? console.log('맞음') : console.log('아님') 
```
- 예를 들어 이렇게 쓰면 3 > 1 이게 참이기 때문에 '맞음'이 출력됩니다. 


그래서 아까 모달창으로 돌아가서
저 state가 true면 <Modal></Modal> 보여주고, false면 아무것도 보여주지마세요~
라고 코드짜고 싶으면 어떻게 할까요? 

```jsx
function App (){

  let [modal, setModal] = useState(false);
  return (
    <div className="app">
      (생략)
      {
        modal == true ? <Modal></Modal> : null
      }
    </div>
  )
}
```

이렇게 코드짜면 됩니다. 
null은 그냥 아무 html도 남기기 싫을 때 쓰는 자료입니다. null은 텅 비었다는 뜻임 
이제 3-step 끝입니다.


## map : 많은 div들을 반복문으로 줄이고 싶은 충동이 들 때

- 똑같은 html이 반복적으로 출현하면 
- 반복문을 이용해서 쉽게 똑같은 html을 생성할 수도 있습니다. 
- 안타깝게도 for 반복문은 JSX 중괄호 안에서 사용할 수 없어서 map() 을 대신 사용합니다. 


### 자바스크립트 map 함수 쓰는 법 

- 모든 array 자료 우측엔 map() 함수를 붙일 수 있습니다. 
- 자바스크립트 기본함수 같은건데 용도를 알아봅시다. 

```jsx
var 어레이 = [2,3,4];
어레이.map(function(){
  console.log(1)
});
```
- 기능 1. array에 들어있는 자료갯수만큼 그 안에 있는 코드를 반복실행해줍니다.

```jsx
var 어레이 = [2,3,4];
어레이.map(function(a){
  console.log(a)
});
```
- 기능 2. 콜백함수에 파라미터 아무렇게나 작명하면
    - 그 파라미터는 어레이 안에 있던 모든 자료를 하나씩 출력해줍니다.
    - (그냥 소괄호안에 있는 함수를 콜백함수라고 합니다)
    - 저러면 진짜로 2, 3, 4가 콘솔창에 출력됨 

```jsx
var 어레이 = [2,3,4];
var newArray = 어레이.map(function(a){
  return a * 10
});
console.log(newArray)
```
- 기능3. return 오른쪽에 뭐 적으면 array로 담아줍니다.
    - 그리고 map() 쓴 자리에 남겨줍니다.
    - 그래서 변수에 담아서 출력해봤더니 진짜로 array에 담아주긴 하는군요 
    - newArray는 [20, 30, 40] 이 출력됩니다. 


### JSX 안에서 html을 반복생성하고 싶으면

- 리액트 중괄호안에서 html을 반복생성하고 싶으면 아까 배운 map을 이용해도 됩니다. 

```jsx
function App (){
  return (
    <div>
      { 
        [1,2,3].map(function(){
          return ( <div>안녕</div> )
        }) 
      }
    </div>
  )
}
```
▲ 이렇게 쓰면 <div>안녕</div> 이 3개나 생성됩니다.
진짜인지 미리보기화면에서 확인해봅시다.


### 예전에 만들었던 글제목 3개도 반복문으로 축약 가능할듯

- 지금 우리 프로젝트를 잘 보면
- <div className="list"> 이 부분이 3번이나 반복되고 있습니다.
- 이것도 map 반복문으로 축약하면 코드 양이 더 줄어들지 않을까요.

```jsx
function App (){
  return (
    <div>
      (생략)
      { 
        글제목.map(function(){
          return (
          <div className="list">
            <h4>{ 글제목[0] }</h4>
            <p>2월 18일 발행</p>
          </div> )
        }) 
      }
    </div>
  )
}
```
▲ 이렇게 하면 글제목이 3개 생성됩니다. 
(글제목이라는 state도 array자료라서 map 붙일 수 있습니다)


### 근데 반복된 HTML에 각각 다른 제목을 부여하고 싶다면

- 지금 위의 코드를 잘 보시면 <h4>{ 글제목[0] }</h4> 이라는 것만 3번 반복되고 있습니다. 
- 그래서 같은 제목만 3번 출현하는듯요

- 그게 아니라 반복문이 돌 때마다
<h4>{ 글제목[0] }</h4>
<h4>{ 글제목[1] }</h4>
<h4>{ 글제목[2] }</h4>

- 이런 데이터가 들어가게 만들고 싶으면 어떻게 코드를 수정해야할까요?
- 그것은 아까 map 함수의 사용법을 잘 상기시켜보면 알 수 있습니다.

```jsx
function App (){
  return (
    <div>
      (생략)
      { 
        글제목.map(function(a){
          return (
          <div className="list">
            <h4>{ a }</h4>
            <p>2월 18일 발행</p>
          </div> )
        }) 
      }
    </div>
  )
}
```
▲ 이렇게 하면 각각 다른 글제목이 3개 생성됩니다. 성공 

```jsx
function App (){
  return (
    <div>
      (생략)
      { 
        글제목.map(function(a, i){
          return (
          <div className="list">
            <h4>{ 글제목[i] }</h4>
            <p>2월 18일 발행</p>
          </div> )
        }) 
      }
    </div>
  )
}
```
▲ 실은 이렇게 해도 되는데 왜냐면 

map(function(a, i))
이렇게 파라미터를 2개까지 작명 가능한데

첫째 파라미터 a는 array안에 있던 자료
둘째 파라미터 i는 0부터 1씩 증가하는 정수
가 되어서 그렇습니다.


### 전에 만들었던 따봉기능도 추가해보면

```jsx
function App (){
  return (
    <div>
      (생략)
      { 
        글제목.map(function(a, i){
          return (
          <div className="list">
            <h4 onClick={()=>{ 따봉변경(따봉+1) }}>{ 글제목[i] }</h4>
            <p>2월 18일 발행</p>
          </div> )
        }) 
      }
    </div>
  )
}
```
▲ 반복문 안에 있는 html에 onClick 같은거 추가해도 아무런 문제가 없습니다.

근데 약간 문제가 있는데
아무 글제목이나 클릭하면 따봉갯수가 다 똑같이 증가하는군요

지금 따봉 기록할 state가 하나라서 그렇습니다.

let [따봉, 따봉변경] = useState(0);
let [따봉1, 따봉변경1] = useState(0);
let [따봉2, 따봉변경2] = useState(0);

이렇게 3개 만든 다음에 각각 글마다 집어넣어주면 완성입니다. 
근데 이렇게 만들면 글이 10개가 있을 경우 10줄 작성할 것입니까
그건 좀 귀찮기 때문에 array자료를 활용해도 됩니다.
let [따봉, 따봉변경] = useState([0,0,0]);

이렇게 array를 이용하면 한 변수에 자료 3개를 저장할 수 있으니까 이래도 됩니다. 


(참고) map 반복문으로 반복생성한 html엔 key={i} 이런 속성을 추가해야합니다. 

```jsx
<div className="list" key={i}> 
```
그래야 리액트가 <div>들을 각각 구분할 수 있어서 그렇습니다. 
없으면 워닝띄워줌 


## 자식이 부모의 state 가져다쓰고 싶을 때는 props

- 자식 컴포넌트가 부모 컴포넌트에 있던 state를 쓰고 싶으면 
- 그냥 쓰면 안되고 props로 전송해서 써야합니다. 


### <Modal>안에 글제목 state 가 필요한데

저번에 만든 <Modal> 내부에 글제목 state를 집어넣고 싶으면 어떻게하죠? 

```jsx
function App (){
  let [글제목, 글제목변경] = useState(['남자코트 추천', '강남 우동맛집', '파이썬독학']);
  return (
    <div>
      <Modal></Modal>
    </div>
  )
}

function Modal(){
  return (
    <div className="modal">
      <h4>{ 글제목[0] }</h4>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  )
}
```
▲ 하지만 제대로 실행되지 않습니다.

- '글제목'이라는 변수가 define 되지 않았다고 에러가 뜹니다.
- 왜냐면 글제목이라는 state 변수는 function App()에 있지 function Modal()에 없으니까요.
- 자바스크립트에선 다른 함수에 있는 변수를 마음대로 가져다쓸 수 없습니다. 

- 근데 컴포넌트 2개가 `부모/자식 관계`인 경우엔 가능합니다. 
(다른 컴포넌트 안에 있는 컴포넌트를 자식컴포넌트라고 부릅니다)
- 부모 컴포넌트의 state를 자식 컴포넌트로 전송해줄 수 있습니다. 그럼 자식도 사용가능

- 전송시엔 props라는 문법을 사용합니다. 


### props로 부모 -> 자식 state 전송하는 법 

2개의 step을 따라주시면 됩니다.
1. 자식컴포넌트 사용하는 곳에 가서 <자식컴포넌트 작명={state이름} /> 
2. 자식컴포넌트 만드는 function으로 가서 props라는 파라미터 등록 후 props.작명 사용

- 글제목이라는 부모 컴포넌트의 state를 자식 컴포넌트 <Modal>에 전송해봅시다.

```jsx
function App (){
  let [글제목, 글제목변경] = useState(['남자코트 추천', '강남 우동맛집', '파이썬독학']);
  return (
    <div>
      <Modal 글제목={글제목}></Modal>
    </div>
  )
}

function Modal(props){
  return (
    <div className="modal">
      <h4>{ props.글제목[0] }</h4>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  )
}
```
1. 자식컴포넌트 사용하는 곳에 가서 <자식컴포넌트 작명={state이름} /> 
2. 자식컴포넌트 만드는 곳에 가서 props라는 파라미터 등록 후 props.작명 사용하면 됩니다.

(참고1) props는 <Modal 이런거={이런거}  저런거={저런거}> 이렇게 10개 100개 1000개 무한히 전송이 가능합니다.

(참고2) 꼭 state만 전송할 수 있는건 아닙니다. 
- <Modal 글제목={변수명}> 일반 변수, 함수 전송도 가능하고 
- <Modal 글제목="강남우동맛집"> 일반 문자전송은 중괄호 없이 이렇게 해도 됩니다.

- 자식 → 부모 패륜방향 전송은 불가능합니다.
- 옆집 컴포넌트로의 불륜전송도 불가능합니다. 


### props는 함수 파라미터 문법이랑 똑같습니다

- 함수에 파라미터같은거 왜 넣죠?

- 자바스크립트 기초강의에서는 "함수 하나로 다양한 기능을 사용하기 위해서 쓰는게 파라미터 문법" 이랬습니다.
- props도 실은 파라미터랑 똑같은 문법입니다. 

그래서 이런 식으로 응용도 가능한데 

```jsx
function Modal(props){
  return (
    <div className="modal" style={{ background : 'skyblue' }}>
      <h4>{ props.글제목[0] }</h4>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  )
}
```
갑자기 하늘색 배경의 모달창이 필요하면 저렇게 스타일 넣으면 됩니다. 
근데 이번엔 오렌지색 모달창이 필요하면 어떻게합니까? 
갑자기 노란색 모달창도 필요하면요?

가장 쉬운 방법은
function Modal2() {}
function Modal3() {}
이렇게 컴포넌트를 또 만들어서 각각 배경색을 다르게 만들어도 되겠지만 

내용이 똑같은데 배경색만 다르면 굳이 같은 함수 여러개 만들 필요가 없습니다. 

```jsx
function Modal(props){
  return (
    <div className="modal" style={{ background : props.color }}>
      <h4>{ props.글제목[0] }</h4>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  )
}
```
props.color 이런 식으로 구멍을 뚫어놓으면 이제 컴포넌트 사용할 때

<Modal color={'skyblue'} /> 이러면 하늘색 모달창이 생성됩니다. 
<Modal color={'orange'} /> 이러면 오렌지색 모달창이 생성됩니다.

그래서 비슷한 컴포넌트를 또 만들 필요가 없어지는 것입니다. 


## props를 응용한 상세페이지 만들기

Q. 지금 누른 글제목이 모달창안에 뜨게 하고 싶으면 어떻게 코드를 짜야할까요?

0번 글을 누르면 0번 글제목이 모달창안에 등장하고
1번 글을 누르면 1번 글제목이 모달창안에 등장하고

그런 식으로 동작하게 만들어봅시다. 

### 1. html css로 미리 디자인해놓고 

### 2. 현재 UI의 상태를 state로 만들어두고

```jsx
let [title, setTitle] = useState(0);
```
그래서 저는 function App(){} 안에 state 하나 만들었습니다. 

모달창 안의 글제목은 0번글이 보이거나 1번글이 보이거나 2번글이 보이거나 
이런 상태밖에 없어서 그냥 숫자로 표현하고 싶어서 숫자적어놨습니다. 

### 3. state에 따라서 UI가 어떻게 보일지 작성

```jsx
function App (){
  let [title, setTitle] = useState(0);
  (생략)
}

function Modal(props){
  return (
    <div className="modal">
      <h4>{ 만약에 title == 0이면 0번 글제목 보여주세요~ }</h4>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  )
}
```
- 만약에 title == 0이면 props.글제목[0] 보여주세요~
- 만약에 title == 1이면 props.글제목[1] 보여주세요~

이렇게 코드짜면 기능완성입니다. 

```jsx
function App (){
  let [title, setTitle] = useState(0);
  (생략)
}

function Modal(props){
  return (
    <div className="modal">
      <h4>{ props.글제목[title] }</h4>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  )
}
```
근데 이렇게 해도 될듯요 
그럼 title이 0이면 props.글제목[0] 보이지 않겠습니까 

아무튼 기능완성인데 왜 에러가 나는 것이죠
title이라는 state는 부모가 가진 state라서 
자식이 사용하고 싶으면 props로 전송해야합니다. 전송하십시오 

```jsx
function App (){
  let [title, setTitle] = useState(0);
  (생략)
  {
    modal == true ? <Modal title={title} 글제목={글제목} /> : null
  }
}

function Modal(props){
  return (
    <div className="modal">
      <h4>{ props.글제목[props.title] }</h4>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  )
}
```
props로 전송했습니다. UI 만들기 끝 

이제 스위치를 다 만들어놨기 때문에
title이라는 스위치를 0, 1, 2로 바꿔주면 그 때마다 알맞은 글이 모달창에 표시됩니다.


### 글에 onClick 집어넣으면 끝임 

- 이제 글을 클릭할 때 스위치만 샤샥 바꿔주면 원하는 기능구현 끝입니다.

- 0번 글을 클릭하면 title이라는 스위치를 0으로 바꿔주고
- 1번 글을 클릭하면 title이라는 스위치를 1로 바꿔주고
- 2번 글을 클릭하면 title이라는 스위치를 2로 바꿔주고

그러면 의도한 기능이 완성되겠군요.

```jsx
 function App (){
  return (
    <div>
      { 
        글제목.map(function(a, i){
          return (
          <div className="list">
            <h4 onClick={()=>{ setModal(true); setTitle(i); }}>{ 글제목[i] }</h4>
            <p>2월 18일 발행</p>
          </div> )
        }) 
      }
    </div>
  )
}
```
- 각각 글제목 누르면 setTitle(i) 해달라고 코드짰습니다.
- map 안에서의 i가 뭐였냐면 반복문이 돌 때 마다 0, 1, 2 ... 이렇게 증가하는 정수라고 했습니다.

- 그래서 첫 글제목은 클릭시 setTitle(0) 이 실행될 것이고
- 둘째 글제목은 클릭시 setTitle(1) 이 실행될 것이고
- 셋째 글제목은 클릭시 setTitle(2) 이 실행될 것이고

그렇습니다. 

Q. state를 자식컴포넌트에 만들어버리면 props 전송안해도 되지않나요?
A. 맞습니다. title같은 state도 자식컴포넌트 안에 만들어보면 편할듯요? 
하지만 지금 title이라는 state는 App도 쓰고 Modal도 쓰고 있습니다.
그렇게 다양한 컴포넌트에서 쓰이는 state는
컴포넌트들 중 최고로 높은 부모에게 만들어놔야합니다. 


오늘 요약 :
1. 그래서 UI만드는 3-step 외워주면 알아서 뭐든 만들 수 있습니다.
2. state는 state를 사용하는 컴포넌트 중 최고 부모에 만들어놓아야합니다.