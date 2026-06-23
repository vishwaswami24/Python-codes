
def Check_Vow(string):
    vowels = "AaEeIiOoUu"
    final = [i for i in string if i in vowels]
    print(len(final))
    print(final)
     
# Driver Code
string = "Geeks for Geeks"
Check_Vow(string)
