import math

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.pages = []
        
        page = []
        for i in range(len(collection)):
            page.append(collection[i])
            if ((i + 1) % items_per_page == 0) or (i + 1 == len(collection)):
                self.pages.append(page)
                page = []
            
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        print(self.pages)
        return len(self.pages)
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        try:
            if page_index >= 0:
                return len(self.pages[page_index])
            else:
                return -1
        except:
            return -1
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        page_index = math.floor(item_index / self.items_per_page)
        if page_index >= len(self.pages) or (page_index < 0) or (item_index >= len(self.collection)):
            return -1
        else:
            return page_index
