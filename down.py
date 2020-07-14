from pytube import YouTube

print("Enter your link below")

link = input()

YouTube(link).streams.first().download()

print("Downloading...")

print("Video downloaded successfully")

