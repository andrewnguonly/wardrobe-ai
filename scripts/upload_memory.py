import ollama
from langgraph_sdk import get_sync_client


if __name__ == "__main__":
    response = ollama.chat(
        model="llama3.2-vision",
        messages=[{
            "role": "user",
            "content": "Describe this piece of clothing in general. Then describe the colors, style, and patterns of the piece of clothing.",
            "images": ["data/IMG_7098.jpg"]
        }]
    )

    client = get_sync_client(url="http://localhost:55217")
    client.store.put_item(
        ["user_id_1234", "articles"],
        key="img_7098",
        value={
            "description": response.message.content
        },
        index=["description"],
    )
