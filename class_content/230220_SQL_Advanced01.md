# SQL-Advanced

## **Transactions**
여러 쿼리문을 묶어서 하나의 작업처럼 처리하는 방법(다 성공하던지 혹은 실패하던지)
```sql
START TRANSACTION;
state_ments;
...
[ROLLBACK|COMMIT];
-- START TRANSACTION : 트랜잭션 구문의 시작을 알림
-- COMMIT : 모든 작업이 정상적으로 완료되면 한꺼번에 DB에 반영
-- ROLLBACK : 부분적으로 작업이 실패하면 트랜잭션 진행한 모든 연상을 취소하고 트랜잭션 실행 전으로 되돌림
```

```sql
-- Transaction 원리
START TRANSACTION;
INSERT INTO ... > 임시 데이터 영역 > COMMIT 할 경우 영구 데이터 영역으로 이동
INSERT INTO ... > 임시 데이터 영역 > ROLLBACK 할 경우 파기
```

```sql
-- Transaction practice
-- 트랜잭션을 사용해 users 테이블에 데이터를 삽입하고 ROLLBACK을 했을 때와 COMMIT을
-- 했을 때 users 테이블의 데이터 상태를 비교

-- ROLLBACK
START TRANSACTION;

INSERT INTO users (name)
VALUES ('james'), ('mary');

SELECT * FROM users;

ROLLBACK;

SELECT * From users;

-- COMMIT
START TRANSACTION;

INSERT INTO users (name)
VALUES ('james'), ('mary');

SELECT * FROM users;

ROLLBACK;

SELECT * From users;
```

    Transaction 정리
    - 쪼개질 수 없는 업무처리의 단위
    - 전체가 수행되거나 또는 전혀 수행되지 않아야함(All or Noting)


## **Triggers**
특정 이벤트(insert, update, delete)에 대한 응답으로 자동으로 실행되는 것
```sql
CREATE TRIGGER trigger_name
  {BEFORE | AFTER} {INSERT | UPDATE | DELETE}
  ON table_name FOR EACH ROW
  trigger_body;
-- CREATE TRIGGER 키워드 다음에 생성하려는 트리거의 이름을 지정
-- 각 레코드의 어느 시점에 트리거가 실행될지 지정(삽입, 수정, 삭제 전/후)
-- ON 키워드 뒤에 트리거가 속한 테이블의 이름을 지정
-- 트리거가 활성화될 때, 실행할 코드를 trigger_body에 지정(여러 명령문을 실행하려면 BEGIN END 키워드로 묶어서 사용)

-- Triggers practice
-- 트리거를 사용해 기존 게시글이 수정되면, 게시글의 수정일자 필드 값을 최신 일자로 업데이트 하기
DELIMITER // -- SQL의 구문 문자(;)를 변경(//)
CREATE TRIGGER beforArticleUpdate
  BEFORE UPDATE
  ON articles FOR EACH ROW
BEGIN -- 하나 이상의 구문 목록을 표현
  SET NEW.updateAt = CURRENT_TIME(); -- NEW/OLD : 트리거에서 특정 시점 전/후의 값에 접근 할 수 있도록 제공라는 키워드
END// -- BEGIN과 END 키워드로 둘러싸는 다중 구문을 구성하게 됨
DELIMITER ; -- BEGIN-END 구문 사이에 여러 SQL 문이 작성되기 때문에 하나의 트리거로써 작동될 수 있도록 사용
```

||OLD|NEW|
|:---:|:---:|:---:|
|INSERT|NO|YES|
|UPDATE|YSE|YES|
|DELETE|YES|NO|

```sql
Triggers 관련 추가 명령문

-- 트리거 목록 확인
SHOW TRIGGERS;

-- 트리거 삭제
DROP TRIGGER trigger_name;

Triggers 생성 시 에러 해결
 - 트랜잭션 생성 후 정상적으로 종료되지 않아 발생하는 에러발생 시 해결법
 - Error Code: 2013.Lost connection to MySQL server during query
 - Error Code: 2015.Lock wait timeout exceeded; try restarting transaction

-- 실행중인 프로세스 목록 확인
SELECT * FROM information_schema.INNODB_TRX;

-- 특정 프로세스의 trx_mysql_thread_id 삭제
KILL [trx_mysql_thread_id];
```