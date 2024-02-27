## Ajax 1 : 개념정리

Ajax는 서버와 데이터주고받는 법 중 하나인데 
서버가 뭔지 모르면 아무리 ajax 문법 외워봤자 응용을 못하기 때문에 서버가 뭔지 정리부터합시다.


### 서버란?

유저가 데이터달라고 요청을 하면 데이터를 보내주는 간단한 프로그램일 뿐입니다.

네이버웹툰 서버 : 유저가 웹툰 달라고 하면 웹툰 보내주는 프로그램
유튜브 서버 : 유저가 영상 달라고 하면 영상 보내주는 프로그램입니다. 

근데 그냥 데이터달라고 떼쓰면 주는게 아니라
서버에 데이터를 요청할 때는

1. 어떤 데이터인지 url로 잘 기재해야하고

2. 어떤 방법으로 요청할지 결정해야 (GET/POST 등)

데이터를 보내줍니다. 

예를 들어서 쇼미더럭키짱이라는 네이버웹툰을 보고싶으면
https://comic.naver.com/webtoon/list?titleId=783054 여기로 GET요청하면 보내줍니다.
예를 들어서 독립일기라는 네이버웹툰을 보고싶으면
https://comic.naver.com/webtoon/list?titleId=748105 여기로 GET요청하면 보내줍니다.


### GET/POST 요청하는 법?

- GET요청은 서버에 있던 데이터를 읽고싶을 때 주로 사용하고
- POST요청은 서버로 데이터를 보내고 싶을 때 사용합니다.
- (서버는 유저데이터를 DB에 저장해주는 역할도 해서요)
- 실은 PUT, DELETE 요청도 있긴 합니다. 

GET요청을 날리고 싶으면 가장 쉬운 방법은 브라우저 주소창입니다.
거기에 url 적으면 그 곳으로 GET요청을 날려줍니다.

POST요청을 날리고 싶으면
<form action="요청할url" method="post"> 태그 이용하면 됩니다.

그럼 폼이 전송되었을 때 POST요청을 날려줍니다. 
근데 GET, POST 요청을 저렇게 날리면 단점이 뭐냐면 브라우저가 새로고침됩니다.


### AJAX란? 

서버에 GET, POST 요청을 할 때 `새로고침 없이` 데이터를 주고받을 수 있게 도와주는 
간단한 브라우저 기능을 AJAX라고 합니다. 

그거 쓰면 새로고침 없이도 쇼핑몰 상품을 더 가져올 수도 있고
새로고침 없이도 댓글을 서버로 전송할 수도 있고 
그런 기능을 만들 수 있는 것임 


### jQuery로 AJAX요청하기 

- $.get() 라는 함수를 쓰고 안에 url만 잘 기입하면 됩니다. 
- 연습삼아서 https://codingapple1.github.io/hello.txt 여기로 GET요청해보십시오.
- 그럼 인삿말을 하나 가져올 수 있습니다. 

```javascript
$.get('https://codingapple1.github.io/hello.txt');
```

```javascript
$.get('https://codingapple1.github.io/hello.txt').done(function(data){
  console.log(data)
});
```

- 근데 가져온 데이터가 어디 들어있냐면 
- .done 아니면 .then 뒤에 붙이고 콜백함수넣고 파라미터 하나 만들면 거기에 들어있습니다.

```javascript
$.post('url~~', {name : 'kim'})
```

- 서버로 데이터를 보낼 수 있는 POST요청을 날리고 싶으면 이렇게 씁니다.
- url 잘 적고 뒤에 서버로 보낼 데이터를 적으면 됩니다.
- 당연히 얘도 .done 이런거 붙이기 가능

```javascript
$.get('https://codingapple1.github.io/hello.txt')
  .done(function(data){
    console.log(data)
  })
  .fail(function(error){
    console.log('실패함')
  });
```

