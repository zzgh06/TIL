# React

## 리액트에서 레이아웃 만들 때 쓰는 JSX 문법 3개


### JSX 문법 1. html에 class 넣을 땐 className

- 스타일을 주기 위한 class명을 넣을 때 class=" " 가 아니라 className=" " 입니다.
- 왜냐면 실은 App.js에 짜고 있는건 html이 아니라 JSX라고 부르는 언어이기 때문.
- 원래 리액트환경에서 `<div>`하나 만들고 싶으면 자바스크립트로 React.createElement('div', null) 

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
3. 그럼 원하는 곳에서 `<함수명></함수명>` 사용하면 아까 축약한 HTML이 등장합니다.

- 이렇게 축약한 HTML 덩어리를 Component 라고 부릅니다. 
- 앞으로 HTML 깔끔하게 축약해서 쓰고싶으면 Component 이런 식으로 많이 만들어 쓰십시오.
- `<div>` 뭉텅이보다 깔끔하게 `<Modal>` 이렇게 되어있으니
- 남이 봤을 때 & 미래의 내가 봤을 때 레이아웃을 바로 파악이 가능하니 나중에 관리하기도 좋겠죠?



### Component 만들 때 주의점 

1. component 작명할 땐 영어대문자로 보통 작명합니다.
2. return () 안엔 html 태그들이 평행하게 여러개 들어갈 수 없습니다.
3. function App(){} 내부에서 만들면 안됩니다. 
왜냐면 function App(){} 이것도 다시보니 컴포넌트 생성문법이죠?
component 안에 component 를 만들진 않습니다. 
4. `<컴포넌트></컴포넌트>` 이렇게 써도 되고 <컴포넌트/> 이렇게 써도 됩니다. 



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
저 state가 true면 `<Modal></Modal>` 보여주고, false면 아무것도 보여주지마세요~
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
▲ 이렇게 쓰면 `<div>안녕</div>` 이 3개나 생성됩니다.
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

- 지금 위의 코드를 잘 보시면 `<h4>{ 글제목[0] }</h4>` 이라는 것만 3번 반복되고 있습니다. 
- 그래서 같은 제목만 3번 출현하는듯요

- 그게 아니라 반복문이 돌 때마다
`<h4>{ 글제목[0] }</h4>`
`<h4>{ 글제목[1] }</h4>`
`<h4>{ 글제목[2] }</h4>`

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
그래야 리액트가 `<div>`들을 각각 구분할 수 있어서 그렇습니다. 
없으면 워닝띄워줌 


## 자식이 부모의 state 가져다쓰고 싶을 때는 props

- 자식 컴포넌트가 부모 컴포넌트에 있던 state를 쓰고 싶으면 
- 그냥 쓰면 안되고 props로 전송해서 써야합니다. 


### `<Modal>`안에 글제목 state 가 필요한데

저번에 만든 `<Modal>` 내부에 글제목 state를 집어넣고 싶으면 어떻게하죠? 

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

- 글제목이라는 부모 컴포넌트의 state를 자식 컴포넌트 `<Modal>`에 전송해봅시다.

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

(참고1) props는 `<Modal 이런거={이런거}  저런거={저런거}>` 이렇게 10개 100개 1000개 무한히 전송이 가능합니다.

(참고2) 꼭 state만 전송할 수 있는건 아닙니다. 
- `<Modal 글제목={변수명}>` 일반 변수, 함수 전송도 가능하고 
- `<Modal 글제목="강남우동맛집">` 일반 문자전송은 중괄호 없이 이렇게 해도 됩니다.

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

`<Modal color={'skyblue'} />` 이러면 하늘색 모달창이 생성됩니다. 
`<Modal color={'orange'} />` 이러면 오렌지색 모달창이 생성됩니다.

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


## input : 사용자가 입력한 글 다루기

### input에 뭔가 입력시 코드를 실행하려면

- 유저가 `<input>`에 뭔가 입력시 코드를 실행해주고 싶을 때가 많습니다.
- 그러고 싶으면 onChange 아니면 onInput 이벤트핸들러를 부착하면 됩니다. 

```jsx
<input onChange={()=>{ 실행할코드 }}/>
```

- onChange, onInput은
- `<input>`에 유저가 뭔가 입력할 때마다 안에 있는 코드를 실행해줍니다. 


### input에 입력한 값 가져오는 법

```jsx
<input onChange={(e)=>{ console.log(e.target.value) }}/>
```

- e라는 파라미터를 추가해주고 
- e.target.value라고 적으면 현재 `<input>`에 입력된 값을 가져올 수 있습니다. 

- 이벤트핸들러에 들어가는 함수에 저렇게 파라미터 e를 추가하면
- e는 이벤트 객체 이런 식으로 부르는데
- 현재 발생하는 이벤트와 관련한 유용한 기능들을 제공하는 일종의 변수입니다.

- e.target 이러면 현재 이벤트가 발생한 곳을 알려주고
- e.preventDefault() 이러면 이벤트 기본 동작을 막아주고
- e.stopPropagation() 이러면 이벤트 버블링도 막아줍니다. 이거 쓰면 좋아요버튼 누를 때 모달창도 떠버리는 버그 해결가능


### 사용자가 input에 입력한 데이터 저장하기 

- 사용자가 input에 입력한 데이터는 state 아니면 변수에 저장해서 쓰는게 일반적입니다. 
- 그래야 편리하기 때문에 일단 저장부터 해봅시다.
- state 배운 기념으로 state를 사용합시다. 

```jsx
function App (){

  let [입력값, 입력값변경] = useState('');
  return (
    <input onChange={(e)=>{ 
      입력값변경(e.target.value) 
      console.log(입력값)
    }} />
  )
}
```

- state를 하나 만들어주고 onChange될 때 마다 state에 e.target.value 넣으라고 코드를 짰습니다. 
- state에 문자를 저장하고 싶은데 일단 기본값을 뭘 넣을지 모르겠으면 따옴표 2개만 치면 됩니다.
- 따옴표 2개는 빈문자를 뜻합니다. 
- 이제 입력값이라는 state를 필요한 곳에서 마음대로 사용하면 되겠습니다. 


## 이미지 넣는 법 & public 폴더 이용하기

리액트는 원래 좀 자유롭습니다. 
이미지 넣는 법도 서너개 있습니다.


### html 안에서 src 폴더의 이미지를 넣고 싶으면 

```jsx
import bg from './bg.png'

function App(){
  return (
    <div>
      <div className="main-bg" style={{ backgroundImage : 'url(' + bg + ')' }}></div>
    </div>
  )
}
```

1. import 작명 from './이미지경로' 한 다음에
2. 이미지경로가 필요한 곳에서 작명한걸 사용하면 됩니다. 
`<img>태그 쓰고싶으면 <img src={bg}/>` 이렇게 써도 보입니다. 
귀찮으면 css파일을 활용합시다. 


### public 폴더의 용도 

- 여러가지 소스코드는 src 폴더에 보관하면 되는데 이미지같은 static 파일의 경우 public 폴더에 보관해도 됩니다.
- 리액트로 개발을 끝내면 build 작업이라는걸 하는데 지금까지 짰던 코드를 한 파일로 압축해주는 작업입니다. 
- src 폴더에 있던 코드와 파일은 다 압축이 되는데 public 폴더에 있는 것들은 그대로 보존해줍니다. 
- 그래서 형태를 보존하고 싶은 파일은 public 폴더에 넣으면 되는데 js 파일은 그럴 일은 거의 없고, 이미지, txt, json 등 수정이 필요없는 static 파일들의 경우엔 public 폴더에 보관해도 상관없습니다.


### public 폴더에 있는 이미지 사용할 땐

```jsx
<img src="/logo192.png" /> 
```
- 그냥 /이미지경로 사용하면 됩니다. 편리하죠?
- 그래서 페이지에 이미지 100장을 넣어야하는 경우 public 폴더에 밀어넣으면 import 100번 안해도 되니 편리합니다. 
- css 파일에서도 /이미지경로 사용하면 됩니다.

```jsx
<img src={process.env.PUBLIC_URL + '/logo192.png'} /> 
```
하지만 권장되는 방식은 이렇게입니다. 
- 왜냐면 리액트로 만든 html 페이지를 배포할 때
- codingapple.com 경로에 배포하면 아무런 문제가 없지만
- codingapple.com/어쩌구/ 경로에 배포하면
- /logo192.png 이렇게 쓰면 파일을 찾을 수 없다고 나올 수도 있습니다. 
- 그래서 /어쩌구/ 를 뜻하는 process.env.PUBLIC_URL 이것도 더해주면 된다고 하는군요.


## 코드 길어지면 import export 하면 됩니다


### export default / import 문법

- 상품정보들을 state로 만들고 싶은데 useState() 안에 넣기엔 너무 깁니다.
- 그럴 땐 다른파일에 보관했다가 import해올 수도 있습니다. 
- 예를 들어서 data.js라는 파일이 있는데 거기 있던 변수를 App.js 에서 가져와서 쓰고 싶으면 

```jsx
(data.js 파일)

let a = 10;
export default a;
```
- export default 변수명; 이렇게 쓰면 원하는 변수를 밖으로 내보낼 수 있습니다.

```jsx
(App.js 파일)

import a from './data.js';
console.log(a)
```

- export 했던 변수를 다른 파일에서 사용하고 싶으면 import 작명 from './파일경로' 하면 됩니다.
- 위 코드에선 a 출력해보면 진짜 10 나옴 

(유의점)
- 변수, 함수, 자료형 전부 export 가능합니다.
- 파일마다 export default 라는 키워드는 하나만 사용가능합니다.
- 파일경로는 ./ 부터 시작해야합니다. 현재경로라는 뜻임 


### export { } / import { } 문법

- 여러개의 변수들을 내보내고싶으면 export default 말고 이런 문법을 씁니다.

```jsx
(data.js 파일)

var name1 = 'Kim';
var name2 = 'Park';
export { name1, name2 }
```
- 그럼 원하는 변수, 함수 등을 여러개 내보낼 수 있습니다.

```jsx
(App.js 파일)

import { name1, name2 } from './data.js';
```
- export {} 이걸로 내보냈으면 가져다가 쓸 때 import {} 문법을 씁니다.

(유의점)
- export { } 했던 것들은 import { } 쓸 때 자유작명이 불가능합니다. export 했던 변수명 그대로 적어야함 

그래서 결론은
- export default / import 쓰거나
- export { } / import { } 쓰거나 둘 중 마음에드는걸 써봅시다. 


## 리액트 라우터 1 : 셋팅이랑 기본 라우팅

`페이지를 나누고 싶으면`

- 반 html css js 사이트는 그냥 html 파일 여러개 만들면 그게 하나의 페이지인데 근데 리액트는 html 파일을 하나만 사용합니다.
- 래서 리액트에선 누가 다른 페이지 요청하면 그냥 내부에 있는 `<div>`를 갈아치워서 보여주면 됩니다. 
- 데 직접 코드짜면 귀찮으니 react-router-dom 이라는 외부 라이브러리 설치해서 구현하는게 일반적이라 그렇게 해봅시다.


### react-router-dom 설치하려면 

외부라이브러리라서 설치 셋팅하는 법은
`react-router-dom 홈페이지` 들어가서 그대로 따라하면 되는데 그냥 알려드리자면 

터미널 열어서 
`npm install react-router-dom@6` 입력해서 설치합니다.

셋팅은 index.js 파일로 가서 

```jsx
import { BrowserRouter } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
      <BrowserRouter>
        <App />
      </BrowserRouter>
  </React.StrictMode>
); 
```
▲ import 어쩌구 해오고
`<BrowserRouter> 이걸로 <App/>` 이걸 감싸면 끝입니다.


### 라우터로 페이지 나누는 법 

다른 웹사이트를 잘 살펴보면 
- `codingapple.com/어쩌구`로 접속하면 A페이지를 보여주고 
- `codingapple.com/저쩌구`로 접속하면 B페이지를 보여줍니다. 

