# [가변 배열](https://www.acmicpc.net/problem/29729)

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 1024 MB | 1066 | 608 | 556 | 60.238% |

## 문제

여러분은 가변 배열에 대하여 아는가? 아직 잘 모른다면, 아마 여러분은 배열을 고정된 크기로 선언할 것이다. 그래서 한 번쯤은 배열의 크기가 부족해 원하지 않는 채점 결과를 마주했던 기억이 있을 것이다. 가변 배열은 선언한 배열의 크기가 부족할 경우 배열의 크기를 자동으로 늘려준다! 어떻게 이것이 가능한지 알아보도록 하자.

가변 배열은 다음과 같이 동작한다.

1. 초기 크기를 원하는 만큼 지정하여 가변 배열을 생성한다. 이때 가변 배열은 비어있는 상태이다.
2. 원소를 저장해야 하는데 가변 배열이 꽉 차 있는 경우, 현재 가변 배열의 크기의 2배에 해당하는 새로운 가변 배열을 선언한다.
3. 새로 생성한 2배 크기의 가변 배열의 맨 앞에 기존 가변 배열에 있는 원소를 모두 복사한 후, 기존 가변 배열을 지우고 새로운 가변 배열로 대체한다. 이후 2번에서 저장하려고 했던 원소를 그 뒤에 저장한다.

이러한 동작을 위하여 가변 배열에서는 2개의 변수를 관리해야 한다. 하나는 가변 배열의 현재 최대 크기를 의미하는 S이고, 다른 하나는 가변 배열에서 현재 사용 중인 크기를 의미하는 U이다.

이 설명을 참조하여 가변 배열의 초기 크기와, 일련의 원소 저장 또는 삭제 명령이 주어졌을 때, 명령들을 모두 수행한 후 가변 배열의 최대 크기를 출력해 보자.

## 입력

첫 번째 줄에 가변 배열의 초기 최대 크기를 의미하는 정수 S0와 배열에 원소를 저장하는 명령의 개수를 의미하는 정수 N, 배열에서 원소를 삭제하는 명령의 개수를 의미하는 정수 M이 공백으로 구분되어 주어진다. (1 ≤ S0 ≤ 10; 1 ≤ N ≤ 100000; 0 ≤ M ≤ N)

두 번째 줄부터 N + M + 1번째 줄까지 한 줄에 하나씩 `1` 혹은 `0`이 주어진다. `1`은 배열에 원소를 저장하는 명령이고, `0`은 배열의 끝에서 원소를 삭제하는 명령이다.

가변 배열에 저장된 원소가 없을 때 삭제 명령이 주어지는 경우는 없다.

## 출력

모든 명령을 처리한 후 가변 배열의 최대 크기를 출력한다.

## 예제 입력 1

```
1 5 1
1
1
1
1
0
1

```

## 예제 출력 1

```
4

```

예제 입력 1에 대한 가변 배열의 동작 과정은 다음과 같다.

![image](https://upload.acmicpc.net/4cb3c84c-e8cc-4bf7-91bf-3f51466c86de/-/preview/)

## 힌트

대표적인 가변 배열의 예시로는 C++의 vector가 있다.
