#!/bin/bash

#SBATCH --job-name=test
#SBATCH --mail-user=xxxx@link.cuhk.edu.hk
#SBATCH --mail-type=END
#SBATCH --gres=gpu:4
#SBATCH -p gpu_24h

python tools/train_net.py --config-file configs/BAText/TotalText/attn_R_50.yaml --eval-only MODEL.WEIGHTS [...]
