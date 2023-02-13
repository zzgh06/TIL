## **Filtering data**
    - Clause
      - DISTINCT : 조회 결과에서 중복된 레코드를 제거
      - WHERE : 조회 시 특정 검색 조건을 지정
      - LIMIT : 조회하는 레코드 수를 제한
    
    - Operator
      - BETWEEN
      - LIKE : 값이 특정 패텀에 일치하는지 확인 with Wildcards
      - Comparison(비교 연산자) : =, >=, <=, !=, IS, LIKE, IN, BETWEEN
      - Logical(논리 연산자) : AND(&&), OR(||), NOT(!)

**DISTINCT clause**
```sql
SELECT DISTINCT
  select_list
FROM
  table_name;
```
    - SELECT 키워드 바로 뒤에 작성해야 함
    - SELECT DISTINCT 키워드 다음에 고유한 값을 선택하려는 하나 이상의 필드를 지정

**WHERE clause**
```sql
SELECT
  select_list
FROM
  table_name
WHERE
  search_condition;
```
    - FROM clause 뒤에 위치
    - search_condition은 비교연산자 및 논리연산자를 사용하는 구문이 사용됨

**LIKE operator**
    Wildcards Characters
    '%' : 0개 이상의 문자열과 일치하는지 확인
    '_' : 단일 문자와 일치하는지 확인

**LIMIT clause**
```sql
SELECT
  select_list
FROM
  table_name
LIMIT [offset,] row_count;
```
    - LIMIT clause는 하나 또는 두 개의 인자를 사용(0 또는 양의 정수)
    - row_count는 조회할 최대 레코드 수를 지정

## **Grouping data**
> 레코드를 그룹화하여 요약본 생성 with 집계함수(Aggregation Functions)

    Aggregation Functions : 값에 대한 계싼을 수행하고 단일한 값을 반환하는 함수
     - SUM, AVG, MAX, MIN, COUNT
```sql
SELECT
  c1, c2,..., cn, aggregation_function(ci)
FROM
  table_name
GROUP BY
  c1, c2, ..., cn;
```