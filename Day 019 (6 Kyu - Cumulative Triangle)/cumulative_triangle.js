function cumulativeTriangle(n) {
    let curr_number = 1
    
    for (curr_row=1; curr_row<=n; curr_row++) {
      var sum = 0
      for (i=0; i<curr_row; i++) {
        sum += curr_number
        curr_number++
      }
    }
    
    return sum
  }