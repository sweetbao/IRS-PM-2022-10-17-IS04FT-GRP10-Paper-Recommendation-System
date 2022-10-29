import operator

import pandas
import pandas as pd
import gensim
from gensim.corpora.dictionary import Dictionary
from nltk import word_tokenize
import os
import numpy as np
from gensim.models import TfidfModel
from sklearn.preprocessing import MaxAbsScaler
import requests
import gzip


class ItemBasedCF:
    def __init__(self, most_similar=30, recommend_num=15):
        self.N = {}  # number of item user have interacted
        self.W = {}  # similarity matrix to store similarity of item i and item j

        self.train = {}
        self.papers = pd.DataFrame()

        # recommend n items from the k most similar to the items user have interacted
        self.k = most_similar
        self.n = recommend_num

    def get_data(self, rating_file_path, paper_file_path):
        """
        @description: load data from file
        @param file_path: path of file
        """
        print('start loading data from ', rating_file_path)
        with open(rating_file_path, "r") as f:
            for i, line in enumerate(f, 0):
                if i != 0:  # remove the first line that is title
                    line = line.strip('\r').strip()
                    item, rating = line.split(',')
                    user = 0
                    self.train.setdefault(user, [])
                    self.train[user].append([item, float(rating)])

        print('start loading data from ', paper_file_path)
        df = pd.read_csv(paper_file_path, index_col=0)
        self.papers = df
        print('loading data successfully')

    # using user data to do filter
    # def similarity(self):
    #     """
    #     @description: caculate similarity between item i and item j
    #     """
    #     print('start caculating similarity matrix ...')
    #     for user, item_ratings in self.train.items():
    #         items = [x[0] for x in item_ratings]  # items that user have interacted
    #         for i in items:
    #             self.N.setdefault(i, 0)
    #             self.N[i] += 1  # number of users who have interacted item i
    #             for j in items:
    #                 if i != j:
    #                     self.W.setdefault(i, {})
    #                     self.W[i].setdefault(j, 0)
    #                     self.W[i][j] += 1  # number of users who have interacted item i and item j
    #     for i, j_cnt in self.W.items():
    #         for j, cnt in j_cnt.items():
    #             self.W[i][j] = self.W[i][j] / (self.N[i] * self.N[j]) ** 0.5  # similarity between item i and item j
    #     print('caculating similarity matrix successfully')

    def similarity(self,model):
        """
        @description: caculate similarity between item i and item j
        """

        sFilePath = os.path.join(os.getcwd(), "PaperRecommend\similarityModels")
        if not os.path.exists(sFilePath):
            os.mkdir(sFilePath)
        print('loading similarity model ...')
      #  word2vec_model = get_model("word2vec", sFilePath, None)
        word2vec_model = model
        dict_file = os.path.join(sFilePath, "dictionary")
        print('generate dictionary ...')
        corpus_dictionary, corpus = get_dictionary(dict_file)
        # if not corpus:
        #     with open('data_only.txt') as f:
        #         w = f.readline()
        #         while w:
        #             corpus.append(word_tokenize(w.strip()))
        #             w = f.readline()
        common_corpus = [corpus_dictionary.doc2bow(text) for text in corpus]
        lda_file, tfidf_file = os.path.join(sFilePath, "lda_model"), os.path.join(sFilePath, "tfidf_model")
        lda_model = get_model(model_name='lda',
                              model_file=lda_file,
                              common_corpus=common_corpus,
                              n_topics=50)
        tfidf_model = get_model('tfidf', tfidf_file, common_corpus)
        print('start caculating similarity matrix ...')
        final_sim, final_index = [], []
        for user, item_ratings in self.train.items():
            items = [x[0] for x in item_ratings]  # items that user have interacted
            for i in items:
                paper1 = self.papers.loc[int(i)]
                for index, j in self.papers.iterrows():
                    if index != int(i):
                        print(int(i), index)
                        self.W.setdefault(int(i), {})
                        self.W[int(i)].setdefault(index, 0)

                        # word similarity using word2vec
                        # keywords1, keywords2 = get_keywords(paper1['summary']), get_keywords(j['summary'])
                        keywords1, keywords2 = paper1['keywords'].split(','), j['keywords'].split(',')
                        word_sim = word_similarity(word2vec_model, keywords1, keywords2)
                        print("word_sim", word_sim)

                        # paragraph similarity using TF-IDF
                        para_sim = para_similarity(tfidf_model, corpus_dictionary, paper1['summary'], j['summary'])
                        print("para_sim", para_sim)

                        # topic similarity using LDA
                        topic_sim = topic_similarity(lda_model, corpus_dictionary, paper1['summary'], j['summary'], num_topics=50)
                        print("topic_sim", topic_sim)

                        final_sim.append([word_sim, para_sim, topic_sim])
                        final_index.append((int(i), index))
        # scale the similarity
        final_sim = np.array(final_sim, dtype='float32')
        transformer = MaxAbsScaler().fit(final_sim)
        final_sim = transformer.transform(final_sim)

        for idx, (i, j) in enumerate(final_index):
            self.W[i][j] = final_sim[idx][0]*0.5 + final_sim[idx][1]*0.7 + final_sim[idx][2]

        print('caculating similarity matrix successfully')

    def recommendation(self, user):
        """
        @description: recommend n item for user
        @param user: recommended user
        @return items recommended for user
        """
        print('start recommending items for user whose userId is ', user)
        rank = {}
        watched_items = [x[0] for x in self.train[user]]
        for i in watched_items:
            for j, similarity in sorted(self.W[int(i)].items(), key=operator.itemgetter(1), reverse=True)[0:self.k]:
                if j not in watched_items:
                    rank.setdefault(j, 0.)
                    rank[j] += float(self.train[user][watched_items.index(i)][
                                         1]) * similarity  # rating that user rate for item i * similarity between item i and item j
        return sorted(rank.items(), key=operator.itemgetter(1), reverse=True)[0:self.n]


