def parse_numbered_questions(file_path):
    # Open and read the file
    with open(file_path, 'r') as file:
        text = file.read()

    # Define a regex pattern to match the numbered questions
    # This will capture the number and the text that follows, allowing for multi-line questions
    pattern = r'(\d+\.)\s*(.*?)\s*(?=\d+\.)|\Z'  # This captures the question up until the next number or end of file
    
    # Find all matches using regex
    matches = re.findall(pattern, text, flags=re.DOTALL)

    # Extract the questions into a list
    questions = [match[1].strip() for match in matches]

    # Convert the questions into chat prompts
    prompts = [
        {"role": "user", "content": question}
        for question in questions
    ]

    return prompts