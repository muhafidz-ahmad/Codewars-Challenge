LOVE_LANGUAGES = ["words", "acts", "gifts", "time", "touch"]

def love_language(partner, weeks):
    # your lovely code here
    count = [{"lang": love, "count": 0} for love in LOVE_LANGUAGES]
    for day in range(weeks*2):
        for i in range(len(count)):
            if partner.response(count[i]["lang"]) == "positive":
                count[i]["count"] += 1
                if day > 0:
                    break
        sortListOfDict(count, "count")
    print(count)
    return count[0]["lang"]
    
def sortListOfDict(arr, key):
    return arr.sort(reverse=True, key=lambda x: x[key])