- ajax 요청 성공시 .done 안에 있는 코드를 실행해줍니다.
- ajax 요청 실패시 .fail 안에 있는 코드를 실행해줍니다. 
- error 저거 출력해보면 에러관련 정보를 출력해줍니다. 그거 보고 디버깅하면 됩니다.
- 예를 들어 404 이런 에러코드는 url 이 잘못되었다는 뜻입니다. 
- done/fail 말고 then/catch 써도 됩니다



## array에 자주 쓰는 sort, map, filter 함수

### array 정렬하는 법

- array 자료는 순서개념이 있다보니 정렬도 가능합니다.
- 그냥 문자 가나다순으로 정렬하려면 .sort() 붙이면 되는데 
- 숫자정렬은 이렇게 코드짜면 됩니다.

```javascript
var 어레이 = [7,3,5,2,40];
어레이.sort(function(a, b){
  return a - b
});

console.log(어레이);
```

- 이러면 숫자순으로 잘 출력됩니다.
- 근데 왜 저렇게 코드짜면 숫자순 정렬이 되는지 알고싶지 않습니까
- 코드 동작원리 이런걸 알면 나중에 응용도 쉽게 가능하기 때문에 sort() 동작원리를 알아봅시다.

```javascript
어레이.sort(function(a, b){
  return a - b
}); 
```

1. a, b는 array 안의 자료들입니다.
2. return 오른쪽이 양수면 a를 오른쪽으로 정렬해줍니다.
3. return 오른쪽이 음수면 b를 오른쪽으로 정렬해줍니다.
4. 그리고 array 안의 자료들을 계속 뽑아서 a, b에 넣어줍니다. 

- 이렇게 동작해서 a - b 저렇게 쓰면 숫자순 정렬이 되는 것입니다. 

- 예를 들면 a, b가 7과 3일 경우 7 - 3 하면 4가 남습니다.
- 4는 양수죠? 그러면 7을 3보다 오른쪽으로 보내줍니다.
- 그래서 숫자 오름차순 (123순) 정렬이 완성되는 것입니다.

Q. 그럼 array 안의 숫자 내림차순 (321순) 정렬은 어떻게 할까요?

```javascript
var 어레이 = [7,3,5,2,40];

어레이.sort(function(a, b){
  return b - a 
}); 
```
이러면 될듯요
- return 우측이 음수면 b를 오른쪽으로 보낸다고 했습니다.
- 그럼 a, b가 7과 3일 경우 return -4 라서 3을 더 오른쪽으로 보내줍니다.
- 이걸 array 자료들마다 계속 해주기 때문에 결국 321순 정렬이 됩니다

Q. 문자정렬과 문자역순정렬은 어떻게 할까요?

```javascript
// 문자 정렬
var 어레이 = ['다', '가', '나'];

어레이.sort(function(a, b){
  if (a.title > b.title){
    return 1;
  } else if (a.title < b.title){
    return -1;
  } else {
    return 0
  }
}); 
```

- 문자를 오름차순으로 정렬하기 위해서는 비교 연산자를 통해 자료들마다 양수, 음수. 0를 반환하여 정렬한다

```javascript
// 문자 역순 정렬
var 어레이 = ['다', '가', '나'];

어레이.sort(function(a, b){
  if (a.title < b.title){
    return 1;
  } else if (a.title > b.title){
    return -1;
  } else {
    return 0
  }
}); 
```

- 문자를 내림차순으로 정렬하는 법은 오름차순과 마찬가지로 비교 연산자를 활용하는데, 오름차순과 부등호를 반대로 한다. 


### array에 자주 쓰는 filter 함수 

- array 자료에서 원하는 자료만 필터링하고 싶으면 filter 함수를 씁니다.

```javascript
var 어레이 = [7,3,5,2,40];

var 새어레이 = 어레이.filter(function(a){
  return 조건식
}); 
```

1. a라고 작명한건 array 에 있던 데이터를 뜻하고
2. return 우측에 조건식을 넣으면 조건식에 맞는 a만 남겨줍니다.
3. 그리고 filter는 원본을 변형시키지 않는 고마운 함수기 때문에 새로운 변수에 담아써야합니다. 

