#1. Write a function that counts the frequency of each character in a string using a dictionary.

def char_frequency(text):
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
input="hello world"
result=char_frequency(input)
print(result)

# 2. Create a function that finds all common elements between two lists.
def find_commonelement(list1,list2):
    return list(set(list1) & set(list2))


list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
common=find_commonelement(list1,list2)
print(common)

# 3. Write a function that reverses each word in a string but keeps their order.

def reverse_order(text):
    words = text.split()                              #text means string append reverse not working in this method so using split and giving crct format for sting with double quotes
    reversedwords=[word[::-1] for word in words]
    return(reversedwords)
input="hello world"
output=reverse_order(input)
print(output)

# 4. Create a function that converts a list of strings into a single dictionary where each string is a key with its length as the value.

def string_into_len_dict(string_list):
    return{word : len(word)for word in string_list}

words=["apple", "banana", "cherry"]
output=string_into_len_dict(words)
print("full dictionary output:",output)

# 5. Write a function that merges two dictionaries into one.

def merge_two_dict(dict1,dict2):
    merged={**dict1,**dict2}
    return(merged)
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4} 
output=merge_two_dict(dict1,dict2)  
print(output)

# 6. Create a function that splits a string into a list of words and sorts them by length.


def sorted_words_length(text):
    words=text.split()
    sorted_words=sorted(words,key=len)
    return(sorted_words)
input="The quick brown fox jumps over the lazy dog"
output=sorted_words_length(input)
print(output)

# 7. Write a function that finds the longest word in a string.

def longest_word(text):
    words=text.split()
    longest=max(words,key=len)
    return(longest)
input="The quick brown fox jumps over the lazy dog"
output=longest_word(input)
print(output)

# 8. Create a function that filters out elements from a list that don't meet a certain condition.

def filter_list_even(list):
    new_list=[]
    for i in list:
        if(i %2 == 0):
            new_list.append(i)
    return(new_list)
input_list=[1,2,3,4,5]
output=filter_list_even(input_list)
print(output)      

9.# Write a function that converts a nested list into a flat list.
def flat_list(nested):
    new_list=[]
    for i in nested:
        if isinstance (i,list):
            new_list.extend(flat_list(i))
        else:    
            new_list.append(i)
    return(new_list)   
input_list=[1, [2, 3], [4, [5, 6]]]     
output=flat_list(input_list)
print(output)

# 10. Create a function that groups elements of a list by their first letter.
def group_firstletter(words):
    grouped={}
    for word in words:
        first_letter=word[0].lower()
        if word is not grouped:
            grouped[first_letter]=[]
            grouped[first_letter].append(word)
    return(grouped)
input=["apple", "banana", "cherry", "avocado", "blueberry"]
output=group_firstletter(input)
print(output)  
#11. Write a function that removes all duplicate items from a list while preserving order.  
def remove_duplicates(items):
    orginal=[] 
    seen=set()
    for item in items:
        if item not in seen:
            orginal.append(item)
            seen.add(item)
    return(orginal)
input=[1, 2, 2, 3, 4, 3, 5]
output=remove_duplicates(input)
print(output)  

# 12. Create a function that checks if a string is a palindrome.
def is_palindrome(text):
    return text==text[::-1]
input="racecar"
output=is_palindrome(input)
print(output)
# 13. Write a function that rotates elements of a list by n position

def rotate_list(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]

my_list = [1, 2, 3, 4, 5]
rotated = rotate_list(my_list, 2)
print("Rotated list:", rotated)

# 14. Create a function that finds the most common word in a string.
def common_word_string(text):
    words=text.split()
    freq={}
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word] =1
    common_word=max(freq,key=freq.get)
    return common_word    
input="the quick brown fox jumps over the lazy dog"   
output=common_word_string(input)
print(output)  

# 15. Write a function that sorts a list of dictionaries based on a specific key.
def get_key_value(d):
    return d["age"]  

def sort_dict_list(data):
    return sorted(data, key=get_key_value)

input=[{"name": "John", "age": 25}, {"name": "Mary", "age": 22}]
output=sort_dict_list(input)
print(output)
# 16. Create a function that converts a dictionary into a list of tuples.
def dict_to_tuples(d):
    return list(d.items())
my_dict={"a": 1, "b": 2, "c": 3}
output=dict_to_tuples(my_dict)
print(output)
# 17. Write a function that creates a dictionary from two lists, one with keys and one with values.
def list_to_dict(keys,values):
    return dict(zip(keys,values))
keys=["a", "b", "c"]
values=[1, 2, 3]
output=list_to_dict(keys,values)
print(output)
# 18. Create a function that counts the number of each word in a string.

