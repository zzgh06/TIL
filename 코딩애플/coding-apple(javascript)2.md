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