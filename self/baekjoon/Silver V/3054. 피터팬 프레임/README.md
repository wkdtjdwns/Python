# [피터팬 프레임 [다국어]](https://www.acmicpc.net/problem/3054)

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 2178 | 1111 | 1002 | 53.128% |

## 문제

"피터팬 프레임"은 단어를 다이아몬드 형태로 장식하는 것이다.

알파벳 X를 피터팬 프레임으로 장식하면 다음과 같다.

```
..#..
.#.#.
#.X.#
.#.#.
..#..
```

"웬디 프레임"은 피터팬 프레임과 유사하지만, 다이아몬드를 '*'로 만드는 것이다.

알파벳 X를 웬디 프레임으로 장식하면 다음과 같다.

```
..*..
.*.*.
*.X.*
.*.*.
..*..
```

단어가 주어졌을 때, 3의 배수 위치(세 번째, 여섯 번째, 아홉번째, ...)에 있는 알파벳은 웬디 프레임으로, 나머지 알파벳은 피터팬 프레임으로 장식하는 프로그램을 작성하시오.

웬디 프레임과 피터팬 프레임이 겹칠 경우에는, 웬디 프레임이 위에 있다.

## 입력

첫째 줄에 알파벳 대문자로 이루어진 최대 15글자 단어가 주어진다.

## 출력

다섯 줄에 걸쳐, 입력으로 주어진 단어를 피터팬 프레임과 웬디 프레임으로 장식한 결과를 출력한다.

## 예제 입력 1

```
A

```

## 예제 출력 1

```
..#..
.#.#.
#.A.#
.#.#.
..#..

```

## 예제 입력 2

```
DOG

```

## 예제 출력 2

```
..#...#...*..
.#.#.#.#.*.*.
#.D.#.O.*.G.*
.#.#.#.#.*.*.
..#...#...*..

```

## 예제 입력 3

```
ABCD

```

## 예제 출력 3

```
..#...#...*...#..
.#.#.#.#.*.*.#.#.
#.A.#.B.*.C.*.D.#
.#.#.#.#.*.*.#.#.
..#...#...*...#..
```