```javascript
var 어레이 = [7,3,5,2,40];

var 새어레이 = 어레이.filter(function(a){
  return a < 4
}); 
```

- 예를 들어 여러 숫자가 있는데 그 중에 4 미만인 것만 남기고 싶으면 이렇게 쓰면 됩니다.
- 새어레이 출력해보면 [2, 3] 이것만 들어있겠군요. 
- 이런거 응용하면 쇼핑몰에서 "6만원 이하 상품만 보기" 이런 필터기능도 만들 수 있는 것입니다.
- products라는 자료에서 6만원 이하만 필터하고 새로 html 생성하면 될 것 같군요 


### array에 자주 쓰는 map 함수

- array 안의 자료들을 전부 변형하려면 map 함수를 씁니다.

```javascript
var 어레이 = [7,3,5,2,40];

var 새어레이 = 어레이.map(function(a){
  return 수식같은거
}); 
```

1. a라고 작명한건 array 에 있던 데이터를 뜻하고
2. return 우측에 변경될 수식같은걸 넣으면 됩니다. 
3. 그리고 filter는 원본을 변형시키지 않는 고마운 함수기 때문에 새로운 변수에 담아써야합니다. 

```javascript
var 어레이 = [7,3,5,2,40];

var 새어레이 = 어레이.map(function(a){
  return a * 4
}); 
```

- 예를 들어 array 안의 숫자들을 전부 4를 곱해주고 싶으면 이렇게 코드짜면 됩니다.
- 새어레이 출력해보면 [28, 12, 20, 8, 160] 이게 들어있겠군요. 
- 이런거 응용하면 쇼핑몰에서 "달러 -> 원화로 변환하기" 이런 기능도 만들 수 있겠군요.
- array 안에 있는 숫자들을 달러가격이라고 생각해봅시다. 이걸 전부 원화가격으로 변경하고 싶으면 어떻게하죠?
- 아마 map 써서 1000얼마 곱해주면 끝일듯요.


(참고)
- sort 함수는 원본을 변형시켜버립니다. 
- 원본을 변형시켜버리면 나중에 원본으로 되돌아갈 수 없으니까 귀찮아질 수 있어서 
- array/object 자료 조작시엔 원본을 따로 복사해두고 조작하는 경우도 있습니다. 



## 장바구니 기능과 localStorage


### 브라우저 저장공간이 여러개 있는데

- 크롬 개발자도구의 Application 탭 들어가보면 구경가능합니다. 

- `Local Storage / Session Storage` (key : value 형태로 문자, 숫자 데이터 저장가능)
- `Indexed DB` (크고 많은 구조화된 데이터를 DB처럼 저장가능, 문법더러움)
- `Cookies` (유저 로그인정보 저장공간)
- `Cache Storage` (html css js img 파일 저장해두는 공간)
- 골라쓰면 되는데 우린 범용적으로 쓸 수 있는 Local Storage를 써봅시다.

- Local Storage / Session Storage 는 
- 문자, 숫자만 key : value 형태로 저장가능하고 5MB까지만 저장가능합니다. 
- Local Storage는 브라우저 재접속해도 영구적으로 남아있는데 Session Storage는 브라우저 끄면 날아갑니다. 
- 유저가 브라우저 청소하지 않는 이상 반영구적으로 데이터저장이 가능합니다. 


## 로컬스토리지 사용법

```javascript
localStorage.setItem('이름', 'kim') //자료저장하는법
localStorage.getItem('이름') //자료꺼내는법
localStorage.removeItem('이름') //자료삭제하는법
```

## 로컬스토리지에 array/object 저장하려면

- array/object를 로컬스토리지에 저장하면 강제로 문자로 바꿔서 저장됩니다.
- 그래서 자료가 깨지고 그럴 수 있습니다. 
- 그래서 약간 편법같은건데 array/object를 JSON으로 바꾸면 문자취급을 받기 때문에 안전하게 로컬스토리지에 저장할 수 있습니다.
- JSON은 그냥 따옴표친 array/object입니다.

