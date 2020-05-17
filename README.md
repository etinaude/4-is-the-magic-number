# 4-is-the-magic-number

There is a common math game named "4 is the magic number" which does something like this

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
len("six") = 3<br>
so...<br>
6 goes to 3<br>
<br>
since 4 goes to 4 it creates an infinate loop<br>
<br>
as far as we know every number will eventually reach 4, this programme counts the number of iterations before reaching 4.
I have tested it up to 12 000 000, I dont have enough ram or time to test much higher. if a number has been calculated it is added to a dictionary which is then stored for later use of the programme, the current dictionary is 24.8MB due to github restrictions.
