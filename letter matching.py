def matching_word(word):
    counter=0
    list=[]
    
    for word in word:
        if len(word)>1 and word[0]==word[-1]:
            counter=counter+1
            list.append(word)
            
    print(f"The list of words having the same character as the first and last letter:\n{list}")
    return counter


l1=['abc','cgc','abba','1219']
count=matching_word(l1)

print(f"Number of words having the same character as their first and last letter: \n{count}")        