# def get_keywords(doc: str):
#     kw_model = KeyBERT()
#     keywords = kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 3), top_n=5, use_mmr=True, diversity=0.7)
#     return [keyword[0] for keyword in keywords]


def word_similarity(model, wordlist1, wordlist2):
    sim = 0
    for kw1 in wordlist1:
        for kw2 in wordlist2:
            tmp_sim = 1
            for w1 in kw1.split():
                for w2 in kw2.split():
                    # print(w1, w2, model.n_similarity(w1, w2))
                    tmp_sim *= model.n_similarity(w1, w2)
            sim += tmp_sim
    return sim


def topic_similarity(lda, corpus_dictionary, doc1, doc2, num_topics=10):
    vector1, vector2 = lda[corpus_dictionary.doc2bow(word_tokenize(doc1))], lda[
        corpus_dictionary.doc2bow(word_tokenize(doc2))]
    # print(vector1)
    # print(vector2)
    list_doc1, list_doc2 = [], []
    for topic1, vec1 in vector1:
        flag = False
        for topic2, vec2 in vector2:
            if topic1 == topic2:
                list_doc1.append(vec1)
                list_doc2.append(vec2)
                flag = True
        if not flag:
            list_doc1.append(0)
            list_doc2.append(1)
    while len(list_doc1) < num_topics:
        list_doc1.append(0)
        list_doc2.append(1)
    try:
        sim = np.dot(list_doc1, list_doc2) / (np.linalg.norm(list_doc1) * np.linalg.norm(list_doc2))
    except ValueError:
        sim = 0
        # Get the similarity between documents. The larger the similarity, the closer it will be
    return sim if not pandas.isnull(sim) else 0


