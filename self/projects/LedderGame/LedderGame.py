import random

def draw_ladder(names, possible_results):
    # 입력된 결과 목록을 참여자 수에 맞게 확장함
    extended_results = possible_results * (len(names) // len(possible_results)) + possible_results[:len(names) % len(possible_results)]
    # 확장된 결과 목록에서 결과를 무작위로 선택함
    results = random.sample(extended_results, len(names))
    return results

def print_ladder(names, results):
    # 결과에 따른 참여자들을 모으는 딕셔너리를 생성함
    result_groups = {}
    for name, result in zip(names, results):
        if result in result_groups:
            result_groups[result].append(name)
        else:
            result_groups[result] = [name]

    # 결과를 그룹별로 출력
    print("\n사다리 결과:")
    for result, names in result_groups.items():
        names_str = ', '.join(names)  # 결과 그룹에 속한 이름들을 하나의 문자열로 합침
        print(f"{result} -> {names_str}")

def main():
    num_people = int(input("참여할 사람 수를 입력하세요: "))
    names = []
    possible_results = []

    for i in range(num_people):
        name = input(f"{i + 1}번째 참여자의 이름을 입력하세요: ")
        names.append(name)

    num_results = int(input("결과의 수를 입력하세요: "))
    for i in range(num_results):
        result = input(f"{i + 1}번째 결과를 입력하세요: ")
        possible_results.append(result)

    results = draw_ladder(names, possible_results)
    print_ladder(names, results)

if __name__ == "__main__":
    main()
