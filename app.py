import streamlit as st
import time
from datetime import datetime
import json

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Sales Cockpit - Benitech",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS CUSTOMIZADO (Visual HUD & Títulos Destacados) ---
st.markdown("""
    <style>
    /* Estilo Geral dos Expanders */
    .stExpander {
        border: none !important;
        margin-bottom: 1rem;
    }
    
    /* Destacar os Títulos das Etapas (Cabeçalho do Expander) */
    div[data-testid="stExpander"] details summary p {
        font-size: 1.3rem !important;
        font-weight: 800 !important;
        color: #ffffff !important;
        text-transform: uppercase;
    }
    
    /* Fundo do cabeçalho do Expander para dar contraste */
    div[data-testid="stExpander"] details summary {
        background-color: #2E2E2E !important; /* Cinza escuro/destaque */
        border: 1px solid #555;
        border-radius: 8px;
        padding: 15px !important;
    }
    
    /* Hover no cabeçalho */
    div[data-testid="stExpander"] details summary:hover {
        background-color: #444 !important;
        border-color: #FFC107 !important; /* Borda amarela ao passar o mouse */
    }

    /* Utilitários */
    .highlight-roi {
        background-color: #d4edda;
        color: #155724;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    div[data-testid="stMetricValue"] {font-size: 3rem;}
    </style>
""", unsafe_allow_html=True)

# --- GERENCIAMENTO DE ESTADO ---
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

# --- SIDEBAR (HUD DE CONTROLE) ---
with st.sidebar:
    st.title("🩺 Cockpit")
    st.markdown("---")
    
    # Timer Global
    if st.session_state.start_time is None:
        if st.button("▶️ INICIAR CALL", type="primary", use_container_width=True):
            st.session_state.start_time = time.time()
            st.rerun()
    else:
        elapsed = int((time.time() - st.session_state.start_time) / 60)
        timer_color = "normal"
        if elapsed > 20: timer_color = "off"
        elif elapsed > 15: timer_color = "inverse"
        
        st.metric(label="Tempo Decorrido", value=f"{elapsed} min", delta="Meta: 50m", delta_color=timer_color)
        
        if st.button("⏹️ Encerrar Timer", use_container_width=True):
            st.session_state.start_time = None
            st.rerun()
        
        st.divider()

    # Mindset SND
    with st.expander("🚨 MINDSET SND (SOS)", expanded=True):
        st.markdown("""
        **S**e Valorizar  
        **N**ão Fazer Questão  
        **D**ominar a Situação
        
        *Cliente enrolando?* 👉 "Parece que não é seu momento."
        *Cliente dominando?* 👉 Interrompa com uma pergunta.
        """)

    # Dados Básicos
    st.markdown("### 👤 Lead Info")
    lead_name = st.text_input("Nome do Lead", placeholder="Ex: João da Silva")
    lead_niche = st.text_input("Nicho/Cargo", placeholder="Ex: Dono de Clínica")

# --- ÁREA PRINCIPAL ---

st.title("Mapa de Voo Cirúrgico ✈️")
st.markdown("---")

# Passo 1
with st.expander("1️⃣ APRESENTAÇÃO (AUTORIDADE) | 5 min", expanded=True):
    c1, c2, c3 = st.columns([1, 1, 2])
    with c1:
        st.checkbox("Dei a 'Carteirada'?", help="Apresentou-se como Diretor/Fundador?")
        st.checkbox("Atenção Total?", help="Ele parou de mexer no celular?")
    with c2:
        perfil = st.radio("Perfil Identificado", ["Visual 👁️", "Auditivo 👂", "Cinestésico 🤝"], horizontal=True)
    with c3:
        st.text_area("Notas Iniciais / Vibe", height=70, key="step1_notes")

# Passo 2
with st.expander("2️⃣ CONEXÃO (A CIRURGIA) | 15-20 min", expanded=True):
    st.info("💡 **Lembrete:** Corte histórias longas. Ache a dor raiz. Use o silêncio.")
    
    c1, c2 = st.columns([1, 2])
    with c1:
        st.checkbox("Fiz a Solução Incompleta?", help="Disse 'Acho que consigo te ajudar'?")
        st.checkbox("Cortei o cliente?", help="Interrompeu divagações?")
    with c2:
        dor_alma = st.text_area("🩸 A DOR DA ALMA (Obrigatório)", 
                     placeholder="Não anote o sintoma. Anote a causa. Ex: Sente-se menos homem por não prover...", 
                     height=100, key="step2_pain")
        ganchos = st.text_area("🪝 Ganchos para Fechamento", 
                    placeholder="O que ele disse que vou usar contra ele no final?", 
                    height=70, key="step2_hooks")

