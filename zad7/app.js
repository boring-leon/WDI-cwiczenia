const isPlanidrome = word => [...word]
.map(letter => letter.toLowerCase())
.every((letter, index, word) => letter == word[word.length - index - 1])

