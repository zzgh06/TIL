
# 원격저장소 주요 개념
 ### 중앙집중버전관리시스템
 > - 로컬에서는 파일을 편집하고 서버에 반영
 > - 중앙 서버에서만 버전을 관리

 ### 분산버전관리시스템
 > - 로컬에서도 버전을 기록하고 관리
 > - 원격 저장소(remote repository)를 활용하여 협업

 ### 원격저장소 활용하기
 > - `push` : 로컬 저장소의 버전을 원격저장소로 보낸다.
 > - `pull` : 원격저장소의 버전을 로컬 저장소로 가져온다.

## GitHub 기반 원격저장소 활용
### 초기 원격저장소 설정하기
> 1) NEW Respository
> 2) 저장소 설정하기(1) respository 이름 설정 (2) 저장소 설명(옵션) (3) 공개여부 설정 (4) 저장소 설정
> 3) URL 확인 : ex) https://github.com/zzgh06/TIL.git()
> 4) 로컬 저장소에 원격 저장소 정보 설정하기
>     - ex) $ git remote add origin https://github.com/zzgh06/TIL.git( 원격저장소 추가해 Origin으로 username/저장소이름)
> 5) 원격 저장소의 정보를 확인함($ git remote -v)

### 기본명령어
> - `$ git push <원격저장소이름><브랜치>` : 로컬 저장소의 버전을 원격저장소로 보낸다
>   - push 주의사항 : 인증정보가 필수적
> - `$ git pull <원격저장소이름><브랜치이름>` : 원격저장소로부터 변경된 내역을 받아와서 이력을 병합함.
> - `$ git clone <원격저장소주소>` : 원격 저장소를 복제하여 가져옴
> - `$ git remote -v` : 원격저장소 정보확인
> - `$ git remote add <원격저장소><url>` : 원격저장소 추가
> - `$ git remote rm <원격저장소>` : 원격저장소 삭제

### Gitignore
> - 버전관리랑 상관 없는 파일(git 파일. 폴더 등을 관리X)
> - Git 저장소에 .gitignore 파일을 생성하고 해당 내용을 관리한다.
> - 작성예시
>   - 특정 파일 : a.txt(모든 a.txt), test/a.txt(텍스트 폴더의 a.txt)
>   - 특정 디텍토리 : /my_secret
>   - 특정 확장자 : *.exe
>   - 예외 처리 : !b.exe
> - `주의! 이미 커밋된 파일은 반드시 삭제를 하여야 .gitignore로 적용됨`