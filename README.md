# DM-ViT: Dark Matter - Liquid Argon Interaction Classifier

Vision Transformer (ViT) aimed to discriminate dark matter interactions with liquid argon (dark trident scattering) from 
neutrino interactions and from cosmic-ray muons. DM-ViT repurposes the MPID package to 
train a binary classifier. Analogously to MPID, this network receives 512x512 LArTPC images. The ViT returns the probability
of the image containing either a dark trident interaction or a background interaction. 

## Dependencies
[LArCV2 v2.0.0](https://github.com/DeepLearnPhysics/larcv2),
ROOT,
PyTorch,
timm

## Setup
0. Download the container 
1. Clone this repo 
2. Activate the apptainer container
3. Setup dependencies: source setup_larcv2_dm.sh
4. Activate virtual environment: source venv/bin/activate

## Training
0. Declare training parameters and paths in ./cfg/training_config.cfg 
1. python ./uboone/train_ViT.py 

Note: You might want to run this command with nohup, so the training will continue even if you close your terminal 

## Inference
0. Declare paths in ./cfg/inference_config_binary.cfg 
1. python ./uboone/inference_ViT.py