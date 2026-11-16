import asyncio
import edge_tts
import os
import sys
import subprocess
import json

def get_audio_duration(path):
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return float(res.stdout.strip())
    except:
        return 0.0

async def generate_line(text, out_path, voice="pt-BR-AntonioNeural", rate="-4%", pitch="-1Hz"):
    for attempt in range(3):
        try:
            comm = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
            await comm.save(out_path)
            dur = get_audio_duration(out_path)
            print(f"Generated: {os.path.basename(out_path)} ({dur:.2f}s)")
            return dur
        except Exception as e:
            print(f"Retry {attempt+1} for {out_path} error: {e}")
            await asyncio.sleep(1.0)
    raise RuntimeError(f"Failed to generate TTS audio for {out_path}")

async def main():
    """
    Usage: python generate_audio.py script.json out_dir [voice]
    script.json format:
    [
        {"id": "line1", "text": "..."},
        {"id": "line2", "text": "..."}
    ]
    """
    if len(sys.argv) < 3:
        print("Usage: python generate_audio.py <script.json> <output_dir> [voice]")
        sys.exit(1)

    json_file = sys.argv[1]
    out_dir = sys.argv[2]
    voice = sys.argv[3] if len(sys.argv) > 3 else "pt-BR-AntonioNeural"

    os.makedirs(out_dir, exist_ok=True)
    with open(json_file, "r", encoding="utf-8") as f:
        lines = json.load(f)

    results = []
    total_speech_time = 0.0

    for idx, item in enumerate(lines):
        filename = f"{item.get('id', f'line_{idx+1}')}.mp3"
        out_path = os.path.join(out_dir, filename)
        dur = await generate_line(item["text"], out_path, voice)
        results.append({
            "id": item.get("id", f"line_{idx+1}"),
            "file": out_path,
            "text": item["text"],
            "duration": dur
        })
        total_speech_time += dur
        await asyncio.sleep(0.4)

    summary_file = os.path.join(out_dir, "audio_manifest.json")
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump({
            "total_speech_time": total_speech_time,
            "recommended_video_duration": total_speech_time + 2.0,
            "lines": results
        }, f, indent=2, ensure_ascii=False)

    print(f"\nManifest saved to {summary_file}")
    print(f"Total speech time: {total_speech_time:.2f}s")
    print(f"Recommended video length (with breathing buffer): {total_speech_time + 2.0:.2f}s")

if __name__ == "__main__":
    asyncio.run(main())
