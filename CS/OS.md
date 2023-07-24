# 운영체제 - 이화여자대학교 : 반효경

## 운영체제란?

운영체제란?
  - 컴퓨터 하드웨어 바로 위에 설치되어 사용자 및 다른 모든 소프트웨어와 하드웨어를 연결하는 소프트웨어 계층

운영체제의 목적
  1. 컴퓨터 시스템을 편리하게 사용할 수 있는 환경을 제공
    - 운영체제는 동시 사용자/프로그램들이 각각 독자적 컴퓨터에서 수행되는 것 같은 환상을 제공
    - 하드웨어를 직접 다루는 복잡한 부분을 운영체제가 대행

  2. 컴퓨터 시스템의 자원을 효율적으로 관리 ⭐
    - CPU, 메모리, I/O 디바이스 등의 효율적 관리
      - 주어진 자원으로 최대한의 성능을 내도록 => 효율성
      - 특정 사용자/프로그램의 지나친 불이익이 발생하지 않도록 => 형평성
    - 사용자 및 운영체제 자신의 보호
    - 실행중인 프로그램들에게 짧은 시간씩 CPU를 번갈아 할당
    - 실행중인 프로그램들에 메모리 공간(유한한 공간)을 적절히 분배

컴퓨터 시스템의 구조
  - 컴퓨터 내부 : CPU, 메모리(프로그램 A,B,C 운영체제(핵심 : 커널))
  - 입출력(I/O) 디바이스 : 디스크, 키보드, 프린트, 모니터
    - CPU의 작업 공간을 메모리라고 볼 수 있으며, 기본적으로 CPU는 컴퓨터 내부에 메모리에만 접근할 수 있기 때문에 입출력(I/O) 디바이스 중 디스크의 파일이 필요할 때는 입출력(I/O) 디바이스에 따로 붙어있는 I/O 컨트롤러라는 일종의 작은 CPU와 메모리에 올라온 파일을 올려서 그 파일을 컴퓨터 내부의 메모리에 올려 CPU가 그 파일을 읽는다
    
