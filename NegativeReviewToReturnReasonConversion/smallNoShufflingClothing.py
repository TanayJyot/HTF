import torch
import json
from tqdm import tqdm
from datasets import load_dataset
import time

# Check CUDA availability
if torch.cuda.is_available():
    print("CUDA is available. Using GPU.")
    device = torch.device("cuda")
else:
    print("CUDA is not available. Using CPU.")
    device = torch.device("cpu")

# Function to print GPU utilization
def print_gpu_utilization():
    if torch.cuda.is_available():
        print(f"GPU memory allocated: {torch.cuda.memory_allocated()/1024**3:.2f} GB")
        print(f"GPU memory reserved: {torch.cuda.memory_reserved()/1024**3:.2f} GB")
    else:
        print("GPU not available. Running on CPU.")

# Function to process a single item
def process_item(meta, review_lookup):
    parent_asin = meta["parent_asin"]
    reviews = review_lookup.get(parent_asin, [])[:5]  # Get up to 5 matching reviews

    return {
        "item name": meta["title"],
        "item description": " ".join(meta.get("features", [])),
        "reviews": reviews
    }

# Function to load datasets
def load_datasets():
    print("Loading datasets...")

    # Load meta dataset (just a small subset to match reviews)
    meta_dataset = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_meta_Clothing_Shoes_and_Jewelry",
                                split="full", streaming=True).take(100)

    # Load review dataset with streaming
    review_dataset = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_review_Clothing_Shoes_and_Jewelry",
                                  split="full", streaming=True)

    print("Datasets loading...")
    return meta_dataset, review_dataset

def main():
    start_time = time.time()

    # Load datasets (streaming reviews)
    meta_dataset, review_dataset = load_datasets()

    # Simply take the first 10,000 reviews
    print("Taking first 10,000 reviews...")
    review_subset = list(review_dataset.take(10000000))

    # Create a lookup dictionary for reviews based on `parent_asin`
    review_lookup = {}
    for review in review_subset:
        if review["rating"] in [1, 2, 3, 4]:  # Filter for specific ratings
            parent_asin = review["parent_asin"]
            if parent_asin not in review_lookup:
                review_lookup[parent_asin] = []
            review_lookup[parent_asin].append({
                "stars": review["rating"],
                "content": f"Title: {review.get('title', '')}, Text: {review.get('text', '')}"
            })

    # Process items
    num_items = 10  # Limit processing to 10 items
    print("Processing items...")
    processed_data = [process_item(meta, review_lookup) for meta in tqdm(meta_dataset.take(num_items))]

    # Save the processed data
    with open("small_no_shuffling_real_dataset_new_clothing.json", "w", encoding="utf-8") as out_file:
        json.dump(processed_data, out_file, indent=4, ensure_ascii=False)

    print("Processing complete!")
    print_gpu_utilization()

    elapsed_time = time.time() - start_time
    print(f"Processing took {elapsed_time:.2f} seconds.")

if __name__ == '__main__':
    main()
