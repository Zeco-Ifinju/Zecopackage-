def top_n (items, n):
    """this is going to return an item in an array, in desc order.
    
    Args:
        items(array) list or array-like object
        n (int): num of item to return 
        
        Reeturn:
            array: top 10 items in desc order
            
        Egs:
            >>> top _n([8,3,2,7,4], 3)
            [8,7,3]
        """
    for i in range(n):  # keep sorting until will have the top n items
        for j in range(len(items) -1 -1):

            if items[j] > items[j + 1]: # if this item is bigger than next item...
                items[j], items[j + 1] = items[j + 1], items[j] #swap the two!

    # get las two items 
    top_n = items[-n:]

    # return in descending order 
    return top_n[::-1]
