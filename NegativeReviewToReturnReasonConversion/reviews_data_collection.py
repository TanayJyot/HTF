import asyncio
import json
from datasets import load_dataset
import aiofiles
import time

async def process_item(meta, review_dataset):
    print("getting reviews for", meta["title"])
    review_with_asin = review_dataset.filter(
        lambda review: review["parent_asin"] == meta["parent_asin"]
    )
    reviews = list(review_with_asin.take(5))
    return {
        "item name": meta["title"],
        "item description": " ".join(meta["features"]),
        "reviews": [{"stars": review["rating"], "content": f"Title: {review['title']}, Text: {review['text']}"} for review in reviews],
    }

async def main():
    start_time = time.time()
    review_dataset = load_dataset(
        "McAuley-Lab/Amazon-Reviews-2023", "raw_review_Appliances", trust_remote_code=True, streaming=True, split="full"
    )
    meta_dataset = load_dataset(
        "McAuley-Lab/Amazon-Reviews-2023", "raw_meta_Appliances", trust_remote_code=True, streaming=True, split="full"
    )

    meta_dataset = meta_dataset.shuffle()
    meta_iterable = iter(meta_dataset)

    tasks = []
    for _ in range(10):
        meta = next(meta_iterable)
        task = asyncio.create_task(process_item(meta, review_dataset))
        tasks.append(task)

    processed_data = await asyncio.gather(*tasks)

    async with aiofiles.open("real_dataset.json", "w") as out_file:
        await out_file.write(json.dumps(processed_data, indent=4))

    end_time = time.time()
    print(f"{end_time - start_time}")

if __name__ == "__main__":
    asyncio.run(main())
