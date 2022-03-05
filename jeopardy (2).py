import pandas as pd
pd.set_option('display.max_colwidth', None)
 
 #Load data and rename columns
jeopardy_data = pd.read_csv("jeopardy.csv")
jeopardy_data = jeopardy_data.rename(columns={'Show Number': 'show_number', " Air Date": 'air_date', ' Round': 'round', ' Category': 'category', ' Value': 'value', ' Question': 'question', ' Answer': 'answer'})
print(jeopardy_data.columns)
print(jeopardy_data)

#funtion for filtering questions with specific words
def filter_data(words):
  # Lowercases all words in the list of words as well as the questions. Returns true is all of the words in the list appear in the question.
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  # Applies the labmda function to the Question column and returns the rows where the function returned True
  return jeopardy_data.loc[jeopardy_data["question"].apply(filter)]
# Testing the filter function
filtered = filter_data(["King", "England"])

#print(len(filtered["question"]))

#Convert values in Value column to float by removing null values, and then replacing '$' and ','
jeopardy_data['value'] = jeopardy_data.value.apply(lambda x: float(x[1:].replace(',','')) if x != "None" else 0)

#find questions with the word 'king'
king_questions = filter_data(['King'])
#average point value of questions with the word 'king'
print(king_questions.value.mean())

#function that returns the count of each unique answers to all of the questions in the df
def num_unique_questions(df):
  return df.answer.value_counts()

#testing unique count function with questions with the word 'king'
print(num_unique_questions(king_questions))

#filter questions by the word 'Computer'
computer_questions = filter_data(['Computer'])
computer_questions['air_date'] = computer_questions.air_date.apply(lambda x: float(x[:4]))
computer_questions['air_date'] = computer_questions.air_date.apply(lambda x: '2000s' if x>=2000 else "90s")

def unique_air_date_counts(df):
    return df.air_date.value_counts()

print(unique_air_date_counts(computer_questions))
