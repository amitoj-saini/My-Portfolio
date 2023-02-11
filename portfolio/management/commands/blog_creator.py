from django.core.management.base import BaseCommand
from portfolio.models import Blog
from string import ascii_letters
import pathlib
import random
import shutil
import sys
import os

# blog creator needs a specific file layout
# - somefolderexample
#   - blog.md
#   - banner.*
#   - images....

class Command(BaseCommand):
    help = 'Helps creates blog pages from word documents!'
    def handle(self, *args, **options):
        write_location = '/'.join(os.path.normpath(__file__).split(os.sep)[:-3])
        try:
            while True:
                # gets info (such as blog folder, title etc)
                print("Make sure you're blog file is name \"\x1b[34mblog.md\x1b[0m\", your banner is named \"\x1b[34mbanner.png/banner.jpg/banner.jpeg\x1b[0m\", and your images are the same as they are linked in the md file\n")
                title = input("Create a title for the blog: ")
                blog_folder = input("Enter the path to your \"\x1b[34mblog\x1b[0m\" folder: ")
                if not os.path.exists(blog_folder) or not os.path.isdir(blog_folder):
                    print("\x1b[31mError folder not found, try again\x1b[0m")
                else:
                    # gets files, stores the blog_file seprate and copies everything else with a random filename
                    files = os.listdir(blog_folder)
                    blog_paths = False
                    banner_file = False
                    static_files = []
                    for i in files:
                        full_file_path = os.path.join(blog_folder, i)
                        new_static_path = os.path.join("static", "portfolio", "blogs", ''.join([random.choice(ascii_letters) for i in range(0, 30)]) + pathlib.Path(full_file_path).suffix)
                        static_file = {"path": full_file_path, "new_static_path": os.path.join("/", new_static_path), "new_static_file": os.path.join(write_location, new_static_path)}

                        if i.lower() == "blog.md":
                            blog_paths = static_file
                            continue
                        elif i.lower().startswith("banner."):
                            banner_file = static_file["new_static_path"]
                        static_files.append(static_file)
                    
                    if not blog_paths or not banner_file:
                        print("\x1b[31mError file not found, try again\x1b[0m")

                    blog_content = open(blog_paths["path"], "r").read()

                    # write and move files

                    for i in static_files:             
                        blog_content = blog_content.replace(os.path.basename(i["path"]), i["new_static_path"])
                        shutil.copy(i["path"], i["new_static_file"])

                    with open(blog_paths["new_static_file"], "w") as blog_file:
                        blog_file.write(blog_content)
                        pass

                    # finally save blog in db

                    Blog(
                        title = title,
                        md = blog_paths["new_static_path"],
                        banner = banner_file
                    ).save()
                    
                    break
        except KeyboardInterrupt:
            print("\x1b[31mExiting blog creator...\x1b[0m")
            sys.exit(1)