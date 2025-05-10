
   
def counters(file_contents):
    count = 0
    counter = []
    for file in file_contents.split():
        count += 1 
    return count
def count_character(test):
        file_dict = {}
        text = test.lower()

        for char in text:
            if char in file_dict:
                file_dict[char] += 1 
            else: 
                file_dict[char] = 1
        return file_dict

def sort_on(d):
    return d["num"]
        
def sorting(char_dict):
    files = []

    for char in char_dict:
        files.append({"ch": char, "num":char_dict[char]})
    files.sort(reverse=True, key=sort_on)

    return files 
       

