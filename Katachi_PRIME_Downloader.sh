#!/bin/bash

BASE_URL="https://www.astr.tohoku.ac.jp/~juanpabloalfonzo/Katachi-PRIME/Final_Data_and_Models/"

# Define the folders exactly as they appear on the remote server
FOLDERS=(
    "final_ili_models"
    "Posterior Summaries"
    "True SFHs"
    "ViT Embeds and Trained Weights"
)

echo "Starting download of Katachi-PRIME replication data..."

for folder in "${FOLDERS[@]}"; do
    # URL encode spaces to %20 so wget formats the request correctly
    ENCODED_FOLDER="${folder// /%20}"
    TARGET_URL="${BASE_URL}${ENCODED_FOLDER}/"
    
    echo "Downloading: ${folder}..."
    
    wget -r -np -nH --cut-dirs=3 -R "index.html*" "${TARGET_URL}"
done

echo "All replication data downloaded successfully."