import os


def download_video(video):
    print(video.to_str())
    video = quotes_filtering(video.video_name)
    module_ = video.module_name
    args = f"""downloadm3u8 -o ./videos/{module_}/{video}.mp4 {video.video_url}"""
    print(f"{module_}/{video} - args {args}")
    os.system(args)


def has_video_been_downloaded(video):
    path = f"""./videos/{quotes_filtering(video['module_name'])}/{quotes_filtering(video['video_name'])}.mp4"""
    return os.path.exists(path)


def quotes_filtering(args):
    single_quote_filter = args.replace("'", r"""\'""")
    double_quote_filter = single_quote_filter.replace('"', r"""\"""")
    return double_quote_filter
