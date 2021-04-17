This folder contains the data splits from v2 of Social Bias Frames / Social Bias Inference Corpus.
Simply read in the file using pandas:
```python
trndf = pd.read_csv("SBIC.v2.trn.csv")
```

Each line in the file contains the following fields (in order):
- _whoTarget_: group vs. individual target - 1_针对族群 vs 0_针对个人
Y_intentYN_: was the intent behind the statement to offend - 冒犯性陳述的傾向（0-1）
Y _sexYN_: is the post a sexual or lewd reference - 是否為色情/猥褻內容
X _sexReason_: free text explanations of what is sexual - 文本：對sexual的解釋
Y _offensiveYN_: could the post be offensive to anyone - 是否有可能冒犯到別人（0，0.5，1）
- _annotatorGender_: gender of the MTurk worker - 注釋者的性別
- _annotatorMinority_: whether the MTurk worker identifies as a minority - 注釋者是否認知為一個少數族群
X _sexPhrase_: part of the post that references something sexual - 推文中的有關sexual的內容
- _speakerMinorityYN_: whether the speaker was part of the same minority group that's being targeted - 發布者是否在針對同一個少數族群
- _WorkerId_: hashed version of the MTurk workerId - X
- _HITId_: id that uniquely identifies each post - X
- _annotatorPolitics_: political leaning of the MTurk worker - 注釋者的政治傾向（自由、保守、偏自由、偏保守、其他）
- _annotatorRace_: race of the MTurk worker - 注釋者的種族
- _annotatorAge_: age of the MTurk worker - 注釋者的年齡
X _post_: post that was annotated - 完整推文
Y _targetMinority_: demographic group targeted - 針對的人群
- _targetCategory_: high-level category of the demographic group(s) targeted - #對[23]的概括性分類#
X _targetStereotype_: implied statement - 陳述內容（可以理解為發布的內容的意思）
- _dataSource_: source of the post (`t/...`: means Twitter, `r/...`: means a subreddit) - X

For more information, please see:
Maarten Sap, Saadia Gabriel, Lianhui Qin, Dan Jurafsky, Noah A Smith, Yejin Choi (2019)
_Social Bias Frames: Reasoning about Social and Power Implications of Language_