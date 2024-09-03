word_count1={"python":3,"code":2,"data":4}
word_count2={"code":3,"openAI":5,"python":1}
def merge_dicts(dict1,dict2):
    merged=dict1.copy()
    for key,value in dict2.items():
        merged[key]=merged.get(key,0)+value
    return merged

print(merge_dicts(word_count1,word_count2))