# src/corp_assistant/rag.py
import os
from dotenv import load_dotenv
load_dotenv()

from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
import socket
def is_langgraph_studio():
    try:
        socket.create_connection(("host.docker.internal", 6333), timeout=1)
        return True
    except OSError:
        return False

QDRANT_HOST = "host.docker.internal" if is_langgraph_studio() else "localhost"
QDRANT_PORT = 6333

client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

# ✅ 컬렉션 존재 여부 확인 후 없으면 생성
def ensure_collection(name: str):
    if not client.collection_exists(name):
        client.create_collection(
            collection_name=name,
            vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
        )

# ✅ 컬렉션 이름으로 벡터스토어 가져오기
def get_vectorstore_by_collection(name: str):
    ensure_collection(name)
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    return QdrantVectorStore(client=client, collection_name=name, embedding=embeddings)