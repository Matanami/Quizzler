import requests
import html

data = requests.get(url='https://opentdb.com/api.php?amount=10&type=boolean')
data.raise_for_status()
question_data = data.json()["results"]

# question_data = [{'question': _['question'], 'correct_answer': _['correct_answer'] } for _ in data_results]
print(question_data)
