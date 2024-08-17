import os
import reflex as rx
from reflex.state import State

# Define the State for Reflex
class DocumentState(State):
    groq_api_key: str = os.getenv("GROQ_API_KEY")
    google_api_key: str = os.getenv("GOOGLE_API_KEY")
    question: str = ""
    response: str = ""
    context: list = []

    def set_question(self, question: str):
        self.question = question

    def create_vector_store(self):
        if "vectors" not in self.session_state:
            from langchain_google_genai import GoogleGenerativeAIEmbeddings
            from langchain_community.document_loaders import PyPDFDirectoryLoader
            from langchain.text_splitter import RecursiveCharacterTextSplitter
            from langchain_community.vectorstores import FAISS

            embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
            loader = PyPDFDirectoryLoader("./pdf_folder")
            docs = loader.load()
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            final_documents = text_splitter.split_documents(docs)
            self.session_state["vectors"] = FAISS.from_documents(final_documents, embeddings)

    def run_query(self):
        if self.question:
            from langchain_groq import ChatGroq
            from langchain.chains.combine_documents import create_stuff_documents_chain
            from langchain_core.prompts import ChatPromptTemplate
            from langchain.chains import create_retrieval_chain

            llm = ChatGroq(groq_api_key=self.groq_api_key, model="Gemma-7b-it")
            prompt = ChatPromptTemplate.from_template(
                """
                Answer the questions based on the provided context only.
                Please provide the most accurate response based on the question.
                <context>
                {context}
                <context>
                Question:{input}
                """
            )

            document_chain = create_stuff_documents_chain(llm, prompt)
            retriever = self.session_state["vectors"].as_retriever()
            retrieval_chain = create_retrieval_chain(retriever, document_chain)

            result = retrieval_chain.invoke({'input': self.question})
            self.response = result['answer']
            self.context = result['context']

# Define Reflex components (frontend part)
def index():
    return rx.box(
        rx.heading("Gemma Document Q&A"),
        rx.input(placeholder="Enter your question from the documents", on_change=DocumentState.set_question),
        rx.button("Create Vector Store", on_click=DocumentState.create_vector_store),
        rx.button("Run Query", on_click=DocumentState.run_query),
        rx.text(DocumentState.response),
        rx.cond(DocumentState.context, rx.expander(
            "Document Similarity Search",
            *[rx.text(doc.page_content) for doc in DocumentState.context]
        )),
    )

# Create the Reflex App
app = rx.App(state=DocumentState)
app.add_page(index)
app.compile()
