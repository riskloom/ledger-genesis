# Provenance — every published file traced to its archived source

This table covers everything under `package/`, which is the copied evidence.
The repository's own files — `README.md`, `LIMITATIONS.md`,
`CLASS_B_SPECIFICATION.md`, `PROVENANCE.md`, `verify.sh`, `reproduce.sh`,
`sha256sums.sh` and the workflow — were written for this package and have no
archived source. They are covered by `SHA256SUMS` and therefore by the root.

Each file under `package/` mirrors an object in the RiskLoom immutable
disclosure archive. The archive path shown is the S3 key with the leading
`disclosure/` prefix removed; the full key is

    s3://rl-raw-inputs-361964630357/disclosure/<archive path>

That bucket is private, versioned, and under S3 Object Lock in COMPLIANCE
mode. It is named here so the mapping is checkable by anyone who is granted
read access; it is not publicly readable and no credentials are published.

**Status column**

- `IDENTICAL` — the published bytes are byte-for-byte the archived object.
  The published SHA-256 equals the archived SHA-256 recorded in the archive's
  own manifest, which was written before this package existed.
- `REDACTED` — the published file is NOT the archived object. See the
  redaction notice at the head of the file itself.

Counts: **48 IDENTICAL**, **2 REDACTED**, 0 other.

