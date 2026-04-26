# calc_delta_div.py — DNS v2.1, keine Schätzung
import json, re
from pathlib import Path
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DIR = Path("03_outputs")
files = sorted(DIR.glob("*.md"))
names = [f.stem for f in files]
texts = [f.read_text(encoding="utf-8") for f in files]

clean = [re.sub(r'[^a-z0-9\s]', ' ', t.lower()) for t in texts]
sets = [set(t.split()) for t in clean]

tfidf = TfidfVectorizer(stop_words='english').fit_transform(clean)
cos = cosine_similarity(tfidf)

mat = np.zeros((6,6))
for i in range(6):
    for j in range(6):
        if i==j: continue
        jac = len(sets[i]&sets[j]) / len(sets[i]|sets[j])
        mat[i,j] = 0.5*(1-jac) + 0.5*(1-cos[i,j])

avg = float(np.mean(mat[np.triu_indices(6,1)]))

out = {
  "formula": "0.5*(1-Jaccard) + 0.5*(1-Cosine)",
  "models": names,
  "average_delta_div": round(avg,4),
  "pairwise_matrix": [[round(float(x),4) for x in row] for row in mat],
  "interpretation": "structured divergence" if 0.62 <= avg < 0.78 else "other"
}
Path("04_delta_div.json").write_text(json.dumps(out, indent=2))
print(json.dumps(out, indent=2))