# Passo 3
with st.expander("3️⃣ D.I. - O PACTO (DECISÃO IMEDIATA)", expanded=True):
    st.markdown("#### 🗣️ *Script: 'No final, SIM ou NÃO. Sem vou pensar. Posso contar com sua objetividade?'*")
    c1, c2 = st.columns(2)
    with c1:
        di_check = st.checkbox("✅ Cliente concordou com o combinado?")
    with c2:
        autonomia = st.toggle("Decide Sozinho?", value=True)
        if not autonomia:
            st.error("⛔ PARE! Se ele não decide, remarque com o sócio/esposa.")

# Passo 4 - ATUALIZADO COM OS PILARES
with st.expander("4️⃣ O SHOW (GERAR DESEJO) | O PROGRAMA", expanded=False):
    # Destaque do ROI e Formato
    st.markdown('<div class="highlight-roi">💎 FOCO TOTAL NO ROI (Return on Investment)</div>', unsafe_allow_html=True)
    
    col_main, col_entrega = st.columns([1, 1])
    
    with col_main:
        st.markdown("### 🏛️ Os 4 Pilares Base")
        st.checkbox("1. Posicionamento")
        st.checkbox("2. Modelo de Negócio")
        st.checkbox("3. Canais de Venda (Tráfego/Ativa)")
        st.checkbox("4. Liderança (Coordenação de Time)")
    
    with col_entrega:
        st.markdown("### 🚀 Formato da Entrega")
        st.info("Começa **INDIVIDUAL** (Mapeamento História) ➡️ depois **GRUPO**")
        st.caption("🔓 **Anderson:** É Acessível (tira dúvidas), mas não disponível.")

    st.markdown("---")
    st.markdown("### 🏆 Diferenciais Premium (High Ticket)")
    
    c_mls, c_livro = st.columns(2)
    with c_mls:
        st.markdown("**5. MLS (Mentoria League Society)**")
        st.checkbox("Falei do Título Ouro?")
        st.checkbox("Encontros Presenciais")
        st.caption("💰 *Pode revender o título por 50% após 1 ano.*")
        
    with c_livro:
        st.markdown("**6. Livro (Buzz Editora)**")
        st.checkbox("Ghostwriter Incluso")
        st.checkbox("Distribuição Nacional")
        st.caption("✍️ *Coordenação e roteiro do Anderson.*")

    st.markdown("---")
    # Termômetro
    c_temp, c_obs = st.columns([1, 2])
    with c_temp:
        st.metric("Temperatura", "🔥 Quente" if st.checkbox("Verbalizou 'EU PRECISO'?") else "❄️ Frio")
    with c_obs:
        st.text_input("Qual pilar brilhou mais o olho dele?", placeholder="Ex: O Livro, a revenda do título...")

# Passo 5
with st.expander("5️⃣ FECHAMENTO (A HORA DA VERDADE) 💰", expanded=True):
    st.warning("🧠 **MINDSET SND:** Se ele hesitar, ameace retirar a vaga.")
    
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        st.markdown("**Checklist**")
        st.checkbox("Ancoragem Feita")
        st.checkbox("Preço Revelado")
    with c2:
        st.markdown("**Valores**")
        valor_fechado = st.number_input("Valor (R$)", step=1000, value=0)
        condicao = st.selectbox("Condição", ["À Vista", "Parcelado", "Entrada + Parc."])
    with c3:
        st.markdown("**Ação Final**")
        st.caption("Se limite baixo, peça R$ 500 agora.")
        comprovante = st.checkbox("🧾 COMPROVANTE NA TELA", key="comprovante")
        
    if comprovante:
        st.success("🎉 VENDA TRAVADA! PARABÉNS!")

# Passo 6 & 7
with st.expander("6️⃣ ONBOARDING & 7️⃣ INDICAÇÃO", expanded=False):
    c1, c2 = st.columns(2)
    with c1:
        st.date_input("Data do Onboarding (Amanhã)", datetime.now())
    with c2:
        st.checkbox("Indicação pedida na hora?")
        referidos = st.text_area("Lista de Referidos", placeholder="Nome - Telefone", height=100)

# --- RODAPÉ / SALVAR ---
st.markdown("---")
c1, c2 = st.columns([3, 1])

with c2:
    if st.button("💾 SALVAR LEAD & LOG", type="primary", use_container_width=True):
        # Estrutura do JSON
        dados_finais = {
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "lead": lead_name,
            "nicho": lead_niche,
            "duracao_min": elapsed if st.session_state.start_time else 0,
            "dor_alma": dor_alma,
            "valor_fechado": valor_fechado,
            "status": "Venda" if comprovante else "Lost/Follow-up",
            "ganchos": ganchos,
            "referidos": referidos
        }
        
        # Exibe o JSON (No futuro, substitua por request.post para seu n8n/webhook)
        st.json(dados_finais)
        st.success("Dados prontos para envio ao CRM!")
        st.toast("Lead Salvo com Sucesso!", icon="🚀")
