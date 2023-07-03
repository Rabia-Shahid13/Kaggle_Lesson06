def word_search(doc_list, keyword):
    '''
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    '''
    indicies = []
    keyword = keyword.lower()
    for counter, doc in enumerate(doc_list):
        doc = doc.lower()
        doc = doc.replace(",", "")
        doc = doc.replace("." "")
        doc_words = doc.split()
        if keyword in doc_words:
            indicies.append(counter)
        return indicies