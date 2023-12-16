function zeros(n) {
  let result = 0
  while (n > 1) {
    n = parseInt(n / 5)
    result += n
  }
  return result
}