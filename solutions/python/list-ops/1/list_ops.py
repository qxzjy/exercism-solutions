def append(list1, list2):
    
    return list1 + list2


def concat(lists):
    
   return [item for list in lists for item in list]


def filter(function, list):
    
    return [item for item in list if function(item)]


def length(list):
    
    return sum(1 for item in list)


def map(function, list):
    
    return [function(item) for item in list if function(item)]


def foldl(function, list, initial):
    
	for x in list:
		initial = function(initial, x)
        
	return initial

    
def foldr(function, list, initial):
    
	for x in list[::-1]:
		initial = function(initial, x)
        
	return initial


def reverse(lists):
    
    return lists[::-1]
