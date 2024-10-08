# [무알콜 칵테일 [스페셜 저지][다국어]](https://www.acmicpc.net/problem/2896)

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 2008 | 1066 | 952 | 56.365% |

## 문제

상근이와 지수는 마트에서 오렌지 주스, 사과 주스, 파인애플 주스를 구매했다. 그들은 인터넷에서 찾은 방법으로 무알콜 칵테일을 만들어 학교에서 팔려고 한다. 하지만, 칵테일을 만드는 방법을 찾기 전에 주스를 구매했기 때문에, 주스가 남을 수도 있다.

무알콜 칵테일을 만드는데 필요한 오렌지, 사과, 파인애플 주스의 비율과 구매한 주스의 양이 주어진다. 칵테일을 최대한 많이 만들었을 때, 각 주스가 얼만큼 남는지 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 구매한 오렌지, 사과, 파인애플 주스의 양 A, B, C가 주어진다. (1 ≤ A, B, C ≤ 500)

둘째 줄에 칵테일을 만드는데 필요한 각 주스의 비율 I, J, K가 주어진다. (1 ≤ I, J, K ≤ 50)

## 출력

첫째 줄에 칵테일을 최대한 많이 만들었을 때, 각 주스가 얼만큼 남는지를 공백으로 구분하여 출력한다. 정답과의 오차는 10-4까지 허용한다.

## 예제 입력 1

```
9 9 9
3 2 1

```

## 예제 출력 1

```
0 3 6

```

## 예제 입력 2

```
10 10 10
3 3 3

```

## 예제 출력 2

```
0 0 0

```

## 예제 입력 3

```
10 15 18
3 4 1

```

## 예제 출력 3

```
0 1.666667 14.666667
```
