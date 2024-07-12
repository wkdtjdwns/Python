# [Rust Study](https://www.acmicpc.net/problem/30033)

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 1024 MB | 1723 | 1260 | 1160 | 73.048% |

## 문제

취준생에서 직장인이 된 임스는 Rust 프로그래밍 언어를 공부하고자 책을 구매했다.

임스는 퇴근 후에 책을 정해진 페이지 수 이상으로 공부하기로 계획하였다.

임스가 공부하고자 한 일수와 공부하고자 계획한 페이지 수, 실제 공부한 페이지 수가 주어졌을 때 임스가 계획을 성실히 지킨 횟수를 구해 보자.

## 입력

첫 번째 줄에는 임스가 계획하고 공부한 일수 𝑁이 주어진다. (1 ≤ 𝑁 ≤ 1000)

두 번째 줄에는 임스가 공부하고자 계획한 페이지 수 𝐴1, 𝐴2, ⋯, 𝐴𝑁가 공백으로 구분되어 주어진다. (1 ≤ 𝐴𝑖 ≤ 100)

세 번째 줄에는 임스가 공부한 페이지 수 𝐵1, 𝐵2, ⋯, 𝐵𝑁가 공백으로 구분되어 주어진다. (1 ≤ 𝐵𝑖 ≤ 100)

입력은 모두 양의 정수로 주어진다.

## 출력

임스가 계획한 페이지 수 이상으로 공부한 횟수를 출력한다.

## 예제 입력 1

```
5
5 6 7 8 9
5 5 5 10 10

```

## 예제 출력 1

```
3
```