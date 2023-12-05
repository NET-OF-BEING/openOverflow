import requests
import openai

# Set your Stack Exchange API key
stack_exchange_api_key = 'c99keUReFfsGseL0IYaonQ(('

# Set your OpenAI API key
openai.api_key = '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'

# Step 1: Retrieve new unanswered questions with the Python tag from Stack Exchange API

# Set parameters for Stack Exchange API
stack_exchange_endpoint = 'https://api.stackexchange.com/2.3/questions'
stack_exchange_params = {
    'site': 'stackoverflow',
    'key': stack_exchange_api_key,
    'filter': 'withbody',
    'order': 'desc',
    'sort': 'creation',
    'tagged': 'python',
    'answers': 0,  # Filter for unanswered questions
}

# Make the API request to Stack Exchange
stack_exchange_response = requests.get(stack_exchange_endpoint, params=stack_exchange_params)

# Check if the request was successful (status code 200)
if stack_exchange_response.status_code == 200:
    # Parse the response JSON
    stack_exchange_data = stack_exchange_response.json()

    # Step 2: Ask ChatGPT for answers to each question

    for question in stack_exchange_data['items']:
        # print(question)
        question_title = question.get('title', '')
        question_body = question.get('body', '')
        print(question_body)
        # Ask ChatGPT for an answer
        chatgpt_response = openai.Completion.create(
            engine="text-davinci-002",  # Specify the ChatGPT engine
            prompt=f"Answer the following question:\n\n{question['title']}",
            max_tokens=150,
        )

        # Print the answer
        print(f"Question Title: {question['title']}")
        print(f"Question Body: {question_body}")
        print(f"ChatGPT Answer: {chatgpt_response['choices'][0]['text'].strip()}")
        print("-" * 50)

else:
    print(f"Error retrieving questions from Stack Exchange API: {stack_exchange_response.status_code}")
    print(stack_exchange_response.text)
