import glob
import os
import re
import shutil
import subprocess
import sys
import argparse

argc = len(sys.argv)

if argc < 3:
    error_message = "python speech_config_file (vbs) input_video_script_file (tex)"
    print(error_message)
    raise Exception(error_message)

speech_config_file = sys.argv[1]
input_video_script_file = sys.argv[2]

with open(input_video_script_file, "r") as fin:
    lines = fin.read()

audios = re.findall(r"\\audio\s*\[(.*?)\]\s*{(.*?)}", lines, re.DOTALL)
for audio in audios:
    file_tag = audio[0]
    audio_script = audio[1]
    print(file_tag)
    print(audio_script)