```javascript
var arr = [1,2,3];
var newArr = JSON.stringify(arr);

localStorage.setItem('num', newArr)
```

1. JSON.stringify() 안에 array/object 집어넣으면 JSON으로 바꿔줍니다. 그럼 문자취급받음
2. 그걸 localStorage에 저장하라고 코드짰습니다. 
그럼 깨지지 않게 저장가능합니다.

```javascript
var arr = [1,2,3];
var newArr = JSON.stringify(arr);

localStorage.setItem('num', newArr);

//꺼내서 쓸 땐
var 꺼낸거 = localStorage.getItem('num');
꺼낸거 = JSON.parse(꺼낸거);
console.log(꺼낸거);
```

- JSON으로 저장했으니 꺼내도 JSON입니다.
- 그래서 꺼낸걸 다시 array/object로 바꾸고 싶으면 
- JSON.parse() 안에 넣으면 됩니다. 

아무튼 결론은 
- array/object -> JSON 변환하고 싶으면 JSON.stringify()
- JSON -> array/object 변환하고 싶으면 JSON.parse()



## 스크롤 위치에 따라 변하는 애니메이션 : Apple Music UI 만들기


### 스크롤 위치에 따라 opacity가 변하는 애니메이션 만들기

```javascript
$(window).scroll(function(){
    var 높이 = $(window).scrollTop();
    console.log(높이);
});
```

- 스크롤 애니메이션의 기본은 위와 같은 자바스크립트입니다. 
- 많이 보던 "스크롤시 내부 코드를 실행해주세요~" 라는 코드입니다. 
- 내부 코드엔 현재 창의 스크롤바 높이를 알려주는 (window).scrollTop(); 이라는 함수를 써본 뒤에

콘솔창에 출력을 해보았습니다. 

`현재 창의 스크롤바 높이를 왜 출력해보는데여?`

- 왜냐면 현재 스크롤바 높이에 따라 opacity가 변하니까 
- 스크롤바가 어디까지 스크롤 되면 opacity가 0이고
- 어디까지 스크롤 되면 opacity가 1인지 찾고 싶어서 그런거지 별 이유는 없습니다. 

그래서 콘솔창에 현재 스크롤바 높이를 출력하면서 측정해보았습니다. 

- 650px 쯤 스크롤하면 opacity를 1로,
- 900px 쯤 스크롤하면 opacity를 대충 0.5로,
- 1150px 쯤 스크롤하면 opacity를 0으로 설정하면 좋을 것 같습니다. 

이걸 코드로 표현해보도록 합시다. 

```javascript
$(window).scroll(function(){

  var 높이 = $(window).scrollTop();
  console.log(높이);
        
// 650~1150까지 스크롤바를 내리면,
// 첫째카드의 opacity 1~0으로 서서히변경해주셈
  $('.card-box').eq(0).css('opacity', ???);

});
```

- 스크롤바를 내릴 때, $('.card-box').eq(0).css('opacity', ???); 이렇게 코드가 동작하도록 설정했습니다. 
- 첫카드의 opacity를 ???로 변하게 해야되는데 ???는 0 이런 고정된 값으로 설정할 수 없을 것 같습니다. 
- `???부분은`
- "스크롤바높이가 650~1150이 될 때 1~0이 되는 가변적인 값"이 되어야하겠죠? 
- 그래서 일단 미지의 변수인 y라고 표현합시다. 

```javascript
$(window).scroll(function(){

  var 높이 = $(window).scrollTop();
  console.log(높이);

  var y = 미지의 변수;
  $('.card-box').eq(0).css('opacity', y);

});
```

Q. "스크롤바높이가 650~1150이 될 때 1~0이 되는 가변적인 값"인 미지의 변수 y를 구해보십시오.

`y = a * 높이 + b`

