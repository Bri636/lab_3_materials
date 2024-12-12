#!/bin/bash

# Check for Conda installation in common locations and source conda.sh
if [ -f ~/anaconda3/etc/profile.d/conda.sh ]; then
    source ~/anaconda3/etc/profile.d/conda.sh
elif [ -f ~/opt/anaconda3/etc/profile.d/conda.sh ]; then
    source ~/opt/anaconda3/etc/profile.d/conda.sh
else
    echo "Error: Conda initialization script not found in ~/anaconda3 or ~/opt/anaconda3."
    exit 1
fi

# # Activate the desired Conda environment
# conda activate dls || { echo "Error: Failed to activate Conda environment 'openai'."; exit 1; }

# Run tests and compare outputs
python brian-l3.1-405B.py > ./out_logs/llama_405B_brian.out
wc -l ./out_logs/llama_405B_brian.out
# # diff 405B.out ref.405B.out
python brian-l3.1-70B.py > ./out_logs/llama_70B_brian.out
wc -l ./out_logs/llama_70B_brian.out
# # # diff 70B.out ref.70B.out
python brian-l3.1-8B.py > ./out_logs/llama_8B_brian.out
wc -l ./out_logs/llama_8B_brian.out
# # diff 8B.out ref.8B.out
python brian-gemma-2-9b.py > ./out_logs/gemma_9B_brian.out
wc -l ./out_logs/gemma_9B_brian.out

python brian-eval-human.py --human 1 > ./out_logs/human_answers.out
python brian-eval-human.py --human 2 >> ./out_logs/human_answers.out
python brian-eval-human.py --human 3 >> ./out_logs/human_answers.out
wc -l ./out_logs/human_answers.out