운영체제의 기능  
  - CPU 스케줄링 : 어떤 프로그램에게 CPU 사용권을 줄까?
  - 메모리 관리 : 한정된 메모리를 어떻게 쪼개어 쓰지?
  - 디스크 스케줄링 : 디스크에 들어온 요청을 어떤 순서로 처리할까?(요청이 들어온 순서대로 하면 비효율적 나중에 들어온 요청이라고 할지라도 그것을 먼저 처리하는 것이 효율적이라고 판단된다면 순서를 뒤집는 것이 디스크 스케줄링의 기능)
  - 인터럽트, 캐싱 : 빠른 CPU와 느린 I/O 장치간 속도차를 어떻게 극복하지?
    - 캐싱 : 중간 계층을 두는 것
    - 인터럽트 : CPU가 프로그램을 실행하고있을 때, 입출력하드웨어(I/O 장치) 등의 장치에 예외상황이 발생하여 처리가 필요할 경우에 CPU에게 알려 처리할 수 있도록 하는 것

  CPU 스케줄링
    1. CPU 스케줄링 FCFS(First-Come First-Served)
      1) 프로세스의 도착 순서 : p1, p2, p3
      waiting time : p1=0; p2=24;, p3=27
      average waiting time = (0+24+27)/3 = 17

      2) 프로세스의 도착 순서 : p2, p3, p1
      waiting time : p1=6; p2=0;, p3=3
      average waiting time = (6+0+3)/3 = 3

      해당 방법은 프로세스 사용시간이 더 오래 걸리는 것이 더 먼저 도착했는지 나중에 도착했는지에 따라 밸류에이션이 굉장히 커짐

    2. CPU 스케줄링 SJF(Shortest-Job-First)
      - 금번 CPU 사용시간이 가장 짧은 프로세스를 제일 먼저 스케줄
      - SJF는 minimum average waiting time을 보장
      - 프로세스의 도착 순서 : p1 : 24s, p2 : 4s, p3 : 2s
      - 프로세스의 처리 순서 : p3, p2, p1
      - 문제 : Starvation(기아 현상) 발생 가능(형평성이 떨어짐)

    3. CPU 스케줄링 Round Robin(RR)
      - 각 프로세스는 동일 크기의 CPU 할당시간을 가짐
      - 할당시간이 끝나면 인터럽트가 발생하여 프로세스는 CPU를 빼앗기고 CPU 큐의 제일 뒤에 줄을 섬
      - n개의 프로세스가 CPU 큐에 있는 경우
        - 어떤 프로세스도 (n-1)*할당시간 이상 기다리지 않음
        - 대기시간이 프로세스의 CPU 사용시간에 비례

  메모리 관리
    한정된 메모리 내에 새롭게 들어오는 페이지를 처리하기 위해서 어떻게 해야하는가?
    예를 들어 메모리 공간이 4페이지 밖에 없을 경우 5번째 페이지를 보관하기 위해서는 어떤 페이지를 삭제해야하는지 골라야할 때 두가지 방법을 고려해볼 수 있다
      - LRU(가장 오래 전에 참조 페이지 삭제)
      - LFU(참조횟수가 가장 적은 페이지 삭제)

  디스크 스케줄링
    디스크 접근 시간의 구성
      - 탐색시간(Seek time) : 헤드를 해당 트랙(실린더)으로 움직이는데 걸리는 시간
      - 회전지연(Rotational latency) : 헤드가 원하는 섹터에 도달하기까지 걸리는 시간
      - 전송시간(Transfer time) : 실제 데이터의 전송 시간

    디스크 스케줄링(Disk Scheduling)
      - seek time을 최소화하는 것이 목표
      - seek time = seek distance

      디스크 스케줄링 SCAN
        - 헤드가 디스크의 한쪽 끝에서 다른쪽 끝으로 이동하며 가는 길목에 있는 모든 요청을 처리한다
        - 다른 한쪽 끝에 도달하면 역방향으로 이동하며 오는 길목에 있는 모든 요청을 처리하며 다시 반대쪽 끝으로 이동한다

    저장장치 계층구조와 캐싱
      primary(executable)
      - 레지스터
      - 캐시 메모리
      - 메인 메모리
      secondary
      - 마그네틱 디스크
      - 옵티컬 디스크
      - 마그네틱 테이프

      - 위로 올라갈수록 빠르고 비싸며, primary(executable) 부분은 CPU에서 접근이 가능하며 휘발성의 특징을 갖고 있으며 secondary은 I/O 의 영역으로 CPU에서 직접 접근이 불가능하며 휘발성의 특징을 갖지 않는다
      - 캐싱 계층을 두는 이유는 장치간 속도 차이를 완충 : 중간에 데이터를 복사를 해놓음으로서 장치간 이동을 끝까지 내려갔다가 다시 올라가는 것이 아니라 중간에 데이터를 저장해놓은 캐싱까지만 감으로서 장치간 속도 차이를 완충할 수 있다

    플래시메모리
      - 플래시메모리
        - 반도체장치(하드디스크: 마그네틱)
        - NAND형(스토리지), NOR형(임베디드 코드저장용)

      - 플래시메모리의 특징
        - Nonvolatile
        - Low power consumption
        - Shock resistance
        - Small size
        - Lightweight
        - 쓰기 횟수 제약

      - 플래시메모리의 사용형태
        - 휴대폰, PDA 등 임베디드 시스템 구성용
        - USB용 메모리 스틱
        - 디지털카메라 등의 SD카드
        - 모바일 장치 뿐 아니라 대용량 시스템에서 SSD란 이름으로 하드디스크 대체 시도

# 컴퓨터시스템의 구조

## 운영 체제란?

