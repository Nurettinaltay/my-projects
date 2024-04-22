# 1. exercise
vowel = ['a', 'e', 'i', 'o', 'u']
letter = input('Give me a letter : ')
if letter in vowel:
    print(f'This {letter} is a vowel')
else: 
    print(f'This {letter} is not a vowel')

# 2. exercise
number = int(input('Give me a number:'))
if number > 1000 and number < 2000:
  print('This number is in between 1000 and 2000')
elif number < 1000:
  print('This number is lower than 1000')
else:
  print('This number is bigger than 2000 ')

# 3. exercise
first_number =int(input('Give me a number: '))
second_number =int(input('Give me a number: '))
third_number =int(input('Give me a number: '))
result= 0
if first_number != second_number:
  result = first_number + second_number + third_number
  print(f"The sum of the numbers is {result}")
else:
  result = (first_number + second_number + third_number)*4
  print(f"These numbers are the same!The sum of the numbers is {first_number + second_number + third_number}, Multiplied by 4 this becomes {result}")

#4. example

first_number =int(input('Give me a number: '))
second_number =int(input('Give me a number: '))
third_number =int(input('Give me a number: '))
fourth_number = int(input('Give me a number: '))
if first_number > second_number and first_number > third_number and first_number > fourth_number:
  print(f'The larges number is {first_number}')
elif  second_number> first_number and second_number > third_number and second_number > fourth_number:
  print(f'The larges number is {second_number}')
elif third_number> first_number and third_number > second_number and third_number > fourth_number:
  print(f'The larges number is {third_number}')
else:
  print(f'The larges number is {fourth_number}')

# 5. example 

income = float(input('Give me your income : '))
net_income = 0 
if income <= 67000:
  net_income = income - income*0.24
  print(f"Your income after taxes is {net_income} euro's")
elif income > 67000 and income <= 97000:
  net_income = income - income*0.31
  print(f"Your income after taxes is {net_income} euro's")
else:
  net_income = income - income*0.34
  print(f"Your income after taxes is {net_income} euro's")

# 6. example
word = str(input('Give me a word: '))
if len(word)==5:
  word_1 = word[0]*6
  print(word_1)
  word_2 = word.replace(word[0],word[1])
  print(word_2)
  word_3 = word[-1] + word[1:4] + word[0]
  print(word_3)
  word_4 = word[::-1]
  print(word_4)
  word_5 = 't'.join(word)
  print(word_5)

# 7. example
answer_1 = 36
answer_2 = 7
answer_3 = 16
question_1 = int(input('What is the answer of 6*6? : '))
if question_1 == answer_1:
  print('That is correct')
elif not question_1 == answer_1:
     print('That is false, you failed the test!')
     exit()
question_2 = int(input('What is the answer of 14/2? : '))
if question_2 == answer_2:
  print('That is also correct')
elif not question_2 == answer_2:
  print('That is false, you failed the test!')
  exit()
question_3 = int(input('What is the answer of 8+8? : '))
if question_3 == answer_3:
    print('Correct! You passed the test!')
elif not question_3 == answer_3:
  print('That is false, you failed the test!')
  exit()