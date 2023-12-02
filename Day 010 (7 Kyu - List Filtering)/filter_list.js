function filter_list(l) {
    return l.filter(function (el) { return Number.isInteger(el) })
  }