import re
from gensim.models import word2vec
import psycopg2


def get_dataset():
    conn = psycopg2.connect('xxxxxx')
    cur = conn.cursor()
    cur.execute("select * from xxxx")
    data = cur.fetchall()
    print('*'*50)
    print('总行数和类型：',len(data),type(data))
    #print(data[0])
    sentence=[]
    for i in range(len(data)):#遍历每行
      if data[i][0]!=None:#空id字段
        print('*'*50)
        print('开始处理',data[i][0])
        text = data[i]
        word_list = []
        for word in text:
          if word != None:
            word_list.append(str(word))
        print(word_list)
        if len(word_list) > 0:#有效词大于多少才加入最后训练样本
            sentence.append(word_list)

    print('*'*50)              
    print('句子结果 ',sentence)
    return sentence
    
def train(sentence):
    print("开始训练")
    model = word2vec.Word2Vec(sentences = sentence, size = 2, window = 2,min_count=1)
    model.save("testmodel.bin")
    print("训练完成")

if __name__ == '__main__':
    content = get_dataset()
    train(content)
