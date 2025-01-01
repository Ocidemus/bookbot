def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count=get_count(text)
    dic=get_string_count(text)
    print("--- BEGIN REPORT OF books/frankenstein.txt ---")
    
    # print(text)
    print(f"{count} words found in the document")
    # print (dic)
    for char in sorted(dic):
        print(f"The '{char}' character was found {dic[char]} times")
    print("--- END REPORT ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["num"]
    
def get_count(text):
    count=0
    words=text.split()
    for i in words:
        count+=1
    return count
def get_string_count(text):
    text=text.lower()
    dict={}
    for word in text:
        if word.isalpha():
            if word in dict:
                dict[word]+=1
            else:
                dict[word]=1
    return dict    


main()