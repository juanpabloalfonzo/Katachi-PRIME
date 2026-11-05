import subprocess
import urllib.parse

# Base URL mapped from the public_html directory path
base_url = "https://www.astr.tohoku.ac.jp/~juanpabloalfonzo/Katachi-PRIME/Final_Data_and_Models/"

# Target folders extracted exactly as structured on the remote server
folders = [
    "final_ili_models", #[cite: 3]
    "Posterior Summaries", #[cite: 3]
    "True SFHs", #[cite: 3]
    "ViT Embeds and Trained Weights" #[cite: 3]
]

for folder in folders:
    # URL encode the spaces (e.g., "True SFHs" becomes "True%20SFHs")
    encoded_folder = urllib.parse.quote(folder)
    target_url = f"{base_url}{encoded_folder}/"
    
    print(f"Starting recursive download for: {folder}")
    
    # wget flag breakdown:
    # -r: Recursive download for directories
    # -np: No parent (prevents ascending to Katachi-PRIME or higher)
    # -nH: No host directories (prevents creating a www.astr.tohoku.ac.jp root folder locally)
    # --cut-dirs=3: Strips the /~juanpabloalfonzo/Katachi-PRIME/Final_Data_and_Models/ hierarchy locally
    # -R "index.html*": Rejects downloading auto-generated Apache index pages
    subprocess.run([
        "wget", 
        "-r", 
        "-np", 
        "-nH", 
        "--cut-dirs=3", 
        "-R", "index.html*", 
        target_url
    ])

print("All Katachi-PRIME replication data downloaded successfully.")