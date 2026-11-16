import subprocess
import json
import sys
import os

def verify_video(video_path):
    if not os.path.exists(video_path):
        print(f"ERROR: Video file not found: {video_path}")
        return False

    cmd = [
        "ffprobe", "-v", "quiet",
        "-print_format", "json",
        "-show_format", "-show_streams",
        video_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("ERROR running ffprobe:", res.stderr)
        return False

    data = json.loads(res.stdout)
    streams = data.get("streams", [])
    format_info = data.get("format", {})

    v_stream = next((s for s in streams if s.get("codec_type") == "video"), None)
    a_stream = next((s for s in streams if s.get("codec_type") == "audio"), None)

    duration = float(format_info.get("duration", 0))
    size_mb = float(format_info.get("size", 0)) / (1024 * 1024)

    print("=" * 50)
    print("VIDEO VERIFICATION REPORT")
    print("=" * 50)
    print(f"File: {os.path.basename(video_path)}")
    print(f"Size: {size_mb:.2f} MB")
    print(f"Duration: {duration:.2f} seconds")

    passed = True

    if v_stream:
        w = v_stream.get("width")
        h = v_stream.get("height")
        codec = v_stream.get("codec_name")
        r_fps = v_stream.get("r_frame_rate", "24/1")
        print(f"Video Stream: {w}x{h} ({codec}) @ {r_fps} FPS")
        if (w, h) != (1080, 1920) and (w, h) != (1920, 1080):
            print("WARNING: Non-standard resolution (expected 1080x1920 vertical or 1920x1080 horizontal)")
        if codec != "h264":
            print(f"WARNING: Video codec is {codec}, expected h264")
    else:
        print("ERROR: No video stream found!")
        passed = False

    if a_stream:
        a_codec = a_stream.get("codec_name")
        sr = a_stream.get("sample_rate")
        ch = a_stream.get("channels")
        print(f"Audio Stream: {a_codec} ({sr} Hz, {ch} ch)")
    else:
        print("Audio Stream: None (Muted video)")

    print("=" * 50)
    if passed:
        print("STATUS: VERIFIED OK!")
    else:
        print("STATUS: FAILED VERIFICATION")
    print("=" * 50)
    return passed

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python verify_video.py <video.mp4>")
        sys.exit(1)
    ok = verify_video(sys.argv[1])
    sys.exit(0 if ok else 1)
