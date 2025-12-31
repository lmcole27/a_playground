from llama_index.readers.smart_pdf_loader import SmartPDFLoader
import llmsherpa

# llmsherpa_api_url = "https://readers.llmsherpa.com/api/document/developer/parseDocument?renderFormat=all"
# pdf_url = "https://arxiv.org/pdf/1910.13461.pdf"  # also allowed is a file path e.g. /home/downloads/xyz.pdf
# pdf_loader = SmartPDFLoader(llmsherpa_api_url=llmsherpa_api_url)
# documents = pdf_loader.load_data(pdf_url)

from llmsherpa.readers import LayoutPDFReader

llmsherpa_api_url = "https://readers.llmsherpa.com/api/document/developer/parseDocument?renderFormat=all"
pdf_url = "https://arxiv.org/pdf/1910.13461.pdf" # also allowed is a file path e.g. /home/downloads/xyz.pdf
# pdf_url = "https://arxiv.org/pdf/2212.14024.pdf"
pdf_reader = LayoutPDFReader(llmsherpa_api_url)
doc = pdf_reader.read_pdf(pdf_url)
