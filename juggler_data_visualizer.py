import os
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import requests
from io import BytesIO

# GitHubからExcelファイルを取得する関数
def download_excel_from_github(repo_url, file_path):
    download_url = f"https://raw.githubusercontent.com/{repo_url}/main/{file_path}"
    response = requests.get(download_url)
    
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        st.error(f"ファイルのダウンロードに失敗しました: {response.status_code}")
        return None

# Excelファイルを読み込む関数
def load_excel_data(excel_io):
    df = pd.read_excel(excel_io, sheet_name="合成確率", engine="openpyxl", index_col=0)
    return df

# グラフのプロット
def plot_synthetic_probabilities(df, selected_machine_number):
    machine_data = df.loc[selected_machine_number].dropna()
    dates = machine_data.index
    probabilities = machine_data.values

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=probabilities, mode='lines+markers', name=f'合成確率: {selected_machine_number}'))
    fig.update_layout(
        title=f"台番号 {selected_machine_number} の合成確率の推移",
        xaxis_title="日付",
        yaxis_title="合成確率",
        xaxis=dict(tickformat="%Y-%m-%d"),
        hovermode="x"
    )
    st.plotly_chart(fig)

# Streamlitアプリケーションのインターフェース
st.title("🎰 Juggler Data Visualizer")
st.write("台番号ごとの合成確率を可視化します。")

# GitHubリポジトリ情報
github_repo = "yudai4452/juggler-data-apps"  # 自分のGitHubリポジトリに置き換える
file_path_in_repo = "マイジャグラーV_塗りつぶし済み.xlsx"  # リポジトリ内のファイルパス

# GitHubからExcelファイルをダウンロード
excel_file_io = download_excel_from_github(github_repo, file_path_in_repo)

# Excelファイルの読み込み
if excel_file_io:
    df_synthetic = load_excel_data(excel_file_io)
    machine_numbers = df_synthetic.index.tolist()
    selected_machine_number = st.selectbox("台番号を選択", machine_numbers)
    
    if selected_machine_number:
        plot_synthetic_probabilities(df_synthetic, selected_machine_number)
else:
    st.error(f"Excelファイルのダウンロードが失敗しました。Juggler Data Managerで生成してください。")

# データ処理アプリへのリンク
st.markdown("[こちらをクリックしてJuggler Data Managerへ移動](https://juggler-data-apps-gepdgbj565ctumtcunzyzh.streamlit.app/)")
