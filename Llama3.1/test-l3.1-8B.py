import openai
import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("--port", type=int, default=80,
#                     help="display a square of a given number")

# args = parser.parse_args()
# print(f'using port: {args.port}')

# # Set OpenAI's API key and API base to use vLLM's API server.
# #openai_api_key = "EMPTY"

# openai_api_key = "cmsc-35360"
# openai_api_base = f"http://103.101.203.226:{args.port}/v1"
# print(openai_api_base)
# print(openai_api_key)
# print("meta-llama/Meta-Llama-3.1-8B-Instruct")
# print("")

# client = openai.OpenAI(
#     api_key=openai_api_key,
#     base_url=openai_api_base,
# )

# chat_response = client.chat.completions.create(
# #    model='upstage/SOLAR-10.7B-Instruct-v1.0',
# #    model='ibivibiv/alpaca-dragon-72b-v1',
# #    model='mistralai/Mixtral-8x7B-Instruct-v0.1',
#     model='meta-llama/Meta-Llama-3.1-8B-Instruct',    
#     messages=[
#         {"role": "user", "content": "Please generate four hypothesis in the origins of life that could be explored with a self-driving laboratory.  For each example please list the key equipment and instruments that would be needed and the experimental protocols that would need to be automated to test the hypotheses."},
#     ],
#     temperature=0.0,
#     max_tokens=2056,
# )
# #print("Chat response:", chat_response)
# print(chat_response.choices[0].message.content)


import openai
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=80,
                    help="display a square of a given number")


args = parser.parse_args()
print(f'using port: {args.port}')




# Set OpenAI's API key and API base to use vLLM's API server.
#openai_api_key = "EMPTY"


openai_api_key = "cmsc-35360"
openai_api_base = f"http://103.101.203.226:{args.port}/v1"
print(openai_api_base)
print(openai_api_key)
print("meta-llama/Meta-Llama-3.1-8B-Instruct")
print("")


client = openai.OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)


chat_response = client.chat.completions.create(
#    model='upstage/SOLAR-10.7B-Instruct-v1.0',
#    model='ibivibiv/alpaca-dragon-72b-v1',
#    model='mistralai/Mixtral-8x7B-Instruct-v0.1',
    model='meta-llama/Meta-Llama-3.1-8B-Instruct',    
    messages=[
        {"role": "user", "content": "Please generate four hypothesis in the origins of life that could be explored with a self-driving laboratory.  For each example please list the key equipment and instruments that would be needed and the experimental protocols that would need to be automated to test the hypotheses."},
    ],
    temperature=0.0,
    max_tokens=2056,
)
#print("Chat response:", chat_response)
print(chat_response.choices[0].message.content)






