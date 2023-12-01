function findNextSquare(sq) {
    // Return the next square if sq is a perfect square, -1 otherwise
    let sqrt = Math.sqrt(sq)
    if (Number.isInteger(sqrt)) {
        return Math.pow(sqrt + 1, 2)
    }
    return -1;
}