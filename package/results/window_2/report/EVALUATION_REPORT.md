# Prospective Evaluation — Window 2 — Evaluation Report

Replication of Window 1 under Protocol v1.0 + Amendment 1, unchanged.

    Boundary   2026-09-08T00:00:00Z inclusive .. 2026-09-15T00:00:00Z exclusive
    Expected   2,016 slots      Actual 2,014      Missing 2
    Missing    2026-09-10T10:35:00Z, 2026-09-12T05:20:00Z
               Neither repaired nor interpolated; absent from the denominator.

## 1. Window integrity

    duplicate timestamps          0
    off-grid rows                 0
    rows carrying writer_sig      2014 of 2014
    distinct writer_key_id        1  (arn:aws:kms:eu-west-2:361964630357:key/e39876f8-fcc7-4c2b-9a8f-277fc44f6f7f)
    chain breaks                  0   (chain continuous across both gaps)
    universe                      69 symbols, consistent across all 2014 rows
    thresholds_digest             0568f24ceb798001ecffed6d9101c4c863d1e6c0f5718f1d5aedc70151cfb25d  (identical to Window 1)
    code_digest                   855fe324b44521aef5d6b1dc90c5be4bf115c9c242d92dbddcd5bdae44571dc9  (identical to Window 1)
    methodology_version           public-state/v2+liqpressure+canon2  (identical to Window 1)
    schema_version                canon2  (identical to Window 1)
    symbol set                    identical to Window 1; all 8 majors present

## 2. Layer 1 — descriptive structural state

Symbol-slot observations: 138966

    band                     slots    share%    runs  mean_min median_min
    NORMAL                  136709    98.376     769     888.9       340
    ELEVATED                  2183     1.571     696      15.7      15.0
    CASCADE_PRESSURE            74     0.053      31      11.9        15

    market state             slots    share%    runs  mean_min median_min
    QUIET                     1195    59.335     159      37.6        20
    BUILDING                   483    23.982     189      12.8        15
    ELEVATED                   217    10.775      95      11.4        10
    STRESSED                   119     5.909      36      16.5      15.0
    UNKNOWN                      0     0.000       0      None      None

Descriptive only. Not combined with Layer 2. Not a predictive performance measure.

## 3. Denominators

    warning episodes   700   (ELEVATED-max 669, CASCADE_PRESSURE-max 31)
    baseline anchors   2898

## 4. Layer 2 — full grid, four predeclared figures per cell

### OVERALL  (warning episodes 700, baseline anchors 2898)

    cell         warn n   excl  base n   excl     warn%   NORMAL%   lift pp      rel
     1%/  30m       699      1    2897      1     57.37     30.48     26.89    1.882
     1%/  60m       695      5    2875     23     72.66     46.61     26.05    1.559
     1%/ 120m       694      6    2813     85     86.17     66.58     19.58    1.294
     1%/ 240m       679     21    2691    207     91.90     81.61     10.29    1.126
     2%/  30m       699      1    2897      1     21.32      6.80     14.52    3.135
     2%/  60m       695      5    2875     23     32.37     15.44     16.93    2.096
     2%/ 120m       694      6    2813     85     51.59     28.69     22.90    1.798
     2%/ 240m       679     21    2691    207     68.63     48.46     20.17    1.416
     3%/  30m       699      1    2897      1      7.73      2.38      5.34    3.244
     3%/  60m       695      5    2875     23     13.67      5.63      8.03    2.426
     3%/ 120m       694      6    2813     85     29.97     12.16     17.81    2.465
     3%/ 240m       679     21    2691    207     44.62     24.67     19.95    1.808
     5%/  30m       699      1    2897      1      3.58      0.59      2.99    6.095
     5%/  60m       695      5    2875     23      4.60      1.08      3.53    4.270
     5%/ 120m       694      6    2813     85      9.65      3.84      5.81    2.515
     5%/ 240m       679     21    2691    207     19.00      8.81     10.19    2.157