이런 식으로 url 경로마다 다른 페이지를 보여주고 싶으면 이렇게 작성합니다.

```jsx
// (App.js)

import { Routes, Route, Link } from 'react-router-dom'

function App(){
  return (
    (생략)
    <Routes>
      <Route path="/detail" element={ <div>상세페이지임</div> } />
      <Route path="/about" element={ <div>어바웃페이지임</div> } />
    </Routes>
  )
}
```
1. 우선 상단에서 여러가지 컴포넌트를 import 해오고 
2. `<Routes>` 만들고 그 안에 `<Route>`를 작성합니다.
3. `<Route path="/url경로" element={ <보여줄html> } />` 이렇게 작성하면 됩니다. 

```jsx
<Route path="/" element={ <div>메인페이지에서 보여줄거</div> } /> 
```
▲ 이 url 경로는 메인페이지입니다.

Q. 저는 메인페이지 접속시에만 상품목록 보여주고 싶습니다 
A. 그럼 element={ } 안에 상품목록 레이아웃 다 넣으면 되는거 아닙니까 

```jsx
<Route path="/" element={ 
  <>
   <div className="main-bg"></div>
   <div className="container">
     <div className="row">
       { shoes.map((a, i)=>{
         return <Card shoes={shoes[i]} i={i} ></Card>
        })}
      </div>
    </div> 
  </>
} /> 
```
- 이러면 메인페이지 접속시에만 상품목록이 보이고 나머지 /detail 그리고 /about 페이지에선 안보이겠군요. 
- 이렇게 페이지에서 보여줄 html 내용은 마음대로 작성하면 됩니다. 


### 페이지 이동 버튼은

- 유저들은 주소창에 url 입력해서 들어가지 않고 링크타고 들어갑니다. 
- 링크를 만들고 싶으면 react-router-dom에서 Link 컴포넌트 import 해오고 원하는 곳에서 `<Link>` 쓰면 됩니다. 

```jsx
<Link to="/">홈</Link>
<Link to="/detail">상세페이지</Link>
```
이러면 각각 url 경로로 이동하는 링크를 생성할 수 있습니다.


## 리액트 라우터 2 : navigate, nested routes, outlet

- 오늘은 navigate() 함수와 간단한 프로젝트에선 쓸데없는데 가끔 쓰는 nested routes라는 기능을 배워봅시다.


### 리액트 프로젝트 폴더구조는

리액트는 그냥 html 이쁘게 만들어주는 쪼그만한 라이브러리일 뿐입니다. 

- 그래서 여러분이 만들 파일들은 95% 확률로 .js 파일이기 때문에 
- 비슷한 .js 파일끼리 한 폴더에 묶어놓으면 그냥 그게 좋은 폴더구조입니다. 

- 컴포넌트 역할하는 js 파일은 components 폴더에 묶고
- 페이지 역할하는 js 파일은 routes 아니면 pages 폴더에 묶고
- 자주 쓰는 함수가 들어있는 js 파일은 utils 폴더에 묶고
알아서 필요할 때마다 폴더 만들어쓰십시오 

```jsx
import { Routes, Route, Link, useNavigate, Outlet } from 'react-router-dom'
```
우선 상단에서 이런 것들을 import 해옵시다.


### 1. 페이지 이동기능을 만들고 싶으면 useNavigate() 씁니다.

페이지 이동은 Link 써도 된다고 했는데 그게 못생겼으면 이거 쓰면 됩니다. 

```jsx
function App(){
  let navigate = useNavigate()
  
  return (
    (생략)
    <button onClick={()=>{ navigate('/detail') }}>이동버튼</button>
  )
}
```

- useNavigate() 쓰면 그 자리에 유용한 함수가 남습니다. 페이지 이동시켜주는 함수입니다.
- 그럼 이제 navigate('/detail') 이런 코드가 실행되면 /detail 페이지로 이동가능합니다.
- navigate(2) 숫자넣으면 앞으로가기, 뒤로가기 기능개발도 가능합니다.
    - -1 넣으면 뒤로 1번 가기
    - 2 넣으면 앞으로 2번 가기 기능입니다. 


### 2. 404페이지는 

- 유저가 이상한 경로로 접속했을 때 "없는 페이지입니다" 이런거 보여주고 싶으면

```jsx
<Route path="*" element={ <div>없는페이지임</div> } />
```
- `<Route path="*">` 하나 맨 밑에 만들어두면 됩니다.
    - `*` 경로는 모든 경로를 뜻해서
    - 위에 만들어둔 /detail 이런게 아닌 이상한 페이지 접속시 * 경로로 안내해줍니다.


### 3. 서브경로 만들 수 있는 nested routes

- /about/member로 접속하면 회사멤버 소개하는 페이지
- /about/location으로 접속하면 회사위치 소개하는 페이지를 만들고 싶으면 어떻게 합니까. 

```jsx
<Route path="/about/member" element={ <div>멤버들</div> } />
<Route path="/about/location" element={ <div>회사위치</div> } />
```
이렇게 만들어도 되겠지만

```jsx
<Route path="/about" element={ <About/> } >  
  <Route path="member" element={ <div>멤버들</div> } />
  <Route path="location" element={ <div>회사위치</div> } />
</Route>
```
이렇게 만들어도 됩니다.

- `<Route>`안에 `<Route>`를 넣을 수 있는데 이걸 Nested routes 라고 부릅니다.
- 저렇게 쓰면 /about/member로 접속시 `<About> &<div>멤버들</div>` 을 보여줍니다.
- /about/location으로 접속시 `<About> & <div>회사위치</div>` 을 보여줍니다.

Q. <div>는 안보이는데요

실은 위처럼 코드짜면 
- /about/member로 접속시 `<About>안에 <div>멤버들</div>` 을 보여줍니다.
- 그래서 `<About`> 컴포넌트 안에 `<div>`를 어디다 보여줄지 표기해야 잘보여줍니다. 

```jsx
<Route path="/about" element={ <About/> } >  
  <Route path="member" element={ <div>멤버들</div> } />
  <Route path="location" element={ <div>회사위치</div> } />
</Route>
...
function About(){
  return (
    <div>
      <h4>about페이지임</h4>
      <Outlet></Outlet>
    </div>
  )
}
```
- 위에서 import해온 `<Outlet>`은 nested routes안의 element들을 어디에 보여줄지 표기하는 곳입니다. 
- 그래서 이렇게 해두면 /about/member로 접속시 `<Outlet>`자리에 아까의 `<div>` 박스들이 잘 보입니다. 
- 그래서 유사한 서브페이지들이 많이 필요하다면 이렇게 만들어도 됩니다.


## 리액트 라우터 3 : URL 파라미터로 상세페이지 100개 만들기

### 상세페이지에 상품명 넣어봅시다

- 임시 글자들만 들어있으면 밋밋해서 그렇습니다.
- 그래서 shoes 라는 state에 있던 상품정보들을 Detail 컴포넌트에 꽂아넣어봅시다.
- 근데 안타깝게도 shoes는 App 컴포넌트에 있으니 App -> Detail 이렇게 전송하면 쓸 수 있겠군요. 

```jsx
<Route path="/detail" element={ <Detail shoes={shoes}/> }/> 
```
그래서 App.js 안에 <Detail> 쓰는 곳에서 일단 props 전송하고 

```jsx
// (Detail.js)
<div className="container>
  <div className="row">
    <div className="col-md-6">
      <img src="https://codingapple1.github.io/shop/shoes1.jpg" width="100%" />
    </div>
    <div className="col-md-6 mt-4">
      <h4 className="pt-5">{props.shoes[0].title}</h4>
      <p>{props.shoes[0].content}</p>
      <p>{props.shoes[0].price}원</p>
      <button className="btn btn-danger">주문하기</button>
    </div>
  </div> 
</div>
```
- Detail 컴포넌트는 props 파라미터 등록해서 shoes를 자유롭게 사용했습니다.
- props.shoes[0].title 하면 0번째 상품명 나올듯 

Q. 근데 shoes라는 state를 Detail.js 안에서 또 만들면 굳이 props 필요없지 않나요?
A. 나중에 수정이 필요하면 두군데 수정해야해서 귀찮으니 그러면 안됩니다. 

### 상세페이지 여러개 만들려면

- 방금 만든건 0번 상품의 상세페이지일 뿐입니다.
- 상품이 3개니까 상세페이지도 3개 필요할텐데 
- 그럼 이렇게 코드짜면 되겠군요.
    - `<Route>` 쓰면 페이지하나 만들 수 있다고 했으니까...

```jsx
<Route path="/detail/0" element={ <Detail shoes={shoes}/> }/>
<Route path="/detail/1" element={ <Detail shoes={shoes}/> }/>
<Route path="/detail/2" element={ <Detail shoes={shoes}/> }/> 
```
- `<Route>`를 3개 만드는겁니다. 그럼 페이지 3개 완성 
- path 작명시 슬래시 기호도 맘대로 사용가능한데 단어간 띄어쓰기용으로 많이 사용합니다.
- 근데 상품이 100만개라면 `<Route>`도 100만개 만들것입니까?
- 그건 너무 끔찍하기 때문에 다른 방법을 사용합니다


```jsx
<Route path="/detail/:id" element={ <Detail shoes={shoes}/> }/>
```
- 페이지를 여러개 만들고 싶으면 `URL 파라미터`라는 문법을 사용가능합니다. 
- path 작명할 때 `/:어쩌구` 이렇게 사용하면 `"아무 문자"`를 뜻합니다.
- 그래서 위의 `<Route>`는 누군가 주소창에 `/detail/아무거나` 입력했을 때 `<Detail> 컴포넌트` 보여달라는 뜻입니다.

이제 그럼
- /detail/0
- /detail/1
- /detail/2
이렇게 접속해도 `<Detail> 컴포넌트` 잘 보여줄 수 있습니다. 


### 페이지마다 똑같은 내용은 보여주기 싫은데요

- 페이지는 여러개 만들어놨지만 접속해보면 다 똑같은 0번째 상품명만 보여주고 있습니다.
- 왜냐면 0번째 상품명 보여달라고 여러분이 코드짰으니까요.
- 이게 싫으면 이렇게 코드짤 수 있지않을까요. 

```jsx
// (Detail.js)
<h4 className="pt-5">{props.shoes[현재url에입력된숫자].title}</h4>
<p>{props.shoes[0].content}</p>
<p>{props.shoes[0].price}원</p>
<button className="btn btn-danger">주문하기</button>
```
- 0이라고 하드코딩해놨던 자리에
- 현재url파라미터에 입력된숫자를 넣는겁니다.
- 그럼 /detail/1로 접속하면 1번째 상품명을 보여줄 수 있을듯요. 

```jsx
import { useParams } from 'react-router-dom'

function Detail(){
  let {id} = useParams();
  console.log(id)
  
  return (
    <div className="container>
      <div className="row">
        <div className="col-md-6">
          <img src="https://codingapple1.github.io/shop/shoes1.jpg" width="100%" />
        </div>
        <div className="col-md-6 mt-4">
        <h4 className="pt-5">{props.shoes[id].title}</h4>
        <p>{props.shoes[0].content}</p>
        <p>{props.shoes[0].price}원</p>
        <button className="btn btn-danger">주문하기</button>
      </div>
    </div>
  </div>
  )
}
```
- `useParams() 라는 함수`를 상단에서 import 해오면 쓸 수 있는데
- 이거 쓰면 현재 /:url파라미터 자리에 유저가 입력한 값을 가져올 수 있습니다.
- 변수에 저장해서 쓰든가 하면 됩니다.

그래서 위처럼 사용하면
- 누가 /detail/1로 접속하면 id라는 변수에 1이 들어옵니다.
- 누가 /detail/2로 접속하면 id라는 변수에 2가 들어옵니다.
- 그래서 props.shoes[id].title 이러면 아까 의도했던 기능이 완성되겠군요. 
- 페이지마다 각각 다른 상품명이 보입니다.


