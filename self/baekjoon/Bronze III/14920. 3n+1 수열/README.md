# [3n+1 수열](https://www.acmicpc.net/problem/14920)

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 512 MB | 3776 | 2689 | 2499 | 74.066% |

## 문제

다음의 점화식에 의해 정해지는 수열 C(n)을 생각하자:

```
     C(n+1) = C(n)/2     (C(n)이 짝수일 때)
            = 3*C(n)+1   (C(n)이 홀수일 때)

```

초항 C(1)이 자연수로 주어지면, 이 점화식은 자연수로 이루어지는 수열을 정한다.  예를 들어, C(1)=26이면, 다음의 수열이 된다.

26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2, 1, ...

이 경우, 수열의 뒷부분은 4, 2, 1 이 끝없이 반복된다. 실제로 C(1)이 5×260보다 작은 자연수인 모든 수열은 언젠가는 4, 2, 1로 끝나게 된다는 것이 알려져 있다.

주어진 입력 C(1)에 대하여 C(n)이 처음으로 1이 되는 n을 출력하시오.

## 입력

C(1); 1 ≤ C(1) ≤ 100000

## 출력

C(n)이 처음으로 1이 되는 n

## 예제 입력 1

```
26

```

## 예제 출력 1

```
11

```

## 예제 입력 2

```
7

```

## 예제 출력 2

```
17
```
