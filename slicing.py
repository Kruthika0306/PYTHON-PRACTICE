def is_palindrome(number):
   # Step 1: Convert the number to a string
   num_str = str(number)
   
   # Step 2: Reverse the string using slicing
   reversed_str = num_str[::-1]
   
   # Step 3: Compare the original and reversed strings
   if num_str == reversed_str:
       return True
   else:
       return False
# Example usage
number = 12321
if is_palindrome(number):
   print(f"{number} is a palindrome number.")
else:
   print(f"{number} is not a palindrome number.")