#### 응용문제 :
Q. 자료의 순서가 변경되면 상세페이지도 고장나는 문제는 어떻게 해결할까요?

상품 순서를 가나다순으로 변경하는 버튼을 만들어버렸다고 가정합시다.
그거 누르면 shoes라는 state 안의 상품이 가나다순으로 정렬됩니다. 
그럼 Grey Yordan이 0번 상품이 되겠군요. 

그럼 평소엔 /detail/0으로 접속하면 0번째 상품을 보여주니까 White and Black 이 뜰텐데
버튼 누른 후엔 /detail/0으로 접속하면 0번째 상품을 보여주니까 Grey Yordan 이 뜨겠군요.

이처럼 상세페이지가 불규칙해지는 문제는 어떻게 해결하면 좋을까요? 

```jsx
// (data.js)
[
  {
    id : 0,
    title : "White and Black",
    content : "Born in France",
    price : 120000
  },
  {둘째상품},
  {셋째상품}
] 
```
- 현재 shoes라는 상품데이터들 안엔 id : 0 이런 영구번호가 있습니다.
- 그럼 현재 /:id 자리에 입력한 값과 영구번호가 같은 상품을 찾아서 데이터바인딩해주면 되는게 아닐까요.
- 자바스크립트엔 .find() 라는 문법이 있는데 이거 쓰면 array 자료안에서 원하는 항목만 찾아올 수 있습니다. 
- array자료.find(()=>{ return 조건식 }) 

이렇게 쓰면 조건식에 맞는 자료를 찾아서 이 자리에 남겨줍니다.

```jsx
// (Detail.js)

function Detail(props){

  let { id } = useParams();
  let 찾은상품 = props.shoes.find(function(x){
    return x.id == id
  });

  return (
    <div className="container">
      <div className="row">
        <div className="col-md-6">
          <img src="https://codingapple1.github.io/shop/shoes1.jpg" width="100%" />
        </div>
        <div className="col-md-6 mt-4">
          <h4 className="pt-5">{찾은상품.title}</h4>
          <p>{찾은상품.content}</p>
          <p>{찾은상품.price}원</p>
          <button className="btn btn-danger">주문하기</button> 
        </div>
      </div>
  </div>  
  )
};

export default Detail 
```
1. find()는 array 뒤에 붙일 수 있으며 return 조건식 적으면 됩니다. 그럼 조건식에 맞는 자료 남겨줌 
2. find() 콜백함수에 파라미터 넣으면 array자료에 있던 자료를 뜻합니다. 전 x라고 작명해봤음 
3. x.id == id 라는 조건식을 써봤습니다. 그럼 array자료.id == url에입력한번호 일 경우 결과를 변수에 담아줍니다. 그럼 {상품1개} 이런거 남을듯요 출력해봅시다. 
4. 마지막으로 찾은 {상품1개}를 html에 데이터바인딩해놨습니다. 


## styled-components 쓰면 CSS 파일 없어도 되는데

컴포넌트가 많은 경우 스타일링을 하다보면 불편함이 생기는데

1. class 만들어놓은걸 까먹고 중복해서 또 만들거나
2. 갑자기 다른 이상한 컴포넌트에 원하지않는 스타일이 적용되거나
3. CSS 파일이 너무 길어져서 수정이 어렵거나

이런 경우가 있습니다.
- 그래서 스타일을 바로 입혀서 컴포넌트를 만들어버릴 수도 있는데
- styled-components 라는 인기 라이브러리를 설치하여 이용하시면 됩니다.


### 일단 설치부터 해봅시다

터미널 열어서 `npm install styled-components` 해주면 됩니다.

```jsx
import styled from 'styled-components'
```
- 그리고 사용하고 싶은 컴포넌트 맨위에 이런걸 import 해와야합니다.
- Detail.js 파일 위에 ▲ 위처럼 입력해서 import 해오십시오. 그럼 셋팅 끝 


### styled-components 기본적인 사용법 

- 이 라이브러리를 이용하면 컴포넌트를 만들 때 스타일을 미리 주입해서 만들 수 있습니다.
- 제가 한번 예시로 padding : 20px인 div박스를 styled-components를 이용해 만들어보겠습니다.

```jsx
import styled from 'styled-components';

let Box = styled.div`
  padding : 20px;
  color : grey
`;
let YellowBtn = styled.button`
  background : yellow;
  color : black;
  padding : 10px;
`;

function Detail(){
  return (
    <div>
      <Box>
        <YellowBtn>버튼임</YellowBtn>
      </Box>
    </div>
  )
}
```
1. `<div>`를 하나 만들고 싶으면 저렇게 `styled.div` 라는걸 사용하면 됩니다. `<p>` 만들려면 `styled.p` 이런 식임 
2. 오른쪽에 `` backtick 기호를 이용해서 CSS 스타일을 넣을 수 있습니다. 
3. 그럼 그 자리에 컴포넌트를 남겨주는데 변수에 저장해서 쓰면 됩니다. 

- 장점1. CSS 파일 오픈할 필요없이 JS 파일에서 바로 스타일넣을 수 있습니다.
- 장점2. 여기 적은 스타일이 다른 JS 파일로 오염되지 않습니다. 원래 그냥 CSS파일은 오염됩니다.
- 장점3. 페이지 로딩시간 단축됩니다.
- 왜냐면 저기 적은 스타일은 html 페이지의 `<style>태그`에 넣어줘서 그렇습니다. 


### 실은 일반 CSS 파일도 오염방지 가능

- 여러분이 App.css 파일을 만들어서 App.js에서 import해서 쓴다고 해도 거기 적은 클래스명들은 Detail.js까지 사용가능합니다. (오염됨)
- 프로젝트 사이즈가 작을 땐 편리하겠지만 사이즈가 커지면 관리하기 힘들어집니다. 
- 그럴 땐 styled-components 써도 되지만 그냥 CSS파일에서도 다른 JS 파일에 간섭하지 않는 '모듈화' 기능을 제공하는데
- `컴포넌트명.module.css` 이렇게 CSS 파일을 작명하면 됩니다.
- 그리고 컴포넌트명.js 파일에서 import 해서 쓰면 그 스타일들은 컴포넌트명.js 파일에만 적용됩니다.


### 추가 문법 : props로 재활용가능

- 여러가지 비슷한 UI가 필요한 경우 어쩌죠?
- 예를 들어 지금 노란 버튼말고 오렌지색 버튼이 필요해지면?
- 물론 예전 강의를 잘 되살려보면 props 이용하면 기존 컴포넌트를 살짝씩 다르게 이용할 수 있다고 했습니다.
- 그래서 여기도 props 문법 지원합니다. 

```jsx
import styled from 'styled-components';

let YellowBtn = styled.button`
  background : ${ props => props.bg };
  color : black;
  padding : 10px;
`;

function Detail(){
  return (
    <div>
        <YellowBtn bg="orange">오렌지색 버튼임</YellowBtn>
        <YellowBtn bg="blue">파란색 버튼임</YellowBtn>
    </div>
  )
}
```
- `${ props => props.bg }` 이게 styled-components 에서의 props 뚫는 문법입니다.
- bg부분에 자유롭게 작명하면되고
- 이제 컴포넌트 쓸 때 bg라는 props를 입력가능합니다.

```jsx
let YellowBtn = styled.button` 
  background : ${ props => props.bg };
  color : ${ props => props.bg == 'blue' ? 'white' : 'black' };
  padding : 10px; 
`; 
```
- 자바스크립트 적는 공간이다보니까 이런 식의 스타일 프로그래밍도 가능합니다. 

### 세상에 장점만 있는게 어딨습니까 

`단점1. JS 파일이 매우 복잡해집니다.`
- 그리고 이 컴포넌트가 styled 인지 아니면 일반 컴포넌트인지 구분도 어렵습니다.

`단점2. JS 파일 간 중복 디자인이 많이 필요하면 어쩌죠?`
- 다른 파일에서 스타일 넣은 것들 import 해와서 쓰면 됩니다.
근데 그럼 CSS파일 쓰는거랑 차이가 없을 수도요

`단점3. CSS 담당하는 디자이너가 있다면 협업시 불편할텐데` 
- 그 사람이 styled-components 문법을 모른다면 
- 그 사람이 CSS로 짠걸 styled-components 문법으로 다시 바꾸거나 그런 작업이 필요하겠군요.

그래서 신기술같은거 도입시엔 언제나 미래를 생각해보아야합니다. 


## Lifecycle과 useEffect 1

### 컴포넌트의 인생 : Lifecycle

- 컴포넌트는 Lifecycle이라는 개념이 있습니다.

컴포넌트는
1. 생성이 될 수도 있고 (전문용어로 mount)
2. 재렌더링이 될 수도 있고 (전문용어로 update)
3. 삭제가 될 수도 있습니다. (전문용어로 unmount)

- 컴포넌트의 인생을 배우는 이유는 컴포넌트 인생 중간중간에 간섭할 수 있기 때문입니다.

간섭이 뭐냐면 그냥 코드실행인데 
- 컴포넌트가 장착이 될 때 특정 코드를 실행할 수도 있고 
- 컴포넌트가 업데이트될 때 특정 코드를 실행할 수도 있다는 겁니다.


### 인생에 간섭하는 방법 

"Detail 컴포넌트 등장 전에 이것좀 해줘"
"Detail 컴포넌트 사라지기 전에 이것좀 해줘"
"Detail 컴포넌트 업데이트 되고나서 이것좀 해줘"
이렇게 코드좀 실행해달라고 간섭할 수 있는데

갈고리를 달아서 코드를 넣어주면 됩니다.
- 그럼 진짜 페이지 장착시, 업데이트시, 제거시 코드실행가능 
- 갈고리는 영어로 hook이라고 합니다. 
- 그래서 저걸 Lifecycle hook 이라고 부릅니다. 


### 요즘 React에서 Lifecycle hook 쓰는 법

```jsx
import {useState, useEffect} from 'react';

function Detail(){

  useEffect(()=>{
    //여기적은 코드는 컴포넌트 로드 & 업데이트 마다 실행됨
    console.log('안녕')
  });
  
  return (생략)
}
```
- 상단에서 useEffect import해오고 
- 콜백함수 추가해서 안에 코드 적으면 이제 그 코드는 컴포넌트가 mount & update시 실행됩니다.
- 그래서 이게 Lifecycle hook 입니다. 


### 근데 useEffect 밖에 적어도 똑같은데요

- 실은 useEffect 바깥에 적어도 똑같이 컴포넌트 mount & update시 실행됩니다. 
- 컴포넌트가 mount & update시 function 안에 있는 코드도 다시 읽고 지나가서 그렇습니다. 

그럼 대체 useEffect 왜 만들어놓은 것이죠 
- 그래서 문법 배우는게 중요한게 아니라 이걸 배웠으면 어떤 상황에서 언제 사용할지도 함께 배워야합니다. 
- 그래야 나중에 "여기서 useEffect 써도 되나요" 이런 초보질문 안함
- useEffect 안에 적은 코드는 html 렌더링 이후에 동작합니다.
- 그럼 이제 useEffect가 뭔가 유용할 것 같지 않습니까 

예를 들어서 굉장히 시간이 오래걸리는 쓸데없는 코드가 필요하다고 가정해봅시다.

```jsx
function Detail(){

  (반복문 10억번 돌리는 코드)
  return (생략)
}
```
▲ 여기에 대충 적으면 반복문 돌리고 나서 하단의 html 보여줌

```jsx
function Detail(){

  useEffect(()=>{
    (반복문 10억번 돌리는 코드)
  });
  
  return (생략)
}
```
▲ useEffect 안에 적으면 html 보여주고 나서 반복문 돌림 

- 이런 식으로 코드의 실행 시점을 조절할 수 있기 때문에
- 조금이라도 html 렌더링이 빠른 사이트를 원하면 쓸데없는 것들은 useEffect 안에 넣어보길 바랍니다. 

