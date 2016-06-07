def find_most_frequent(text):
    """
        Function, that takes 1 argument, it's a text of any length
        Text may contain alphabetical letters, spaces and punctuation characters
        Return list of words in lower register, which are appearing it text more often than others.
        Words that wrote over hyphen considering as two words.
        Register of words does not matter.
    """
    #list for end result
    result = []
    #list for words that repeat more then once in string
    common_words = []
    #list for words without any non-alphabetical characters
    lst = []
    #variable for counting how much every word appearing in string
    word_count = 0
    #variable for counting maximum value of appearing particular word
    most_word = 0

    #iterate over text and search and add all non-alphabetical items to lst
    for i in text:
        if i == "-" or i == "," or i == "/":
            lst.append(" ")
        elif i == "." or i == ":" or i == ";" or i == "!" or i == "?":
            pass
        else:
            lst.append(i)

    #convert all items in lst to lower register        
    lst = [i.lower() for i in lst]

    #convert lst to string
    lst = "".join(lst)

    #convert lst to list with words
    lst = lst.split()

    #iterate over word in lst and if word appear in more than once add it to common_words list
    for word in lst:
        if lst.count(word) > 1:
            common_words.append(word)

    #for every word in common_words set variable word_count to value of particular word appearing in a string        
    for word in common_words:
        word_count = common_words.count(word)
    #if word_count bigger than most_word, than most_word set to word_count value    
        if word_count > most_word:
            most_word = word_count

    #for word in common_words adding words with maximum values to result list        
    for x in common_words:
        if common_words.count(x) == most_word:
            result.append(x)

    #remove all duplicates from result
    for char in result:
        while result.count(char) > 1:
            result.remove(char)

    #sorting list of results
    result.sort()        

    return result        
            
          

            
    
    
            
    
    

            
   
   
    
   
