from neo4j.v1 import GraphDatabase
import json


def close(self):
    self._driver.close()

def classify_and_store(x):
    pass

def get_categories(tx):
    print "::::categories::::"
    for result in tx.run("MATCH (c:Category) RETURN c.name"):
        print result["c.name"]

def get_articles(tx, topics=[]):
    print ":::::articles:::::"
    for result in tx.run("MATCH (a:Article) RETURN a.title"):
        print result["a.title"]

def insert_article(tx, article):
    tx.run("CREATE (a: Article {title:" +article.title+ ", url: "+article.url+ ", content:" +article.content+ " }) RETURN a")

def insert_category(tx, category):
    tx.run("CREATE (c: Category {name: %S }) RETURN a" %category)


# driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
# with driver.session() as session:
#     session.read_transaction(get_articles)
#     session.read_transaction(get_categories)