### MAJORS  (warning episodes 88, baseline anchors 336)

    cell         warn n   excl  base n   excl     warn%   NORMAL%   lift pp      rel
     1%/  30m        88      0     336      0     32.95      8.33     24.62    3.955
     1%/  60m        87      1     332      4     43.68     16.57     27.11    2.637
     1%/ 120m        87      1     327      9     64.37     32.42     31.95    1.986
     1%/ 240m        82      6     312     24     71.95     54.17     17.78    1.328
     2%/  30m        88      0     336      0      6.82      0.60      6.22   11.455
     2%/  60m        87      1     332      4     10.34      4.22      6.13    2.453
     2%/ 120m        87      1     327      9     25.29      7.03     18.25    3.595
     2%/ 240m        82      6     312     24     29.27     16.03     13.24    1.826
     3%/  30m        88      0     336      0      2.27      0.00      2.27      n/a
     3%/  60m        87      1     332      4      3.45      0.90      2.54    3.816
     3%/ 120m        87      1     327      9     17.24      2.45     14.79    7.047
     3%/ 240m        82      6     312     24     18.29      5.77     12.52    3.171
     5%/  30m        88      0     336      0      0.00      0.00      0.00      n/a
     5%/  60m        87      1     332      4      0.00      0.00      0.00      n/a
     5%/ 120m        87      1     327      9      4.60      1.53      3.07    3.007
     5%/ 240m        82      6     312     24      8.54      2.56      5.97    3.329

### NON_MAJORS  (warning episodes 612, baseline anchors 2562)

    cell         warn n   excl  base n   excl     warn%   NORMAL%   lift pp      rel
     1%/  30m       611      1    2561      1     60.88     33.39     27.50    1.824
     1%/  60m       608      4    2543     19     76.81     50.53     26.28    1.520
     1%/ 120m       607      5    2486     76     89.29     71.08     18.21    1.256
     1%/ 240m       597     15    2379    183     94.64     85.20      9.44    1.111
     2%/  30m       611      1    2561      1     23.40      7.61     15.79    3.074
     2%/  60m       608      4    2543     19     35.53     16.91     18.62    2.101
     2%/ 120m       607      5    2486     76     55.35     31.54     23.82    1.755
     2%/ 240m       597     15    2379    183     74.04     52.71     21.33    1.405
     3%/  30m       611      1    2561      1      8.51      2.69      5.82    3.159
     3%/  60m       608      4    2543     19     15.13      6.25      8.88    2.420
     3%/ 120m       607      5    2486     76     31.80     13.44     18.36    2.367
     3%/ 240m       597     15    2379    183     48.24     27.15     21.09    1.777
     5%/  30m       611      1    2561      1      4.09      0.66      3.43    6.164
     5%/  60m       608      4    2543     19      5.26      1.22      4.04    4.317
     5%/ 120m       607      5    2486     76     10.38      4.14      6.24    2.505
     5%/ 240m       597     15    2379    183     20.44      9.63     10.81    2.123

### MAX_ELEVATED  (warning episodes 669, baseline anchors 2898)

    cell         warn n   excl  base n   excl     warn%   NORMAL%   lift pp      rel
     1%/  30m       668      1    2897      1     56.89     30.48     26.41    1.866
     1%/  60m       664      5    2875     23     72.59     46.61     25.98    1.557
     1%/ 120m       663      6    2813     85     86.12     66.58     19.54    1.293
     1%/ 240m       649     20    2691    207     91.99     81.61     10.38    1.127
     2%/  30m       668      1    2897      1     20.66      6.80     13.86    3.038
     2%/  60m       664      5    2875     23     31.78     15.44     16.33    2.058
     2%/ 120m       663      6    2813     85     51.28     28.69     22.59    1.788
     2%/ 240m       649     20    2691    207     68.57     48.46     20.11    1.415
     3%/  30m       668      1    2897      1      7.04      2.38      4.65    2.954
     3%/  60m       664      5    2875     23     13.10      5.63      7.47    2.325
     3%/ 120m       663      6    2813     85     30.02     12.16     17.86    2.469
     3%/ 240m       649     20    2691    207     44.07     24.67     19.39    1.786
     5%/  30m       668      1    2897      1      3.29      0.59      2.71    5.612
     5%/  60m       664      5    2875     23      4.37      1.08      3.29    4.050
     5%/ 120m       663      6    2813     85      9.35      3.84      5.51    2.436
     5%/ 240m       649     20    2691    207     18.95      8.81     10.15    2.152