- 그래서 이걸 알면 리액트만든 놈이 이 함수를 useEffect라고 작명한 이유도 알 수 있는데 
- 함수안에 이것저것 코드짤 때, 함수의 핵심기능 외에 쓸데없는 기능들을 프로그래밍 용어로 side effect라고 부릅니다.

- 그래서 useEffect도 거기서 따온건데
- 컴포넌트의 핵심 기능은 html 렌더링이라 그거 외의 쓸데없는 기능들은 useEffect 안에 적으라는 소리입니다. 
- 오래걸리는 반복연산, 서버에서 데이터가져오는 작업, 타이머다는거 이런건 useEffect 안에 많이 적습니다.


## Lifecycle과 useEffect 2

### 저번시간 숙제는 : Detail 페이지 후 2초 후에 박스가 사라지게 만들기

동적인 UI 같은거라 그런거 만들 땐 
1. UI 상태를 저장할 state 만들고
2. state에 따라서 UI가 어떻게 보일지 작성하라고 했으니 그거부터 해봅시다. 

```jsx
function Detail(){

  let [alert, setAlert] = useState(true)

  return (
  {
    alert == true
    ? <div className="alert alert-warning">
        2초이내 구매시 할인
      </div>
    : null
  }
  )
}
```

그랬습니다.
- 이제 alert라는 state를 true로 바꾸면 노란박스가 보이고 false로 바꾸면 안보임 
- 그럼 이제 Detail 페이지 접속 후 2초 후에 저걸 안보이게 처리하려면 

useEffect와 setTimeout 이런거 쓰면 될듯요 

```jsx
function Detail(){

  let [alert, setAlert] = useState(true)
  useEffect(()=>{
    setTimeout(()=>{ setAlert(false) }, 2000)
  }, [])

  return (
  {
    alert == true
    ? <div className="alert alert-warning">
        2초이내 구매시 할인
      </div>
    : null
  }
  )
} 
```
이랬더니 2초 후에 잘 동작하는군요. 
근데 [ ] 이거가 갑자기 어디서 나온건지 알아봅시다.


### useEffect에 넣을 수 있는 실행조건 

```jsx
useEffect(()=>{ 실행할코드 }, [count])
```

- useEffect()의 둘째 파라미터로 [ ] 를 넣을 수 있는데 거기에 변수나 state같은 것들을 넣을 수 있습니다.
- 그렇게 하면 [ ]에 있는 변수나 state 가 변할 때만 useEffect 안의 코드를 실행해줍니다.
- 그래서 위의 코드는 count라는 변수가 변할 때만 useEffect 안의 코드가 실행되겠군요. 
- (참고) [ ] 안에 state 여러개 넣을 수 있음

```jsx
useEffect(()=>{ 실행할코드 }, [])
```
- 아무것도 안넣으면 컴포넌트 mount시 (로드시) 1회 실행하고 영영 실행해주지 않습니다.
- 그래서 저번시간 숙제에도 [ ] 이걸 넣어봤습니다. 


### clean up function

- useEffect 동작하기 전에 특정코드를 실행하고 싶으면
- return ()=>{} 안에 넣을 수 있습니다. 

```jsx
useEffect(()=>{ 
  그 다음 실행됨 
  return ()=>{
    여기있는게 먼저실행됨
  }
}, [count])
```

- 그럼 useEffect 안에 있는 코드를 실행하기 전에
- return ()=>{ } 안에 있는 코드를 실행해줍니다. 
- 참고로 저걸 clean up function 이라고 부릅니다. 

`왜 저딴 쓸데없는 기능이 있냐고요?`

여러분 복잡하고 어려운 숙제할 때 책상을 싹 치우고 하면 잘되는 것 처럼 
useEffect 안에 있는 코드를 실행할 때도 싹 치우고 깔끔한 마음으로 실행하는게 좋을 때가 있습니다. 

예를 들면 숙제로 했던 setTimeout 타이머인데
setTimeout() 쓸 때마다 브라우저 안에 타이머가 하나 생깁니다.
근데 useEffect 안에 썼기 때문에 컴포넌트가 mount 될 때 마다 실행됩니다. 

그럼 잘못 코드를 짜면 타이머가 100개 1000개 생길 수도 있겠군요.

나중에 그런 버그를 방지하고 싶으면useEffect에서 타이머 만들기 전에 기존 타이머를 싹 제거하라고 코드를 짜면 되는데
그런거 짤 때 return ()=>{} 안에 짜면 됩니다. 

```jsx
useEffect(()=>{ 
  let a = setTimeout(()=>{ setAlert(false) }, 2000)
  return ()=>{
    clearTimeout(a)
  }
}, [])
```
- 타이머 제거하고 싶으면 clearTimeout(타이머)
- 이렇게 코드짜면 됩니다. 
- 그래서 숙제를 이렇게 하면 좀 더 안전한 코드가 되겠군요.
- 타이머 장착하기 전에 기존 타이머가 있으면 제거를 해줄듯요 

- (참고1) clean up function에는 타이머제거, socket 연결요청제거, ajax요청 중단 이런 코드를 많이 작성합니다.
- (참고2) 컴포넌트 unmount 시에도 clean up function 안에 있던게 1회 실행됩니다.


### 정리

```jsx
useEffect(()=>{ 실행할코드 })
```
1. 이러면 재렌더링마다 코드를 실행가능합니다.

```jsx
useEffect(()=>{ 실행할코드 }, [])
```
2. 이러면 컴포넌트 mount시 (로드시) 1회만 실행가능합니다.

```jsx
useEffect(()=>{ 
  return ()=>{
    실행할코드
  }
})
```
3. 이러면 useEffect 안의 코드 실행 전에 항상 실행됩니다. 

```jsx
useEffect(()=>{ 
  return ()=>{
    실행할코드
  }
}, [])
```
4. 이러면 컴포넌트 unmount시 1회 실행됩니다.

```jsx
useEffect(()=>{ 
  실행할코드
}, [state1])
```
5. 이러면 state1이 변경될 때만 실행됩니다. 


## 리액트에서 서버와 통신하려면 ajax 1

### AJAX란? 

- 서버에 GET, POST 요청을 할 때 새로고침 없이 데이터를 주고받을 수 있게 도와주는 간단한 브라우저 기능을 AJAX라고 합니다. 
- 그거 쓰면 새로고침 없이도 쇼핑몰 상품을 더 가져올 수도 있고 새로고침 없이도 댓글을 서버로 전송할 수도 있고 그런 기능을 만들 수 있는 것임 

AJAX로 GET/POST요청하려면 방법 3개 중 택1 하면 됩니다.
1. XMLHttpRequest라는 옛날 문법 쓰기
2. fetch() 라는 최신 문법 쓰기
3. axios 같은 외부 라이브러리 쓰기 

### AJAX 요청하는 법

- 버튼누르면 제가 만든 서버로 ajax 요청을 해봅시다.
- `https://codingapple1.github.io/shop/data2.json` 이 URL로 GET요청을 하면 상품 3개를 가져와줍니다.

여기로 요청해봅시다. 

```jsx
import axios from 'axios'

function App(){
  return (
    <button onClick={()=>{
      axios.get('https://codingapple1.github.io/shop/data2.json').then((결과)=>{
        console.log(결과.data)
      })
      .catch(()=>{
        console.log('실패함')
      })
    }}>버튼</button>
  )
}
```
1. axios를 쓰려면 상단에서 import해오고
2. axios.get(URL) 이러면 그 URL로 GET요청이 됩니다.
3. 데이터 가져온 결과는 결과.data 안에 들어있습니다. 
그래서 위의 버튼 누르면 서버에서 가져온 데이터가 콘솔창에 출력됩니다. 
4. 인터넷이 안되거나 URL이 이상하면 실패하는데 실패했을 때 실행할 코드는 .catch() 안에 적으면 됩니다.


## 리액트에서 서버와 통신하려면 ajax 2 : post, fetch

### POST요청 하는 법

```jsx
axios.post('URL', {name : 'kim'})
```
- 이거 실행하면 서버로 { name : 'kim' } 자료가 전송됩니다. 
- 완료시 특정 코드를 실행하고 싶으면 이것도 역시 .then() 뒤에 붙이면 됩니다.


### 동시에 AJAX 요청 여러개 날리려면

```jsx
Promise.all( [axios.get('URL1'), axios.get('URL2')] )
```
- 이러면 URL1, URL2로 GET요청을 동시에 해줍니다.
- 둘 다 완료시 특정 코드를 실행하고 싶으면 .then() 뒤에 붙이면 됩니다.


### 원래 서버와 문자자료만 주고받을 수 있음 

object/array 이런거 못주고받습니다.
근데 방금만해도 array 자료 받아온 것 같은데 그건 어떻게 한거냐면 
object/array 자료에 따옴표를 쳐놓으면 됩니다.

"{"name" : "kim"}"
이걸 JSON 이라고 합니다.
JSON은 문자 취급을 받기 때문에 서버와 자유롭게 주고받을 수 있습니다.

그래서 실제로 결과.data 출력해보면 따옴표쳐진 JSON이 나와야하는데
axios 라이브러리는 JSON -> object/array 변환작업을 자동으로 해줘서 
출력해보면 object/array가 나옵니다. 


### 자주묻는 질문 : ajax로 가져온 데이터를 html에 꽂을 때 왜 에러남? 

1. ajax요청으로 데이터를 가져와서 
2. state에 저장하라고 코드를 짜놨고
3. state를 html에 넣어서 보여달라고 `<div> {state.어쩌구} </div>` 

이렇게 코드 짰습니다.
- 잘 될 것 같은데 이 상황에서 state가 텅 비어있다고 에러가 나는 경우가 많습니다.
- 이유는 ajax 요청보다 html 렌더링이 더 빨라서 그럴 수 있습니다. 
- state안에 뭐가 들어있으면 보여달라고 if문 같은걸 추가하거나 그러면 됩니다.


## 리액트에서 탭 UI 만들기

오늘은 쇼핑몰에서 흔히 볼 수 있는 탭 UI를 만들어봅시다. 
버튼 3개와 박스 3개를 미리 만들어놓고 버튼 누를 때 마다 그에 맞는 박스 보여주는게 탭 UI입니다. 
동적인 UI 만드는 법 다 알려드렸는데 그거 가지고 혼자 코드짜보는게 실력향상에 많은 도움이 될듯 합니다. 

1. html css로 디자인 미리 완성해놓고
2. UI의 현재 상태를 저장할 state 하나 만들고
3. state에 따라서 UI가 어떻게 보일지 작성하면 된다고 했습니다. 


### 1. html css로 탭 디자인 미리 완성하기

```jsx
<Nav variant="tabs"  defaultActiveKey="link0">
    <Nav.Item>
      <Nav.Link eventKey="link0">버튼0</Nav.Link>
    </Nav.Item>
    <Nav.Item>
      <Nav.Link eventKey="link1">버튼1</Nav.Link>
    </Nav.Item>
    <Nav.Item>
      <Nav.Link eventKey="link2">버튼2</Nav.Link>
    </Nav.Item>
</Nav>
<div>내용0</div>
<div>내용1</div>
<div>내용2</div> 
```
- 문서 보니까 eventKey 속성은 버튼마다 맘대로 작명하면 된다고 합니다. 
- defaultActiveKey 여기는 페이지 로드시 어떤 버튼에 눌린효과를 줄지 결정하는 부분입니다. 


### 2. UI의 현재 상태를 저장할 state 하나 만들기

```jsx
function Detail(){
  let [탭, 탭변경] = useState(0)
  (생략)
}
```
- 상단에 state 하나 만들었습니다.
- 탭 UI의 상태는 0번 내용이 보이거나 / 1번 내용이 보이거나 / 2번 내용이 보이거나 
- 셋 중 하나기 때문에 저는 0, 1, 2 숫자로 상태를 표현해보겠습니다.


### 3. state에 따라서 UI가 어떻게 보일지 작성

