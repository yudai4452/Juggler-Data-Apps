import os
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Excelファイルを読み込み
def load_excel_data(excel_path):
    df = pd.read_excel(excel_path, sheet_name="合成確率", engine="openpyxl", index_col=0)
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

# Excelファイルの読み込み
excel_file_name = "マイジャグラーV_塗りつぶし済み.xlsx"
if os.path.exists(excel_file_name):
    df_synthetic = load_excel_data(excel_file_name)
    machine_numbers = df_synthetic.index.tolist()
    selected_machine_number = st.selectbox("台番号を選択", machine_numbers)
    
    if selected_machine_number:
        plot_synthetic_probabilities(df_synthetic, selected_machine_number)
else:
    st.error(f"Excelファイル {excel_file_name} が存在しません。Juggler Data Managerで生成してください。")

# データ処理アプリへのリンク
st.markdown("[こちらをクリックしてJuggler Data Managerへ移動](https://share.streamlit.io/your-username/juggler-data-manager)")
import os
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Excelファイルを読み込み
def load_excel_data(excel_path):
    df = pd.read_excel(excel_path, sheet_name="合成確率", engine="openpyxl", index_col=0)
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
st.title("🎰 Juggler Data Visualizer 🎰")
st.write("台番号ごとの合成確率を可視化します。")

# Excelファイルの読み込み
excel_file_name = "マイジャグラーV_塗りつぶし済み.xlsx"
if os.path.exists(excel_file_name):
    df_synthetic = load_excel_data(excel_file_name)
    machine_numbers = df_synthetic.index.tolist()
    selected_machine_number = st.selectbox("台番号を選択", machine_numbers)
    
    if selected_machine_number:
        plot_synthetic_probabilities(df_synthetic, selected_machine_number)
else:
    st.error(f"Excelファイル {excel_file_name} が存在しません。Juggler Data Managerで生成してください。")

# データ処理アプリへのリンク
st.markdown("[こちらをクリックしてJuggler Data Managerへ移動](https://share.streamlit.io/yudai4452/juggler-data-manager)")
