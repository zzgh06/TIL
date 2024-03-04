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
