def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)


# string1 = "wholesome python activity"
# string2 = "Woven Polytheistic Mat Toy"

string1 = "a gentleman"
string2 = "elegant man"

if is_anagram(string1, string2):
    print("The two sentences are anagrams.")
else:
    print("The two sentences are not anagrams.")
