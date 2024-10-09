# NLP-Regular-Expressions

dollar_program.py ouputs matches of dollar amounts.
telephone_regexp.py outputs matches of telephone numbers. 

Program was developed using all-OANC.txt as a training corpus. 
Program requires a text file in the command line, and will output a file (dollar_output.txt for dollar_program.py; telephone_output.txt for telephone_regex.py) that contains the respective matches.

To run:
  python dollar_program.py test_dollar_phone_corpus.txt
  python telephone_regex.py test_dollar_phone_corpus.txt

Program results:

telephone_regex.py
instances in key:  72
instances in student  72
correct =  72
precision =  1.0
recall =  1.0
f1 =  1.0

dollar_program.py
instances in key:  96
instances in student  93
correct =  90
precision =  0.967741935483871
recall =  0.9375
f1 =  0.9523809523809523

final scores
correct =  162
keytotal=  168
studtotal=  165
precision =  0.9818181818181818
recall =  0.9642857142857143
f1 =  9.72972972972973

