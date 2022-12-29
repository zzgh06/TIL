# **Branch(브랜치)**

### **브랜치**
 - 브랜치란?
 > - 브랜치란 독립적으로 어떤 작업을 진행하기 위한 개념
 > - 필요에 의해 만들어지는 각각의 브랜치는 다른 브랜치의 영향을 받지 않기 때문에, 여러 작업을 동시에 진행할 수 있다.
 > - 이렇게 만들어진 브랜치는 다른 브랜치와 병합(Merge)함으로써, 작업한 내용을 다시 새로운 하나의 브랜치로 모을 수 있다.

- 브랜치 주요 명령어
 1) 브랜치 생성
 > `(master)` $ git branch {브랜치 이름}
 2) 브랜치 이동
 > `(master)` $ git checkout {브랜치 이름}
 3) 브랜치 생성 및 이동
 > `(master)` $ git checkout -b {브랜치 이름}
 4) 브랜치 목록
 > `(master)` $ git branch
 5) 브랜치 삭제
 > `(master)` $ git branch -d {브랜치 이름}

### **변경 이력 병합(Merge)하기**
 - **Merge**
 > - 내가 끌어온 저장소가 최신 버전이 아닌 경우, 즉 내가 pull을 실행한 후 다른 사람이 push를 하여 원격 저장소를 업데이트 해버린 경우에는 push 요청이 거부됨.
 > - 이런 경우 병합(Merge)이라는 작업을 진행하여 다른 사람의 업데이트 이력을 내 저장소에도 갱신해야함. 만약 병합하지 않은 채로 이력을 덮어쓸 경우 다른 사람이 push g한 업데이트 내역(커밋)이 사라짐.

 - **충돌 해결하기**
 > - 병합 기능은 Git 에서 변경한 부분을 자동으로 통합해 주는 기능, 그러나 경우에 따라 자동으로 병합할 수 없는 경우도 있음.
 > - 바로 원격 저장소와 로컬 저장소 양쪽에서 파일의 동일한 부분을 변경한 경우, 이 경우 두 변경 내용중 어느 쪽을 저장할 것인지 자동으로 판단 할 수 없기 때문에 충돌이 발생, **이 부분을 우리가 직접 수정해 주어야 한다**

### Git Flow
> - Git을 활용하여 협업하는 흐름, 브랜치를 활용한 전략

- **기본원칙**
> - master branch는 반드시 배포 가능한 상태여야 한다.
> - feature branch는 각 기능의 의도를 알 수 있도록 작성.
> - commit message는 매우 중요, 명확하게 작성
> - Pull Request를 통해 협업을 진행한다.
> - 변경사항을 반영하고 싶을 때, master branch에 병합한다.

- **GitHub Flow Models**
> - Shared Repository Model
> - Fork & Pull Model
> - `참고` : 가장 큰 차이점은 내가 원격 저장소에 직접적인 push 권한이 있는지 여부

- **Shared Repository Model**
> - Shared Repository Models은 동일한 저장소를 공유
> 1) 팀원 초대 및 저장소 Clone
>    - collaborator에 등록 되어야 해당 저장소에 대한 push 권한이 부여(settings `클릭` > collaborators `클릭`)
>    - 이메일을 통한 초대 수락(저장소 주소 뒤에 /invitation 해도 가능)
>    - clone 이후 작업에 맞춘 작업 환경 설정을 마무리
> 2) 개별 작업용 branch 생성 및 작업
>    - master branch 외 다른 개별적인 브랜치를 생성하여 작업한다.
> 3) commit으로 작업의 이력(history)을 남긴다.
> 4) 완성된 코드는 원격 저장소에 push를 한다.
> 5) Github에 들어가서 Pull Request 버튼을 누르고 PR과 관련된 설정을 진행한 후 요청을 생성
> 6) 작성된 코드를 확인 후 병합(Merge pull request `클릭`)
> 7) merge되었으면 로컬 저장소에서 개별작업하던 branch는 삭제 후 master branch를 업데이트 한다.

- **Fork & Pull Model**
> - Fork & Pull Model은 Repository에 Collaborator에 등록되지 않은 상태에서 진행
> - GitHub 기반의 오픈소스 참여 과정에서 쓰이는 방식
>     - Forking project repository : 원격저장소를 fork, 내 저장소에서 복제본을 가져와 로컬에서 작업 후 원격저장소에 push하는 것(나중에 허락 받는 것)
> - 이후 작업(commit, push, PR) Shared Repository Models와 동일