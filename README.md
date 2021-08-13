##  ABCNet for LSVT from AdelaiDet

[AdelaiDet](https://github.com/aim-uofa/AdelaiDet) is an open source toolbox for multiple instance-level recognition tasks on top of [Detectron2](https://github.com/facebookresearch/detectron2).

### Train 

To train a model with "train_net.py", first
generate labels,
then run:

```
OMP_NUM_THREADS=1 python tools/train_net.py \
    --config-file configs/BAText/TotalText/attn_R_50.yaml \
    --num-gpus 4 \
    OUTPUT_DIR training_dir/lsvt
```
To evaluate the model after training, run:

```
OMP_NUM_THREADS=1 python tools/train_net.py \
    --config-file configs/BAText/TotalText/attn_R_50.yaml \
    --eval-only \
    --num-gpus 4 \
    OUTPUT_DIR training_dir/lsvt \
    MODEL.WEIGHTS [...]
```
