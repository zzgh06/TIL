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

// for (let i = 0; i < 버튼.length; i++){
//   버튼.eq(i).on('click', function(){
//     // 버튼.removeClass('orange')
//     // 버튼.eq(구멍).addClass('orange')
//     // 내용.removeClass('show')
//     // 내용.eq(구멍).addClass('show')
//     탭열기(i)
//   });
// }

$('.list').click(function(e){
  // 지금 누른게 버튼 0이면 탭열기(0)
  // if (e.target == document.querySelectorAll('.tab-button')[0]){
  //   탭열기(0)
  // }
  // if (e.target == document.querySelectorAll('.tab-button')[1]){
  //   탭열기(1)
  // }
  // if (e.target == document.querySelectorAll('.tab-button')[2]){
  //   탭열기(2)
  // }

  // 이벤트리스너 1개만 써도 개발가능
  탭열기(e.target.dataset.id)
})

// 함수로 축약할 때 변수있으면 파라미터로 바꿔보셈
function 탭열기(구멍){
  버튼.removeClass('orange')
  버튼.eq(구멍).addClass('orange')
  내용.removeClass('show')
  내용.eq(구멍).addClass('show')
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