import nltk.corpus
import mysql_credits # Доступ к БД
import pymysql


# Коннектимся к божественному, бесплатному MySQL
connection = pymysql.connect(
    host=mysql_credits.db_host,
    user=mysql_credits.db_user,
    password=mysql_credits.db_password,
    db=mysql_credits.db,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    all_articles_sql = 'SELECT article.article_text FROM article WHERE article_origin = "vk"'
    cursor.execute(all_articles_sql)
    all_articles = cursor.fetchall()
    print(all_articles)


stopwords = nltk.corpus.stopwords.words('russian')

# print(stopwords)


def freq(word, doc):
    return doc.count(word)


def word_count(doc):
    return len(doc)


def tf(word, doc):
    return (freq(word, doc) / float(word_count(doc)))


def num_docs_containing(word, list_of_docs):
    count = 0
    for document in list_of_docs:
        if freq(word, document) > 0:
            count += 1
    return 1 + count


def idf(word, list_of_docs):
    return math.log(len(list_of_docs) /
            float(num_docs_containing(word, list_of_docs)))