- y에 대한 1차함수는 우리가 뭐 기울기 이런걸 모를 때 일단 ax+b 이런 식으로 표현할 수 있다고 배웠습니다.
- 그럼 a랑 b라는 미지수만 잘 구하면 y가 뭔지 알 수 있는거네요? 
- a는 전문용어로 기울기, b는 전문용어로 y절편이라고 합니다만 
- 그건 너무 어려우니 우리는 대입법을 이용해보도록 합시다. 

- a,b를 구하는건 대입법을 이용합니다. 

    위의 함수는
    - 높이가 650일 때 y가 1, 
    - 높이가 1150일 때 y가 0입니다


```javascript
// 수학시간
1 = a * 650 + b
0 = a * 1150 + b

a = -1/500
b = 115/50

var y = -1/500 * 높이 + 115/50
```

```javascript
// 수학시간
$(window).scroll(function(){

  var 높이 = $(window).scrollTop();
  console.log(높이);

  var y =  -1/500 * 높이 + 115/50;
  $('.card-box').eq(0).css('opacity', y);

});
```



### 캐러셀에 스와이프 기능 만들기

터치되는 캐러셀같은거 조작해보면 대충 이런 기능이 들어있습니다.

- 기능1. 드래그한 거리만큼 사진도 왼쪽으로 움직여야함
- 기능2. 마우스 떼었을 때 일정거리 이상 이동했으면 사진2 보여줌, 아니면 다시 사진1 보여줌
- 기능1 부터 만들어봅시다. 

근데 이거 만들려면 알아야할 이벤트가 3개 있습니다.


## mouse 이벤트 3개

마우스로 어떤 html 요소를 조작할 때 발동하는 이벤트가 있습니다.

- `mousedown` (어떤 요소에 마우스버튼 눌렀을 때)
- `mouseup` (어떤 요소에 마우스버튼 뗐을 때)
- `mousemove` (어떤 요소위에서 마우스 이동할 때)

알아두면 유용합니다

```html
<div>캐러셀있는곳</div>

<script>
  $('.slide-box').eq(0).on('mousemove', function(){
    console.log('안녕')
  })
</script>

// 그래서 예를 들어 이렇게 코드짜면 .slide-box 위에 마우스 움직일 때 마다 '안녕'이 출력됩니다.
```

```html
<div>캐러셀있는곳</div>

<script>
  $('.slide-box').eq(0).on('mousemove', function(e){
    console.log(e.clientX)
  })
</script>
```

- 이게 더 유용한데 mouse어쩌구 이벤트리스너안에선 e.clientX e.clientY를 출력해볼 수 있는데 
- 현재 마우스 좌표를 알려줍니다. 유용하겠죠?
- 이거 쓰면 유저가 얼마나 사진을 드래그 했는지 그런 것도 알 수 있을듯 ㄷㄷ


## 기능1. 사진1을 왼쪽으로 드래그한 거리만큼 사진1도 왼쪽으로 움직여야함

- 예를 들어 사진1을 클릭하고 왼쪽으로 50px 잡아끌었다면
- 사진1도 왼쪽으로 50px 움직여야합니다.
- 근데 사진1만 움직이는거말고 사진3개 전부 담긴 큰 박스 움직이는게 좋을듯

이동거리를 어떻게 파악하죠?

- 마우스 누를 때의 X좌표 & 마우스 움직일 때의 X좌표를 빼보면 나오는거 아닙니까 초등학교 수학문제인듯 
- 빼보도록 합시다. 

```html
<div>캐러셀있는곳</div>

<script>
  $('.slide-box').eq(0).on('mousedown', function(e){
    e.clientX ← 이거랑
  });

  $('.slide-box').eq(0).on('mousemove', function(e){
    e.clientX ← 이거를 빼야할듯
  });
</script>
```

저거 e.clientX 두개 빼면 됩니다. 

- 근데 안타깝게도 모든 변수는 범위가 있어서 함수 바깥으로 탈출할 수 없습니다.
- 근데 함수 바깥에 있던 변수는 함수 안에서 맘대로 쓸 수 있습니다.
- 그래서 함수 바깥에 변수를 만들어두면 함수들끼리 변수 공유가 가능합니다.

