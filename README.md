
# 初期設定

前提条件
- ローカル環境にDockerが入っていること
- VSCodeで開くこと
- Remote ContainersをVSCodeにインストールすること
- Remote Containersで環境を開くこと

```sh
# AtCoderへのログイン
acc login

# online-judge-toolsでもログインする
oj login https://atcoder.jp/
```

# コンテストディレクトリの作成

```sh
acc new <contest id>
# ex: acc new abc101
```

# テストの方法
```sh
# 問題のディレクトリ内で
# ex: cd abc101/a
oj t -c 'pypy3 main.py'
```

# 提出方法
```sh
acc s main.py -- --guess-python-interpreter pypy
```


# 参考

- [Tatamo/atcoder-cli](https://github.com/Tatamo/atcoder-cli)
- [atcoder-cli チュートリアル](http://tatamo.81.la/blog/2018/12/07/atcoder-cli-tutorial/)