운영 체제란?
  - 컴퓨터 하드웨어 바로 위에 설치되어 사용자 및 다른 모든 소프트웨어와 하드웨어를 연결하는 소프트웨어 계층
  - 협의의 운영체제(커널)
    - 운영체제의 핵심 부분으로 메모리에 상주하는 부분
  - 광의의 운영체제
    - 커널 뿐 아니라 각종 주변 시스템 유틸리티를 포함한 개념

  운영 체제의 목적
  1. 컴퓨터 시스템을 편리하게 사용할 수 있는 환경을 제공
    - 운영체제는 동시 사용자/프로그램들이 각각 독자적 컴퓨터에서 수행되는 것 같은 환상을 제공
    - 하드웨어를 직접 다루는 복잡한 부분을 운영체제가 대행

  2. 컴퓨터 시스템의 자원을 효율적으로 관리 ⭐
    - 프로세서, 기억장치, 입출력 장치 등의 효율적 관리
      - 사용자간의 형평성 있는 자원 분배(실행중인 프로그램들에게 짧은 시간씩 CPU를 번갈아 할당, 실행중인 프로그램들에 메모리 공간을 적절히 분배)
      - 주어진 자원으로 최대한의 성능을 내도록
    - 사용자 및 운영체제 자신의 보호
    - 프로세스, 파일, 메시지 등을 관리
  
  운영 체제의 분류
    - 동시 작업 가능 여부
      - 단일 작업(single tasking)
        - 한 번에 하나의 작업만 처리
          예) MS-DOS 프롬프트 상에서는 한 명령의 수행을 끝내기 전에 다른 명령을 수행시킬 수 없음

      - 다중 작업(multi tasking)
        - 동시에 두 개 이상의 작업 처리
          예) UNIX, MS Windows 등에서는 한 명령의 수행이 끝나기 전에 다른 명령이나 프로그램을 수행할 수 있음

    - 사용자의 수(동시에)
      - 단일 사용자(single user)
        예) MS-DOS, MS Windows

      - 다중 사용자(multi user)
        예) UNIX, NT server

    - 처리방식
      - 일괄처리(batch processing)
        - 작업 요청이 일정량 모아서 한꺼번에 처리
        - 작업이 완전 종료될 때까지 기다려야 함
        예) 초기 Punch Card 처리 시스템

      - 시분할(time sharing)
        - 여러 작업을 수행할 때 컴퓨터 처리 능력을 일정한 시간 단위로 분할하여 사용
        - 일괄 처리 시스템에 비해 짧은 응답 시간을 가짐
          예) UNIX
        - interactive(상호활동적인) 한 방식

      - 실시간(Realtime OS)
        - 정해진 시간 안에 어떠한 일이 반드시 종료됨이 보장되어야하는 실시간시스템을 위한 OS
        - 예) 원자로/공장 제어, 미사일 제어, 반도체 장비, 로보트 제어

      - 실시간 시스템의 개념 확장
        - Hard realtime system(경성 실시간 시스템)
        - Soft realtime system(연성 실시간 시스템)

    용어
    - Multitasking
    - Multiprogramming
    - Time sharing
    - Multi process
      - 구분
        - 위의 용어들은 컴퓨터에서 여러 작업을 동시에 수행하는 것을 뜻한다
        - Multiprogramming은 여러 프로그램이 메모리에 올라가 있음을 강조
        - Time sharing은 CPU의 시간을 분할하여 나누어 쓴다는 의미를 강조

    - Multiprocessor
      - 하나의 컴퓨터에 CPU (Processor)가 여러 개 붙어 있음을 의미

  운영체제의 구조  
  - CPU 스케줄링 : 어떤 프로그램에게 CPU 사용권을 줄까?
  - 메모리 관리 : 한정된 메모리를 어떻게 쪼개어 쓰지?
  - 파일 관리 : 디스크에 파일을 어떻게 보관하지?
  - 입출력 관리 : 각기 다른 입출력장치와 컴퓨터 간에 어떻게 정보를 주고 받게 하지?
  - 프로세스 관리
    - 프로세스의 생성과 삭제
    - 자원 할당 및 반환
    - 프로세스 간 협력

  컴퓨터 시스템의 구조

  ![컴퓨터시스템의구조](./images/컴퓨터시스템의구조.png)

    Mode bit
      - 사용자 프로그램의 잘못된 수행으로 다른 프로그램 및 운영체제에 피해가 가지 않도록 하기 위한 보호 장치 필요
      - Mode bit을 통해 하드웨어적으로 두 가지 모드의 operation 지원
        1 사용자 모드 : 사용자 프로그램 수행
        0 모니터 모드(=커널모드, 시스템모드) : OS 코드 수행
        - 보안을 해칠 수 있는 중요한 명령어는 모니터 모드에서만 수행 가능한 '특정명령'으로 규정
        - Interrupt나 Exception 발생시 하드웨어가 mode bit을 0으로 바꿈
        - 사용자 프로그램에게 CPU를 넘기기 전에 mode bit을 1로 셋팅

    Timer
      - 타이머
        - 정해진 시간이 흐른 뒤 운영체제에게 제어권이 넘어가도록 인터럽트를 발생시킴
        - 타이머는 매 클럭 틱 때마다 1씩 감소
        - 타이머 값이 0이 되면 타이머 인터럽트 발생
        - CPU를 특정 프로그램이 족접하는 것으로부터 보호
      - 타이머는 time sharing을 구현하기 위해 널리 이용됨
      - 타이머는 현재 시간을 계산하기 위해서도 사용

    Device Controller
      - I/O device controller
        - 해당 I/O 장치유형을 관리하는 일종의 작은 CPU
        - 제어 정보를 위해 control register, status register를 가짐
        - local buffer를 가짐(일종의 data register)
      - I/O는 실제 device와 local buffer 사이에서 일어남
      - Device controller는 I/O가 끝났을 경우 interrupt로 CPU에 그 사실을 알림

      - device driver(장치구동기)
        : OS 코드 중 각 장치별 처리루틴 -> software
      - device controller(장치제어기)
        : 각 장치를 통제하는 일종의 작은 CPU -> hardware

    인터럽트(Interrupt)
      - 현대의 운영체제는 인터럽트에 의해 구동됨
      - 인터럽트
        : 인터럽트 당한 시점의 레지스터와 program counter를 save 한 후 CPU의 제어를 인터럽트 처리 루틴에 넘긴다
      - 인터럽트의 넓은 의미
        - Trap (소프트웨어 인터럽트)
          - Exception : 프로그램이 오류를 범한 경우
          - System call : 사용자 프로그램이 운영체제의 서비스를 받기 위해 커널 함수를 호출하는 것

        - Interrupt (하드웨어 인터럽트 : 디스크 컨트롤러, 타이머) 
        : 하드웨어가 발생시킨 인터럽트 I/O 디바이스에 의한 인터럽트로 프로그램이 하드웨어, I/O 디바이스에 담긴 파일을 읽어와야 할 때, CPU는 직접 접근을 할 수 없기 때문에 I/O 디바이스를 전담하는 Controller에게 부탁(device driver)하여 파일을 불러오며 발생하는 인터럽트

    동기식 입출려과 비동기식 입출력
      - 동기식 입출력(synchronous I/O)
        - I/O 요청 후 입출력 작업이 완료된 후에야 제어가 사용자 프로그램에 넘어감
        - 구현 방법 1
          - I/O가 끝날 때까지 CPU를 낭비시킴
          - 매시점 하나의 I/O만 일어날 수 있음
        - 구현 방법 2
          - I/O가 완료될 때까지 해당 프로그램에게서 CPU를 빼앗음
          - I/O 처리를 기다리는 줄에 그 프로그램에게서 줄 세움
          - 다른 프로그램에게 CPU를 줌
      - 비동기식 입출력(asynchronous I/O)
        - I/O가 시작된 후 입출력 작업이 끝나기를 기다리지 않고 제어가 사용자 프로그램에 즉시 넘어감
      - 두 경우 모두 I/O의 완료는 인터럽트로 알려줌

    DMA(Direct Memory Access)
      - DMA (Direct Memory Access)
        - 빠른 입출력 장치를 메모리에 가까운 속도로 처리하기 위해 사용
        - CPU의 중재 없이 device controller가 device의 buffer storage의 내용을 메모리에 block 단위로 직접 전송
        - 바이트 단위가 아니라 block 단위로 인터럽트를 발생시킴