### MAX_CASCADE_PRESSURE  (warning episodes 31, baseline anchors 2898)

    cell         warn n   excl  base n   excl     warn%   NORMAL%   lift pp      rel
     1%/  30m        31      0    2897      1     67.74     30.48     37.26    2.223
     1%/  60m        31      0    2875     23     74.19     46.61     27.58    1.592
     1%/ 120m        31      0    2813     85     87.10     66.58     20.51    1.308
     1%/ 240m        30      1    2691    207     90.00     81.61      8.39    1.103
     2%/  30m        31      0    2897      1     35.48      6.80     28.68    5.218
     2%/  60m        31      0    2875     23     45.16     15.44     29.72    2.924
     2%/ 120m        31      0    2813     85     58.06     28.69     29.38    2.024
     2%/ 240m        30      1    2691    207     70.00     48.46     21.54    1.445
     3%/  30m        31      0    2897      1     22.58      2.38     20.20    9.481
     3%/  60m        31      0    2875     23     25.81      5.63     20.17    4.580
     3%/ 120m        31      0    2813     85     29.03     12.16     16.87    2.388
     3%/ 240m        30      1    2691    207     56.67     24.67     31.99    2.297
     5%/  30m        31      0    2897      1      9.68      0.59      9.09   16.491
     5%/  60m        31      0    2875     23      9.68      1.08      8.60    8.975
     5%/ 120m        31      0    2813     85     16.13      3.84     12.29    4.201
     5%/ 240m        30      1    2691    207     20.00      8.81     11.19    2.271

Excluded counts are incomplete forward coverage only, per horizon, applied
identically to warning and baseline anchors, never counted as a miss or a
false positive.

## 5. Per-symbol detail

Reference cell 2% / 60 min. Visible for inspection; no claim is made from any
individual symbol. Full table verbatim in report/run_log_06.txt.

## 6. WINDOW 1 vs WINDOW 2

### Layer 1

                                       WINDOW 1           WINDOW 2
    rows                                   2016               2014
    symbol-slot obs                      139104             138966
    NORMAL                     136690 (98.265%)   136709 (98.376%)
    ELEVATED                      2328 (1.674%)      2183 (1.571%)
    CASCADE_PRESSURE                86 (0.062%)        74 (0.053%)
    QUIET                        1014 (50.298%)     1195 (59.335%)
    BUILDING                      624 (30.952%)      483 (23.982%)
    ELEVATED                      249 (12.351%)      217 (10.775%)
    STRESSED                       129 (6.399%)       119 (5.909%)
    UNKNOWN                          0 (0.000%)         0 (0.000%)

