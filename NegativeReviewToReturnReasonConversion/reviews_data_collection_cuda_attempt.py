import torch
import json
import multiprocessing
from tqdm import tqdm
from datasets import load_dataset
import time
import asyncio

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

# Function to process a single item (now filters for 1 or 2 star reviews)
def process_item(meta, review_data_stream):
    reviews = []
    for review in review_data_stream:
        if review["parent_asin"] == meta["parent_asin"]:
            # Only include reviews with 2 or 1 stars
            if review["rating"] in [1, 2, 3, 4]:
                reviews.append({
                    "stars": review["rating"],
                    "content": f"Title: {review.get('title', '')}, Text: {review.get('text', '')}"
                })
        if len(reviews) >= 5:  # Limit to 5 reviews
            break

    return {
        "item name": meta["title"],
        "item description": " ".join(meta.get("features", [])),
        "reviews": reviews
    }

# Async function for loading datasets (simulate async I/O task)
async def load_datasets():
    print("Loading datasets asynchronously...")
    # Simulate async data loading with asyncio.sleep (for demonstration)
    await asyncio.sleep(1)  # This can be replaced by an actual async task, such as I/O bound tasks
    meta_dataset = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_meta_Appliances", split="full", streaming=True)
    review_dataset = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_review_Appliances", split="full", streaming=True)
    print("Datasets loaded.")
    return meta_dataset, review_dataset

async def main():
    # Start timer
    start_time = time.time()

    # Load datasets asynchronously (for demonstration purposes)
    meta_dataset, review_dataset = await load_datasets()

    # Process items using multiprocessing for speed
    num_items = 10  # Process only 10 items for now
    meta_iter = iter(meta_dataset)  # Convert streaming dataset to iterator

    print("Processing items in parallel...")

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        processed_data = list(
            tqdm(pool.starmap(process_item, [(next(meta_iter), review_dataset) for _ in range(num_items)]), total=num_items)
        )

    # Save the processed data to a JSON file
    with open("real_dataset_new1234.json", "w", encoding="utf-8") as out_file:
        json.dump(processed_data, out_file, indent=4, ensure_ascii=False)

    print("Processing complete!")

    # Print GPU utilization
    print_gpu_utilization()

    # End timer and calculate the duration
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Processing took {elapsed_time:.2f} seconds.")

# 🛠 Fix: Required for Windows multiprocessing
if __name__ == '__main__':
    asyncio.run(main())
