import webbrowser, time

url = input("Enter your video URL")
duration = input("duration")

for i in range(4):
    webbrowser.open_new(url)
    time.sleep(int(duration))