def count_each_word(text):
    words=text.split()
    freq={}
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=  1
    return(freq)  
input="apple banana cherry banana apple"
output=count_each_word(input)
print(output)

# 19. Write a function that returns a list of all indices where a specific element appears in a list.
def find_indices(lst,target):
    indices=[]
    for i in range(len(lst)):
        if lst[i] == target:
            indices.append(i)
    return indices
input=[1, 2, 3, 2, 4, 2, 5] 
target=2
output=find_indices(input,target)   
print(output) 
# 20. Create a function that removes a specific key-value pair from a dictionary.
def remove_dict_value(d,key):
    if key in d:
        del d[key]
    return d
input={"a": 1, "b": 2, "c": 3}
output=remove_dict_value(input,"b")
print(output)

#21. Write a function that creates a nested dictionary from a list of TUPLES
def build_nested_dict(tuples):
    result = {}
    for tup in tuples:
        current = result
        for key in tup[:-1]:  
            if key not in current:
                current[key] = {}
            current = current[key]  
        current[tup[-2]] = tup[-1]
    return result
input=[("a", 1, "x"), ("b", 2, "y"), ("c", 3, "z")]
output=build_nested_dict(input)
print(output)
#Create a function that checks if two strings are anagrams.
def is_anagram(str1,str2):
    str1=str1.replace("", "").lower()
    str2=str2.replace("", "").lower()
    return sorted(str1)==sorted(str2)
print(is_anagram("listen","silent"))

# 23. Write a function that filters a dictionary based on values.
def filter_dict(d):
    new_dict={}
    for key,value in d.items():
        if value >= 2:
            new_dict[key]=value
    return new_dict               
input={"a": 1, "b": 2, "c": 3, "d": 4} 
output=filter_dict(input)
print(output) 
# 24. Create a function that finds all pairs in a list that sum to a given value.
def find_pairs_sum(nums,target):
    seen=set()
    pairs=set()
    for num in nums:
        complement=target-num
        if complement in seen:
            pairs.add(tuple(sorted([num,complement])))
        seen.add(num)
    return list(pairs)
input=[1, 2, 3, 4, 5, 6, 7]
target=8
output=find_pairs_sum(input,target)
print(output)   
# 25. Write a function that converts snake_case strings to camelCase.
def snake_to_camel(text):
    parts=text.split('_')
    camel_case=parts[0]+ ''.join(word.capitalize() for word in parts[1::] )
    return camel_case
snake="hello_world_python"
camel=snake_to_camel(snake)
print(camel)
#Create a function that generates a dictionary of character indices in a string.
def dict_char_index(text):
    my_dict={}
    for i in range(len(text)):
        char=text[i]
        if char in my_dict:
            my_dict[char].append(i)
        else:
            my_dict[char]=[i]
    return my_dict
input="hello"
output=dict_char_index(input)
print(output)
# 27. Write a function that merges multiple lists alternating their elements.
def merge_alternating(*lists):
    merged = []
    max_length = max(len(lst) for lst in lists)
    for i in range(max_length):
        for lst in lists:
            if i < len(lst):
                merged.append(lst[i])
    return merged 
list1=[1,2,3]
list2=["a","b","c"]
list3=["true","false"] 
output=merge_alternating(list1,list2,list3)
print(output)        

# 29. Write a function that groups dictionary items by their values.

def group_dict_by_values(d):
    my_dict={}
    for key,values in d.items():
        if values in d:
            my_dict[values].append(key)
        else:
            my_dict[values]=key
    return my_dict
input={"apple": 3, "banana": 2, "cherry": 3, "date": 2, "elderberry": 5} 
output=group_dict_by_values(input)
print(output)

# # 30. Create a function that zips multiple dictionaries together into a new dictionary.
def zip_dicts(*dicts):
    zipped = {}
    keys = set().union(*dicts)  
    for key in keys:
        zipped[key] = tuple(d.get(key) for d in dicts)
        
    return zipped
dict1 ={"a": 1, "b": 2}
dict2 ={"a": "apple", "b": "banana"}
dict3 ={"a": True, "b": False}

output = zip_dicts(dict1, dict2, dict3)
print(output)

# 28. Create a function that finds all substrings of a string that are palindromes.
def find_palindrome_substrings(text):
    palindromes = set()  # duplicate avoid செய்ய set
    n = len(text)
    
    for i in range(n):
        for j in range(i+1, n+1):
            substring = text[i:j]
            if substring == substring[::-1] and len(substring) > 1:
                palindromes.add(substring)
    
    return list(palindromes)
input="racecar"
output=find_palindrome_substrings(input)
print(output)