state가 0이면 0번 내용 보여주세요~ 1이면 1번 내용 보여주세요~
이렇게 코드짜면 됩니다. 삼항연산자 이런거 써도 되는데 심심하니까 컴포넌트로 만들어봅시다.

```jsx
function Detail(){
  let [탭, 탭변경] = useState(0)
  
  return (
    <TabContent 탭={탭}/>
  )
}

function TabContent(props){
  if (props.탭 === 0){
    return <div>내용0</div>
  }
  if (props.탭 === 1){
    return <div>내용1</div>
  }
  if (props.탭 === 2){
    return <div>내용2</div>
  }
}
```
- 완성이군요 이제 탭이라는 state를 0, 1, 2로 변경할 때마다 원하는 내용들이 잘 보입니다.

그럼 0번 버튼 누르면 0번 내용 1번 버튼 누르면 1번 내용 2번 버튼 누르면 2번 내용을 보여주고 싶으면 코드 어떻게 짜야합니까?

```jsx
<Nav variant="tabs"  defaultActiveKey="link0">
    <Nav.Item>
      <Nav.Link onClick={()=>{ 탭변경(0) }} eventKey="link0">버튼0</Nav.Link>
    </Nav.Item>
    <Nav.Item>
      <Nav.Link onClick={()=>{ 탭변경(1) }} eventKey="link1">버튼1</Nav.Link>
    </Nav.Item>
    <Nav.Item>
      <Nav.Link onClick={()=>{ 탭변경(2) }} eventKey="link2">버튼2</Nav.Link>
    </Nav.Item>
</Nav>
```
이러면 버튼 누를 때 마다 원하는 탭 내용을 보여줄 수 있습니다. 


### 센스좋으면 if 필요 없을 수도 있습니다

```jsx
function TabContent(props){
  return [ <div>내용0</div>, <div>내용1</div>, <div>내용2</div> ][props.탭]
}
```
이래도 될듯요, 왜냐면 props.탭이 0이면 저 긴 array자료에서 0번 자료를 꺼내줄테니까요. 


### 참고사항 : props 쉽게 쓰고 싶으면

```jsx
function TabContent({탭}){
  return [ <div>내용0</div>, <div>내용1</div>, <div>내용2</div> ][탭]
}
```
- 자식컴포넌트에서 props라고 파라미터를 하나만 작명하는게 아니라
- {state1이름, state2이름 ... }
- 이렇게 작성하면 props.state1이름 이렇게 쓸 필요가 없어집니다. 


### 멋있게 컴포넌트 전환 애니메이션 주는 법 (transition)

- 컴포넌트 등장, 퇴장 애니메이션같은게 필요하면 
- 라이브러리설치해서 써도 되겠지만 CSS 잘하면 간단한건 알아서 개발가능합니다.
- 옛날에 배웠던 useEffect 이런거 활용하면 되는데 
- CSS 애니메이션 처음인 분들을 위해 오늘도 정확한 개발스텝을 알려드립니다. 

`애니메이션 만들고 싶으면` 
1. 애니메이션 동작 전 스타일을 담을 className 만들기 
2. 애니메이션 동작 후 스타일을 담을 className 만들기 
3. transition 속성도 추가
4. 원할 때 2번 탈부착

이게 끝입니다. CSS 잘쓰면 모든 애니메이션 알아서 만들 수 있습니다. 
저번에 만들었던 탭의 내용이 서서히 등장하는 fade in 애니메이션을 만들어봅시다.


### 1. 애니메이션 동작 전 2. 애니메이션 동작 후 className 만들기 

```css
.start {
  opacity : 0
}
.end {
  opacity : 1;
}
```
CSS 파일 열어서 이런거 추가하면 됩니다. 
애니메이션 동작 전엔 투명도가 0, 동작 후엔 투명도가 1이 되면 좋을듯요 


### 3. transition 추가

```css
.start {
  opacity : 0
}
.end {
  opacity : 1;
  transition : opacity 0.5s;
}
```
- transition은 "해당 속성이 변할 때 서서히 변경해주세요~" 라는 뜻입니다. 
- 그럼 이제 원하는 <div> 요소에 start 넣어두고 end 를 탈부착할 때 마다 fade in이 됩니다. 

```jsx
function TabContent({탭}){

  return (
    <div className="start end">
      { [<div>내용0</div>, <div>내용1</div>, <div>내용2</div>][탭] }
    </div>
  )
}
```
▲ end라는 className 떼었다가 붙여보면 진짜로 애니메이션이 동작합니다. 
안보이면 저장을 안했거나 CSS파일이 import 안되어있는 것임 

### 4. 원할 때 end 부착

- `버튼누르면 end 부착하라고 코드`짜려면 코드를 3번이나 짜야할듯요 버튼이 3개니까요.
- 이제 "버튼을 누를 때 마다 end를 저기 부착해주세요" 라고 코드짜면 애니메이션 동작합니다.
- 그게 싫으면 `useEffect` 이런거 활용해봐도 됩니다.
- useEffect 쓰면 `특정 state 아니면 props가 변할 때` 마다 코드실행이 가능하다고 했습니다. 
- 그래서 `"탭이라는 state가 변할 때 end를 저기 부착해주세요"` 라고 코드짜도 같을듯 

```jsx
function TabContent({탭}){

  let [fade, setFade] = useState('')

  useEffect(()=>{
    setFade('end')
  }, [탭])

  return (
    <div className={'start ' + fade}>
      { [<div>내용0</div>, <div>내용1</div>, <div>내용2</div>][탭] }
    </div>
  )
}
```

탭이라는게 변할 때 end를 저기 부착하고 싶으면 동적인 UI 만드는 법 떠올리면 됩니다. 
- fade라는 state 하나 만들고 
- state에 따라서 className이 어떻게 보일지 작성하고
- 원할 때 fade를 변경했습니다.

이제 탭이라는 state가 변할 때 마다 fade라는 state가 'end'로 변하고 
그럼 lassName="start end" 이렇게 변합니다.  
이제 버튼 막 누르면 end가 부착되니까 애니메이션이 잘 보이겠군요 

Q. 안보이는데요
내 의도와 다르게 동작하는건 개발자도구에서 검사해보면 됩니다. 
end라는 클래스명을 부착하는게 맞긴 맞는데 
실은 떼었다가 붙여야 애니메이션이 보입니다. end를 떼었다가 붙여보셈 

```jsx
function TabContent({탭}){

  let [fade, setFade] = useState('')

  useEffect(()=>{
    setTImeout(()=>{ setFade('end') }, 100)
  return ()=>{
    setFade('')
  }
  }, [탭])

  return (
    <div className={'start ' + fade}>
      { [<div>내용0</div>, <div>내용1</div>, <div>내용2</div>][탭] }
    </div>
  )
}
```
▲ 떼었다가 부착하라고 코드짜봤습니다.
clean up function 안에 fade라는 state를 공백으로 바꾸라고 했으니
useEffect 실행 전엔 'end'가 ' ' 이걸로 바뀝니다.

Q. setTimeout 왜 씁니까
- 리액트 18버전 이상부터는 automatic batch 라는 기능이 생겼습니다.
- state 변경함수들이 연달아서 여러개 처리되어야한다면 
- state 변경함수를 다 처리하고 마지막에 한 번만 재렌더링됩니다. 
- 그래서 'end' 로 변경하는거랑 ' ' 이걸로 변경하는거랑 약간 시간차를 뒀습니다.
- 찾아보면 setTimeout 말고 flushSync() 이런거 써도 될 것 같기도 합니다. automatic batching을 막아줍니다.


## props 싫으면 Context API 써도 됩니다

`App에 있던 state를 TabContent 컴포넌트에서 사용하고 싶어지면 어떻게 코드짜야하죠?`
- App -> Detail -> TabContent 이렇게 props를 2번 전송해주면 됩니다.
- 이게 귀찮으면 Context API 문법을 쓰거나 Redux 같은 외부 라이브러리 쓰면 되는데 오늘은 전자를 알아봅시다.


### Context API 문법으로 props 없이 state 공유하기

재고라는 state를 App 컴포넌트에 만들어봅시다.
이걸 TabContent라는 자식컴포넌트에서 쓰고싶다고 가정해봅시다.
Context API 문법을 쓰면 props 전송없이도 TabContent 컴포넌트가 쓸 수 있는데 이거 쓰려면 일단 셋팅부터 해야합니다.

```jsx
// (App.js)
export let Context1 = React.createContext();

function App(){
  let [재고, 재고변경] = useState([10,11,12]);

  (생략)
}
```
▲ 1. 일단 createContext() 함수를 가져와서 context를 하나 만들어줍니다.
context를 쉽게 비유해서 설명하자면 state 보관함입니다.

```jsx
export let Context1 = React.createContext();

function App(){
  let [재고, 재고변경] = useState([10,11,12]);

  return (
    <Context1.Provider value={ {재고, shoes} }>
      <Detail shoes={shoes}/>
    </Context1.Provider>
    
  )
}
```
▲ 2. 아까만든 Context1로 원하는 곳을 감싸고 공유를 원하는 state를 value 안에 다 적으면 됩니다.
그럼 이제 Context1로 감싼 모든 컴포넌트와 그 자식컴포넌트는 state를 props 전송없이 직접 사용가능합니다.


### Context 안에 있던 state 사용하려면

1. 만들어둔 Context를 import 해옵니다.
2. useContext() 안에 넣습니다. 

그럼 이제 그 자리에 공유했던 state가 전부 남는데 그거 쓰면 됩니다. 

```jsx
// (Detail.js)

import {useState, useEffect, useContext} from 'react';
import {Context1} from './../App.js';

function Detail(){
  let {재고} = useContext(Context1)

  return (
    <div>{재고}</div>
  )
}
```
▲ 예를 들어서 Detail 컴포넌트에서 Context에 있던 state를 꺼내 쓰려면
1. Context1을 import 하고 
2. useContext() 안에 담으면 됩니다. Context 해체해주는 함수임

그럼 그 자리에 공유했던 모든 state가 남습니다.
변수에 담아서 가져다쓰거나 하면 됩니다. 

심지어 Detail 안에 있는 모든 자식컴포넌트도 useContext() 쓰면 자유롭게 재고 state를 사용가능합니다.

TabContent 안에서 실험해봅시다.


### Context API 단점

실은 잘 안쓰는 이유는 
1. state 변경시 쓸데없는 컴포넌트까지 전부 재렌더링이 되고 
2. useContext() 를 쓰고 있는 컴포넌트는 나중에 다른 파일에서 재사용할 때 Context를 import 하는게 귀찮아질 수 있습니다.

그래서 이것 보다는 redux 같은 외부라이브러리를 많이들 사용합니다.


## 장바구니 페이지 만들기 & Redux 1 : Redux Toolkit 설치

- redux toolkit 설치시 `npm install @reduxjs/toolkit@1.8.1 react-redux` 입력합시다.

### 장바구니 페이지만들기

- 페이지하나 필요하면 어떻게 해야합니까.
- 라우터 쓰면 되는 것 아니겠습니까 그래서 `App.js의 <Routes>` 쓰던 곳을 찾아가봅시다.

```jsx
<Route path="/cart" element={ <Cart/> } /> 
```
- 그리고 <Route>를 하나 추가했습니다. 누가 /cart 로 접속하면 <Cart> 컴포넌트를 보여주기로 했습니다.


### Redux 쓰면 뭐가 좋냐면

- Redux는 props 없이 state를 공유할 수 있게 도와주는 라이브러리입니다. 

- 이거 설치하면 `js 파일 하나에 state들을 보관`할 수 있는데 그걸 모든 컴포넌트가 직접 꺼내쓸 수 있습니다. 
- 그래서 귀찮은 props 전송이 필요없어집니다. 
- 컴포넌트가 많아질 수록 좋겠군요. 
- 그래서 사이트가 커지면 쓸 수 밖에 없어서 개발자 구인시에도 redux같은 라이브러리 숙련도를 대부분 요구합니다. 


### Redux 설치는 

