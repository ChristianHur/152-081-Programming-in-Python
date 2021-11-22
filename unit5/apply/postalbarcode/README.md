# Description
Create a Python program that asks the user for a 5-digit zip code and prints the bar code.
-------------------------
Background Information
-------------------------
For faster sorting of letters, the United States Postal Service encourages companies that send large volumes of mail to use a bar code denoting the zip code.
The encoding scheme for a five-digit zip code is shown in Figure 13. There are full-height frame bars on each side. The five encoded digits are followed by a check digit, which is computed as follows: 

Add up all digits and choose the check digit to make the sum a multiple of 10. 

For example, the zip code `95014` has a sum of `19`, so the check digit is `1` to make the sum equal to `20`.

Use `:` for half bars, `|` for full bars. 

For example, 95014 becomes:
    
    ||:|:::|:|:||::::::||:|::|:::|||
    
    
