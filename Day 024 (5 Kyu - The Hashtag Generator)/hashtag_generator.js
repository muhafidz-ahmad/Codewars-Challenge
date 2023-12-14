function generateHashtag (string) {
    if (string.trim() == "") {
      return false
    }
    
    let hashtag = "#" + string.trim().split(/\s+/)
      .map(word => word[0].toUpperCase() + word.toLowerCase().slice(1))
      .join("")
    
    if (hashtag.length > 140) {
      return false
    }
    
    return hashtag
  }