`npm install @reduxjs/toolkit@1.8.1 react-redux `
터미널에 입력하면됩니다. 

참고로 redux toolkit이라는 라이브러리를 설치할 건데 redux의 개선버전이라고 보면 됩니다. 문법이 좀 더 쉬워짐 

근데 설치하기 전에 package.json 파일을 열어서
"react"
"react-dom" 
항목의 버전을 확인합시다.
이거 두개가 18.1.x 이상이면 사용가능합니다. 

그게 아니면 직접 두개를 18.1.0 이렇게 수정한 다음 파일저장하고
터미널에서 npm install 누르면 됩니다. 그럼 이제 redux 설치가능


### Redux 셋팅은 

```jsx
import { configureStore } from '@reduxjs/toolkit'

export default configureStore({
  reducer: { }
}) 
```
1. 아무데나 store.js 파일을 만들어서 위 코드를 복붙해줍니다. 
    - 저는 src 폴더 안에 만들었음 
    - 이게 뭐냐면 아까 말했던 state들을 보관하는 파일입니다. 

```jsx
import { Provider } from "react-redux";
import store from './store.js'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Provider store={store}>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </Provider>
  </React.StrictMode>
); 
```
2. index.js 파일가서 Provider 라는 컴포넌트와 아까 작성한 파일을 import 해옵니다. 
    - 그리고 밑에 <Provider store={import해온거}> 이걸로 <App/> 을 감싸면 됩니다. 
    - 그럼 이제 <App>과 그 모든 자식컴포넌트들은 store.js에 있던 state를 맘대로 꺼내쓸 수 있습니다.


## Redux 2 : store에 state 보관하고 쓰는 법 

- 뭐 배우기 전에 항상 이걸 왜 쓰는지 생각해보는게 중요합니다. 그래야 나중에 "여기서 Redux 쓰는게 맞나요?" 이런 질문 안하고 알아서 코드 잘짬 
- Redux 라이브러리 왜 쓴다고 했냐면
- state를 Redux store에 보관해둘 수 있는데 모든 컴포넌트가 거기 있던 state를 직접 꺼내쓸 수 있어서
- props 없어도 편리하게 state 공유가 가능하다고 했습니다. 
- 오늘은 Redux store에 state 보관하는 법을 알아봅시다


### Redux store에 state 보관하는 법 

저번시간에 만들어둔 store.js 파일 열어서 이렇게 코드짜면 state 하나 만들 수 있습니다.
step 1. createSlice( ) 로 state 만들고
step 2. configureStore( ) 안에 등록하면 됩니다.

```jsx
import { configureStore, createSlice } from '@reduxjs/toolkit'

let user = createSlice({
  name : 'user',
  initialState : 'kim'
})

export default configureStore({
  reducer: {
    user : user.reducer
  }
}) 
```
1. createSlice( ) 상단에서 import 해온 다음에 
    - { name : 'state이름', initialState : 'state값' } 이거 넣으면 state 하나 생성가능합니다. 
    - (createSlice( ) 는 useState( ) 와 용도가 비슷하다고 보면 됩니다)

2. state 등록은 configureStore( ) 안에 하면 됩니다.
    - { 작명 : createSlice만든거.reducer } 이러면 등록 끝입니다. 
    - 여기 등록한 state는 모든 컴포넌트가 자유롭게 사용가능합니다. 


### Redux store에 있던 state 가져다쓰는 법

```jsx
// (Cart.js)

import { useSelector } from "react-redux"

function Cart(){
  let a = useSelector((state) => { return state } )
  console.log(a)

  return (생략)
}
```
- 아무 컴포넌트에서 useSelector((state) => { return state } ) 쓰면 store에 있던 모든 state가 그 자리에 남습니다. 
- 변수에 저장해서 진짜로 출력해보십시오. 
- { user : 'kim' } 이런거 출력될듯


### Redux 편하니까 맨날 쓰면 되겠네요

- 간단한거 만들 때
- 컴포넌트가 몇개 없을 때 
- 이럴 땐 그냥 props 쓰는게 더 코드가 짧습니다. 


## Redux 3 : store의 state 변경하는 법

Redux의 state를 변경하고 싶으면 변경하는 법이 따로 있습니다. 
1. store.js에 state변경해주는 함수부터 만들고
2. export 해두고
3. 필요할 때 import 해서 쓰면 되는데 dispatch() 로 감싸서 써야합니다.

### store의 state 변경하는 법 

큰 그림부터 그려드리면 
    - state 수정해주는 함수부터 store.js에 만들어두고 그걸 컴포넌트에서 원할 때 실행하는 식으로 코드를 짭니다. 
    - 버튼누르면 예전에 'kim' 이라고 저장해놓은걸 'john kim' 으로 수정하고 싶으면 어떻게 해야할지 알아봅시다. 
    - 정확한 step으로 딱딱 알려드려야 혼자 코드짤 때 편하니까 step을 알려드리면 


1. store.js 안에 state 수정해주는 함수부터 만듭니다. 
```jsx
let user = createSlice({
  name : 'user',
  initialState : 'kim',
  reducers : {
    changeName(state){
      return 'john ' + state
    }
  }
}) 
```
slice 안에 reducers : { } 열고 거기 안에 함수 만들면 됩니다.
- 함수 작명 맘대로 합니다.
- 파라미터 하나 작명하면 그건 기존 state가 됩니다.
- return 우측에 새로운 state 입력하면 그걸로 기존 state를 갈아치워줍니다. 
- 이제 changeName() 쓸 때 마다 'kim' -> 'john kim' 이렇게 변할듯 


2. 다른 곳에서 쓰기좋게 export 해둡니다.
```jsx
export let { changeName } = user.actions 
```
- 이런 코드 store.js 밑에 추가하면 됩니다.
- slice이름.actions 라고 적으면 state 변경함수가 전부 그 자리에 출력됩니다.
- 그걸 변수에 저장했다가 export 하라는 뜻일 뿐임 


3. 원할 때 import 해서 사용합니다. 근데 dispatch() 로 감싸서 써야함 

예를 들어서 Cart.js 에서 버튼같은거 하나 만들고
그 버튼 누르면 state를 'kim' -> 'john kim' 이렇게 변경하고 싶으면

```jsx
// (Cart.js)

import { useDispatch, useSelector } from "react-redux"
import { changeName } from "./../store.js"

(생략) 

<button onClick={()=>{
  dispatch(changeName())
}}>버튼임</button> 
```
이렇게 코드짜면 됩니다. 
- store.js에서 원하는 state변경함수 가져오면 되고 
- useDispatch 라는 것도 라이브러리에서 가져옵니다.
- 그리고 dispatch( state변경함수() ) 이렇게 감싸서 실행하면 state 진짜로 변경됩니다.


### 그지같고 복잡한데요

store안에 있는 state를 수정하고 싶으면 
- state 수정해주는 함수를 store.js에 만들어두고 
- 컴포넌트는 그걸 부르기만 하는 식으로 state 수정하게 되어있습니다. 

Q. 왜 이렇게 복잡하고 그지같나요?
Redux 만든 사람이 정한 문법일 뿐이라 Redux 만든사람에게 뭐라하면 됩니다. 

Q. 컴포넌트에서 state 직접 수정하면 편하지 않나요?
그럼 당장은 편한데 나중에 프로젝트가 커지면 심각한 단점이 있을 수 있습니다. 

- 컴포넌트 100개에서 직접 'kim' 이라는 state 변경하다가 갑자기 'kim'이 123이 되어버리는 버그가 발생하면 범인 찾으려고 컴포넌트 100개를 다 뒤져야합니다. 
- 근데 state 수정함수를 store.js에 미리 만들어두고 컴포넌트는 그거 실행해달라고 부탁만 하는 식으로 코드를 짜놓으면 'kim'이 123이 되어버리는 버그가 발생했을 때 범인찾기가 수월합니다.
- 범인은 무조건 store.js에 있으니까요. (수정함수를 잘 만들어놨다면)


## Redux 4 : state가 object/array일 경우 변경하는 법

store에 저장된 state가 array, object 자료인 경우 state 변경을 좀 쉽게 편리하게 할 수 있는데 오늘은 그 방법을 알아봅시다. 


### redux state가 array/object인 경우 변경하려면 

대충 {name : 'kim', age : 20} 이렇게 생긴 자료를 state로 만들어봅시다. 
근데 저기서 'kim' -> 'park' 이렇게 변경하고 싶으면 state 변경함수 어떻게 만들어야할까요? 

```jsx
let user = createSlice({
  name : 'user',
  initialState : {name : 'kim', age : 20},
  reducers : {
    changeName(state){
      return {name : 'park', age : 20}
    }
  }
}) 
```
- 당연히 저렇게 쓰면 changeName() 사용시 변경됩니다.
- return 오른쪽에 적은걸로 기존 state를 갈아치워주니까요. 

```jsx
let user = createSlice({
  name : 'user',
  initialState : {name : 'kim', age : 20},
  reducers : {
    changeName(state){
      state.name = 'park'
    }
  }
}) 
```
- 근데 state를 직접 수정하라고해도 변경 잘 됩니다. 
- state를 직접 수정하는 문법을 사용해도 잘 변경되는 이유는
- `Immer.js 라이브러리`가 state 사본을 하나 더 생성해준 덕분인데 Redux 설치하면 딸려와서 그렇습니다.

- 그래서 결론은 array/object 자료의 경우 state변경은 state를 직접 수정해버려도 잘 되니까 직접 수정하십시오. 
- (참고) 그래서 state 만들 때 문자나 숫자하나만 필요해도 redux에선 일부러 object 아니면 array에 담는 경우도 있습니다. 수정이 편리해지니까요. 


### state 변경함수가 여러개 필요하면

함수는 파라미터문법 이용하면 비슷한 함수 여러개 만들 필요가 없다고 했습니다. 
state변경함수에도 파라미터문법 사용가능함 

```jsx
let user = createSlice({
  name : 'user',
  initialState : {name : 'kim', age : 20},
  reducers : {
    increase(state, a){
      state.age += a.payload
    }
  }
}) 
```
state변경함수의 둘째 파라미터를 작명하면 이제 
increase(10)
increase(100)
이런 식으로 파라미터입력을 해서 함수사용이 가능합니다.
파라미터자리에 넣은 자료들은 a.payload 하면 나옵니다.

그래서 위처럼 코드 작성해놓으면
increase(10) 이거 실행하면 +10 됩니다.
increase(100) 이거 실행하면 +100 됩니다. 

여기서도 파라미터문법 이용하면 비슷한 함수들은 여러개 만들 필요없습니다. 

(참고)
- a 말고 action 이런 식으로 작명 많이 합니다. 
- action.type 하면 state변경함수 이름이 나오고
- action.payload 하면 파라미터가 나옵니다. 


### 파일 분할은

- 코드가 길어서 보기싫으면 코드 덩어리들을 다른 파일로 빼면 됩니다. 
- 그래서 강의에선 let user 변수와 state변경함수 export 부분을
- store폴더/userSlice.js로 빼봤습니다.
- import export 문법 배웠으면 알아서 잘할 수 있겠군요. 


## localStorage로 만드는 최근 본 상품 기능 1

- 새로고침하면 모든 state 데이터는 리셋됩니다.
- 왜냐면 새로고침하면 브라우저는 html css js 파일들을 첨부터 다시 읽기 때문입니다.
- 이게 싫다면 state 데이터를 서버로 보내서 DB에 저장하거나 하면 됩니다.
- 내가 서버나 DB 지식이 없다면 localStorage를 이용해도 됩니다.

### localStorage 문법 

그냥 js 파일 아무데서나 다음 문법을 쓰면 localStorage에 데이터 입출력할 수 있습니다.

```jsx
localStorage.setItem('데이터이름', '데이터');
localStorage.getItem('데이터이름');
localStorage.removeItem('데이터이름')
```
차례로 추가, 읽기, 삭제 문법입니다.
진짜 저장되었는지 application 탭에서 확인해보십시오.