# 프로세스 관리

프로그램의 실행(메모리 load)

  프로그램 실행 -> 각자의 주소공간(가상 메모리) : 코드, 데이터, 스택 ->(Address transition)-> 물리적 메모리

커널 주소 공간의 내용
  - code : 커널 코드
    - 시스템콜, 인터럽트 처리 코드
    - 자원관리를 위한 코드
    - 편리한 서비스 제공을 위한 코드
  - data : PCB, CPU, mem, disk
  - stack : 프로세스별 커널 스택

사용자 프로그램이 사용하는 함수
  - 함수(function)
    - 사용자 정의 함수
      : 자신의 프로그램에서 정의한 함수
    - 라이브러리 함수
      - 자신의 프로그램에서 정의하지 않고 갖다 쓴 함수
      - 자신의 프로그램의 실행 파일에 포함되어 있다
    - 커널 함수
      - 운영체제 프로그램의 함수
      - 커널 함수의 호출 = 시스템콜

프로세스의 개념

  ![프로세스의 개념](./images/프로세스의_개념.png)
  - "Process is program in execution" : 실행중인 프로그램
  - 프로세스의 문맥(context)
    - CPU 수행 상태를 나타내는 하드웨어 문맥
      - Program Counter
      - 각종 register
    - 프로세스의 주소 공간
      - code, data, stack
    - 프로세스 관련 커널 자료 구조
      - PCB(Process Control Block)
      - Kernel stack

