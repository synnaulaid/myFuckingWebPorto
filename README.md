# myFuckingWebPorto
myFuckingWebPorto 

Initial Project Web Portofolio
## Upadte
> Design Minimalis 

> Integrated Github API

## Structure
```
my Fucking  portofolio web
├── app.py
├── README.md
├── req.txt
├── services
│   ├── github_api.py
│   ├── github.py
│   ├── __init__.py
│   └── __pycache__
│       ├── github_api.cpython-310.pyc
│       ├── github.cpython-310.pyc
│       └── __init__.cpython-310.pyc
├── static
│   ├── css
│   │   └── style.css
│   ├── font
│   │   ├── eng-old
│   │   │   └── BeckettRegular-8zj0.ttf
│   │   └── textura-font
│   │       ├── info.txt
│   │       ├── misc
│   │       │   └── License.txt
│   │       └── TexturaModern-5XxV.ttf
│   ├── images
│   │   ├── hm.jpg
│   │   └── pp.png
│   └── js
│       └── scripts.js
├── templates
│   ├── base.html
│   ├── index.html
│   └── repo.html
└── test
    ├── tes.html
    └── tes.sh

13 directories, 22 files
```

## Installation
```
git clone https://github.com/synnaulaid/myFuckingWebPorto.git
cd myFuckingWebPorto 
pip install -r req.txt
python3 app.py
```

### configuration
edit file .env.example or copy
``` cp .env.example .env ```

<b>.env files</b>
```
GITHUB_USERNAME=your_username
GITHUB_TOKEN=ghp_xxx  # Your Fucking Token (Rekomendasi: pake token github klasik jangan pake yang fine-grained. tapi terserah sih :v belum coba pake itu soal nya.)
CACHE_TIMEOUT=600     # detik
```