### localStorage에 array/object 자료를 저장하려면

- 문자만 저장할 수 있는 공간이라 array/object를 바로 저장할 수는 없습니다. 
- 강제로 저장해보면 문자로 바꿔서 저장해주는데 그럼 array/object 자료가 깨져서 저장됩니다.
- 그래서 편법이 하나 있는데 array/object -> JSON 이렇게 변환해서 저장하면 됩니다. 
- JSON은 문자취급을 받아서 그렇습니다. 
- JSON은 그냥 따옴표친 array/object 자료입니다. 

```jsx
localStorage.setItem('obj', JSON.stringify({name:'kim'}) );
```
- JSON.stringify() 라는 함수에 array/object를 집어넣으면 그 자리에 JSON으로 변환된걸 남겨줍니다.
- 그래서 위처럼 코드짜면 저장가능합니다. 
- "{"name":"kim"}" 이런거 저장될듯 

```jsx
var a = localStorage.getItem('obj');
var b = JSON.parse(a)
```
- 당연히 데이터를 다시 꺼내면 JSON이 나옵니다. 
- JSON -> array/object 변환하고 싶으면 JSON.parse()를 쓰면 되겠습니다.


### 최근 본 상품 UI 기능 만들기 

누가 내 사이트로 접속시 localStorage에 [ ] 가 하나 있어야 자료 추가같은게 쉬울 것 같습니다. 

```jsx
function App() {

  useEffect(()=>{
    localStorage.setItem('watched', JSON.stringify( [] ))
  },[]) 

}
```
그래서 이런코드 하나 넣고 시작하면 편리할듯요


## localStorage로 만드는 최근 본 상품 기능 2

### 저번시간 숙제는
1. 누가 Detail페이지 접속하면 
2. 현재 페이지에 보이는 상품id 가져와서
3. localStorage에 watch항목에 있던 [ ] 에 추가

```jsx
// (Detail.js)

useEffect(()=>{
  console.log(찾은상품.id)
}, [])
```
1번 2번은 이렇게 하면 되겠군요. 
Detail.js 아무데나 useEffect() 하나 집어넣으면 1번 번역 끝이고
2번은 아마 예전에 let 찾은상품 이런거 만들어둔 적이 있을겁니다 
그거 쓰면 현재 페이지의 상품번호도 잘 출력가능합니다.
2번 번역 끝 

3번 localStorage에 watch항목에 추가는 localStorage에 있던 기존 데이터를 수정하고 그런건 불가능하다고 했습니다.
입력/출력밖에 안됩니다. 

그래서 watch에 있던 [ ] 빼서 
찾은상품.id를 추가하고 다시 watch 항목으로 저장하는 식으로 코드짜면 됩니다.
localStorage 수정할 때 이렇게 하라고 저번시간에 배운듯

```jsx
// (Detail.js)

useEffect(()=>{
  let 꺼낸거 = localStorage.getItem('watched')
  꺼낸거 = JSON.parse(꺼낸거)
  꺼낸거.push(찾은상품.id)
  localStorage.setItem('watched', JSON.stringify(꺼낸거))
}, [])
```

그래서 watched에 있던 [ ] 꺼내서 찾은상품.id 추가하고 다시 watched 이름으로 집어넣으라고 했습니다. 
3번 번역 끝 

근데 같은 상품페이지 계속 접속하면 
똑같은 상품id가 계속 추가되는 현상이 발생하는군요. 


### 중복제거하기

그런 버그같은건 여러분이 한글을 대충적어놔서 생기는 것입니다.
한글을 아주 상세히 정확히 짜면 이론상 버그가 절대없음 

"상품id가 이미 [ ]에 있으면 추가하지 말아주세요" 라고 추가만 하면 될 것 같은데 자바스크립트 기초를 잘 배운 분들은 딱봐도 if 대충 쓰면 되는구나 각이 나올텐데

if 이런거 쓰기 귀찮으면 Set 자료형 쓰면 됩니다.
Set은 array와 똑같은데 중복을 알아서 제거해주는 array입니다. 
그리고 array <-> Set 변환도 쉬워서 
array -> Set -> array 이런 식으로 쓰면 array에서 중복제거를 좀 쉽게 할 수 있습니다. 

```jsx
// (Detail.js)

useEffect(()=>{
  let 꺼낸거 = localStorage.getItem('watched')
  꺼낸거 = JSON.parse(꺼낸거)
  꺼낸거.push(찾은상품.id)

  //Set으로 바꿨다가 다시 array로 만들기
  꺼낸거 = new Set(꺼낸거)
  꺼낸거 = Array.from(꺼낸거)
  localStorage.setItem('watched', JSON.stringify(꺼낸거))
}, [])
```
- 그래서 Set으로 바꿨다가 다시 array로 변환해봤습니다. 
    - 구글찾아보니 new Set(array자료) 하면 array를 Set으로 바꿀 수 있고
    - Array.from(Set자료) 하면 Set을 array로 바꿀 수 있다는군요.  
    - 아무튼 이제 상세페이지 접속할 때 마다 localStorage에 상품번호들이 중복없이 잘 추가됩니다. 

- 이제 심심하면 메인페이지 이런데다가 UI 하나 만들고 그 안에 최근 본 상품 id를 진열해주거나 그래봅시다.

- 상품id만 진열하면 안이쁠테니 상품id가지고 실제 상품명이나 이미지나 그런걸 진열해보는 것도 좋겠군요. 


### localStorage에 state를 자동저장되게 만들고 싶으면

직접 코드짜도 되긴 하는데 
redux-persist 이런 라이브러리 설치해서 쓰면 redux store 안에 있는 state를 자동으로 localStorage에 저장해줍니다.
state 변경될 때마다 그에 맞게 localStorage 업데이트도 알아서 해줌 
하지만 셋팅문법 복잡하고 귀찮습니다. 

그래서 요즘은 신규 사이트들은 Redux 대신 Jotai, Zustand 같은 라이브러리를 사용합니다. 
같은 기능을 제공하는데 셋팅도 거의 필요없고 문법이 훨씬 더 쉬우니까요.
그리고 그런 라이브러리들도 아마 localStorage 자동저장기능들이 있습니다. 

## redux-persist 설치방법 및 셋팅(redux toolkit + redux-persist)

- `redux 상태 관리 라이브러리`를 많이 사용하실 것입니다.
- 리덕스의 store는 페이지를 새로고침 할 경우 state가 날아가는 것을 보실 수 있습니다.
- 이것에 대한 대응 방안으로 `localStorage 또는 session`에 저장하고자 하는 reducer state를 저장하여, 새로고침 하여도 저장공간에 있는 데이터를 redux에 불러오는 형식으로 이루어집니다.
- 위에서 말한 이 작동을 위해 `redux-persist`를 사용합니다.

### 설치

터미널 창에 
`npm install redux-persist` 
입력하여 Redux Persist 설치합니다.

### store.js 코드

```jsx
import { configureStore, getDefaultMiddleware } from '@reduxjs/toolkit';
import { persistStore, persistReducer } from 'redux-persist';
import storage from 'redux-persist/lib/storage';
import rootReducer from './reducers/rootReducer';

// Redux Persist 설정
const persistConfig = {
  key: 'root',
  storage: storage,
};

// rootReducer에 추가할 리듀서들 추가
const persistedReducer = persistReducer(persistConfig, rootReducer);

// Redux 스토어 생성
const store = configureStore({
  reducer: persistedReducer,
});

const persistor = persistStore(store);

export { store, persistor };
```

### reducer에 persist store 정의 및 설정
localStorage에 저장하고 싶으면
```jsx
import storage from 'redux-persist/lib/storage
```

session Storage에 저장하고 싶으면
```jsx
import storageSession from 'redux-persist/lib/storage/session
```

```jsx
const persistConfig = {
  // 로컬 스토리지에 저장될 키(key)의 이름입니다.
  key: 'root',
  // localStorage에 저장
  storage: storage,
};
```

### rootReducer에 추가할 리듀서들 추가

rootReducer.js 파일에 필요한 리듀서 함수들을 import 하여 담아준다.

```jsx
(rootReducer.js)

import { combineReducers  } from "@reduxjs/toolkit";
import userReducer from './userSlice';
import cartReducer from './cartSlice';

const rootReducer = combineReducers({
  user : userReducer.reducer,
  cart: cartReducer.reducer, 
});

export default rootReducer;
```
주의할점은
- Redux Toolkit에서 createSlice 함수를 사용하면 액션 생성자와 리듀서를 함께 정의하는 것이 가능하지만 이 객체를 바로 combineReducers 함수에 넣을 수는 없기 때문에 
- 따라서 Redux의 combineReducers 함수에는 직접적으로 createSlice로 생성한 객체를 넣을 수 없습니다.
- 대신에 createSlice로 생성한 객체 안에 있는 reducer 속성을 사용해야 합니다. reducer 속성에는 실제 리듀서 함수가 들어 있습니다. 이 함수를 - combineReducers에 전달하면 됩니다.

```jsx
(store.js)

import rootReducer from './reducers/rootReducer';

const persistedReducer = persistReducer(persistConfig, rootReducer);
```
`persistedReducer`를 통해 로컬 스토리지에 Redux 상태를 지속적으로 저장


### Redux 스토어 생성

```jsx
const store = configureStore({
  reducer: persistedReducer,
});

const persistor = persistStore(store);

export { store, persistor };
```

### 컴포넌트에서 Redux Store 사용: Redux 스토어를 컴포넌트에 제공

```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter } from 'react-router-dom';
import { Provider } from 'react-redux';
import { PersistGate } from 'redux-persist/integration/react';
import { store, persistor } from './store'; // Redux 스토어 및 persistor를 가져옵니다.

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Provider store={store}>
    <PersistGate loading={null} persistor={persistor}>
      <BrowserRouter>
      <App />
      </BrowserRouter>
    </PersistGate>
  </Provider>
);
```


## 성능개선 1 : 개발자도구 & lazy import

- props를 보냈는데 출력이 안된다거나 이미지를 넣었는데 안보이는 버그같은게 생기면 개발자도구를 켜서 Elements 탭 살펴보면 되는데
- 여기선 여러분이 짠 코드가 실제 html css로 변환되어서 보여집니다. 
- 그게 싫고 컴포넌트로 미리보고 싶으면 리액트 개발자도구를 설치해서 켜보면 됩니다. 


### 크롬 확장프로그램 : React Developer Tools 

- 크롬 웹스토어 들어가면 확장프로그램 설치가 가능합니다. 
- 여기서 React Developer Tools 설치하면 Components 탭이 생기는데 여러분들이 개발중인 리액트사이트를 컴포넌트로 미리볼 수 있습니다. 

- 왼쪽에서 컴포넌트구조 파악이 가능하고 왼쪽상단 아이콘눌러서 컴포넌트 찍어보면 거기 있는 state, props 이런거 조회가능합니다. 수정해볼 수도 있음 


### Profiler 탭에서 성능평가 가능

Profiler 탭 들어가서
- 녹화버튼 누르고
- 페이지 이동이나 버튼조작을 해보고
- 녹화를 끝내면 

방금 렌더링된 모든 컴포넌트의 렌더링시간을 측정해줍니다. 

- 이상하게 느린 컴포넌트가 있다면 여기서 범인을 찾을 수 있습니다. 
- <div>를 1만개 만들거나 그러지 않는 이상 보통은 걱정할 필요는 없습니다.
- 지연 원인 대부분은 서버에서 ajax 요청결과가 늦게 도착해서 그런 경우가 많습니다.
- 서버가 느린 건 어쩔 수 없음 


### Redux Developer Tools 

- 이것도 크롬 웹스토어에서 설치가능합니다. 
- Redux store에 있던 state를 전부 확인가능합니다.
- 그리고 dispatch 날릴 때 마다 뭐가 어떻게 바뀌었는지 로그를 작성해줍니다. 
- store 복잡해지면 유용함 


### lazy import