프로세스의 상태

  ![프로세스의 상태](./images/프로세스의상태.png)
  - 프로세스의 상태가 변경되며 수행된다
    - Running
      - CPU를 잡고 instruction을 수행 중인 상태
    - Ready
      - CPU를 기다리는 상태(메모리 등 다른 조건을 모두 만족하고)
    - Blocked(wait, sleep)
      - CPU를 주어도 당장 instruction을 수행할 수 없는 상태
      - Process 자신이 요청한 event(예 : I/O)가 즉시 만족되지 않아 이를 기다리는 상태
      - 예) 디스크에서 file을 읽어와야 하는 경우
    - Suspended(stopped)
      - 외부적인 이유로 프로세스의 수행이 정지된 상태
      - 프로세스는 통째로 디스크에 swap out 된다
      - 예) 사용자가 프로그램을 일시 정지시킨 경우(break key) 시스템이 여러 이유로 프로세스를 잠시 중단시킴(메모리에 너무 많은 프로세스가 올라와 있을 때)

      * Blocked : 자신이 요청한 event가 만족되면 Ready
        Suspended : 외부에서 resume해주어야 Active

Process Control Block(PCB)
  - PCB
    - 운영체제가 각 프로세스를 관리하기 위해 프로세스당 유지하는 정보
    - 다음의 구성 요소를 가진다(구조체로 유지) 
      (1) OS가 관리상 사용하는 정보
        - Process state, Process ID
        - scheduling information, priority
      (2) CPU가 수행 관련 하드웨어 값
        - Program counter, register
      (3) 메모리 관련
        - Code, data, stack의 위치 정보
      (4) 파일 관련
        - Open file descriptors 

문맥 교환(Context Switch)
  - CPU를 한 프로세스에서 다른 프로세스로 넘겨주는 과정
  - CPU가 다른 프로세스에게 넘어갈 때 운영체제는 다음을 수행
    - CPU를 내어주는 프로세스의 상태를 그 프로세스의 PCB에 저장
    - CPU를 새롭게 얻는 프로세스의 상태를 PCB에서 읽어옴

프로세스를 스케줄링하기 위한 큐
  - Job queue : 현재 시스템 내에 있는 모든 프로세스의 집합
  - Ready queue : 현재 메모리 내에 있으면서 CPU를 잡아서 실행되기를 기다리는 프로세스의 집합
  - Device queues : I/O device의 처리를 기다리는 프로세스의 집합
  - 프로세스들은 각 큐들을 오가며 수행된다

