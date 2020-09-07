# 4-is-the-magic-number

There is a math game named "4 is the magic number" which does something like this

pick a number eg 6.<br>
6 goes to 3<br>
3 goes to 5<br>
5 goes to 4 <br>
... and 4 is the magic number<br>
<br>
the way it works is the output of each iteration is the number of letters in the word of the number,<br>
<br>
eg<br>
6 --> "six"<br>
length("six") = 3<br>
so...<br>
6 "goes to" 3<br>
<br>
since length("four") = 4 it creates an infinate loop<br>
<br>
as far as we know every number will eventually reach 4, I do not know if this has been proven or not, this programme counts the number of iterations before reaching 4.
I have tested it up to 12,000,000. If a number has been calculated it is added to a dictionary which is then stored for later use of the programme, the current dictionary is 24.8MB due to github restrictions. This way if you enter a ne number it need to find where it enters the dictionary and add this steps take to the dictionary + steps in the dictionary to find its number, and then also add itself to the dictionary.

Since english is fluffy there are a few variations
eg "one hundred" vs "A hundred"
or "two thousand and two" vs "two thousand two" or "two zero zero two"
or "billion" vs "milliard" ([short form/ long form](https://simple.wikipedia.org/wiki/Names_for_large_numbers))

So depending on which of the options are picked there are drastically different implementations
