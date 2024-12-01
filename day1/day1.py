
def main():

    print("Hello world")

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

    print(totalDistance)

if __name__ == "__main__":
    main()