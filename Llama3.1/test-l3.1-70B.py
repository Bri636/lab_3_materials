import openai
import argparse
import re




parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=80,
                    help="display a square of a given number")

args = parser.parse_args()
print(f'using port: {args.port}')


# Set OpenAI's API key and API base to use vLLM's API server.
#openai_api_key = "EMPTY"

openai_api_key = "cmsc-35360"
openai_api_base = f"http://195.88.24.64:{args.port}/v1"
print(openai_api_key)
print(openai_api_base)
print("meta-llama/Meta-Llama-3.1-70B-Instruct")
print("")


import openai
import argparse
import re

ANS_RE_OLD = re.compile(r"####\s*\$?\s*([-+]?\d+(?:,\d{3})*(?:\.\d+)?)", re.IGNORECASE)
ANS_RE = re.compile(r"####\s*([\w\.\-]+)", re.IGNORECASE)
INVALID_ANS = "[invalid]"
def extract_answer(completion: str) -> str:
    """ 
    Parses through a string and returns the answer as a str
    
    Expects the answer in this format: 
    Answer is #### -567.89 or #### -567.89. ===> -567.89
    """
    match = ANS_RE.search(completion)
    if match:
        match_str = match.group(1).strip()
        match_str = match_str.replace(",", "")
        match_str = match_str.rstrip('.')
        return match_str
    else:
        return INVALID_ANS
    
    
def is_correct(idx: int, answer: str, gold_answer: str) -> bool:
    """ Checks if final model's output matches the gold answer """ 
    answer = str(extract_answer(answer)).lower()
    gold_answer = str(extract_answer(gold_answer)).lower()
    print(f'Question #{idx + 1} << Model Guess: {answer} ||| Gold Answer: {gold_answer} >>\n')
    return bool(answer==gold_answer)

def is_correct_str(idx: int, answer: str, gold_answer: str) -> bool:
    """ Checks if final model's output matches the gold answer """ 
    print(f'Question #{idx + 1} << Model Guess: {answer} ||| Gold Answer: {gold_answer} >>\n')
    return bool(answer==gold_answer)


def read_chat_prompts(file_path):
    """
    Reads a text file line by line and returns a list of chat prompts.

    Args:
        file_path (str): The path to the text file to read.

    Returns:
        list: A list of chat prompts.
    """
    chat_prompts = []
    with open(file_path, 'r') as file:
        for line in file:
            chat_prompts.append(line.strip())
    return chat_prompts

def parse_numbered_questions(file_path):
    """
    Parses a text file containing numbered questions into a list of chat prompts.

    Args:
        file_path (str): The path to the text file to read.

    Returns:
        list: A list of chat prompts formatted for client.chat.completions.create.
    """
    chat_prompts = read_chat_prompts(file_path)
    
    # Format chat prompts for the model
    formatted_prompts = []
    for prompt in chat_prompts:
        # Ensure each prompt is wrapped in the correct dictionary format
        formatted_prompts.append({
            "role": "user",
            "content": prompt + ' Return your answer as as single world or name, and do not include any punctuation #### answer'
        })
    
    return formatted_prompts


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=80,
                    help="display a square of a given number")

args = parser.parse_args()
print(f'using port: {args.port}')


# Set OpenAI's API key and API base to use vLLM's API server.
#openai_api_key = "EMPTY"

# openai_api_key = "cmsc-35360"
# #openai_api_base = f"http://103.101.203.226:{args.port}/v1"
# openai_api_base = f"http://66.55.67.65:{args.port}/v1"
# print(openai_api_key)
# print(openai_api_base)
# print('llama31-405b-fp8')
# print("")

client = openai.OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

# Example usage:
file_path = './batch_1.txt'  # Replace with your actual file path
prompts = parse_numbered_questions(file_path)
answer_path = '/Users/BrianHsu/Desktop/CMSC/deep_learning_systems/lab_3/Llama3.1/batch_1_answers.txt'
answers = read_chat_prompts(answer_path)
parsed_answers = [extract_answer(prompt).lower() for prompt in answers]

num_correct, total_number_tried = 0, 0
# Example of calling the chat API with parsed prompts
for idx, (prompt, parsed_answer) in enumerate(zip(prompts, parsed_answers)):
    chat_response = client.chat.completions.create(
        # model='llama31-405b-fp8',
        model='meta-llama/Meta-Llama-3.1-70B-Instruct',
        messages=[prompt],
        temperature=0.0,
        max_tokens=2056,
    )
    print(chat_response.choices[0].message.content + '\n' + "****************************************************" '\n')
    str_response = str(chat_response.choices[0].message.content).lower()
    num_correct += is_correct_str(idx, str_response, parsed_answer)
    total_number_tried += 1
    

percent_correct_405 = float(num_correct / total_number_tried) * 100
print(percent_correct_405)


# client = openai.OpenAI(
#     api_key=openai_api_key,
#     base_url=openai_api_base,
# )

# chat_response = client.chat.completions.create(
#     model='meta-llama/Meta-Llama-3.1-70B-Instruct',    
#     messages=[
#         {"role": "user", "content": "Please generate four hypothesis in the origins of life that could be explored with a self-driving laboratory.  For each example please list the key equipment and instruments that would be needed and the experimental protocols that would need to be automated to test the hypotheses."},
#     ],
#     temperature=0.0,
#     max_tokens=2056,
# )
# #print("Chat response:", chat_response)
# print(chat_response.choices[0].message.content)