### OVERALL

    W1 episodes 733 / baseline 2898      W2 episodes 700 / baseline 2898

    cell        W1 warn% W1 norm%  W1 lift   W1 rel | W2 warn% W2 norm%  W2 lift   W2 rel | d lift pp
     1%/  30m      68.33    27.43    40.90    2.491 |    57.37    30.48    26.89    1.882 |    -14.01
     1%/  60m      79.86    44.38    35.49    1.800 |    72.66    46.61    26.05    1.559 |     -9.44
     1%/ 120m      87.34    66.11    21.23    1.321 |    86.17    66.58    19.58    1.294 |     -1.65
     1%/ 240m      93.01    82.93    10.08    1.122 |    91.90    81.61    10.29    1.126 |      0.21
     2%/  30m      36.53     6.94    29.59    5.267 |    21.32     6.80    14.52    3.135 |    -15.07
     2%/  60m      47.78    15.29    32.49    3.126 |    32.37    15.44    16.93    2.096 |    -15.56
     2%/ 120m      58.69    29.57    29.12    1.985 |    51.59    28.69    22.90    1.798 |     -6.22
     2%/ 240m      73.29    48.53    24.75    1.510 |    68.63    48.46    20.17    1.416 |     -4.58
     3%/  30m      18.75     3.11    15.64    6.037 |     7.73     2.38     5.34    3.244 |    -10.30
     3%/  60m      27.50     8.14    19.36    3.377 |    13.67     5.63     8.03    2.426 |    -11.33
     3%/ 120m      39.08    15.94    23.14    2.452 |    29.97    12.16    17.81    2.465 |     -5.33
     3%/ 240m      55.38    28.28    27.11    1.959 |    44.62    24.67    19.95    1.808 |     -7.16
     5%/  30m       9.31     1.00     8.30    9.299 |     3.58     0.59     2.99    6.095 |     -5.31
     5%/  60m      13.33     2.93    10.40    4.546 |     4.60     1.08     3.53    4.270 |     -6.87
     5%/ 120m      20.31     6.07    14.23    3.344 |     9.65     3.84     5.81    2.515 |     -8.42
     5%/ 240m      31.47    11.24    20.23    2.800 |    19.00     8.81    10.19    2.157 |    -10.04

### MAJORS

    W1 episodes 94 / baseline 336      W2 episodes 88 / baseline 336

    cell        W1 warn% W1 norm%  W1 lift   W1 rel | W2 warn% W2 norm%  W2 lift   W2 rel | d lift pp
     1%/  30m      34.83     6.85    27.99    5.088 |    32.95     8.33    24.62    3.955 |     -3.37
     1%/  60m      50.56    13.69    36.87    3.693 |    43.68    16.57    27.11    2.637 |     -9.76
     1%/ 120m      65.17    33.63    31.54    1.938 |    64.37    32.42    31.95    1.986 |      0.41
     1%/ 240m      86.52    59.15    27.37    1.463 |    71.95    54.17    17.78    1.328 |     -9.59
     2%/  30m      13.48     0.30    13.19   45.303 |     6.82     0.60     6.22   11.455 |     -6.97
     2%/  60m      14.61     2.98    11.63    4.908 |    10.34     4.22     6.13    2.453 |     -5.50
     2%/ 120m      17.98     8.63     9.35    2.083 |    25.29     7.03    18.25    3.595 |      8.90
     2%/ 240m      37.08    21.65    15.43    1.713 |    29.27    16.03    13.24    1.826 |     -2.19
     3%/  30m       3.37     0.00     3.37      n/a |     2.27     0.00     2.27      n/a |     -1.10
     3%/  60m       3.37     1.79     1.59    1.888 |     3.45     0.90     2.54    3.816 |      0.95
     3%/ 120m       6.74     4.17     2.57    1.618 |    17.24     2.45    14.79    7.047 |     12.22
     3%/ 240m      17.98    10.98     7.00    1.638 |    18.29     5.77    12.52    3.171 |      5.52
     5%/  30m       0.00     0.00     0.00      n/a |     0.00     0.00     0.00      n/a |      0.00
     5%/  60m       0.00     0.00     0.00      n/a |     0.00     0.00     0.00      n/a |      0.00
     5%/ 120m       1.12     0.00     1.12      n/a |     4.60     1.53     3.07    3.007 |      1.95
     5%/ 240m       2.25     1.22     1.03    1.843 |     8.54     2.56     5.97    3.329 |      4.94