- 리액트 코드 다 짰으면 npm run build 입력해서 여러분이 짰던 이상한 코드들을 역사와 전통의 html css js 파일로 변환해야합니다.  
- 근데 리액트로 만드는 Single Page Application의 특징은 html, js 파일이 하나만 생성됩니다. 
- 그 안에 지금까지 만든 App / Detail / Cart 모든 내용이 들어있어서 파일사이즈가 좀 큽니다. 
- 원래 그래서 리액트 사이트들은 첫 페이지 로딩속도가 매우 느릴 수 있습니다. 

- 그게 싫다면 js 파일을 잘게 쪼개면 됩니다.
- 쪼개는 방법은 import 문법을 약간 고치면 되는데 지금 메인페이지 보면 Detail, Cart를 import 해서 쓰고있습니다.
- 근데 잘 생각해보면 Detail, Cart 컴포넌트는 메인페이지에서 전혀 보이지 않고 있기 때문에 이런 컴포넌트들은 이런 문법으로 import 해놓으면 좋습니다. 

```jsx
(App.js)

import Detail from './routes/Detail.js'
import Cart from './routes/Cart.js'
```

▼▼▼▼

```jsx
(App.js)
import {lazy, Suspense, useEffect, useState} from 'react'

const Detail = lazy( () => import('./routes/Detail.js') )
const Cart = lazy( () => import('./routes/Cart.js') )
```
이렇게 바꾸라는 소리입니다.

- lazy 문법으로도 똑같이 import가 가능한데 이 경우엔
- "Detail 컴포넌트가 필요해지면 import 해주세요" 라는 뜻이 됩니다. 
- 그리고 이렇게 해놓으면 Detail 컴포넌트 내용을 다른 js 파일로 쪼개줍니다.
- 그래서 첫 페이지 로딩속도를 향상시킬 수 있습니다.

```jsx
<Suspense fallback={ <div>로딩중임</div> }>
  <Detail shoes={shoes} />
</Suspense>
```

lazy 사용하면 당연히 Detail 컴포넌트 로드까지 지연시간이 발생할 수 있습니다. 그럴 땐
1. Suspense 라는거 import 해오고
2. Detail 컴포넌트를 감싸면

Detail 컴포넌트가 로딩중일 때 대신 보여줄 html 작성도 가능합니다. 
귀찮으면 `<Suspense>` 이걸로 `<Routes>` 전부 감싸도 됩니다. 


## 성능개선 2 : 재렌더링 막는 memo, useMemo

- 컴포넌트가 재렌더링되면 거기 안에 있는 자식컴포넌트는 항상 함께 재렌더링됩니다.
- 리액트는 그렇게 대충 무식하게 동작하는데 평소엔 별 문제가 없겠지만 자식컴포넌트가 렌더링시간이 1초나 걸리는 무거운 컴포넌트면 어쩔 것입니까. 
- 부모컴포넌트에 있는 버튼 누를 때 마다 1초 버벅이는 불상사가 발생합니다. 
- 그럴 땐 자식을 memo로 감싸놓으면 됩니다. 


### 테스트용 자식 컴포넌트 하나 만들어보기 

```jsx
function Child(){
  console.log('재렌더링됨')
  return <div>자식임</div>
}

function Cart(){ 

  let [count, setCount] = useState(0)

  return (
    <Child />
    <button onClick={()=>{ setCount(count+1) }}> + </button>
  )
}
```
- Cart 컴포넌트 안에 Child 컴포넌트를 만들었습니다.
- 그리고 버튼누를 때 Cart 컴포넌트가 재렌더링되게 만들어놨는데 이 경우 `<Child>` 이것도 재렌더링됩니다.

- 평소엔 별 문제가 없겠지만 `<Child>` 얘가 렌더링이 2초정도 걸리는 느린 컴포넌트면 어쩌죠?
- 그럼 버튼 누를 때 마다 버벅일듯요.

- 그럴 땐 memo라는 함수를 쓰면
- "꼭 필요할 때만 `<Child>` 컴포넌트 재렌더링해주세요" 라고 코드를 짤 수도 있습니다. 


### memo()로 컴포넌트 불필요한 재렌더링 막기

memo() 써보려면 'react' 라이브러리로부터 import 해오시면 됩니다.

```jsx
import {memo, useState} from 'react'

let Child = memo( function(){
  console.log('재렌더링됨')
  return <div>자식임</div>
})

function Cart(){ 

  let [count, setCount] = useState(0)

  return (
    <Child />
    <button onClick={()=>{ setCount(count+1) }}> + </button>
  )
}
```
1. memo를 import 해와서
2. 원하는 컴포넌트 정의부분을 감싸면 됩니다. 

- 근데 컴포넌트를 let 컴포넌트명 = function( ){ } 이런 식으로 만들어야 감쌀 수 있습니다.
- 그럼 이제 Child로 전송되는 props가 변하거나 그런 경우에만 재렌더링됩니다. 

- `Q. 어 그럼 memo는 좋은거니까 막써도 되겠네요?`
    - memo로 감싼 컴포넌트는 헛된 재렌더링을 안시키려고 기존 props와 바뀐 props를 비교하는 연산이 추가로 진행됩니다.
    - props가 크고 복잡하면 이거 자체로도 부담이 될 수도 있습니다.
    - 그래서 꼭 필요한 곳에만 사용합시다. 


### 비슷하게 생긴 useMemo

- 비슷한 useMemo라는 문법도 있는데 이건 그냥 useEffect와 비슷한 용도입니다.
- 컴포넌트 로드시 1회만 실행하고 싶은 코드가 있으면 거기 담으면 됩니다. 

```jsx
import {useMemo, useState} from 'react'

function 함수(){
  return 반복문10억번돌린결과
}

function Cart(){ 

  let result = useMemo(()=>{ return 함수() }, [])

  return (
    <Child />
    <button onClick={()=>{ setCount(count+1) }}> + </button>
  )
}
```

1. 예를 들어서 반복문을 10억번 돌려야하는 경우 
2. 그 함수를 useMemo 안에 넣어두면 컴포넌트 로드시 1회만 실행됩니다. 

그럼 재렌더링마다 동작안하니까 좀 효율적으로 동작하겠죠? 
useEffect 처럼 dependency도 넣을 수 있어서 특정 state, props가 변할 때만 실행할 수도 있습니다. 


## 성능개선 3 : useTransition, useDeferredValue

리액트18버전 이후부터
- 렌더링 성능이 저하되는 컴포넌트에서 쓸 수 있는 혁신적인 기능이 하나 추가되었습니다. 
- useTransition 이건데 이걸로 오래걸리는 부분을 감싸면 렌더링시 버벅이지 않게 해줍니다.
- 실은 코드 실행시점만 조절해주는 식임


### 리액트 18버전부터 추가된 기능 1 : 일관된 batching

automatic batching 이라는 기능이 있는데 

```jsx
setCount(1) 
setName(2) 
setValue(3)   //여기서 1번만 재렌더링됨
```
- state변경함수를 연달아서 3개 사용하면 재렌더링도 원래 3번 되어야하지만 
- 리액트는 똑똑하게도 재렌더링을 마지막에 1회만 처리해줍니다. 
- 일종의 쓸데없는 재렌더링 방지기능이고 batching이라고 합니다.

```jsx
fetch().then(() => {
    setCount(1)   //재렌더링됨
    setName(2)   //재렌더링됨
}) 
```
- 근데 문제는 ajax요청, setTimeout안에 state변경함수가 있는 경우 batching이 일어나지 않습니다. 
- 리액트 17버전까진 그런 식으로 일관적이지 않게 동작했는데
- 18버전 이후 부터는 어디 있든 간에 재렌더링은 마지막에 1번만 됩니다. 


### 리액트 18버전부터 추가된 기능 2 : useTransition 추가됨

- 렌더링시간이 매우 오래걸리는 컴포넌트가 있다고 칩시다. 
- 버튼클릭, 타이핑할 때 마다 그 컴포넌트를 렌더링해야한다면 이상하게 버튼클릭, 타이핑 반응속도도 느려집니다. 
- 사람들은 원래 클릭, 타이핑을 했을 때 0.3초 이상 반응이 없으면 불편함을 느끼기 때문에 (한국인은 0.2초)

개선방법을 알아봅시다. 
- 당연히 그 컴포넌트 안의 html 갯수를 줄이면 대부분 해결됩니다. 
- 근데 그런게 안되면 useTransition 기능을 쓰면 됩니다. 


### 우선 재렌더링이 느린 컴포넌트 만들어보기 

```jsx
import {useState} from 'react'

let a = new Array(10000).fill(0)

function App(){
  let [name, setName] = useState('')
  
  return (
    <div>
      <input onChange={ (e)=>{ setName(e.target.value) }}/>
      {
        a.map(()=>{
          return <div>{name}</div>
        })
      }
    </div>
  )
}
```
- 데이터가 10000개 들어있는 array자료를 하나 만들고
- 그 갯수만큼 `<div>`를 생성하라고 했습니다.
- 그리고 유저가 타이핑할 수 있는 `<input>`도 만들어봤습니다.

유저가 `<input>`에 타이핑하면 그 글자를 `<div>` 1만개안에 집어넣어줘야하는데
`<div>` 1만개 렌더링해주느라 `<input>`도 많은 지연시간이 발생합니다.
타이핑한 결과가 바로바로 반응이 안옵니다. 답답해죽음 


### useTransition 쓰면 

```jsx
import {useState, useTransition} from 'react'

let a = new Array(10000).fill(0)

function App(){
  let [name, setName] = useState('')
  let [isPending, startTransition] = useTransition()
  
  return (
    <div>
      <input onChange={ (e)=>{ 
        startTransition(()=>{
          setName(e.target.value) 
        })
      }}/>

      {
        a.map(()=>{
          return <div>{name}</div>
        })
      }
    </div>
  )
}
```
- useTransition() 쓰면 그 자리에 [변수, 함수]가 남습니다. 
- 그 중 우측에 있는 startTransition() 함수로 state변경함수 같은걸 묶으면 `그걸 다른 코드들보다 나중에` 처리해줍니다.

- 그래서 <input> 타이핑같이 즉각 반응해야하는걸 우선적으로 처리해줄 수 있습니다. 
- 타이핑해보면 아까보다 반응속도가 훨씬 낫습니다. 
- 물론 근본적인 성능개선이라기보단 특정코드의 실행시점을 뒤로 옮겨주는 것일 뿐입니다. 
- html이 많으면 여러페이지로 쪼개십시오. 


### isPending은 어디다 쓰냐면 

startTransition() 으로 감싼 코드가 처리중일 때 true로 변하는 변수입니다.

```jsx
{
  isPending ? "로딩중기다리셈" :
  a.map(()=>{
    return <div>{name}</div>
  })
} 
```
그래서 이런 식으로 코드짜는 것도 가능합니다.
위의 코드는 useTransition으로 감싼게 처리완료되면 `<div>{name}</div>` 이게 보이겠군요.


### useDeferredValue 이것도 비슷함

- startTransition() 이거랑 용도가 똑같습니다.
- 근데 얘는 state 아니면 변수하나를 집어넣을 수 있게 되어있습니다. 
- 그래서 그 변수에 변동사항이 생기면 그걸 늦게 처리해줍니다. 

```jsx
import {useState, useTransition, useDeferredValue} from 'react'

let a = new Array(10000).fill(0)

function App(){
  let [name, setName] = useState('')
  let state1 = useDeferredValue(name)
  
  return (
    <div>
      <input onChange={ (e)=>{ 
          setName(e.target.value) 
      }}/>

      {
        a.map(()=>{
          return <div>{state1}</div>
        })
      }
    </div>
  )
}
```
이렇게 쓰면 아까랑 똑같은 기능을 개발가능합니다.
- useDeferredValue 안에 state를 집어넣으면 그 state가 변동사항이 생겼을 때 나중에 처리해줍니다.
- 그리고 처리결과는 let state에 저장해줍니다. 