function postfixEvaluator(string) {
    let operator = {
        "+": (a, b) => Number(a) + Number(b),
        "-": (a, b) => Number(a) - Number(b),
        "*": (a, b) => Number(a) * Number(b),
        "/": (a, b) => Math.floor(Number(a) / Number(b)), // Integer division
    };

    let elements = string.split(" ");

    if (elements.length == 1) {
        return elements[0];
    }

    let numbers = [];
    for (let i = 0; i < elements.length; i++) {
        if (!"+-*/".includes(elements[i])) {
            numbers.push(elements[i]);
        } else {
            let operand2 = numbers.pop();
            let operand1 = numbers.pop();
            numbers.push(operator[elements[i]](operand1, operand2));
        }
    }

    return numbers[0];
}