### NON_MAJORS

    W1 episodes 639 / baseline 2562      W2 episodes 612 / baseline 2562

    cell        W1 warn% W1 norm%  W1 lift   W1 rel | W2 warn% W2 norm%  W2 lift   W2 rel | d lift pp
     1%/  30m      73.06    30.13    42.93    2.425 |    60.88    33.39    27.50    1.824 |    -15.43
     1%/  60m      83.99    48.40    35.59    1.735 |    76.81    50.53    26.28    1.520 |     -9.31
     1%/ 120m      90.48    70.37    20.10    1.286 |    89.29    71.08    18.21    1.256 |     -1.89
     1%/ 240m      93.93    86.05     7.88    1.092 |    94.64    85.20     9.44    1.111 |      1.56
     2%/  30m      39.78     7.81    31.97    5.096 |    23.40     7.61    15.79    3.074 |    -16.18
     2%/  60m      52.46    16.90    35.56    3.104 |    35.53    16.91    18.62    2.101 |    -16.94
     2%/ 120m      64.44    32.32    32.13    1.994 |    55.35    31.54    23.82    1.755 |     -8.31
     2%/ 240m      78.43    52.06    26.38    1.507 |    74.04    52.71    21.33    1.405 |     -5.05
     3%/  30m      20.92     3.51    17.41    5.955 |     8.51     2.69     5.82    3.159 |    -11.59
     3%/  60m      30.90     8.98    21.93    3.442 |    15.13     6.25     8.88    2.420 |    -13.05
     3%/ 120m      43.65    17.49    26.16    2.496 |    31.80    13.44    18.36    2.367 |     -7.80
     3%/ 240m      60.70    30.55    30.16    1.987 |    48.24    27.15    21.09    1.777 |     -9.07
     5%/  30m      10.62     1.13     9.49    9.381 |     4.09     0.66     3.43    6.164 |     -6.06
     5%/  60m      15.21     3.32    11.90    4.586 |     5.26     1.22     4.04    4.317 |     -7.86
     5%/ 120m      23.02     6.87    16.15    3.350 |    10.38     4.14     6.24    2.505 |     -9.91
     5%/ 240m      35.62    12.55    23.07    2.837 |    20.44     9.63    10.81    2.123 |    -12.26

### MAX_ELEVATED

    W1 episodes 700 / baseline 2898      W2 episodes 669 / baseline 2898

    cell        W1 warn% W1 norm%  W1 lift   W1 rel | W2 warn% W2 norm%  W2 lift   W2 rel | d lift pp
     1%/  30m      67.39    27.43    39.96    2.457 |    56.89    30.48    26.41    1.866 |    -13.55
     1%/  60m      79.33    44.38    34.95    1.788 |    72.59    46.61    25.98    1.557 |     -8.97
     1%/ 120m      87.03    66.11    20.91    1.316 |    86.12    66.58    19.54    1.293 |     -1.37
     1%/ 240m      92.82    82.93     9.89    1.119 |    91.99    81.61    10.38    1.127 |      0.49
     2%/  30m      35.81     6.94    28.87    5.163 |    20.66     6.80    13.86    3.038 |    -15.01
     2%/  60m      47.31    15.29    32.02    3.095 |    31.78    15.44    16.33    2.058 |    -15.69
     2%/ 120m      58.31    29.57    28.74    1.972 |    51.28    28.69    22.59    1.788 |     -6.15
     2%/ 240m      73.31    48.53    24.78    1.511 |    68.57    48.46    20.11    1.415 |     -4.67
     3%/  30m      17.47     3.11    14.36    5.624 |     7.04     2.38     4.65    2.954 |     -9.71
     3%/  60m      26.35     8.14    18.20    3.235 |    13.10     5.63     7.47    2.325 |    -10.73
     3%/ 120m      38.19    15.94    22.25    2.396 |    30.02    12.16    17.86    2.469 |     -4.39
     3%/ 240m      54.84    28.28    26.56    1.939 |    44.07    24.67    19.39    1.786 |     -7.17
     5%/  30m       8.44     1.00     7.44    8.437 |     3.29     0.59     2.71    5.612 |     -4.73
     5%/  60m      12.66     2.93     9.73    4.318 |     4.37     1.08     3.29    4.050 |     -6.44
     5%/ 120m      19.39     6.07    13.31    3.192 |     9.35     3.84     5.51    2.436 |     -7.80
     5%/ 240m      30.50    11.24    19.26    2.713 |    18.95     8.81    10.15    2.152 |     -9.11

