import os
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Excelファイルを読み込み
def load_excel_data(excel_path):
    df = pd.read_excel(excel_path, sheet_name="合成確率", engine="openpyxl", index_col=0)
    return df

# 分数表示のための関数
def format_as_fraction(value):
    return f"1/{int(value)}" if value != 0 else "N/A"

# 設定表をもとにしたY軸の目盛設定
SETTINGS_PROBABILITIES = {
    "1": 163.8,
    "2": 159.1,
    "3": 148.6,
    "4": 135.4,
    "5": 126.8,
    "6": 114.6
}

# グラフのプロット
def plot_synthetic_probabilities(df, selected_machine_number):
    machine_data = df.loc[selected_machine_number].dropna()
    dates = machine_data.index
    probabilities = machine_data.values
    
    # 1/合成確率を計算
    inverse_probabilities = 1 / probabilities

    # 軸ラベルを分数形式に変換
    fraction_labels = [format_as_fraction(p) for p in probabilities]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=inverse_probabilities, mode='lines+markers', name=f'1/合成確率: {selected_machine_number}'))
    
    # 設定表をもとにY軸の目盛を設定
    tickvals = [1/p for p in SETTINGS_PROBABILITIES.values()]
    ticktext = [f"1/{int(p)}" for p in SETTINGS_PROBABILITIES.values()]

    fig.update_layout(
        title=f"台番号 {selected_machine_number} の1/合成確率の推移",
        xaxis_title="日付",
        yaxis_title="1/合成確率",
        xaxis=dict(tickformat="%Y-%m-%d"),
        yaxis=dict(tickvals=tickvals, ticktext=ticktext),  # Y軸目盛設定
        hovermode="x"
    )
    
    st.plotly_chart(fig)

# Streamlitアプリケーションのインターフェース
st.title("🎰 Juggler Data Visualizer 🎰")
st.write("台番号ごとの「1/合成確率」を可視化します。")

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
st.markdown("[こちらをクリックしてJuggler Data Managerへ移動](https://juggler-data-apps-gepdgbj565ctumtcunzyzh.streamlit.app/)")
