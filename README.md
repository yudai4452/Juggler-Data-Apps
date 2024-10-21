# Juggler Data Apps 

Juggler Data Apps は、ジャグラーのスロット台に関連するデータを管理し、可視化するための2つのアプリケーションを提供します。

- **Juggler Data Manager**: HTMLファイルから台ごとのデータを抽出し、Excelファイルに保存し、GitHubへアップロードする機能を提供します。
- **Juggler Data Visualizer**: Juggler Data Managerで生成されたデータを読み込み、合成確率の推移を可視化する機能を提供します。

## アプリケーションの概要

### 1. Juggler Data Manager
HTMLファイルをアップロードして、台ごとのスロットデータを抽出し、整形されたExcelファイルに保存します。また、保存されたファイルをGitHubに自動アップロードします。

#### 使用方法
1. Streamlit Community Cloudで公開されたアプリにアクセスします。
2. HTMLファイルをアップロードし、処理を開始します。
3. データがExcelファイルに保存され、GitHubにアップロードされます。


### 2. Juggler Data Visualizer
Excelファイルから台ごとの合成確率のデータを読み込み、選択した台番号の合成確率の推移をグラフで表示します。

#### 使用方法
1. Streamlit Community Cloudで公開されたアプリにアクセスします。
2. 表示したい台番号を選択します。
3. 選択した台番号の合成確率の推移がグラフで表示されます。
