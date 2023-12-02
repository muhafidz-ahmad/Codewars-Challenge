function toCamelCase(str){
    let split_str = str.split(/[-_]+/)
    for (i in split_str) {
      if (i > 0) {
        split_str[i] = split_str[i][0].toUpperCase() + split_str[i].slice(1)
      }
    }
    return split_str.join("")
  }