import streamlit as st 
from dotenv import load_dotenv
import pickle
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
import os


with st.sidebar:
    st.title("LLM chatBot")
    st.markdown(" ")
    st.write("VidBot")

load_dotenv()

def main():
    pdf=st.file_uploader("Upload a file",type='pdf')
    if pdf is not None:
        pdf_reader=PdfReader(pdf)

        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        text_splitter =RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks=text_splitter.split_text(text=text)

        store_name=pdf.name[:-4]
        st.write(f'{store_name}')

        if os.path.exists(f"{store_name}.pkl"):
            with open(f"{store_name}.pkl","rb") as f:
                VectorStore=pickle.load(f)
        else:
            embeddings=OpenAIEmbeddings()
            VectorStore=FAISS.from_texts(chunks,embedding=embeddings)
            with open(f"{store_name}.pkl","wb") as f:
                pickle.dump(VectorStore,f)


        query=st.text_input("Ask questions")
        
        if query:
            docs=VectorStore.similarity_search(query=query, k=3)

            llm=OpenAI(model_name="gpt-3.5-turbo-instruct")
            chain=load_qa_chain(llm=llm,chain_type="stuff")
            with get_openai_callback() as cb:
                response=chain.run(input_documents=docs,question=query)
                print(cb)
            st.write(response)

if __name__=="__main__":
    main()