# SQL-Nested Queries

## **Introduction to Sub query**
    Sub query : "A query inside a query" 단일 퀴리문에 여러 테이블의 데이터를 결합시키는 방법
    <특징>
      - 조건에 따라 하나 이상의 테이블에서 데이터를 검색하는데 사용
      - SELECT, FROM, WHERE, HAVING 절 등에서 다양한 맥락에서 사용
```sql
-- 예시 : table1 에서 가장 나이가 어린 사람을 삭제해야 한다면?
DELETE FROM table1
WHERE age = (
  SELECT MIN(age) FROM table1 -- Sub query
);
```

    EXISTS operator : 쿼리 문에서 반환된 레코드의 존재 여부를 확인
```sql
SELECT
  select_list
FROM
  table
WHERE
  [NOT] EXISTS (sub query);
-- sub query가 하나 이상의 행을 반환하면 EXISTS 연산자는 true를 반환하고 그렇지 않으면 false를 반환
-- 주로 WHERE 절에서 sub query의 반환 값 존재 여부를 확인하는데 사용

-- 예시 : 적어도 한번 이상 주문을 한 고개들의 번호와 이름 조회(고객 테이블은 customers, 주문 테이블은 orders이며 두 테이블의 customerNumber 필드를 기준으로 비교)
SELECT customerNumber, CustomerName
FROM customers
WHERE
  EXISTS (
    SELECT *
    FROM orders
    WHERE customers.customerNumber = orders.customerNumber
);
```

## **Conditional Statements**
    CASE statement : SQL 문에서 조건문을 구성
```sql
CASE case_value
  WHEN when_value1 THEN statements
  WHEN when_value2 THEN statements
  ...
  [ElSE else_statement]
END CASE;
-- case_value가 when_value와 동일한 것을 찾을 때까지 순차적으로 비교
-- when_value와 동일한 case_value를 찾으면 해당 THEN 절의 코드를 실행
-- 동일한 값을 찾지 못하면 ELSE 절의 코드를 실행(ELSE 절이 없을 때 동일한 값을 찾지 못하면 오류 발생)
```