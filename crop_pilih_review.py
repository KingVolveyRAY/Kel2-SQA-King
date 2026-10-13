#!/usr/bin/env python3
"""
crop_pilih_review.py -- membantu memilih review dari CSV metadata CROP.

Contoh:
  python crop_pilih_review.py metadata/indexing.csv --ringkas
  python crop_pilih_review.py metadata/indexing.csv --kandidat --min-revisi 3 --top 10
  python crop_pilih_review.py metadata/indexing.csv --kandidat --status ABANDONED
  python crop_pilih_review.py metadata/indexing.csv --review 12345 --repo git_repos/indexing

Satu baris CSV = satu revisi. Nama kolom dinormalkan (huruf kecil, '-' jadi '_'),
jadi 'Author', 'change-id', 'change_id' semuanya dikenali.
"""
import argparse
import csv
from collections import Counter, defaultdict

WAJIB = ["review_number", "revision_number", "status", "before_commit_id", "after_commit_id"]


def norm(nama):
    return nama.strip().lower().replace("-", "_").replace(" ", "_")


def baca_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        pembaca = csv.DictReader(f)
        pembaca.fieldnames = [norm(n) for n in pembaca.fieldnames]
        kolom = set(pembaca.fieldnames)
        kurang = [k for k in WAJIB if k not in kolom]
        if kurang:
            raise SystemExit(f"Kolom tidak ditemukan: {kurang}\nKolom di file: {sorted(kolom)}")
        return list(pembaca)


def kelompokkan(baris):
    per_review = defaultdict(list)
    for b in baris:
        per_review[b["review_number"]].append(b)
    for rev in per_review.values():
        rev.sort(key=lambda b: int(b["revision_number"]))
    return per_review


def ringkas(baris, per_review):
    print(f"Jumlah baris (= revisi)         : {len(baris)}")
    print(f"Jumlah review unik              : {len(per_review)}")
    status = Counter(rev[-1]["status"].upper() for rev in per_review.values())
    print(f"Status revisi terakhir per review: {dict(status)}")
    terbanyak = max(len(r) for r in per_review.values())
    print(f"Revisi terbanyak dalam 1 review : {terbanyak}")


def kandidat(per_review, min_revisi, status, top):
    hasil = []
    for nomor, rev in per_review.items():
        if len(rev) < min_revisi:
            continue
        if status and rev[-1]["status"].upper() != status.upper():
            continue
        hasil.append((len(rev), nomor, rev))
    hasil.sort(key=lambda x: (-x[0], x[1]))
    print(f"{'review':>8} {'#rev':>5} {'status_akhir':<12} author_revisi_pertama")
    for n_rev, nomor, rev in hasil[:top]:
        print(f"{nomor:>8} {n_rev:>5} {rev[-1]['status']:<12} {rev[0].get('author', '-')}")
    print(f"\n{len(hasil)} review memenuhi syarat (ditampilkan maks. {top}).")


def detail(per_review, nomor, repo):
    if nomor not in per_review:
        raise SystemExit(f"Review {nomor} tidak ada di CSV.")
    print(f"Review {nomor}: {len(per_review[nomor])} revisi\n")
    for b in per_review[nomor]:
        print(f"-- revisi {b['revision_number']}  status={b['status']}  author={b.get('author', '-')}")
        print(f"   before_commit_id: {b['before_commit_id']}")
        print(f"   after_commit_id : {b['after_commit_id']}")
        if b.get("url"):
            print(f"   url             : {b['url']}")
        print(f"   git -C {repo} diff --stat {b['before_commit_id']} {b['after_commit_id']}")
        print(f"   git -C {repo} diff {b['before_commit_id']} {b['after_commit_id']}\n")


def main():
    ap = argparse.ArgumentParser(description="Pilih review dari metadata CROP")
    ap.add_argument("csv")
    ap.add_argument("--ringkas", action="store_true")
    ap.add_argument("--kandidat", action="store_true")
    ap.add_argument("--min-revisi", type=int, default=2)
    ap.add_argument("--status", default=None, help="mis. MERGED atau ABANDONED")
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--review", default=None, help="nomor review untuk dilihat detailnya")
    ap.add_argument("--repo", default="git_repos/<nama_proyek>")
    a = ap.parse_args()

    baris = baca_csv(a.csv)
    per_review = kelompokkan(baris)
    if a.ringkas:
        ringkas(baris, per_review)
    if a.kandidat:
        kandidat(per_review, a.min_revisi, a.status, a.top)
    if a.review:
        detail(per_review, a.review, a.repo)
    if not (a.ringkas or a.kandidat or a.review):
        ap.print_help()


if __name__ == "__main__":
    main()
