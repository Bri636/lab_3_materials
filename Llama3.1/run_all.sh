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

# Activate the desired Conda environment
conda activate openai || { echo "Error: Failed to activate Conda environment 'openai'."; exit 1; }

# Run tests and compare outputs
python test-l3.1-405B.py > 405B.out
wc -l 405B.out
diff 405B.out ref.405B.out
python test-l3.1-70B.py > 70B.out
wc -l 70B.out
diff 70B.out ref.70B.out
python test-l3.1-8B.py > 8B.out
wc -l 8B.out
diff 8B.out ref.8B.out
