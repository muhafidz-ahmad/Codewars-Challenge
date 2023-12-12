function count(string) {
    let result = {}
    for (char of string) {
      if (isNaN(result[char])) {
        result[char] = 1
      } else {
        result[char]++
      }
    }
    return result;
  }