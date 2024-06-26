| 시간 제한 | 메모리 제한 |
| --- | --- |
| 1초 | 256 MB |

## 문제 배경

비버고등학교 학생들이 전북특별자치도 군산시로 2박 3일의 수학여행을 갔다. 학생들은 선생님의
안내에 따라 군산스탬프투어에 참여해야 한다. 선생님은 스탬프투어 시간 동안 군산의 관광지 중에서 학생이 원하는 관광지를 관람하고 스탬프를 받아오는 학생들에게 특별한 기념품을 주기로 하였다. 어떤 관광지에서 스탬프를 받기 위해서는 일정 시간 동안 관람해야 한다.

![image](https://github.com/wkdtjdwns/Python/assets/128266768/6a72c9d6-4481-4380-b80a-e71fb3ed0f44)

## 문제 도전

전체 관광지 수는 5개이고, 선생님이 정해준 관광지 수는 3개, 학생들의 수는 10명, 스탬프투어
시간은 100이다. 각 관광지의 관람 시간은 1번 관광지 30분, 2번 관광지 25분, 3번 관광지 20분, 4번 관광지 30분, 5번 관광지 35분이다. 10명의 학생의 관광지 관람 순서가 다음과 같이 주어질
때, 기념품을 받는 학생의 수를 구해보자.

| 학생 번호 | 관광지 관람 순서 | 학생 번호 | 관광지 관람 순서 |
| --- | --- | --- | --- |
| 1 | 3번 → 5번 → 2번 | 6 | 5번 → 2번 → 1번 |
| 2 | 2번 → 3번 → 5번 | 7 | 3번 → 2번 → 1번 |
| 3 | 5번 → 2번 → 3번 | 8 | 4번 → 1번 → 3번 |
| 4 | 5번 → 2번 → 1번 | 9 | 3번 → 4번 → 5번 |
| 5 | 2번 → 5번 → 1번 | 10 | 1번 → 2번 → 4번 |

## **입력 설명**

```
입력은 없다.
```

## **출력 설명**

```
기념품을 받는 학생들의 인원 수를 출력한다.
```
