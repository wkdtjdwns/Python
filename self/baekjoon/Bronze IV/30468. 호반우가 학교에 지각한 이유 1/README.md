# [호반우가 학교에 지각한 이유 1](https://www.acmicpc.net/problem/30468)

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 1024 MB | 1350 | 933 | 894 | 70.952% |

## 문제

경북대학교의 마스코트이자 따봉 요정인 호반우는 오늘도 수업을 듣기 위해 경북대학교 정문을 지나치던 도중 정체불명의 차원문에 휘말려 이세계로 오게 되었다.

이세계의 신인 당신이 호반우가 마왕을 물리치고 지구로 돌아가 학교에 지각하지 않도록 도와주자!

호반우의 현재 스탯인 힘(𝑆𝑇𝑅), 민첩(𝐷𝐸𝑋), 지능(𝐼𝑁𝑇), 운(𝐿𝑈𝐾)에 해당하는 4가지 수가 주어진다.

4가지 스탯 중 하나의 수치를 1씩 올릴 수 있는 축복을 여러 번 사용해 호반우의 평균 스탯 수치를 𝑁$N$ 이상으로 만들려고 할 때 최소 몇 번의 축복을 사용해야 하는지 구해보자.

## 입력

첫 번째 줄에 𝑆𝑇𝑅, 𝐷𝐸𝑋, 𝐼𝑁𝑇, 𝐿𝑈𝐾이 공백을 두고 주어진다. (1 ≤ 𝑆𝑇𝑅, 𝐷𝐸𝑋, 𝐼𝑁𝑇, 𝐿𝑈𝐾, 𝑁 ≤ 100)

입력되는 모든 수는 양의 정수이다.

## 출력

호반우의 평균 스탯 수치를 𝑁 이상으로 만들기 위해 사용해야 할 축복의 최소 횟수를 출력한다.

## 예제 입력 1

```
4 5 1 2 4

```

## 예제 출력 1

```
4

```

## 예제 입력 2

```
7 12 4 23 11

```

## 예제 출력 2

```
0

```

## 힌트

호반우의 평균 스탯 수치는 다음과 같이 구할 수 있습니다.

평균 스탯 수치 = 𝑆𝑇𝑅+𝐷𝐸𝑋+𝐼𝑁𝑇+𝐿𝑈𝐾 / 4
