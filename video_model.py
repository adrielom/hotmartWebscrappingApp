class VideoModel:
    def __init__(self, args):
        module_name = args.split("**")[0]
        video_name = args.split("**")[1].split("-Request URL: ")[0]
        video_url = args.split("-Request URL: ")[1]

        self.module_name = module_name
        self.video_name = video_name
        self.video_url = video_url

    def to_str(self):
        return f""" ------------
                    module {self.module_name}
                    video {self.video_name}
                    url {self.video_url}
                    """
