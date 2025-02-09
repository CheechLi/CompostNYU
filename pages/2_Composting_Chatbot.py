import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import Ollama
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
import chromadb
import time

chromadb.api.client.SharedSystemClient.clear_system_cache()
# Set up the model connection
HOST = "http://68.173.160.106:11434"
MODEL_NAME = "ch-doonoi-01:latest"

llm = Ollama(base_url=HOST, model=MODEL_NAME, num_gpu=2)

# Load documents
md_path = "./compost.md"
loader = TextLoader(md_path)
docs = loader.load()

# Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

# Create embeddings
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Initialize ChromaDB vector store
vectorstore = Chroma.from_documents(splits, embedding_function)
retriever = vectorstore.as_retriever()

# Conversation memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Set up conversational retrieval chain
qa = ConversationalRetrievalChain.from_llm(
    llm,
    retriever=retriever,
    memory=memory
)

# Function to get AI response
def get_response(question):
    try:
        result = qa({"question": question})
        return result["answer"]
    except Exception as e:
        return f"Error processing request: {e}"

# Streamlit UI
st.title("Test AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input handling
if prompt := st.chat_input("Ask me anything!"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    response = get_response(prompt)
    with st.chat_message("assistant"):
        # Generate response
        def typewriter(text: str, speed: int):
            tokens = response.split()
            container = st.empty()
            for index in range(len(tokens) + 1):
                curr_full_text = " ".join(tokens[:index])
                container.markdown(curr_full_text)
                time.sleep(1 / speed)

        speed = 10
        typewriter(text=response, speed=speed)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
