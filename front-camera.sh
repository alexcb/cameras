#!/bin/sh
set -e
CAM_DIR="/media/securitycam/videos/front-yard"
cd "$CAM_DIR"

# TODO: figure out how to use strftime_mkdir

mkdir -p $(date '+%Y-%m-%d')
ffmpeg -hide_banner -y -loglevel info -rtsp_transport tcp -use_wallclock_as_timestamps 1 -i rtsp://admin:pannkeFX8@192.168.0.128:554/h264 -vcodec copy -acodec copy -f segment -reset_timestamps 1 -segment_time 900 -segment_format mkv -segment_atclocktime 1 -strftime 1 ./%Y-%m-%d/front-%Y-%m-%dT%H-%M-%S.mkv
