# [간판 [다국어]](https://www.acmicpc.net/problem/5534)

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 256 MB | 1382 | 651 | 559 | 51.237% |

## 문제

상근이는 학교 근처에 새로운 편의점을 열었다. 편의점의 얼굴은 간판이라고 할 수 있다. 상근이가 새로 연 편의점은 프랜차이즈 편의점이 아니기 때문에, 간판도 자신이 직접 돈을 들여서 만들어야 한다.

근처 편의점은 이미 할인 카드, 적립 카드와 같은 정책으로 손님을 끌어 모으고 있다. 상근이는 전 품목을 5%해서 손님을 모으려고 한다. 이렇게 물건의 가격을 할인해서 팔려면, 다른 곳에 들어가는 비용을 줄어야 한다. 따라서, 상근이는 간판을 재활용해서 만들기로 했다.

편의점이 있기 전에 원래 이 곳은 간판 가게였다. 따라서, 편의점에는 이전 주인이 버리고 간 오래된 간판이 N개 있다. 상근이는 오래된 간판에서 일부 문자를 지워 새로운 간판을 만들려고 한다. 이때, 남은 문자열이 편의점 이름이어야 하고, 남은 문자가 모두 일정한 간격으로 떨어져 있어야 한다. 간판은 오래된 간판 하나에서 만들어야 하고, 간판을 자르거나 붙일수는 없다.

편의점 이름과 오래된 간판의 정보가 주어졌을 때, 만들 수 있는 새 간판의 수를 구하는 프로그램을 작성하시오. 하나의 오래된 간판에서 만들 수 있는 방법이 여러 개인 경우에도 만들 수 있는 간판은 하나이다.

## 입력

첫째 줄에 오래된 간판의 수 N이 주어진다. (1 ≤ N ≤ 100) 둘째 줄에는 상근이가 새로 연 편의점의 이름이 주어진다. 이름은 알파벳 소문자로만 이루어져 있고, 길이는 3자 이상, 25자 이하이다. 다음 N개 줄에는 이전 주인이 버리고 간 간판에 쓰여 있는 문자가 주어진다. 이 간판에 쓰여 있는 문자는 알파벳 소문자이고, 길이는 1자 이상 100자 이하이다.

## 출력

첫째 줄에 상근이가 만들 수 있는 간판의 수를 출력한다.

## 예제 입력 1

```
4
bar
abracadabra
bear
bar
baraxbara

```

## 예제 출력 1

```
3

```

## 힌트

가게의 이름은 bar이다.

첫 번째 오래된 간판에는 abracadabra가 써있다. 이때, 2, 6, 10번째 문자를 제외하고 모두 지우면 간판을 만들 수 있다.

두 번째 간판에서 2번째 문자를 지우면 bar를 만들 수 있다. 하지만, 남은 문자가 일정한 간격이 아니다.

세 번째 간판은 그냥 그대로 사용하면 된다.

네 번째 오래된 간판에서 간판을 만드는 방법은 두 가지가 있다. 한 방법은 1, 2, 3번째 문자를 제외하고 모두 지우는 방법이다. 또 다른 방법은 6, 7, 8번째 문자를 제외하고 모두 지우는 방법이다.

상근이는 1, 3, 4번째 오래된 간판에서 새 간판을 만들 수 있기 때문에 정답은 3이 된다.
