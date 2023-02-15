#  SQL - Multi Table Queries
## Joining tables

**JOIN clause** : 둘 이상의 테이블에서 데이터에서 데이터를 검색하는 방법

    JOIN 종류
      - INNER JOIN : 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환
      - OUTER JOIN
        - LEFT JOIN : 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드를 반환
        - RIGHT JOIN : 왼쪽 테이블의 일치하는 레코드와 함께 오른쪽 테이블의 모든 레코드 반환

    INNER JOIN clause : 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환
```sql
SELECT
  select_list
FROM
  table1
INNER JOIN table2
  ON table1.fk = table2.pk;
-- FROM 절 이후 메인 테이블 지정(table1)
-- INNER JOIN 절 이우 메인 테이블과 조인할 테이블을 지정(table2)
-- ON 키워드 이후 조인 조건을 작성(조인 조건은 table1과 table2 간의 레코드를 일치시키는 규칙을 지정)
```

```sql
-- 제시된 두 테이블을 참고하여 orderNumber 값이 같은 레코드의 orders 테이블 orderNumber, status, priceEach 필드를 조회
SELECT
  t1.orderNumber, -- <테이블.필드>
  t2.status,
  t3.priceEach
FROM
  orders AS t1 -- 별칭
INNER JOIN orderdetails AS t2
  ON t1.orderNumber = t2.orderNumber;
-- join 하는 두 테이블 간의 필드명이 같은 경우 AS 문을 통해 테이블명을 변경(별칭을 지정해주지 않을 경우 코드가 길어져서 복잡해짐), 겹치는 필드명은 <테이블.필드>의 형태로 작성
```

**LEFT JOIN clause** : 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드를 반환
    
    LEFT JOIN 특징
      - 왼쪽은 무조건 표시하고, 매치되는 레코드가 없으면 NULL을 표시
      - 왼쪽 테이블 한 개의 레코드에 여러 개의 오른쪽 테이블 레코드가 일치할 경우, 해당 왼쪽 레코드를 여러번 표시

```sql
SELECT
  select_list
FROM
  table1
LEFT [OUTER] JOIN table2
  ON table1.fk = table2.pk;
-- FROM 절 이후 왼쪽 테이블 지정(table1)
-- LEFT JOIN 절 이후 오른쪽 테이블 지정(table2)
-- ON 키워드 이후 조인 조건을 작성(왼쪽 테이블의 각 레코드를 오른쪽 테이블의 모든 레코드와 일치시킴)
```

**RIGHT JOIN clause** : 왼쪽 테이블의 일치하는 레코드와 함께 오른쪽 테이블의 모든 레코드 반환

    RIGHT JOIN 특징
      - 오른쪽은 무조건 표시하고, 매치되는 레코드가 없으면 NULL을 표시
      - 오른쪽 테이블 한 개의 레코드에 여러 개의 왼쪽 테이블 레코드가 일치할 경우, 해당 오른쪽 레코드를 여러번 표시
```sql
SELECT
  select_list
FROM
  table1
RIGHT [OUTER] JOIN table2
  ON table1.fk = table2.pk;
-- FROM 절 이후 왼쪽 테이블 지정(table1)
-- RIGHT JOIN 절 이후 오른쪽 테이블 지정(table2)
-- ON 키워드 이후 조인 조건을 작성(오른쪽 테이블의 각 레코드를 왼쪽 테이블의 모든 레코드와 일치시킴)
```