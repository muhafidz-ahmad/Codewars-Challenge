function digitalRoot(n) {
    let result_str = String(n)
    while (result_str.length > 1) {
        let result_int = 0
        for (digit of result_str) {
            result_int += Number(digit)
        }
        result_str = String(result_int)
    }
    return Number(result_str)
}