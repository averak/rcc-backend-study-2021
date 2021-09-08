# RCC バックエンド勉強会

![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)
![MIT License](http://img.shields.io/badge/license-MIT-green.svg?style=flat)

## 開発環境

- Python 3.9
- Pipenv

## 使い方

### 1. インストール

```sh
pipenv install
```

### 2. アプリケーションを起動

```sh
pipenv run start
```

本コマンドを実行すると[localhost:8000](http://localhost:8000/)へアクセスできるようになります。

### 3. テストを実行

```sh
pipenv run test
```

## API docs

このプロジェクトは Swagger をサポートしています。

1. アプリケーションを起動
2. [Swagger UI](http://localhost:8000/docs)にアクセス
