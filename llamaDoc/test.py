import pymupdf4llm
import pathlib
from llama_index.readers.file import MarkdownReader
from llama_index import Document


# md_text = pymupdf4llm.to_markdown("2024_CityofGuelph.pdf")
# pathlib.Path("output.md").write_bytes(md_text.encode())
llama_reader = pymupdf4llm.LlamaMarkdownReader()
llama_docs = llama_reader.load_data("resume.pdf")

for doc in llama_docs:

    if "resume" in doc.metadata.get("file_name", ""):
        doc.metadata["category"] = "resume"

        doc.metadata.update({
            "category": "resume",
            "uploaded_by": "Linda",
            "tag": "job-search"
        })






# for i, doc in enumerate(llama_docs):
#     print(f"Document {i + 1}")
#     print("Text preview:\n", doc.text[:500])  # Show first 500 characters
#     print("Metadata:", doc.metadata)
#     print("-" * 80)


#print(llama_docs)

print("complete")