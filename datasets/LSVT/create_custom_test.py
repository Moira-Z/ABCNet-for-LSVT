import json
import os
import glob
from shapely.geometry import *

filepath = r'./train_full_labels_new.json'
with open(filepath, 'r') as f:
    labels = json.load(f)

for il, label in labels.items():
    num = il.split('_')[-1]
    fill = num.zfill(7)
    out = r'./sorted_gt_lsvt_res/' + fill + '.txt'
    fout = open(out, 'w', encoding = "utf-8")
    for box in label:
        rec  = box["transcription"]
        cors = box["points"]
        if rec == '###': continue
        pts = [(round(float(ix[0])), round(float(ix[1]))) for ix in cors]
        try:
            pgt = Polygon(pts)
        except Exception as e:
            print(e)
            print('An invalid detection in {} line {} is removed ... '.format(il, rec))
            continue
        
        if not pgt.is_valid:
            print('An invalid detection in {} line {} is removed ... '.format(il, rec))
            continue
            
        pRing = LinearRing(pts)
        if pRing.is_ccw:
            pts.reverse()
        outstr = ''
        for ipt in pts[:-1]:
            outstr += (str(int(ipt[0]))+','+ str(int(ipt[1]))+',')
        outstr += (str(int(pts[-1][0]))+','+ str(int(pts[-1][1])))
        outstr = outstr+',####' + rec
        fout.writelines(outstr+'\n')
    fout.close()

import zipfile
os.chdir("sorted_gt_lsvt_res")
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

zipf = zipfile.ZipFile('../gt_lsvt.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('./', zipf)
zipf.close()
os.chdir("../")

'''
Step five: eval_dataset to 'custom' in main.py and run.
    Example results:
        "E2E_RESULTS: precision: 0.6666666666666666, recall: 0.6666666666666666, hmean: 0.6666666666666666"
        "DETECTION_ONLY_RESULTS: precision: 1.0, recall: 1.0, hmean: 1.0"

    E2E is less than Det result because 'happy' is not matched to 'enjoy'.
'''
