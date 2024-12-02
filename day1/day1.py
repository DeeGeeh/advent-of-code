from collections import Counter
import os


def main():
    file = open("source.txt", "r")
    fileContent: str = file.read()

    left = []
    right = []
    totalDistance = 0

    lines = fileContent.strip().split("\n")

    for line in lines:
        leftCol, rightCol = map(int, line.split())
        left.append(leftCol)
        right.append(rightCol)

    left.sort()
    right.sort()

    for i in range(len(left)):
        totalDistance += abs(left[i] - right[i])

    similarityScore = 0
    right = Counter(right)
    for l in left:
        similarityScore += l * right[l]

    print(totalDistance)
    print(similarityScore)
if __name__ == "__main__":
    main()