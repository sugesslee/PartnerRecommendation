## 数据库配置
在conf下新建db_config.json文件并复制下面内容  
```
{
  "host": "",
  "user": "",
  "password": "",
  "db": "",
  "charset": "utf8mb4",
  "port": 3306,
  "use_unicode": true
}
```
# AMiner 数据集
[AMiner 数据集网址](https://www.aminer.cn/data_cn  "Markdown")


```
## AMiner-Author2Paper 
The relaionship between author id and paper id AMiner-Author2Paper.zip. The 1st column is index, the 2nd colum is 
auhor id, the 3rd column is paper id, the 4th column is author's position.  
 Data Description
This dataset consists of three files:
 
1) AMiner-Paper.rar [download from mirror site]
 
This file saves the paper information and the citation network. The format is as follows:
 
#index ---- index id of this paper
#* ---- paper title
#@ ---- authors (separated by semicolons)
#o ---- affiliations (separated by semicolons, and each affiliaiton corresponds to an author in order)
#t ---- year
#c ---- publication venue
#% ---- the id of references of this paper (there are multiple lines, with each indicating a reference)
#! ---- abstract
 
The following is an example:
 
#index 1083734
#* ArnetMiner: extraction and mining of academic social networks
#@ Jie Tang;Jing Zhang;Limin Yao;Juanzi Li;Li Zhang;Zhong Su
#o Tsinghua University, Beijing, China;Tsinghua University, Beijing, China;Tsinghua University, Beijing, China;Tsinghua University, Beijing, China;IBM, Beijing, China;IBM, Beijing, China
#t 2008
#c Proceedings of the 14th ACM SIGKDD international conference on Knowledge discovery and data mining
#% 197394
#% 220708
#% 280819
#% 387427
#% 464434
#% 643007
#% 722904
#% 760866
#% 766409
#% 769881
#% 769906
#% 788094
#% 805885
#% 809459
#% 817555
#% 874510
#% 879570
#% 879587
#% 939393
#% 956501
#% 989621
#% 1117023
#% 1250184
#! This paper addresses several key issues in the ArnetMiner system, which aims at extracting and mining academic social networks. Specifically, the system focuses on: 1) Extracting researcher profiles automatically from the Web; 2) Integrating the publication data into the network from existing digital libraries; 3) Modeling the entire academic network; and 4) Providing search services for the academic network. So far, 448,470 researcher profiles have been extracted using a unified tagging approach. We integrate publications from online Web databases and propose a probabilistic framework to deal with the name ambiguity problem. Furthermore, we propose a unified modeling approach to simultaneously model topical aspects of papers, authors, and publication venues. Search services such as expertise search and people association search have been provided based on the modeling results. In this paper, we describe the architecture and main features of the system. We also present the empirical evaluation of the proposed methods.
 
2) AMiner-Author.zip [download from mirror site]
 
This file saves the author information. The format is as follows:
 
#index ---- index id of this author
#n ---- name  (separated by semicolons)
#a ---- affiliations  (separated by semicolons)
#pc ---- the count of published papers of this author
#cn ---- the total number of citations of this author
#hi ---- the H-index of this author
#pi ---- the P-index with equal A-index of this author
#upi ---- the P-index with unequal A-index of this author
#t ---- research interests of this author  (separated by semicolons)
 
Note: Please refer to [J. Stallings et al, Determining scientific impact using a collaboration index] for the concepts of P-index and A-index.
 
The following is an example:
 
#index 1488277
#n Juanzi Li
#a Tsinghua University;Department of Computer Science & Technology, Tsinghua, University, Beijing, China 100084
#pc 70
#cn 370
#hi 9
#pi 76.3254
#upi 73.7573
#t semantic web;social network;Semantic Annotation;ontology caching;semantic information;knowledge base
 
3) AMiner-Coauthor.zip [download from mirror site]
 
This file saves the collaboration network among the authors in the second file. The format is as follows:
 
#00 11 22 ---- 00 means the index id of one author, 11 means the index id of another author, 22 means the number of collaborations btween them
 
The following is an example:
 
#693708 1658058 2
 
 

References
If you use this dataset for research, please must cite the following paper:
Jie Tang, Jing Zhang, Limin Yao, Juanzi Li, Li Zhang, and Zhong Su. ArnetMiner: Extraction and Mining of Academic Social Networks. In Proceedings of the Fourteenth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (SIGKDD'2008). pp.990-998. [PDF] [Slides] [System] [API]
You please also consider referring to the following papers:

Jie Tang, Limin Yao, Duo Zhang, and Jing Zhang. A Combination Approach to Web User Profiling. ACM Transactions on Knowledge Discovery from Data (TKDD), (vol. 5 no. 1), Article 2 (December 2010), 44 pages.  [PDF]
Jie Tang, A.C.M. Fong, Bo Wang, and Jing Zhang. A Unified Probabilistic Framework for Name Disambiguation in Digital Library. IEEE Transaction on Knowledge and Data Engineering (TKDE) , Volume 24, Issue 6, 2012, Pages 975-987. [PDF][Code&Data&System]
Jie Tang, Jing Zhang, Ruoming Jin, Zi Yang, Keke Cai, Li Zhang, and Zhong Su. Topic Level Expertise Search over Heterogeneous Networks. Machine Learning Journal, Volume 82, Issue 2 (2011), Pages 211-237. [PDF] [URL]
Jie Tang, Duo Zhang, and Limin Yao. Social Network Extraction of Academic Researchers. In Proceedings of 2007 IEEE International Conference on Data Mining(ICDM'2007). pp. 292-301. [PDF] [Slides] [Data]
@INPROCEEDINGS{Tang:08KDD,
    AUTHOR = "Jie Tang and Jing Zhang and Limin Yao and Juanzi Li and Li Zhang and Zhong Su",
    TITLE = "ArnetMiner: Extraction and Mining of Academic Social Networks",
    pages = "990-998",
    YEAR = {2008},
    BOOKTITLE = "KDD'08",
}
 
@article{Tang:10TKDD,
     author = {Jie Tang and Limin Yao and Duo Zhang and Jing Zhang},
     title = {A Combination Approach to Web User Profiling},
     journal = {ACM TKDD},
     year = {2010},
     volume = {5},
     number = {1},
    pages = {1--44},
 }
 
@article{Tang:11ML,
     author = {Jie Tang and Jing Zhang and Ruoming Jin and Zi Yang and Keke Cai and Li Zhang and Zhong Su},
     title = {Topic Level Expertise Search over Heterogeneous Networks},
     year = {2011},
     volume = {82},
     number = {2},
     pages = {211--237},
     journal = {Machine Learning Journal},
}
 
@article{Tang:12TKDE,
    author = {Jie Tang and Alvis C.M. Fong and Bo Wang and Jing Zhang},
    title = {A Unified Probabilistic Framework for Name Disambiguation in Digital Library},
    journal ={IEEE Transactions on Knowledge and Data Engineering},
    volume = {24},
    number = {6},
    year = {2012},
    pages = {975-987},
}
@INPROCEEDINGS{Tang:07ICDM,

    AUTHOR = "Jie Tang and Duo Zhang and Limin Yao",
    TITLE = "Social Network Extraction of Academic Researchers",
    PAGES = "292-301",
    YEAR = {2007},
    BOOKTITLE = "ICDM'07",
}
```

#K-Means聚类算法以及扩展算法K-Modes、K-Prototype
