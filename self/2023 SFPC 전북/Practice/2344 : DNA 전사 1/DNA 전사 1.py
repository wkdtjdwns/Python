def transcription(dna):
    nucleotide = {"A": "U", "T": "A", "C": "G", "G": "C"}
    rna= "".join((nucleotide[n] for n in DNA)) # join() -> 리스트를 사용할 때 괄호 없애고 추가하기
    return rna

n = int(input())
dna= input()

print(transcription(dna))
