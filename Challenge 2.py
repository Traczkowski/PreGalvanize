#Challenge 2
"""
listz = [1,3,7,8,0,8,9]
rem = 8

The above were just test cases I was using. can be uncommented if there is a need.
"""

def remove_item(itemlist, remover):
    newlist = []
    found = False
    
    """
    The function remove_item takes in a list of items and then a single 
    item (that should match the type of the items in the list) and then
    will remove the first instance of that object from a list by creating
    newlist, which will be passed back out of the function. found is a
    placeholder boolean which will be used within the latter part of the code.
    """
    
    if itemlist.count(remover) == 0:
        return 'The item is not in the list'
    

#The first if is a catch-all that will return the required string back out of
#the function in the case that there are zero instances of the item to be
#removed in itemlist.
    
    
    else:
        for i in range(len(itemlist)):
            if not found:
                if itemlist[i] != remover:
                    newlist.append(itemlist[i])
                    
                else:
                    found = True
                    
                """
                The above code happens if remover is in the itemlist.
                For each index in itemlist, the first thing the code does
                within the for loop is to check if the "found" condition is still
                false. So long as it is false, the item from itemlist at index i
                will be appended to newlist (which is the list that is 
                returned at the end of this function). Next, the code would
                check to see if the item at index i is NOT equal to remover,
                so long as it wasn't, it was appended to newlist and it moved
                on. When itemlist at index i was equal to remover, found was
                set to true.
                """
                    
            else:
                if i == len(itemlist):
                    break
                    
                else:
                    newlist.append(itemlist[i])
                    
                """
                This part of the code was for when "found" would be equal to
                True. it would first see if i was in the last position, and
                if it was it would break the loop to prevent any issues with
                the end of the list. If it was not at the end, it would just
                add everything else in the list (so that if there were multiple
                instances of an item within the list, they would be added as
                normal once the item to be removed was taken out)
                """
        
    return newlist
                