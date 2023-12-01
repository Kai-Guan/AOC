with open("1_input.txt", "r") as file:
    total = 0
    words = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    def get(string):
        for i in range(1, len(string)):
            for word in words:
                if word in string[0:i]:
                    return int(words[word])
            if [x for x in string[0:i] if x.isdigit()]:
                return int([x for x in string[0:i] if x.isdigit()][0])
    def get_reversed(string):
        for i in range(len(string)-1, -1, -1):
            for word in words:
                if word in string[i:len(string)]:
                    return int(words[word])
            if [x for x in string[i:len(string)] if x.isdigit()]:
                return int([x for x in string[i:len(string)] if x.isdigit()][0])

    list = []
    for line in file.readlines():
        first = 10*get(line)
        second = get_reversed(line)
        total += first+second
        list.append(first+second)
print(total)