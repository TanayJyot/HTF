import torch
import json
import asyncio
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

# Async function to process a single item
async def process_item(meta, review_data_stream):
    reviews = []
    for review in review_data_stream:
        if review["parent_asin"] == meta["parent_asin"]:
            if review["rating"] in [1, 2, 3, 4]:
                reviews.append({
                    "stars": review["rating"],
                    "content": f"Title: {review.get('title', '')}, Text: {review.get('text', '')}"
                })
        if len(reviews) >= 5:
            break

    return {
        "item name": meta["title"],
        "item description": " ".join(meta.get("features", [])),
        "reviews": reviews
    }

# Async function for loading datasets
async def load_datasets():
    print("Loading datasets asynchronously...")
    for _ in tqdm(range(100), desc="Preparing environment", unit="%"):
        await asyncio.sleep(0.05)
    meta_dataset = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_meta_Clothing_Shoes_and_Jewelry",
                                split="full", streaming=True)
    review_dataset = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_review_Clothing_Shoes_and_Jewelry",
                                  split="full", streaming=True)
    print("Datasets loaded.")
    return meta_dataset, review_dataset

async def main():
    start_time = time.time()

    # Load datasets asynchronously
    meta_dataset, review_dataset = await load_datasets()

    # Process items asynchronously
    num_items = 10
    meta_iter = iter(meta_dataset)

    print("Preloading metadata items...")
    meta_items = []
    for _ in tqdm(range(num_items), desc="Loading metadata"):
        try:
            meta_items.append(next(meta_iter))
        except StopIteration:
            break

    print("Processing items asynchronously...")
    tasks = [process_item(meta, review_dataset) for meta in meta_items]
    processed_data = await asyncio.gather(*tasks)

    # Save the processed data
    with open("real_dataset_new_clothing.json", "w", encoding="utf-8") as out_file:
        json.dump(processed_data, out_file, indent=4, ensure_ascii=False)

    print("Processing complete!")
    print_gpu_utilization()

    elapsed_time = time.time() - start_time
    print(f"Processing took {elapsed_time:.2f} seconds.")

if __name__ == '__main__':
    asyncio.run(main())
