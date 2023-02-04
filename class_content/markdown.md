# 마크다운

## 마크다운 사용법 및 실습

### 마크다운의 개요
> - 텍스트 기반의 가벼운 **마크업 언어**

### 마크다운의 특징
> - 가능한 읽을 수 있도록 **최소한의 문법**으로 구조화
> - 마크다운은 단순 텍스트 문법으로 내용을 작성, **다양한 환경에서 변화**하여 보여짐

### 마크다운 활용 예시 - README.md
 #### Github 등의 사이트에서는 파일명이 **README.md**인 것을 모두 보여줌
>  - 오픈소스의 공식 문서를 작서아거나 개인 프로젝트의 프로젝트 소개서로 활용
>  - 혹은 모든 페이지에 README.md를 넣어 문서를 바로 볼 수 있도록 활용

### 마크다운 활용 예시 - 기술블로그
 #### 다양한 기술블로그에서는 정적사이트생성기
> - **Jekyll, Gatsby, Hugo, Hexo** 등을 통해 작성된 마크다운을 **HTMK, CSS, JS 파일** 등으로 변환
> - **Github pages** 기능을 통해 호스팅(외부공개)

## **마크다운 문법 정리**

### **제목(Heading)**
> - **#의 개수에** 따라 대응되는 수준이 표현가능하다.
> - 문서의 구조를 위해 작성되면 글자 크기를 조절하기 위해 사용하며는 안된다.


### **리스트(List)**
> - 순서가 있는 **리스트(ol)** 와 순서가 없는 **리스트(ul)** 로 구성

### **코드블록(Fenced Code block)**
```python
print('hello')
```

### **링크(link)**
 - [문자열](url)을 통해 링크 작성
 > [구글](https://google.com)
 > [네이버](http://naver.com)

### **이미지**
 - ![이미지 이름](이미지 주소)
 > ![1](1.jpg)

### **텍스트 강조**
 - **굵게** : **
 - *기울임* : *
 - 수평선 : ***, --- , ___
 ***
 - ~~취소선~~ : ~~


# Git bash를 활용하기 위한 기본개념
## CLI(Command Line Interface)
 - **CLI**, 커맨드 라인 인터페이스) 또는 명령어 인터페이스 가상 터미널을 통해 사용자와 컴퓨터가 상호작용하는 방식
 - 작업 명령은 사용자가 툴바 키보드 등을 통해 문자열의 형태로 입력하며, 컴퓨터로부터의 출력 역시 문자열의 형태로 주어진다.
> GUI - 그래픽 기반의 인터페이스 

> CLI - 명령 기반의 인터페이스

### 디렉토리 관리
> - **pwd(print working directory)** : 현재 디렉토리 출력
> - **cd 디렉토리이름** : 디렉토리 이동
>    - . : 현재 디렉토리 / .. : 디렉토리 이동
> - **ls(list)** : 목록
> - **mkdir(make directory)** : 디렉토리 생성
> - **touch** : 파일 생성
> - **rm 파일명** : 파일 삭제하기
>    - *rm -r 폴더명* : 폴더 삭제하기
---
# 버전관리

## Git
 - Git은 **분산버전관리시스템**으로 코드의 버전을 관리하는 도구
 - 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율
> 분산버전관리시스템(DVCS)
> - **중앙집중식버전관리시스템**은 중앙에서 버전을 관리하고 파일을 받아서 사용
> - **분산버전관리시스템**은 원격 저장소(remote repository)를 통하여 협업하고, 모든 히스토리를 클라이언트들이 공유

### 기본 명령어 
 > 기본 명령어
 > - **$ git init** : **특정 폴더를 git 저장소**를 만들어 git으로 관리
 >    - .git 폴더가 생성되며
 >    - git bash에서는 **(master)**라는 표기를 확인할 수 있음
 > - **$ git add <file>** : working directory상의 변경 내용을 **staging area**에 추가하기 위해 사용
 > - **$ git commit -m '<커밋메세지>'** :  staged 상태의 파일들을 커밋을 통해 버전으로 기록
 > - **$ git log** : 현재 저장소에 기록된 커밋을 조회 / 다양한 옵션을 통해 로그를 조회할 수 있음
 > - **$git status** : Git 저장소에 있는 파일의 상태를 확인하기 위하여 활용
 >    - 파일의 상태를 알 수 있음(Untracked files, Changes not staged for commit, Changes to be committed)
 >    - Noting to commit, working tree clean 

### 기본 흐름
> - 1)작업하면(작업한 파일 : working directory) 2) add하여 staging area에 모아 3) commit으로 버전 기록
> - Git은 파일을 **modified, staged, committed**로 관리
>   - **modified** : 파일이 수정된 상태(add 명령어를 통하여 staging area로)
>   - **staged** : 수정한 파일을 곧 커밋할 것이락 표시한 상태(commit 명령어로 저장소)
>   - **committed** : 커밋이 된 상태

### 파일 라이프사이클
> - Status로 확인할 수 있는 파일의 상태
>   - **Tracked** : 이전부터 버전으로 관리되고 있는 파일
>     - **Unmodified** : git status에 나타나지 않음
>     - **Modified** : Changes not staged for commit
>     - **Staged** : Changes to be committed
>   - **Untracked** : 버전으로 관리된 적 없는 파일(파일을 새로 만든 경우)

### Git 설정 파일(config)
- 사용자 정보(commit author) : 커밋을 하기 위해 반드시 필요
> - git config --global user.name *"username"*
>   - *GitHub*에서 설정한 *username*으로 설정
> - git config --global user.email *"my@email.com"*
>   - *GitHub*에서 설정한 *email*로 설정

- 설정확인
> - git config -l
> - git config --global -l
> - git config user.name