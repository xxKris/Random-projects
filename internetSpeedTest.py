import speedtest

def internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / (10 ** 6)
    upload_speed = st.upload() / (10 ** 6)
    return download_speed, upload_speed

download_speed, upload_speed = internet_speed()
print("Download speed: {:.2f} Mbps".format(download_speed))
print("Upload speed: {:.2f} Mbps".format(upload_speed))