스케줄러
  - Long-term scheduler(장기 스케줄러 or job scheduler)
    - 시작 프로세스 중 어떤 것들을 ready queue로 보낼지 결정
    - 프로세스에 memory(및 각종 자원)을 주는 문제
    - degree of Multiprogramming을 제어
    - time sharing system에는 보통 장기 스케줄러가 없음(무조건 ready)
  - Short-term scheduler(단기 스케줄러 or CPU scheduler)
    - 어떤 프로세스를 다음번에 running 시킬지 결정
    - 프로세스에 CPU를 주는 문제
    - 충분히 빨라야 함(millisecond 단위)
  - Medium-term scheduler(중기 스케줄러 or Swapper)
    - 여유 공간 마련을 위해 프로세스를 통째로 메모리에서 디스크로 쫓아냄
    - 프로세스에게서 memory를 뺏는 문제
    - degree of Multiprogramming을 제어

프로세스의 상태도

  ![프로세스상태도](./images//프로세스상태도.png)

Thead(CPU 수행의 실행단위)
  - "A thead(or lightweight process) is a basic unit of CPU utilization"
  - Thead의 구성
    - program counter
    - register set
    - stack space
  
  - Thead가 동료 thead와 공유하는 부분(=task)
    - code section
    - data section
    - OS resources

  - 전통적인 개념의 heavyweight process는 하나의 thead를 가지고 있는 task로 볼 수 있다

  - 다중 스레드로 구성된 태스크 구조에서는 하나의 서버 스레드가 blocked(waiting) 상태인 동안에도 동일한 태스크 내의 다른 스레드가 실행(running)되어 처리를 할 수 있다

  - 동일한 일을 수행하는 다중 스레드가 협력하여 높은 처리율(throughput)과 성능 향상을 얻을 수 있다

  - 스레드를 사용하면 병렬성을 높일 수 있다
  
  ![싱글,멀티스레드](./images//싱글,멀티스레드.png)

Benefits of Threads

  - Responsiveness : 응답성이 빠르다
  - Resource Sharing : 자원공유(동일 프로세스의 스레드)
  - Economy : 효율적(경제성)
  - Utilization of MP Architectures : 병렬성

프로세스 생성(Process Creation)

  - 부모 프로세스가 자식 프로세스 생성 : fork()
  
  - 프로세스의 트리(계층 구조)형성

  - 프로세스는 자원을 필요로 함
    - 운영체제로부터 받는다
    - 부모와 공유한다 : 가끔, 보통은 경쟁

  - 자원의 공유
    - 부모와 자식이 모든 자원을 공유하는 모델
    - 일부를 공유하는 모델
    - 전혀 공유하지 않는 모델

  - 수행(Execution)
    - 부모와 자식은 공존하며 수행되는 모델
    - 자식이 종료(terminate)될 때까지 부모가 기다리는(wait) 모델

  - 주소 공간(Address space)
    - 자식은 부모의 공간을 복사함(binary and OS data)
    - 자식은 그 공간에 새로운 프로그램을 올림

  - 유닉스의 예
    - fork() 시스템 콜이 새로운 프로세스를 생성
      - 부모을 그대로 복사(OS data except PID + binary)
      - 주소 공간 할당
    - fork 다음에 이어지는 exec() 시스템 콜을 통해 새로운 프로그램을 메모리에 올림

프로세스 종료(Process Termination)

  - 프로세스가 마지막 명령을 수행한 후 운영체제에게 이를 알려줌(exit)
    - 자식이 부모에게 output data를 보냄(via wait)
    - 프로세스의 각종 자원들이 운영체제에게 반납됨

  - 부모 프로세스가 자식의 수행을 종료시킴(abort)
    - 자식이 할당 자원의 한계치를 넘어섬
    - 자식에게 할당된 태스크가 더 이상 필요하지 않음
    - 부모가 종료(exit)하는 경우
      - 운영체제는 부모 프로세스가 종료하는 경우 자식이 더 이상 수행되도록 두지 않는다
      - 단계적인 종료