```html
<script>
  var 시작좌표 = 0;

  $('.slide-box').eq(0).on('mousedown', function(e){
    시작좌표 = e.clientX;
  });

  $('.slide-box').eq(0).on('mousemove', function(e){
    console.log(e.clientX - 시작좌표)
  });
</script>
```

1. 시작좌표라는 변수를 함수들 바깥에 만들어둡니다. (그럼 모든 함수에서 이용가능)
2. 마우스 클릭시 현재 좌표를 var 시작좌표에 저장해줌
3. mousemove 이벤트발생시 var 시작좌표랑 현재좌표인 e.clientX를 빼봄

- 그걸 출력해보면 현재 드래그 이동거리가 잘 나오는군요
- 왼쪽으로 드래그하면 -100 이렇게 출력되고 오른쪽으로 드래그하면 100 이런거 출력되는듯  


## 이동거리만큼 저거 박스도 이동해달라

```html
<script>
  var 시작좌표 = 0;

  $('.slide-box').eq(0).on('mousedown', function(e){
    시작좌표 = e.clientX;
  });

  $('.slide-box').eq(0).on('mousemove', function(e){
    console.log(e.clientX - 시작좌표)
    $('.slide-container').css('transform', `translateX( ${e.clientX - 시작좌표}px )`)
  });
</script>
```


## 왜 마우스 클릭도 안했는데 박스가 움직임?

"클릭하고나서만 박스 이동해달라"고 컴퓨터에게 명령을 주면 됩니다. 

```html
<script>
  var 시작좌표 = 0;

  $('.slide-box').eq(0).on('mousedown', function(e){
    시작좌표 = e.clientX;
  });

  $('.slide-box').eq(0).on('mousemove', function(e){
    if (마우스눌렀냐???) {
      $('.slide-container').css('transform', `translateX( ${e.clientX - 시작좌표}px )`)
    }
  });
</script>
```

- if문 추가하면 되는거 아닙니까 
- 근데 마우스 눌렀는지 아닌지는 어떻게 판단하죠?
- 그건 다행히 mousedown 이벤트리스너가 있군요 그 안에서 판단하면 될 것 같습니다.

```html
<script>
  var 시작좌표 = 0;
  let 눌렀냐 = false;

  $('.slide-box').eq(0).on('mousedown', function(e){
    시작좌표 = e.clientX;
    var 눌렀냐 = true;
  });

  $('.slide-box').eq(0).on('mousemove', function(e){
    if (눌렀냐 === true) {
      $('.slide-container').css('transform', `translateX( ${e.clientX - 시작좌표}px )`)
    }
  });
</script>
```

1. 마우스 누르면 var 눌렀냐 변수를 true로 만들라고 코드짰습니다.
2. 그리고 if문에선 var 눌렀냐가 true일 때만 박스움직이라고 코드짰습니다.


## 기능2. 마우스 떼었을 때 이동거리가 100 이상이면 2번사진 보여주기

이거는 마우스를 떼면 실행할 기능이니까 mouseup 이벤트리스너안에 코드짜면 되겠군요 

```html
<script>
  (생략)

  $('.slide-box').eq(0).on('mouseup', function(e){
    눌렀냐 = false;

    if (이동거리 100이상) {
      2번사진보여주셈 
    } else {
      1번사진보여주셈
    }
  });
</script>
```

Q. 이동거리는 어떻게 구하죠? 

- 그건 저번시간에 e.clientX - 시작좌표 이렇게 구해봤습니다. 그거 넣으면 될듯요 
- 근데 안타깝게도 e.clientX - 시작좌표는 다른 함수안에 있어서 함부로 가져다쓰지 못합니다.
- 쓰고싶으면 전역변수 하나 만들면 되는 것임 

