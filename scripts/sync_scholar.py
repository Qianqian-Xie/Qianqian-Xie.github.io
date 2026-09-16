#!/usr/bin/env python3
"""Pull the publication list and citation stats from Google Scholar into data/pubs.js.

Usage: python3 scripts/sync_scholar.py [SCHOLAR_USER_ID]
No third-party dependencies. Google Scholar may rate-limit automated requests;
if a run fails, the previous data/pubs.js is left untouched.
"""
import html, json, re, sys, time, urllib.request, datetime, pathlib

USER = sys.argv[1] if len(sys.argv) > 1 else "UYW7X_0AAAAJ"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
OUT = pathlib.Path(__file__).resolve().parent.parent / "data" / "pubs.js"

RULES = [
 ('neurips','NeurIPS'),('nature communications','Nature Communications'),('npj digital','npj Digital Medicine'),
 ('nature medicine','Nature Medicine'),('acl rolling','ARR'),('findings of the association','ACL Findings'),
 ('empirical methods in natural language','EMNLP'),('emnlp','EMNLP'),('north american chapter','NAACL'),('naacl','NAACL'),
 ('eacl','EACL'),('international conference on computational','COLING'),('coling','COLING'),
 ('chinese national conference on computational','CCL'),('\\bccl\\b','CCL'),
 ('annual meeting of the association for computational','ACL'),('association for computational linguistics','ACL'),('\\bacl\\b','ACL'),
 ('web conference','WWW'),('\\bwww\\b','WWW'),('sigir','SIGIR'),('sigkdd','KDD'),('\\bkdd\\b','KDD'),
 ('transactions on information systems','TOIS'),('\\btois\\b','TOIS'),('jamia','JAMIA'),('journal of the american medical informatics','JAMIA'),('amia','AMIA'),
 ('journal of biomedical informatics','JBI'),('journal of biomedical and health','IEEE JBHI'),('briefings in bioinformatics','Briefings in Bioinformatics'),
 ('bioinformatics','Bioinformatics'),('information processing','IPM'),('medical informatics','IJMI'),('tkde','TKDE'),('knowledge and data eng','TKDE'),
 ('tnnls','TNNLS'),('aaai','AAAI'),('ijcai','IJCAI'),('ijcnn','IJCNN'),('natural language processing and chinese','NLPCC'),('nlpcc','NLPCC'),
 ('learning representations','ICLR'),('iclr','ICLR'),('icml','ICML'),('plos','PLOS ONE'),('medrxiv','medRxiv'),('biorxiv','bioRxiv'),('arxiv','arXiv'),('ssrn','SSRN'),
 ('中文信息学报','JCIP'),('cikm','CIKM'),('workshop on biomedical','BioNLP'),('bionlp','BioNLP'),('financial technology and natural language','FinNLP'),
 ('lrec','LREC'),('icdm','ICDM'),('applied intelligence','Applied Intelligence'),('expert systems','ESWA'),('neurocomputing','Neurocomputing'),
 ('knowledge-based systems','KBS'),('knowledge and information','KAIS'),('scientific reports','Scientific Reports'),('ecir','ECIR'),('dasfaa','DASFAA'),
 ('pakdd','PAKDD'),('wsdm','WSDM'),('computing survey','ACM CSUR'),('software: practice','SPE'),('systems and software','JSS'),('jmir','JMIR'),
 ('healthcare informatics','IEEE ICHI'),('chinese journal of computers','计算机学报'),('south china agricultural','华南农业大学学报'),('武汉大学学报','武汉大学学报'),
 ('web information systems','WISE'),('web-age information','WAIM'),('computer supported cooperative','CSCWD'),('patent','Patent'),('physionet','PhysioNet'),
 ('yearbook','IMIA Yearbook'),('annual review','Annu. Rev. Biomed. Data Sci.'),('computers in biology','CBM'),('occupational','OEM'),('methods, applications','Methods & Applications'),
 ('information fusion','Information Fusion'),('ieee transactions','IEEE Trans.'),('ieee','IEEE'),('journal','Journal'),('proceedings','Proc.'),('conference','Conf.'),('workshop','Workshop'),
]

def short(v):
    v = re.sub(r',\s*\d{4}$', '', v).strip(); l = v.lower()
    for k, t in RULES:
        if re.search(k, l): return t
    return (v[:26] + '…') if len(v) > 27 else (v or 'Preprint')

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en"})
    with urllib.request.urlopen(req, timeout=30) as r: return r.read().decode("utf-8", "replace")

rows, stats = [], {}
for start in range(0, 1000, 100):
    s = fetch(f"https://scholar.google.com/citations?user={USER}&hl=en&cstart={start}&pagesize=100&sortby=pubdate")
    if start == 0:
        st = re.findall(r'<td class="gsc_rsb_std">(\d+)</td>', s)
        if len(st) >= 5: stats = {"citations": int(st[0]), "h": int(st[2]), "i10": int(st[4])}
    page = 0
    for m in re.finditer(r'<tr class="gsc_a_tr">(.*?)</tr>', s, re.S):
        r = m.group(1)
        a = re.search(r'<a href="([^"]+)" class="gsc_a_at">(.*?)</a>', r)
        if not a: continue
        gs = re.findall(r'<div class="gs_gray">(.*?)</div>', r, re.S)
        au = html.unescape(re.sub('<[^>]+>', '', gs[0])) if gs else ''
        ve = html.unescape(re.sub('<[^>]+>', '', gs[1])) if len(gs) > 1 else ''
        cit = re.search(r'class="gsc_a_ac gs_ibl">(\d*)<', r)
        yr = re.search(r'gsc_a_hc gs_ibl">(\d*)<', r)
        rows.append({"t": html.unescape(a.group(2)), "a": [x.strip() for x in au.split(',')],
                     "v": short(ve), "y": yr.group(1) if yr else '',
                     "c": int(cit.group(1)) if cit and cit.group(1) else 0,
                     "u": "https://scholar.google.com" + html.unescape(a.group(1))})
        page += 1
    if page < 100: break
    time.sleep(3)

if len(rows) < 50:
    sys.exit(f"Only {len(rows)} rows parsed; Scholar probably blocked the request. Keeping existing data.")
stats.update({"n": len(rows), "date": datetime.date.today().isoformat()})
OUT.write_text("window.STATS=" + json.dumps(stats) + ";\nwindow.PUBS=" + json.dumps(rows, ensure_ascii=False) + ";\n", encoding="utf-8")
print(f"Wrote {len(rows)} publications, stats {stats}")
