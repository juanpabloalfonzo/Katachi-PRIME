# Katachi-PRIME (形')
**Is Morphology All You Need?
Quantifying Imprints of Past Star Formation in the Present-Day Morphologies of Galaxies**
[![arXiv](https://img.shields.io/badge/arXiv-https://arxiv.org/abs/2611.07373-b31b1b.svg)](https://arxiv.org/abs/2611.07373)

**Using Morphology + Photometry for Galaxy Physical Property Inference**

Katachi-PRIME is an interpretable deep learning framework designed to infer physical galaxy parameters and reconstruct non-parametric Star Formation Histories (SFHs) directly from 3-band broadband imaging and 5-band optical photometry. 

By utilizing Vision Transformers (ViT) to extract morphological spatial embeddings and fusing them with photometry via Simulation-Based Inference (SBI) and Normalizing Flows, Katachi-PRIME maps the continuous morphological memory of galaxy populations, revealing how present-day structure encodes billions of years of past star formation.

![Katachi_prime_summary](Katachi_prime_summary.png)

## Repository Structure

This repository contains the core training and plotting scripts used to generate the results in the paper.

*   **`Katachi_Prime_data_download.py`**: Python script to retrieve the massive pre-trained weights, true SFHs, and posterior summaries.
*   **`Katachi_PRIME_Downloader.sh`**: Alternative bash script for users who prefer `wget` over Python for data retrieval.
*   **`vit_trainer_release.ipynb`**: Notebook detailing the Vision Transformer architecture and the training pipeline for extracting the 768-D morphological embeddings.
*   **`train_ili_release.ipynb`**: Notebook for configuring the Normalizing Flows, setting up the `ltu-ili` inference engine, and training the density estimators on the multi-modal inputs.
*   **`Katachi_PRIME_paper_plots_final.ipynb`**: The master notebook for recreating all primary manuscript figures.

## Getting Started

### 1. Download the Replication Data
The trained models, embedding vectors, and posterior samples are too large to host on GitHub. To download them, clone this repository and run the provided Python script:

```bash
git clone [https://github.com/juanpabloalfonzo/Katachi-PRIME.git](https://github.com/juanpabloalfonzo/Katachi-PRIME.git)
cd Katachi-PRIME
python Katachi_Prime_data_download.py