```html
<script>
  (생략)

  $('.slide-box').eq(0).on('mouseup', function(e){
    눌렀냐 = false;

    if (e.clientX - 시작좌표 < -100) {
      $('.slide-container').css('transition', 'all 0.5s').css('transform', 'translateX(-100vw)');
    } else {
      $('.slide-container').css('transition', 'all 0.5s').css('transform', 'translateX(0vw)');
    }
    setTimeout(()=>{
      $('.slide-container').css('transition', 'none')
    }, 500)
    
  });
</script>
```


## 모바일은 터치 이벤트리스너 달아야함 

- 사이트를 모바일기기로 테스트하고 싶으면 크롬개발자도구 좌상단 toggle device toolbar 버튼누르면 됩니다. 
- 근데 모바일기기로 테스트해보면 스와이프가 안됩니다.
- 왜냐면 마우스이벤트리스너를 달아놨기 때문입니다.
- 모바일은 터치이벤트리스너를 달아줘야 터치에 반응합니다.

- `touchstart` (터치시작시 발동)
- `touchmove` (터치중일 때 계속 발동)
- `touchend `(터치종료시 발동)

- 이런 이벤트를 듣는 리스너를 부착하면 이제 터치스와이프 가능

```html
<script>
  $('.slide-box').eq(0).on('touchstart', function(){
    시작좌표 = e.touches[0].clientX;
    생략
  })

  $('.slide-box').eq(0).on('touchmove', function(){
    생략
  })

  $('.slide-box').eq(0).on('touchend', function(){
    생략
  })

</script>
```

기존 코드를 이렇게 바꾸면 됩니다.

- 그럼 모바일에서도 아까랑 똑같이 동작하는데 주의사항은 
- e.clientX를 e.touches[0].clientX 이걸로 바꾸면 됩니다.
- 왜냐면 터치는 여러 손가락으로 할 수 있어서 그 중 몇번째 손가락인지 지정해줘야합니다. 
- touchend 이벤트리스너에선 e.clientX 말고 e.changedTouches[0].clientX 쓰면 됩니다. 


Q. 어 그럼 PC환경에서는 안되는데요?

그럼 기존걸 touch로 바꾸는게 아니라 touch 이벤트리스너3개를 하단에 추가하면 됩니다. 


(참고)
`Hammer.js` 같은거 가져다쓰면 조금 쉽게 기능개발이 가능합니다. 

- 브라우저 호환성도 알아서 잡아주고
- 이벤트리스너 6개대신 1개만 써도 되고 
- 스와이프, pinch, rotate 등 여러 제스쳐를 감지하는 이벤트리스너 제공해서 편리하고



### 간혹 쓰는 Switch 문법

- if else 문법 대신 쓸 수 있는 switch 라는 문법이 있습니다.
- if else로도 모든걸 할 수 있지만 좀 더 간단하게 적고 싶을 때 switch를 어쩌다 한 번 쓰는데
- 어떻게 쓰는지 알아봅시다. 


## switch 사용법

```javascript
let 변수 = 2 + 2;

switch (변수){
  case 3 :
    alert('변수가 3이네요');
    break
  case 4 :
    alert('변수가 4네요');
    break
}
```

- switch의 소괄호엔 조건식이 아니라 검사해볼 변수를 넣으면 됩니다. 
- 그리고 변수가 3일 때 코드 실행해주세요~ 라고 코드짜고 싶으면
- case 문법 저렇게 사용하면 됩니다.
- 그리고 코드실행을 끝내고 싶으면 break라는걸 추가해주면 됩니다. 그럼 switch 중괄호를 탈출해줍니다.

```javascript
let 변수 = 2 + 5;

switch (변수){
  case 3 :
    alert('변수가 3이네요');
    break
  case 4 :
    alert('변수가 4네요');
    break
  default : 
    alert('다 아니네')
}
```

- else같은걸 쓰고 싶으면 default : 추가해주면 됩니다.
- 그러면 case에 해당되는게 하나도 없을 때 안에 있는 코드를 실행해줍니다. 

- if로도 모든걸 만들 수 있는데 switch를 쓰는 이유는 
- 변수값에 따른 조건분기를 만들고 싶을 때 조금 더 간편하게 적을 수 있어서 그렇습니다. 