def get_dictionary(dict_file):
    corpus = []
    if not os.path.exists(dict_file):
        with open(os.path.join(os.getcwd(),'PaperRecommend\\arxiv_data\data_only.txt') )as f:
            w = f.readline()
            while w:
                corpus.append(word_tokenize(w.strip()))
                w = f.readline()
        # Train the model on the corpus.
        corpus_dictionary = Dictionary(corpus)
        corpus_dictionary.save(dict_file)
    else:
        corpus_dictionary = Dictionary.load(dict_file)
    return corpus_dictionary, corpus
    # if dict already exist, return corpus will be empty


def get_model(model_name, model_file, common_corpus, n_topics=50):
    if model_name == 'lda':
        if not os.path.exists(model_file):
            model = gensim.models.LdaModel(common_corpus, num_topics=n_topics)
            # Save model to disk.
            model.save(model_file)
        else:
            model = gensim.models.LdaModel.load(model_file)
    elif model_name == 'tfidf':
        if not os.path.exists(model_file):
            model = TfidfModel(common_corpus)  # fit model
            model.save(model_file)
        else:
            model = gensim.models.TfidfModel.load(model_file)
    elif model_name == 'word2vec':
        if not os.path.exists(os.path.join(model_file, 'lexvec.enwiki+newscrawl.300d.W.pos.vectors')):
            print('downloading word2vec model ...')
            url = 'https://www.dropbox.com/s/kguufyc2xcdi8yk/lexvec.enwiki%2Bnewscrawl.300d.W.pos.vectors.gz?dl=1'
            down_res = requests.get(url)
            filename = os.path.join(model_file, 'lexvec.enwiki+newscrawl.300d.W.pos.vectors.gz')
            with open(filename, 'wb') as file:
                file.write(down_res.content)

            # 获取文件的名称，去掉后缀名
            f_name = filename.replace(".gz", "")
            # 开始解压
            print('unzip word2vec model ...')
            g_file = gzip.GzipFile(filename)
            # 读取解压后的文件，并写入去掉后缀名的同名文件（即得到解压后的文件）
            open(f_name, "wb+").write(g_file.read())
        print('load word2vec model ...')
        model = gensim.models.KeyedVectors.load_word2vec_format(os.path.join(model_file, 'lexvec.enwiki+newscrawl.300d.W.pos.vectors'),
                                                                         binary=False)
    else:
        model = None
    return model


def para_similarity(tfidf, corpus_dictionary, doc1, doc2):
    vector1, vector2 = tfidf[corpus_dictionary.doc2bow(word_tokenize(doc1))], \
                       tfidf[corpus_dictionary.doc2bow(word_tokenize(doc2))]
    index = gensim.similarities.SparseMatrixSimilarity([vector1], num_features=len(corpus_dictionary.keys()))
    sim = index[[vector2]]
    return sim[0][0]


def proceed_data(userid, user_favor: list, papers: pd.DataFrame,model):
    """

    :param userid: 0
    :param user_favor: [paperId] -> [1, 3, 5]
    :param papers: Papers in user's interested area, type: pd.DataFrame, column index is paperId
                        title  summary  keywords
                    1   'XX'   'XX'     'XX XX XX'
                    4   'XX'   'XX'     'XX XX XX'
                    5   'XX'   'XX'     'XX XX XX'
                    6   'XX'   'XX'     'XX XX XX'
    :return:
    """
    itemBasedCF = ItemBasedCF()
    for favor_paper in user_favor:
        item, rating = favor_paper, 5.0
        itemBasedCF.train.setdefault(userid, [])
        itemBasedCF.train[userid].append([item, float(rating)])
    itemBasedCF.papers = papers
    itemBasedCF.similarity(model)
    rec = itemBasedCF.recommendation(userid)
    return rec


# if __name__ == "__main__":
#     file_path = "arxiv_data/ratings.csv"
#     itemBasedCF = ItemBasedCF()
#     itemBasedCF.get_data(file_path, "arxiv_data/papers.csv")
#     # itemBasedCF.similarity()
#     user = random.sample(list(itemBasedCF.train), 1)
#     rec = itemBasedCF.recommendation(user[0])
#     print('\nitems recommeded for user whose userId is', user[0], ':')
#     print(rec)
