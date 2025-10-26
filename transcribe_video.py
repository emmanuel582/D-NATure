import whisper
import json

def transcribe_video(video_path, output_json="transcript.json"):
    """
    Transcribe video using OpenAI Whisper and generate word-level timestamps
    """
    print("Loading Whisper model...")
    # Load the model (options: tiny, base, small, medium, large)
    # 'base' is a good balance between speed and accuracy
    model = whisper.load_model("base")
    
    print(f"Transcribing {video_path}...")
    # Transcribe with word-level timestamps
    result = model.transcribe(
        video_path,
        word_timestamps=True,
        language="de"  # German language (change to "en" for English)
    )
    
    # Extract word-level data
    transcript_data = []
    
    for segment in result['segments']:
        if 'words' in segment:
            for word in segment['words']:
                transcript_data.append({
                    'start': round(word['start'], 2),
                    'end': round(word['end'], 2),
                    'text': word['word'].strip()
                })
    
    # Save to JSON file
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(transcript_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ Transcription complete!")
    print(f"✓ Saved to: {output_json}")
    print(f"✓ Total words: {len(transcript_data)}")
    
    # Also print JavaScript array format for easy copy-paste
    print("\n" + "="*60)
    print("JavaScript format (copy this into your HTML):")
    print("="*60)
    print("\nconst transcriptData = [")
    for item in transcript_data:
        print(f"    {{ start: {item['start']}, end: {item['end']}, text: \"{item['text']}\" }},")
    print("];")
    
    return transcript_data

if __name__ == "__main__":
    # Transcribe the video
    video_file = "Oct_19__1621_24s_202510192038_saxlr.mp4"
    transcribe_video(video_file)
