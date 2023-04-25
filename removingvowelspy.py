string="premkumar"
vowels=['a','e','i','o','u']
result=""
for i in range(len(string)):
    if string[i] not in vowels:
        result=result+string[i]
print("\n after removunng vowels:",result)