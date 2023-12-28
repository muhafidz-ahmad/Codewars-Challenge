var solution = function (firstArray, secondArray) {
    let sum = 0
    for (i in firstArray) {
        sum += Math.pow(Math.abs(firstArray[i] - secondArray[i]), 2)
    }
    return sum / firstArray.length
}