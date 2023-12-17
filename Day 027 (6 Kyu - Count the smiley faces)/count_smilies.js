//return the total number of smiling faces in the array
function countSmileys(arr) {
    let face = {
        'eyes': ":;",
        'nose': "-~",
        "smiling_mouth": ")D"
    }

    let count = 0

    for (emot of arr) {
        if (face.eyes.includes(emot[0])) {
            if (face.nose.includes(emot[1])) {
                if (face.smiling_mouth.includes(emot[2])) {
                    count++
                }
            }
            else if (face.smiling_mouth.includes(emot[1])) {
                count++
            }
        }
    }

    return count
}