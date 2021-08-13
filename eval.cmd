#!/bin/bash

#SBATCH --job-name=test
#SBATCH --mail-user=1155141582@link.cuhk.edu.hk
#SBATCH --mail-type=END
#SBATCH --gres=gpu:4
#SBATCH -p gpu_24h

python tools/train_net.py --config-file configs/BAText/TotalText/attn_R_50.yaml --eval-only MODEL.WEIGHTS new_lsvt/model_0039999.pth 
