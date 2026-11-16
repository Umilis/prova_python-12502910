import streamlit as st
import pandas as pd

st.title("LeitoOcupação")

st.set_page_config(page_title="LeitoOcupacao", layout="wide")

st.sidebar.header("Controles")
opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Gráficos"])

df = p.read_csv("esus-vepi.LeitoOcupacao_2020.csv", sep=";")
df["mes"] = ["dataNotificacao"]. astype(str). str[5:7]

df_filtrado = df[
    (df["NOMEUP"].isin(["Minas Gerais"]))
].copy()

if opcao == "Tabela":
    st.header("Tabela de ocupação (Série Histórica)")
    st.dataframe(df_tabela, use_container_width=True, hide_index=True)

elif opcao == "Gráficos":
    st.header("Gráficos de ocupação — Minas Gerais")

df_tabela = df_filtrado[["NOMEUP", "mes", "ocupação"]]

st.subheader("2. Gráfico de Linha — Minas Gerais")
    df_minas_gerais = df_tabela[df_tabela["NOMEUP"] == "Minas Gerais"]

    fig_minas_gerais = px.line(
        df_minas_gerais,
        x="mes",
        y="ocupação",
        markers=True,
        title="ocupação",
        template="plotly_dark"
    )
    fig_minas_gerais.update_traces(line_color="#00F5D4", line_width=3, marker_size=8)
    fig_minas_gerais.update_xaxes(type="category")
    fig_minas_gerais.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig_minas_gerais, use_container_width=True)

caminho_arquivo = r"H:\prova_python(49)\esus-vepi.LeitoOcupacao_2020.csv"

try:
    df = carregar_dados(caminho_arquivo)

    st.markdown("---")
st.caption("Fonte dos dados: dados abertos da Prefeitura de Belo Horizonte — https://opendatasus.saude.gov.br/")