import os 
from flask import Flask, request, render_template, redirect, url_for
import subprocess
from moviepy.editor import *
from time import sleep
from datetime import datetime
import asyncio
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home(): 
    files = os.listdir("./static/videos/upload/")
    return render_template("home.html", files=files)



@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        f = request.files["video"]
        f.save('static/videos/upload/' + f.filename)
        return redirect(url_for("show"))
    else:
        files = os.listdir("./static/videos/upload/")
        return render_template("upload.html", files=files)



@app.route("/change", methods=["GET", "POST"])
def change():
    if request.method == "POST":
        video_file = request.form["video"]
        bitrate_video = request.form["bitrate"]
        output_file = request.form["output"]
        start_time = request.form["start_time"]
        end_time = request.form["end_time"]
        clip = VideoFileClip(video_file)
        clip1 = clip.subclip(start_time, end_time).resize(width=int(bitrate_video))
        clip1.write_videofile(datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p" ) + "_" + output_file + ".mp4")
        # a = datetime.datetime.now().strftime() + "_" + o
        # g = "ffmpeg -i {0} -b:v {1} -bufsize {1} ./static/videos/pupload/{2}.mp4".format(f, b, datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p" ) + "_" + o)
        # h = os.system(g)
        return redirect("show_1")
      
    else:
        files = os.listdir("./static/videos/upload/")
        return render_template("change.html",files=files)



@app.route("/show", methods=["GET"])
def show():
    files = os.listdir("./static/videos/upload/")
    return render_template("show.html", files= files)

@app.route("/show_changed", methods=["GET"])
def show_changed():
    files = os.listdir("./static/videos/pupload/")
    return render_template("show_changed.html", files= files)



@app.route("/concat_videos", methods=["GET", "POST"])
def concat_videos():
    if request.method == "POST":
        video_file1 = request.form["video1"]
        video_file2 = request.form["video2"]
        output_file = request.form["output"]
        clip1 = VideoFileClip(video_file1)
        clip1 = clip1.resize(width=800)
        clip2 = VideoFileClip(video_file2)
        clip2 = clip2.resize(width=800)
        clipx = [clip1,clip2]
        final_clip = concatenate_videoclips(clipx)
        # final_clip1 = CompositeVideoClip([clip1, # starts at t=0
                            # clip2.set_start(5).crossfadein(1)])
        # final_clip = clips_array([[clip1, clip2]])
        # final_clip.write_videofile(datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p" ) + "_" + output_file + ".mp4")
        final_clip.write_videofile("./static/videos/pupload/" + datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p" ) + "_" + output_file + ".mp4")
        return redirect("show_changed")
    else:
        files = os.listdir("./static/videos/pupload/")
        return render_template("concat_videos.html",files=files)


@app.route("/composite_videos", methods=["GET", "POST"])
def composite_videos():
    if request.method == "POST":
        video_file1 = request.form["video1"]
        video_file2 = request.form["video2"]
        output_file = request.form["output"]
        clip1 = VideoFileClip(video_file1)
        clip2 = VideoFileClip(video_file2)
        
        # final_clip = concatenate_videoclips([clip1,clip2])
        final_clip1 = CompositeVideoClip([clip1, # starts at t=0
                            clip2.set_position((100,100))])
        # final_clip = clips_array([[clip1, clip2]])
        # final_clip.write_videofile(datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p" ) + "_" + output_file + ".mp4")
        final_clip1.write_videofile("./static/videos/pupload/" + datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p" ) + "_" + output_file + ".mp4")
        return redirect("show_changed")
    else:
        files = os.listdir("./static/videos/pupload/")
        return render_template("composite_videos.html",files=files)


# async def main():
#     print('Hello ...')
#     await asyncio.sleep(5)
#     print('... World!')

# # Python 3.7+
# asyncio.run(main())





if __name__ == "__main__":
       app.run(debug=True)
