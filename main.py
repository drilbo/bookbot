def main():
    bookpath = "books/frankenstein.txt"
    with open(bookpath) as f:
        file_contents = f.read()
        #print(file_contents)
    chars = charcount(file_contents)
    print(f"--- Begin report of {bookpath} ---")
    print(f"{wordcount(file_contents)} words found in the document")
    print()
    for char in countsorted(chars):
        if char['name'].isalpha():
            print(f"the '{char}' character was found {char['num']} times")
    print("--- End report ---")

def wordcount(t):
    words = t.split()
    return len(words)

def charcount(t):
    chars = {}
    for c in t.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def countsorted(d):
    s = []
    for k in d:
        s.append({"name": k, "num": d[k]})
    s.sort(reverse=True, key=sort_on)
    return s





main()
