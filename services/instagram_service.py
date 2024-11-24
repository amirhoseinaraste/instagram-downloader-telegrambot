# define instagram content downloader service
import instaloader

# define loader
loader = instaloader.Instaloader()

# define instagram content downloader 
def download_instagram_content(link):
    try:
        post = instaloader.Post.from_shortcode(loader.context, link.split('/')[-2])
        if post.is_video:
            return post.video_url, 'video'
        else:
            return post.url, 'photo'
    except Exception as e:
        print(f"Error downloading content: {e}")
        return None, None
