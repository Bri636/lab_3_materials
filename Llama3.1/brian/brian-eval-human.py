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

def is_correct_str(idx: int, answer: str, gold_answer: str) -> bool:
    """ Checks if final model's output matches the gold answer """ 
    print(f'Question: {idx + 1}.) Evaluation - << Model Guess: {answer} ||| Gold Answer: {gold_answer} ||| Correct: {bool(answer==gold_answer)} >>\n')
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

    formatted_prompts = []
    for prompt in chat_prompts:
        formatted_prompts.append({
            "role": "user",
            "content": prompt + ' Return your answer as as single world or name, and do not include any punctuation #### answer'
        })
    
    return formatted_prompts


##### runnning inference #####

parser = argparse.ArgumentParser()
parser.add_argument("--human", 
                    type=int, 
                    default=1)
parser.add_argument("--file_path", type=str, default='./question_answers/gaming_questions.txt')
parser.add_argument("--answers_path", type=str, default='./question_answers/gaming_answers.txt')
args = parser.parse_args()

print(f"Evaluating on Human: {args.human}")
print("")


# Example usage:
file_path = args.file_path
answer_path = args.answers_path
human_answers_path = f'./human_answers/human_{args.human}_answers.txt'

prompts = parse_numbered_questions(file_path)
answers = read_chat_prompts(answer_path)
parsed_answers = [extract_answer(prompt).lower() for prompt in answers]

human_answers = read_chat_prompts(human_answers_path)

num_correct, total_number_tried = 0, 0
for idx, (prompt, parsed_answer, human_answer) in enumerate(zip(prompts, parsed_answers, human_answers)):
    parsed_human_answer = extract_answer(human_answer).lower().replace("\n", " ").strip()
    print(f'Question: ' + prompt['content'])

    num_correct += is_correct_str(idx, parsed_human_answer, parsed_answer)
    total_number_tried += 1
    
percent_correct_405 = float(num_correct / total_number_tried) * 100
print(f'<< Number Questions Asked: {total_number_tried}, Number Correct Answers: {num_correct}, Percent Correct: {percent_correct_405:.2f} % >>\n\n')