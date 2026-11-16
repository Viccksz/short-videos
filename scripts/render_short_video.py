import os
import sys
import json
import math
import subprocess
import cv2
import numpy as np

W, H = 1080, 1920
FPS = 24
DISSOLVE_FRAMES = 4

def apply_motion(base_img, motion_type, progress, f_idx, total_f):
    h, w = base_img.shape[:2]
    
    if motion_type == "push_in":
        zoom = 1.0 + 0.06 * progress
        nw, nh = int(w / zoom), int(h / zoom)
        crop = base_img[(h - nh)//2 : (h + nh)//2, (w - nw)//2 : (w + nw)//2]
        return cv2.resize(crop, (w, h), interpolation=cv2.INTER_LINEAR)
        
    elif motion_type == "pan_down":
        zoom = 1.05
        nw, nh = int(w / zoom), int(h / zoom)
        y_offset = int((h - nh) * (0.15 + 0.7 * progress))
        crop = base_img[y_offset : y_offset + nh, (w - nw)//2 : (w + nw)//2]
        return cv2.resize(crop, (w, h), interpolation=cv2.INTER_LINEAR)
        
    elif motion_type == "pan_right":
        zoom = 1.05
        nw, nh = int(w / zoom), int(h / zoom)
        x_offset = int((w - nw) * (0.2 + 0.6 * progress))
        crop = base_img[(h - nh)//2 : (h + nh)//2, x_offset : x_offset + nw]
        return cv2.resize(crop, (w, h), interpolation=cv2.INTER_LINEAR)

    elif motion_type == "pan_left":
        zoom = 1.05
        nw, nh = int(w / zoom), int(h / zoom)
        x_offset = int((w - nw) * (0.8 - 0.6 * progress))
        crop = base_img[(h - nh)//2 : (h + nh)//2, x_offset : x_offset + nw]
        return cv2.resize(crop, (w, h), interpolation=cv2.INTER_LINEAR)
        
    elif motion_type == "push_in_warm":
        zoom = 1.0 + 0.07 * progress
        nw, nh = int(w / zoom), int(h / zoom)
        crop = base_img[(h - nh)//2 : (h + nh)//2, (w - nw)//2 : (w + nw)//2]
        frame = cv2.resize(crop, (w, h), interpolation=cv2.INTER_LINEAR)
        pulse = 1.0 + 0.035 * math.sin(2 * math.pi * progress * 2)
        return np.clip(frame.astype(np.float32) * pulse, 0, 255).astype(np.uint8)
        
    elif motion_type == "sway_window":
        zoom = 1.06 - 0.04 * progress
        nw, nh = int(w / zoom), int(h / zoom)
        crop = base_img[(h - nh)//2 : (h + nh)//2, (w - nw)//2 : (w + nw)//2]
        frame = cv2.resize(crop, (w, h), interpolation=cv2.INTER_LINEAR)
        local_t = f_idx / FPS
        angle = 0.75 * math.sin(2 * math.pi * 0.4 * local_t)
        M = cv2.getRotationMatrix2D((w * 0.5, h * 0.65), angle, 1.0)
        frame = cv2.warpAffine(frame, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        if f_idx >= total_f - 24:
            fade_progress = (f_idx - (total_f - 24)) / 24.0
            frame = (frame.astype(np.float32) * (1.0 - fade_progress)).astype(np.uint8)
        return frame

    elif motion_type == "slow_pull_out":
        zoom = 1.08 - 0.06 * progress
        nw, nh = int(w / zoom), int(h / zoom)
        crop = base_img[(h - nh)//2 : (h + nh)//2, (w - nw)//2 : (w + nw)//2]
        frame = cv2.resize(crop, (w, h), interpolation=cv2.INTER_LINEAR)
        if f_idx >= total_f - 24:
            fade_progress = (f_idx - (total_f - 24)) / 24.0
            frame = (frame.astype(np.float32) * (1.0 - fade_progress)).astype(np.uint8)
        return frame
        
    else:
        return base_img.copy()

def render_video(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    shots = cfg["shots"]  # list of {image_path, duration_seconds, motion}
    output_mp4 = cfg["output_video"]
    ambient_music = cfg.get("ambient_music", None)
    voice_lines = cfg.get("voice_lines", [])  # list of {file, delay_ms, volume}
    particles_enabled = cfg.get("particles", True)

    raw_mp4 = os.path.join(os.path.dirname(output_mp4), "temp_raw_video.mp4")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(raw_mp4, fourcc, FPS, (W, H))

    # Pre-render subtle grain textures for fast performance
    np.random.seed(42)
    grains = [np.random.normal(0, 1.5, (H, W, 3)).astype(np.float32) for _ in range(12)]

    # Dust motes
    particles = [
        {
            'x': np.random.uniform(50, W - 50),
            'y': np.random.uniform(100, H - 50),
            'vy': -np.random.uniform(0.5, 1.8),
            'vx': np.random.uniform(-0.25, 0.25),
            'r': np.random.uniform(2.5, 5.5),
        }
        for _ in range(50)
    ]

    loaded_shots = []
    for s in shots:
        img = cv2.imread(s["image_path"])
        if img is None:
            raise FileNotFoundError(f"Image not found: {s['image_path']}")
        resized = cv2.resize(img, (W, H), interpolation=cv2.INTER_LANCZOS4)
        frames = int(round(s["duration_seconds"] * FPS))
        loaded_shots.append({
            "img": resized,
            "duration_frames": frames,
            "motion": s.get("motion", "push_in")
        })

    total_rendered_frames = 0
    print(f"Rendering {len(loaded_shots)} shots into raw video...")

    for i, shot in enumerate(loaded_shots):
        base_img = shot["img"]
        dur = shot["duration_frames"]
        motion = shot["motion"]

        for f in range(dur):
            prog = f / float(dur)
            frame = apply_motion(base_img, motion, prog, f, dur).astype(np.float32)

            if particles_enabled:
                overlay = np.zeros((H, W, 3), dtype=np.uint8)
                for p in particles:
                    p['y'] += p['vy']
                    p['x'] += p['vx']
                    if p['y'] < 50: p['y'] = H - 50
                    if p['x'] < 50: p['x'] = W - 50
                    elif p['x'] > W - 50: p['x'] = 50
                    cv2.circle(overlay, (int(p['x']), int(p['y'])), int(p['r']), (215, 245, 255), -1, cv2.LINE_AA)
                frame = cv2.addWeighted(overlay.astype(np.float32), 0.6, frame, 1.0, 0)

            grain = grains[total_rendered_frames % len(grains)]
            final_frame = np.clip(frame + grain, 0, 255).astype(np.uint8)
            writer.write(final_frame)
            total_rendered_frames += 1

        # Dissolve between shots
        if i < len(loaded_shots) - 1:
            next_shot = loaded_shots[i+1]
            for df in range(DISSOLVE_FRAMES):
                alpha = (df + 1) / float(DISSOLVE_FRAMES + 1)
                f1 = apply_motion(base_img, motion, 1.0, dur - 1, dur).astype(np.float32)
                f2 = apply_motion(next_shot["img"], next_shot["motion"], 0.0, 0, next_shot["duration_frames"]).astype(np.float32)
                blended = (1.0 - alpha) * f1 + alpha * f2
                grain = grains[total_rendered_frames % len(grains)]
                final_frame = np.clip(blended + grain, 0, 255).astype(np.uint8)
                writer.write(final_frame)
                total_rendered_frames += 1

    writer.release()
    total_sec = total_rendered_frames / float(FPS)
    print(f"Raw video created: {total_rendered_frames} frames ({total_sec:.2f}s)")

    # Audio Muxing
    inputs = ["-i", raw_mp4]
    filter_parts = []
    mix_inputs = []

    # Voice inputs
    for idx, v in enumerate(voice_lines, start=1):
        inputs.extend(["-i", v["file"]])
        delay = v.get("delay_ms", 0)
        vol = v.get("volume", 1.2)
        filter_parts.append(f"[{idx}:a]adelay={delay}|{delay},volume={vol}[v{idx}]")
        mix_inputs.append(f"[v{idx}]")

    # Ambient music
    if ambient_music and os.path.exists(ambient_music):
        amb_idx = len(voice_lines) + 1
        inputs.extend(["-i", ambient_music])
        fade_start = max(0.0, total_sec - 2.0)
        amb_vol = cfg.get("music_volume", 0.22)
        filter_parts.append(f"[{amb_idx}:a]volume={amb_vol},afade=t=out:st={fade_start:.2f}:d=2.0[amb]")
        mix_inputs.append("[amb]")

    cmd = ["ffmpeg", "-y"] + inputs

    if mix_inputs:
        filter_parts.append(f"{''.join(mix_inputs)}amix=inputs={len(mix_inputs)}:duration=longest:dropout_transition=0[aout]")
        filter_str = ";".join(filter_parts)
        cmd.extend([
            "-filter_complex", filter_str,
            "-map", "0:v",
            "-map", "[aout]",
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "18",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac",
            "-b:a", "256k",
            "-shortest",
            output_mp4
        ])
    else:
        # No audio (mute)
        cmd.extend([
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "18",
            "-pix_fmt", "yuv420p",
            output_mp4
        ])

    print("Running FFmpeg muxing...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("FFmpeg error:", res.stderr)
        raise RuntimeError("FFmpeg muxing failed")

    # Clean up temp raw video
    if os.path.exists(raw_mp4):
        try:
            os.remove(raw_mp4)
        except:
            pass

    print(f"SUCCESS! Rendered final video: {output_mp4}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python render_short_video.py <config.json>")
        sys.exit(1)
    render_video(sys.argv[1])
