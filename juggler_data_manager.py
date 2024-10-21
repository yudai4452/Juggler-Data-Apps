import os
import pandas as pd
import openpyxl
from openpyxl.styles import PatternFill, Font
import pytz
from datetime import datetime
import streamlit as st
from github import Github

# GitHubへのファイルアップロード関数
def upload_file_to_github(file_path, repo_name, file_name_in_repo, commit_message, GITHUB_TOKEN):
    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo(repo_name)
        
        with open(file_path, 'rb') as file:
            content = file.read()

        path = file_name_in_repo

        try:
            contents = repo.get_contents(path)
            repo.update_file(path, commit_message, content, contents.sha)
            st.info(f"{file_name_in_repo} を更新しました。")
        except Exception as e_inner:
            repo.create_file(path, commit_message, content)
            st.info(f"{file_name_in_repo} を作成しました。")
    except Exception as e_outer:
        st.error(f"GitHubへのファイルアップロード中にエラーが発生しました: {e_outer}")

# データ抽出と保存
def extract_data_and_save_to_csv(html_path, output_csv_path, date):
    # ... (BeautifulSoupを使用したデータ抽出ロジック)
    df = pd.DataFrame(data)  # データの例
    df.to_csv(output_csv_path, index=False, encoding="shift-jis")
    return df

# Excelファイルに色付け
def apply_color_fill_to_excel(excel_path):
    wb = openpyxl.load_workbook(excel_path)
    ws = wb.active
    yellow_fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")
    light_blue_fill = PatternFill(start_color="ADD8E6", end_color="ADD8E6", fill_type="solid")

    for row in ws.iter_rows(min_row=2, min_col=2, max_row=ws.max_row, max_col=ws.max_column):
        for cell in row:
            try:
                cell_value = float(cell.value)
                if cell_value < 125:
                    cell.fill = yellow_fill
                elif 125 <= cell_value < 140:
                    cell.fill = light_blue_fill
            except (TypeError, ValueError):
                pass

    wb.save(excel_path)

# Streamlitアプリケーションのインターフェース
st.title("🎰 Juggler Data Manager 🎰")
st.write("このアプリでは、HTMLからデータを抽出し、Excelファイルに保存し、色付けします。")

# GitHubトークンの取得
GITHUB_TOKEN = st.secrets["github"]["token"]

# 日本時間の今日の日付を取得
japan_time_zone = pytz.timezone('Asia/Tokyo')
current_date_japan = datetime.now(japan_time_zone)

# HTMLファイルの入力
uploaded_html = st.file_uploader("HTMLファイルをアップロード", type=["html", "htm", "txt"])
date_input = st.date_input("日付を選択", current_date_japan)

# ファイルの処理開始ボタン
if st.button("処理開始"):
    if uploaded_html:
        html_path = os.path.join(".", uploaded_html.name)
        with open(html_path, "wb") as f:
            f.write(uploaded_html.getbuffer())
        
        output_csv_path = os.path.join(".", f"slot_machine_data_{date_input}.csv")
        excel_path = "マイジャグラーV_塗りつぶし済み.xlsx"
        
        # データ処理とExcelファイル作成
        df_new = extract_data_and_save_to_csv(html_path, output_csv_path, date_input)
        apply_color_fill_to_excel(excel_path)

        st.success(f"データ処理が完了し、{excel_path} に保存されました。")

        # GitHubアップロード
        repo_name = "yudai4452/juggler-data-apps"
        commit_message = f"Add data for {date_input}"
        upload_file_to_github(excel_path, repo_name, f"{excel_path}", commit_message, GITHUB_TOKEN)

        # 可視化アプリへのリンク
        st.markdown("[こちらをクリックしてJuggler Data Visualizerへ移動](https://juggler-data-apps-6qz2wrn69bezyvzykh5bdb.streamlit.app/)")


# 可視化アプリへのリンク
st.markdown("[こちらをクリックしてJuggler Data Visualizerへ移動](https://juggler-data-apps-6qz2wrn69bezyvzykh5bdb.streamlit.app/)")

