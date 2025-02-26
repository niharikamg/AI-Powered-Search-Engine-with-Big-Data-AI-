from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

def index_document(index, doc):
    es.index(index=index, document=doc)
