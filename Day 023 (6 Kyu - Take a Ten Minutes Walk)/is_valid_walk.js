function isValidWalk(walk) {
  //insert brilliant code here
  let coordinate = { x: 0, y: 0, step: 0 }

  for (step of walk) {
    if (step == "n") { coordinate.y++; }
    else if (step == "s") { coordinate.y--; }
    else if (step == "e") { coordinate.x++; }
    else if (step == "w") { coordinate.x--; }
    coordinate.step++
  }

  console.log(walk)

  return coordinate.x == 0 && coordinate.y == 0 && coordinate.step == 10
}