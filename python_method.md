# **메서드**
## **튜플(Tuple)과 세트(set)**
### 튜플
    - 불편한 값들의 나열
    - 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음
    - 변경 불가능, 반복 가능함
    - 소괄호 형태로 정의, 요소는 콤마로 구분
    - 소괄호 (()), tuple()를 통해 생성

### 세트
    - 유일한 값들의 모음(collection)
    - 순서가 없고 중복된 값이 없음(수학에서의 집합과 동일한 구조)
    - 변경 가능, 반복가능(순서가 없어 결과가 정의한 순서와 다를 수 있음)
    - 중괄호{}, set()를 통해 생성
    - 순서가 없어 별도의 값에 접근할 수 없음
    - 값 추가는 .add() 값 삭제는 .remove()
    - 세트를 활용하면 다른 컨테이너에서 중복된 값을 쉽게 제거할 수 있음

## **메서드(methods)**
### 문자열
문자열 탐색/검증
|문법|설명|
|:---:|:---:|
|s.find(x)|x의 첫 번째 위치를 반황. 없으면. -1을 반환|
|s.index(x)|x의 첫 번째 위치를 반환, 없으면, 오류 발생|
|s.isalpha()|알파벳 문자 여부|
|s.isupper()|대문자 여부|
|s.islower()|소문자 여부|
|s.istitle()|타이틀 형식 여부|


#### ***.find(x)*** : x이 첫 번째 위치를 반환, 없으면 -1을 반환
```python
print('apple'.find('p')) # 1
print('apple',find('k')) # -1
```

#### ***.index(x)*** : x의 첫 번째 위치를 반환, 없으면 오류 발생
```python
print('apple'.index('p')) # 1
```

문자열 변경
|문법|설명|
|:---:|:---:|
|s.replace(old, new[,count])|바꿀 대상 글자를 새로운 글자로 바꿔서 반환|
|s.strip([chars])|공백이나 특정 문자를 제거|
|s.split(sep=None, maxsplit=-1)|공백이나 특정 문자를 기준으로 분리|
|'separator'.join([iterable=-1])|구분자로 iterable을 합침|
|s.capitialize|가장 첫 번째 글자를 대문자로 변경|
|s.title()|공백 이후를 대문자로 변경|
|s.upper()|모두 대문자로 변경|
|s.lower()|모두 소문자로 변경|
|s.swapcase()|대, 소문자 서로 변경|

#### ***.strip([chars])*** : 특정한 문자들을 지정하면. 양쪽(strip), 왼쪽(lstrip), 오른쪽(rstrip)을 제거
```python
print('    와우!\n'.strip()) # '와우!'
print('    와우!\n'.lstrip()) # '와우!\n'
print('    와우!\n'.rstrip()) # '     와우!'
```

#### ***.split(sep=None, maxsplit=-1)*** : 문자열을 특정한 단위로 나눠 리스트로 반환
```python
print('a,b,c'.split('_')) # ['a, b, c']
print('a,b,c'.split()) # ['a', 'b', 'c']
```

### ***'separator'.join([iterable])*** : 반복가능한 컨테이너 요소들을 ''구분자로 합쳐 문자열 반환
```python
print(''.join(['3', '5'])) # 35
```

### **< list >**

|문법|설명|
|:---:|:---:|
|L.append(x)|마지막에 항목 x 추가|
|L.insert(i, x)|인덱스 i에 항목 x를 삽입|
|L.remove(x)|가장 왼쪽에 있는 항목 x를 제거|
|L.pop()|가장 오른쪽에 있는 항목을 반환 후 제거|
|L.pop(i)|인덱스 i에 있는 항목을 반환 후 제거|
|L.extend(m)|순회형 m의 모든 항목들의 리스트 끝에 추가(+= 같은 기능)|
|L.index(x, start, end)|항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환|
|L.reverse()|리스트 역순으로 뒤집음|
|L.sort()|리스트를 정렬|
|L.count(x)|항목 x가 몇 개 존재하는지 갯수를 반환|

### **< 세트(set) 메서드 >**
|문법|설명|
|:---:|:---:|
|s.copy()|세트의 얕은 복사본을 반환|
|s.add(x)|항목 x가 세트 s에 없다면 추가|
|s.pop()|세트에서 랜덤하게 항목을 반환하고 해당 항목을 제거|
|s.remove(x)|항목 x를 세트 s에서 삭제|
|s.discard(x)|항목 x가 세트 s에 있는 경우 항목 x를 세트에서 삭제|
|s.update(t)|세트 t에 있는 모든 항목 중 세트에 없는 항목을 추가|
|s.clear()|모든 항목을 제거|