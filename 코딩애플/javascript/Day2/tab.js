// for 반복문 쓰는 법
for (var i = 0; i < 3; i++){
  console.log('안녕')
}

// 버튼0 누르면
//  - 모든 버튼에 붙은 orange 클래스 제거
//  - 버튼0에 orange 클래스 추가
//  - 모든 div에 붙은 show 클래스 제거
//  - div0에 show 클래스 추가

// 좋은 관습 : 자주쓰는 셀렉터 변수에 넣어쓰기
var 버튼 = $('.tab-button');
var 내용 = $('.tab-content');
// eq(0) == querySelectorAll('.tap-button')[0]
for (let i = 0; i < 버튼.length; i++){
  버튼.eq(i).on('click', function(){
    버튼.removeClass('orange')
    버튼.eq(i).addClass('orange')
    내용.removeClass('show')
    내용.eq(i).addClass('show')
  });
}

// 버튼.eq(1).on('click', function(){
//   버튼.removeClass('orange')
//   버튼.eq(1).addClass('orange')
//   $('.tab-content').removeClass('show')
//   $('.tab-content').eq(1).addClass('show')
// });

// 버튼.eq(2).on('click', function(){
//   버튼.removeClass('orange')
//   버튼.eq(2).addClass('orange')
//   $('.tab-content').removeClass('show')
//   $('.tab-content').eq(2).addClass('show')
// });