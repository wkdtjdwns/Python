# [폰 노이만 [스페셜 저지][다국어]](https://www.acmicpc.net/problem/9469)

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 2041 | 1644 | 1359 | 83.579% |

## 문제

250마일 길이의 철로 양 끝에 두 기차 A와 B가 있다. A는 시속 10마일, B는 시속 15마일로 서로를 향해 출발했다. 두 기차의 출발과 동시에 기차 A 앞에 붙어있던 파리 한 마리가 기차가 충돌할 때 까지 시속 20마일로 두 기차를 사이를 왔다갔다 한다. 이때, 파리가 이동한 거리는 몇 마일일까?

폰 노이만은 문제를 듣자마자 머리속으로 무한 급수를 이용해 계산한 다음 1초도 지나지 않은 시간에 200 마일이라고 대답했다.

철로의 길이 D, 두 기차 A, B의 속도와 파리의 속도 F가 주어졌을 때, 위 문제의 답을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 테스트 케이스의 개수 P (1 ≤ P ≤ 1000)가 주어진다.

각 테스트 케이스는 다섯 숫자 N, D, A, B, F이루어져 있다. N은 테스트 케이스의 번호이고, D는 철로의 길이 (10 ≤ D ≤ 1000), A와 B는 두 기차의 속도 (1 ≤ A, B ≤ 40), F는 파리의 속도 (A ≤ B < F ≤ 50)이다. D, A, B, F는 실수이다. 실수는 최대 소수점 둘째자리까지 주어진다.

## 출력

각 테스트 케이스마다 테스트 케이스 번호를 출력하고, 두 기차가 충돌할 때까지 파리가 움직인 거리를 출력한다. 절대 오차는 10-2까지 허용한다.

## 예제 입력 1

```
5
1 250 10 15 20
2 10.7 3.5 4.7 5.5
3 523.7 15.3 20.7 33.3
4 1000 30 30 50
5 500 15 15 25

```

## 예제 출력 1

```
1 200.000000
2 7.176829
3 484.422500
4 833.333333
5 416.666667
```
