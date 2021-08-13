#!/bin/bash

#SBATCH --job-name=test
#SBATCH --mail-user=xxxx@link.cuhk.edu.hk
#SBATCH --mail-type=END
#SBATCH --gres=gpu:4
#SBATCH -p gpu_24h

OMP_NUM_THREADS=1 python tools/train_net.py --config-file configs/BAText/TotalText/attn_R_50.yaml --num-gpus 4 
 
