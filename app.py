import streamlit as st
import pandas as pd

# Cấu hình trang
st.set_page_config(page_title="Thẩm định vay", page_icon="🏦", layout="wide")

# Tiêu đề với CSS
st.markdown("<h1 style='text-align: center; color: #1f77b4;'>🏦 HỆ THỐNG THẨM ĐỊNH TÍN DỤNG</h1>", unsafe_allow_html=True)

# Khối nhập liệu
col1, col2 = st.columns(2)
with col1:
    st.subheader("Thông tin Khách hàng")
    thu_nhap = st.number_input("Thu nhập hàng tháng (VNĐ)", min_value=0, step=1000000)
    du_no = st.number_input("Dư nợ hiện tại (VNĐ)", min_value=0)
    cic = st.selectbox("Phân loại CIC", ["Nhóm 1 (Tốt)", "Nhóm 2", "Nhóm 3 (Xấu)"])

with col2:
    st.subheader("Thông tin Khoản vay")
    so_tien_vay = st.number_input("Số tiền đề nghị vay (VNĐ)", min_value=0)
    thoi_han = st.slider("Thời hạn vay (Tháng)", 6, 360, 12)
    lai_suat = st.number_input("Lãi suất (%/năm)", 0.0, 20.0, 10.0)

# Xử lý Logic
if st.button("🚀 Thực hiện thẩm định"):
    goc_lai_hang_thang = (so_tien_vay / thoi_han) + (so_tien_vay * (lai_suat/100/12))
    dti = ((du_no + goc_lai_hang_thang) / (thu_nhap + 1)) * 100
    
    st.divider()
    # Hiển thị kết quả
    m1, m2 = st.columns(2)
    m1.metric("Tỷ lệ nợ trên thu nhập (DTI)", f"{dti:.2f}%")
    m2.metric("Kết quả", "ĐẠT" if dti < 45 and cic == "Nhóm 1 (Tốt)" else "CẦN XEM XÉT")
