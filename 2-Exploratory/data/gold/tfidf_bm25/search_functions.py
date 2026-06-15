import pickle, numpy as np, pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path

_DIR  = Path(__file__).parent
_vect = pickle.load(open(_DIR / 'tfidf_vectorizer.pkl','rb'))
_bm25 = pickle.load(open(_DIR / 'bm25_index.pkl','rb'))
_map  = pd.read_parquet(_DIR / 'doc_index_map.parquet')

def _tok(q):
    import re, unicodedata
    t2 = unicodedata.normalize('NFD',q).encode('ascii','ignore').decode().lower()
    return [w for w in re.findall(r'[a-z]{3,}',t2) if len(w)>=3]

def search_bm25(query, top_k=10):
    sc = np.array(_bm25.get_scores(_tok(query)))
    idx = sc.argsort()[::-1][:top_k]
    r = _map.iloc[idx].copy(); r['score_bm25']=sc[idx]; r['rank']=range(1,len(idx)+1)
    return r

def search_tfidf(query, top_k=10):
    from scipy.sparse import load_npz
    qv = _vect.transform([' '.join(_tok(query))])
    mat = load_npz(_DIR/'tfidf_matrix.npz')
    sc = cosine_similarity(qv,mat).flatten()
    idx = sc.argsort()[::-1][:top_k]
    r = _map.iloc[idx].copy(); r['score_tfidf']=sc[idx]; r['rank']=range(1,len(idx)+1)
    return r