### MAX_CASCADE_PRESSURE

    W1 episodes 33 / baseline 2898      W2 episodes 31 / baseline 2898

    cell        W1 warn% W1 norm%  W1 lift   W1 rel | W2 warn% W2 norm%  W2 lift   W2 rel | d lift pp
     1%/  30m      87.88    27.43    60.45    3.203 |    67.74    30.48    37.26    2.223 |    -23.19
     1%/  60m      90.91    44.38    46.53    2.049 |    74.19    46.61    27.58    1.592 |    -18.95
     1%/ 120m      93.94    66.11    27.82    1.421 |    87.10    66.58    20.51    1.308 |     -7.31
     1%/ 240m      96.97    82.93    14.04    1.169 |    90.00    81.61     8.39    1.103 |     -5.65
     2%/  30m      51.52     6.94    44.58    7.427 |    35.48     6.80    28.68    5.218 |    -15.90
     2%/  60m      57.58    15.29    42.29    3.766 |    45.16    15.44    29.72    2.924 |    -12.57
     2%/ 120m      66.67    29.57    37.09    2.254 |    58.06    28.69    29.38    2.024 |     -7.71
     2%/ 240m      72.73    48.53    24.19    1.499 |    70.00    48.46    21.54    1.445 |     -2.65
     3%/  30m      45.45     3.11    42.35   14.636 |    22.58     2.38    20.20    9.481 |    -22.15
     3%/  60m      51.52     8.14    43.37    6.326 |    25.81     5.63    20.17    4.580 |    -23.20
     3%/ 120m      57.58    15.94    41.63    3.612 |    29.03    12.16    16.87    2.388 |    -24.76
     3%/ 240m      66.67    28.28    38.39    2.358 |    56.67    24.67    31.99    2.297 |     -6.40
     5%/  30m      27.27     1.00    26.27   27.254 |     9.68     0.59     9.09   16.491 |    -17.18
     5%/  60m      27.27     2.93    24.34    9.298 |     9.68     1.08     8.60    8.975 |    -15.74
     5%/ 120m      39.39     6.07    33.32    6.487 |    16.13     3.84    12.29    4.201 |    -21.03
     5%/ 240m      51.52    11.24    40.27    4.583 |    20.00     8.81    11.19    2.271 |    -29.08

## 7. What the two windows demonstrate, and what they do not

They demonstrate that across two non-adjacent prospective seven-day windows,
evaluated under an identical frozen protocol with an identical pipeline (same
code digest, same thresholds digest, same 69-symbol universe), structural-state
warnings preceded larger absolute price displacement than fixed-stride NORMAL
anchors in all 16 predeclared cells of the overall grid, in both windows.
Relative incidence exceeded 1.0 in every overall cell of both windows. The sign
of the effect replicated without exception.

They do not demonstrate a stable magnitude. The measured lift fell in 15 of 16
overall cells in Window 2, in several cells by more than half: 2%/60m from
+32.49pp to +16.93pp, 3%/60m from +19.36pp to +8.03pp. Because NORMAL-anchor
incidence was nearly unchanged between windows (2%/60m 15.29 -> 15.44; 1%/60m
44.38 -> 46.61), the attenuation comes from the warning arm, not from a shifted
baseline. Window 2 was a materially quieter regime: QUIET 50.298% -> 59.335%,
STRESSED 6.399% -> 5.909%, CASCADE_PRESSURE slots 86 -> 74. Two windows cannot
distinguish between a genuinely smaller effect, sensitivity to market regime,
and ordinary sampling variation. Nothing here establishes which.

They do not demonstrate anything about majors, where the two windows disagree in
direction across 6 of 16 cells on 88-94 episodes. They do not demonstrate
anything about the CASCADE_PRESSURE split, which rests on 31-33 episodes. They
do not establish any predictive accuracy figure: Layer 1 and Layer 2 are
reported separately and are not combined, no cell was selected as preferred, no
statistical test beyond the four predeclared descriptive figures was applied,
and no parameter was examined against outcome data.

Two windows are two observations. The direction replicated; the magnitude did
not.
