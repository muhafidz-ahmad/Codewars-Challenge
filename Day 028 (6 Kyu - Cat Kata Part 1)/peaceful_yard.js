function peacefulYard(yard, minDistance) {
    // your code here
    let cats = []
    for (x in yard) {
        for (y in yard[0]) {
            if (yard[x][y] != "-") {
                cats.push([x, y])
            }
        }
    }

    // count distance every cats
    if (cats.length <= 1) {
        return true
    } else {
        for (i in cats) {
            for (j = Number(i) + Number(1); j < cats.length; j++) {
                if (euclideanDistance(cats[i], cats[j]) < minDistance) {
                    return false
                }
            }
        }
        return true
    }
}

function euclideanDistance(A, B) {
    return Math.sqrt(Math.pow(B[0] - A[0], 2) + Math.pow(B[1] - A[1], 2))
}