| Published path | Archive path | Archived SHA-256 | Published SHA-256 | Status |
|---|---|---|---|---|
| `package/MANIFEST.json` | `MANIFEST.json` | `1728f088c3e4d3622b30c31fd2dd8736301b4d48c31e231ca0190190c1d9cc52` | `1728f088c3e4d3622b30c31fd2dd8736301b4d48c31e231ca0190190c1d9cc52` | IDENTICAL |
| `package/protocol/AMENDMENT_1.md` | `protocol/AMENDMENT_1.md` | `f6a8d80c7da1cf1687eae39b7bdd40d8cd7e23197e3982d4643f9c668753b60c` | `f6a8d80c7da1cf1687eae39b7bdd40d8cd7e23197e3982d4643f9c668753b60c` | IDENTICAL |
| `package/protocol/RiskLoom_Prospective_Evaluation_Protocol_v1.0.pdf` | `protocol/RiskLoom_Prospective_Evaluation_Protocol_v1.0.pdf` | `9ebf02e41ea4b45f707cf029be68e41f26aba9ec578c4ec52a15bed71d168127` | `9ebf02e41ea4b45f707cf029be68e41f26aba9ec578c4ec52a15bed71d168127` | IDENTICAL |
| `package/results/window_1/MANIFEST.json` | `results/window_1/MANIFEST.json` | `c2a2d136f1743f61b09bc8ba462c7d9df43d0a585c9b3f381fcb514c46a6b69a` | `c2a2d136f1743f61b09bc8ba462c7d9df43d0a585c9b3f381fcb514c46a6b69a` | IDENTICAL |
| `package/results/window_1/WINDOW_2_DECLARATION.md` | `results/window_1/WINDOW_2_DECLARATION.md` | `39a9abcf41107d76ad6a30eec5d25a86d43a68fb6f8e0ada2b547c431d6dbb9e` | `39a9abcf41107d76ad6a30eec5d25a86d43a68fb6f8e0ada2b547c431d6dbb9e` | IDENTICAL |
| `package/results/window_1/code/01_load_ledger.py` | `results/window_1/code/01_load_ledger.py` | `ba05f22a29e458446d60933759c2d4394815214945f78438f901f84dd7c36318` | `ba05f22a29e458446d60933759c2d4394815214945f78438f901f84dd7c36318` | IDENTICAL |
| `package/results/window_1/code/02_layer1_and_anchors.py` | `results/window_1/code/02_layer1_and_anchors.py` | `b6fdf2904d4e6a3211e01f9cdf0b3b65668b79d28a37274621c66e6142bc5d33` | `b6fdf2904d4e6a3211e01f9cdf0b3b65668b79d28a37274621c66e6142bc5d33` | IDENTICAL |
| `package/results/window_1/code/03_build_price_series.py` | `results/window_1/code/03_build_price_series.py` | `57079f22c99b139e6505142aca01b31518efafbf86328d453462550aafab99a9` | `57079f22c99b139e6505142aca01b31518efafbf86328d453462550aafab99a9` | IDENTICAL |
| `package/results/window_1/code/04_layer2_grid.py` | `results/window_1/code/04_layer2_grid.py` | `bce2aa2782e7c353f010a5bc1af0eeedbc78d56098fc91b85628148745204f90` | `bce2aa2782e7c353f010a5bc1af0eeedbc78d56098fc91b85628148745204f90` | IDENTICAL |
| `package/results/window_1/code/05_maxstate_split.py` | `results/window_1/code/05_maxstate_split.py` | `67edd89bb5853d94ab85d94cb3221be90c4c799c064fbba088a5f88fe8f38771` | `67edd89bb5853d94ab85d94cb3221be90c4c799c064fbba088a5f88fe8f38771` | IDENTICAL |
| `package/results/window_1/code/06_per_symbol.py` | `results/window_1/code/06_per_symbol.py` | `655e4adfe4a7be1adbd1729335b528d8c522529039f557115c43f361bcef9f42` | `655e4adfe4a7be1adbd1729335b528d8c522529039f557115c43f361bcef9f42` | IDENTICAL |
| `package/results/window_1/code/INVOCATION.redacted.md` | `results/window_1/code/INVOCATION.md` | `dbcee8780c561aa61af7f0ea245a18aeff2be0c8efe6a0f4ba91bb28fe68f077` | `45f283bb424a90ab8a795dd1b38dc6c8a347f58cf791c1f5f754a97084406bf2` | REDACTED |
| `package/results/window_1/data/bars.json` | `results/window_1/data/bars.json` | `c5f4c26d7adc29e986ce0e140a63c2200b2eae3166050372fd5cd06cb33d5e55` | `c5f4c26d7adc29e986ce0e140a63c2200b2eae3166050372fd5cd06cb33d5e55` | IDENTICAL |
| `package/results/window_1/data/baseline.json` | `results/window_1/data/baseline.json` | `33d105b24d25f14e4d680aa9271ef632326be7d0b2053e776269f3e5f27ae6bd` | `33d105b24d25f14e4d680aa9271ef632326be7d0b2053e776269f3e5f27ae6bd` | IDENTICAL |
| `package/results/window_1/data/episodes.json` | `results/window_1/data/episodes.json` | `c9d23216ab4a4f9dfdbbee900c8a4718cea3b1cbd0f9568e69893c7f50ae1d6e` | `c9d23216ab4a4f9dfdbbee900c8a4718cea3b1cbd0f9568e69893c7f50ae1d6e` | IDENTICAL |
| `package/results/window_1/data/layer1.json` | `results/window_1/data/layer1.json` | `3f4f7cd748741b37149195646ce2e42990aad249fd3e4d224c5d78235b2fc0be` | `3f4f7cd748741b37149195646ce2e42990aad249fd3e4d224c5d78235b2fc0be` | IDENTICAL |
| `package/results/window_1/data/layer2.json` | `results/window_1/data/layer2.json` | `438809cbd0c7d58ddd50c73a513acfdd1dd50df15cce3a920d0ceb4ae9e93e34` | `438809cbd0c7d58ddd50c73a513acfdd1dd50df15cce3a920d0ceb4ae9e93e34` | IDENTICAL |
| `package/results/window_1/data/ledger_window.json` | `results/window_1/data/ledger_window.json` | `78a295190565cd30a27109165c44788cd72dcce7b84d4a3caf04ae890678e985` | `78a295190565cd30a27109165c44788cd72dcce7b84d4a3caf04ae890678e985` | IDENTICAL |
| `package/results/window_1/data/universe.json` | `results/window_1/data/universe.json` | `be2a6c67c62f13b7c4a946bf829e79f30c5c6e63e12fbd719b2ce98aed9f3eee` | `be2a6c67c62f13b7c4a946bf829e79f30c5c6e63e12fbd719b2ce98aed9f3eee` | IDENTICAL |
| `package/results/window_1/report/EVALUATION_REPORT.md` | `results/window_1/report/EVALUATION_REPORT.md` | `2b87d8f305f30d9543d77c802504870df8c441edd62e1431af8702f881cf39c5` | `2b87d8f305f30d9543d77c802504870df8c441edd62e1431af8702f881cf39c5` | IDENTICAL |
| `package/results/window_1/report/run_log_01_02.txt` | `results/window_1/report/run_log_01_02.txt` | `7043b320f614cf3b59442fd3a03791ff8e2518a0ae5d1925745e5dbc1c48d17b` | `7043b320f614cf3b59442fd3a03791ff8e2518a0ae5d1925745e5dbc1c48d17b` | IDENTICAL |
| `package/results/window_1/report/run_log_03_prices.txt` | `results/window_1/report/run_log_03_prices.txt` | `6b6d201938a003e0217cb14962c17058fc37fb6c0d83827ae460eb99dbdca8c1` | `6b6d201938a003e0217cb14962c17058fc37fb6c0d83827ae460eb99dbdca8c1` | IDENTICAL |
| `package/results/window_1/report/run_log_04_grid.txt` | `results/window_1/report/run_log_04_grid.txt` | `370143d42d5d7ba28b3f562d8ade825a6fe0a71c1712a1196dace3e21a4cbed3` | `370143d42d5d7ba28b3f562d8ade825a6fe0a71c1712a1196dace3e21a4cbed3` | IDENTICAL |
| `package/results/window_1/report/run_log_05_maxstate.txt` | `results/window_1/report/run_log_05_maxstate.txt` | `98db813374896b951e7c3c5806ca110969b1a1e9cb322944d20a6c5f6024669c` | `98db813374896b951e7c3c5806ca110969b1a1e9cb322944d20a6c5f6024669c` | IDENTICAL |
| `package/results/window_1/report/run_log_06_per_symbol.txt` | `results/window_1/report/run_log_06_per_symbol.txt` | `d45a168b3df95e9d5f456e7a33ca3541f1e9e0ea4c7b977f0a73b6b1fcd09909` | `d45a168b3df95e9d5f456e7a33ca3541f1e9e0ea4c7b977f0a73b6b1fcd09909` | IDENTICAL |
| `package/results/window_2/ARCHIVAL_INCIDENT.md` | `results/window_2/ARCHIVAL_INCIDENT.md` | `279bd9582208622c35567202233a35c70bdeb01d389e84e8d8930a22880f109c` | `279bd9582208622c35567202233a35c70bdeb01d389e84e8d8930a22880f109c` | IDENTICAL |
| `package/results/window_2/MANIFEST.json` | `results/window_2/MANIFEST.json` | `41a4c50162f1cc5398ea5a8711ea3cdead3236cb23f4a26030b4b91cc2ad6ee6` | `41a4c50162f1cc5398ea5a8711ea3cdead3236cb23f4a26030b4b91cc2ad6ee6` | IDENTICAL |
| `package/results/window_2/code/01_load_ledger.py` | `results/window_2/code/01_load_ledger.py` | `33ff8681bc99cef83f8d23b9b787cdda3d7d4ebca24d8be7d4d1b1f9ef2eaf9e` | `33ff8681bc99cef83f8d23b9b787cdda3d7d4ebca24d8be7d4d1b1f9ef2eaf9e` | IDENTICAL |
| `package/results/window_2/code/02_layer1_and_anchors.py` | `results/window_2/code/02_layer1_and_anchors.py` | `1176b7465361fdee658e7aa41256034cbda844262096d9b0a9cbb97a0f90fb32` | `1176b7465361fdee658e7aa41256034cbda844262096d9b0a9cbb97a0f90fb32` | IDENTICAL |
| `package/results/window_2/code/03_build_price_series.py` | `results/window_2/code/03_build_price_series.py` | `1625c1bf48e1c640336d8e15bbb6c30bf00f6878d5e193cee4c1469b740702a5` | `1625c1bf48e1c640336d8e15bbb6c30bf00f6878d5e193cee4c1469b740702a5` | IDENTICAL |
| `package/results/window_2/code/04_layer2_grid.py` | `results/window_2/code/04_layer2_grid.py` | `ad41963494f6251198701321f2d9e49ea2681ecfdf6ee73567a0113cb3103a4b` | `ad41963494f6251198701321f2d9e49ea2681ecfdf6ee73567a0113cb3103a4b` | IDENTICAL |
| `package/results/window_2/code/05_maxstate_split.py` | `results/window_2/code/05_maxstate_split.py` | `87370fdd825f810c123646337957e492b5c06dd6bf1a6abd01ae2a901929b253` | `87370fdd825f810c123646337957e492b5c06dd6bf1a6abd01ae2a901929b253` | IDENTICAL |
| `package/results/window_2/code/06_per_symbol.py` | `results/window_2/code/06_per_symbol.py` | `edd19d758304e30162374a1b105068dcb244bcc725fed681d2790b22f028b505` | `edd19d758304e30162374a1b105068dcb244bcc725fed681d2790b22f028b505` | IDENTICAL |
| `package/results/window_2/code/INVOCATION.redacted.md` | `results/window_2/code/INVOCATION.md` | `a15dc4f16a730319a5795cf1119cb2c971ad36ec40358df86a5908666ae1c00f` | `17f95f457a85ae3ff7f5c0431a23a3715b6072935608fb049f11d1da9942216d` | REDACTED |
| `package/results/window_2/data/bars.json` | `results/window_2/data/bars.json` | `e3d1b3560d52ea76ea38bfcdae0c427fac3ee43d7ae38fc3cc9c3be69d6eb580` | `e3d1b3560d52ea76ea38bfcdae0c427fac3ee43d7ae38fc3cc9c3be69d6eb580` | IDENTICAL |
| `package/results/window_2/data/baseline.json` | `results/window_2/data/baseline.json` | `a2e8d47511ad3467344af6c3fcc343dbbfea95eacefd6010692b78d2c2636564` | `a2e8d47511ad3467344af6c3fcc343dbbfea95eacefd6010692b78d2c2636564` | IDENTICAL |
| `package/results/window_2/data/episodes.json` | `results/window_2/data/episodes.json` | `fdffd0e10d628b09b7de3b05868dbda7762e8b38d93903fe90cf42797c26b262` | `fdffd0e10d628b09b7de3b05868dbda7762e8b38d93903fe90cf42797c26b262` | IDENTICAL |
| `package/results/window_2/data/layer1.json` | `results/window_2/data/layer1.json` | `b84d451fdef39795fd1dd8e6874dacf47e8b4403653e3cdb11e65d4a80274f1d` | `b84d451fdef39795fd1dd8e6874dacf47e8b4403653e3cdb11e65d4a80274f1d` | IDENTICAL |
| `package/results/window_2/data/layer2.json` | `results/window_2/data/layer2.json` | `5fbe53f0820893f611a31cfc82b55acdaa350e4dbddeaae88f5036304858768b` | `5fbe53f0820893f611a31cfc82b55acdaa350e4dbddeaae88f5036304858768b` | IDENTICAL |
| `package/results/window_2/data/ledger_window.json` | `results/window_2/data/ledger_window.json` | `e77eefedbdfca0d5dd04ea66a5cae66db87bba2b3e6b6aedce9ef2d0361bbaaa` | `e77eefedbdfca0d5dd04ea66a5cae66db87bba2b3e6b6aedce9ef2d0361bbaaa` | IDENTICAL |
| `package/results/window_2/data/universe.json` | `results/window_2/data/universe.json` | `be2a6c67c62f13b7c4a946bf829e79f30c5c6e63e12fbd719b2ce98aed9f3eee` | `be2a6c67c62f13b7c4a946bf829e79f30c5c6e63e12fbd719b2ce98aed9f3eee` | IDENTICAL |
| `package/results/window_2/report/EVALUATION_REPORT.md` | `results/window_2/report/EVALUATION_REPORT.md` | `a64cf93437c1ac7e2e217cd61c9e088b93ba915550fe94bdcb49de55a0868b06` | `a64cf93437c1ac7e2e217cd61c9e088b93ba915550fe94bdcb49de55a0868b06` | IDENTICAL |
| `package/results/window_2/report/run_log_01.txt` | `results/window_2/report/run_log_01.txt` | `2210fffce494a7ed57fced400bd21acd96ab699dfcc007ac0cf07811e084f531` | `2210fffce494a7ed57fced400bd21acd96ab699dfcc007ac0cf07811e084f531` | IDENTICAL |
| `package/results/window_2/report/run_log_02.txt` | `results/window_2/report/run_log_02.txt` | `e464163e914362063b06d7361bd3cc2a31c2eaeac7c421ca13f64ba34bd6edcd` | `e464163e914362063b06d7361bd3cc2a31c2eaeac7c421ca13f64ba34bd6edcd` | IDENTICAL |
| `package/results/window_2/report/run_log_03.txt` | `results/window_2/report/run_log_03.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | IDENTICAL |
| `package/results/window_2/report/run_log_03_attempt2.txt` | `results/window_2/report/run_log_03_attempt2.txt` | `163e77227b358c8cf46d3d374389a7a7a7104eba65d4fd2040295971a29e631a` | `163e77227b358c8cf46d3d374389a7a7a7104eba65d4fd2040295971a29e631a` | IDENTICAL |
| `package/results/window_2/report/run_log_04.txt` | `results/window_2/report/run_log_04.txt` | `1f1eeb808ca9cb0da831b18378e9be432d05005f4b3cde6bb7268b93c7e703f2` | `1f1eeb808ca9cb0da831b18378e9be432d05005f4b3cde6bb7268b93c7e703f2` | IDENTICAL |
| `package/results/window_2/report/run_log_05.txt` | `results/window_2/report/run_log_05.txt` | `ac6b78455fd8d2837593717f6b93f0076144e457c65102cd509dd9324d5617fe` | `ac6b78455fd8d2837593717f6b93f0076144e457c65102cd509dd9324d5617fe` | IDENTICAL |
| `package/results/window_2/report/run_log_06.txt` | `results/window_2/report/run_log_06.txt` | `f384dad08d3eca83f03651e67a38ea4608e657d1864dadd08717e1db5dc7e31c` | `f384dad08d3eca83f03651e67a38ea4608e657d1864dadd08717e1db5dc7e31c` | IDENTICAL |
| `package/thresholds/thresholds.json` | `thresholds/thresholds.json` | `abaf499d9089fd363dd6fdd6f5b1be59177dccb99520b16f9ed1913de83232d3` | `abaf499d9089fd363dd6fdd6f5b1be59177dccb99520b16f9ed1913de83232d3` | IDENTICAL |

